import numpy as np


class Detection(object):

    # TLWH ARRAY LIKE
    # BOUNDING BOX FORMAT (X,Y,W,H)

    def __init__(self, tlwh, confidence, feature):
        self.tlwh = np.asarray(tlwh, dtype=np.float)
        self.confidence = float(confidence)
        self.feature = np.asarray(feature.cpu(), dtype=np.float32)

    # CONVERT BOUNDING BOX TO FORMAT:
    # (min x, min y, max x, max y)
    # (top left, bottom right)
    def to_tlbr(self):
        ret = self.tlwh.copy()
        ret[2:] += ret[:2]
        return ret

    # CONVERT BOUNDING BOX TO FORMAT:
    # (center x, center y, aspect ratio, height)
    # ASPECT RATIO : WIDTH/HEIGHT
    def to_xyah(self):
        ret = self.tlwh.copy()
        ret[:2] += ret[2:] / 2
        ret[2] /= ret[3]
        return ret
