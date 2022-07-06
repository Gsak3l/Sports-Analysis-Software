import numpy as np
import torch
import sys

from .sort.nn_matching import NearestNeighborDistanceMetric
from .sort.detection import Detection
from .sort.tracker import Tracker

sys.path.append('deep_sort/deep/reid')
from torchreid.utils import FeatureExtractor

__all__ = ['DeepSort']


class DeepSort(object):
    def __init__(self, model_type, device, max_dist=0.2, max_iou_distance=0.7, max_age=70, n_init=3, nn_budget=100):

        self.extractor = FeatureExtractor(
            model_name=model_type,
            device=str(device)
        )

        max_cosine_distance = max_dist
        metric = NearestNeighborDistanceMetric(
            "euclidean", max_cosine_distance, nn_budget)
        self.tracker = Tracker(
            metric, max_iou_distance=max_iou_distance, max_age=max_age, n_init=n_init)

    def update(self, bbox_x_y_w_h, confidences, classes, ori_img, use_yolo_preds=False):
        self.height, self.width = ori_img.shape[:2]
        # generate detections
        features = self._get_features(bbox_x_y_w_h, ori_img)
        bbox_tlwh = self._xywh_to_tlwh(bbox_x_y_w_h)
        detections = [Detection(bbox_tlwh[i], conf, features[i]) for i, conf in enumerate(
            confidences)]

        # run on non-maximum supression
        boxes = np.array([d.tlwh for d in detections])
        scores = np.array([d.confidence for d in detections])

        # update tracker
        self.tracker.predict()
        self.tracker.update(detections, classes)

        # output bbox identities
        outputs = []
        for track in self.tracker.tracks:
            if not track.is_confirmed() or track.time_since_update > 1:
                continue
            if use_yolo_preds:
                det = track.get_yolo_pred()
                x1, y1, x2, y2 = self._tlwh_to_xyxy(det.tlwh)
            else:
                box = track.to_tlwh()
                x1, y1, x2, y2 = self._tlwh_to_xyxy(box)
            track_id = track.track_id
            class_id = track.class_id
            outputs.append(np.array([x1, y1, x2, y2, track_id, class_id], dtype=np.int))
        if len(outputs) > 0:
            outputs = np.stack(outputs, axis=0)
        return outputs

    """
    TODO:
        Convert bbox from xc_yc_w_h to xtl_ytl_w_h
    Thanks JieChen91@github.com for reporting this bug!
    """

    @staticmethod
    def _xywh_to_tlwh(bbox_x_y_w_h):
        if isinstance(bbox_x_y_w_h, np.ndarray):
            bbox_t_l_w_h = bbox_x_y_w_h.copy()
        elif isinstance(bbox_x_y_w_h, torch.Tensor):
            bbox_t_l_w_h = bbox_x_y_w_h.clone()
        bbox_t_l_w_h[:, 0] = bbox_x_y_w_h[:, 0] - bbox_x_y_w_h[:, 2] / 2.
        bbox_t_l_w_h[:, 1] = bbox_x_y_w_h[:, 1] - bbox_x_y_w_h[:, 3] / 2.
        return bbox_t_l_w_h

    def _xywh_to_xyxy(self, bbox_x_y_w_h):
        x, y, w, h = bbox_x_y_w_h
        x1 = max(int(x - w / 2), 0)
        x2 = min(int(x + w / 2), self.width - 1)
        y1 = max(int(y - h / 2), 0)
        y2 = min(int(y + h / 2), self.height - 1)
        return x1, y1, x2, y2

    def _tlwh_to_xyxy(self, bbox_t_l_w_h):
        # FIXME, *BUG*: Convert bbox from xtl_ytl_w_h to xc_yc_w_h
        x, y, w, h = bbox_t_l_w_h
        x1 = max(int(x), 0)
        x2 = min(int(x + w), self.width - 1)
        y1 = max(int(y), 0)
        y2 = min(int(y + h), self.height - 1)
        return x1, y1, x2, y2

    def increment_ages(self):
        self.tracker.increment_ages()

    def _xyxy_to_tlwh(self, bbox_xyxy):
        x1, y1, x2, y2 = bbox_xyxy

        t = x1
        l = y1
        w = int(x2 - x1)
        h = int(y2 - y1)
        return t, l, w, h

    def _get_features(self, bbox_x_y_w_h, ori_img):
        im_crops = []
        for box in bbox_x_y_w_h:
            x1, y1, x2, y2 = self._xywh_to_xyxy(box)
            im = ori_img[y1:y2, x1:x2]
            im_crops.append(im)
        if im_crops:
            features = self.extractor(im_crops)
        else:
            features = np.array([])
        return features
