# training using yolov5
#yolov5/python3 train.py --img 640 --batch 16 --epochs 800 --data custom_data.yaml --weights \
#yolov5s.pt --nosave --cache --patience 0

# detection using yolov5
#python3 yolov5/detect.py --source 'videos/Tactical View- Pixellot C Coaching.mp4' \
#--weights yolov5/runs/train/exp3/weights/last.pt --hide-labels --classes 0 1 2 3 4 --save-txt


# detection using deepsort with the weights of yolov5
python3 track.py --yolo_mode yolov5/runs/train/exp3/weights/last.pt \
--source 'videos/Tactical View- Pixellot C Coaching.mp4' --classes 0 1 2 3 4 \
 --save-vid --save-txt


# stock yolov5 deeposort