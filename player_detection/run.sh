# training using yolov5
#cd yolov5
#python3 train.py --img 640 --batch 16 --epochs 800 --data custom_data.yaml --weights yolov5s.pt --nosave --cache --patience 0

# detection using yolov5
#cd yolov5
#python3 detect.py --weights runs/train/che_mun_ref_ball_goalpost_800_epochs/weights/last.pt --classes 0 1 2 3 4 --source ../CROPPED.mp4


# detection using deepsort with the weights of yolov5
#cd ..
python3 track.py --yolo_mode yolov5/runs/train/exp3/weights/last.pt --classes 0 1 2 3 4 --source 'videos/Tactical View- Pixellot C Coaching.mp4' --save-vid --save-txt


# stock yolov5 deeposort