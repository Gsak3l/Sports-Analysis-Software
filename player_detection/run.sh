# training using yolov5
#cd yolov5
#python3 train.py --img 640 --batch 24 --batch-size 24 --epochs 800 \
#--data custom_data.yaml --weights yolov5s.pt --nosave --cache

# detection using yolov5
#cd yolov5
#python3 detect.py --source 'videos/Tactical View- Pixellot C Coaching.mp4' \
#--weights runs/train/exp3/weights/last.pt --hide-labels --classes 0 1 2 3 4 --save-txt

# detection using deepsort with the weights of yolov5
python3 track.py --yolo_mode yolov5/runs/train/exp46/weights/best.pt \
  --source 'videos/Tactical View- Pixellot C Coaching.mp4' --classes 0 \
  --save-vid --save-txt
