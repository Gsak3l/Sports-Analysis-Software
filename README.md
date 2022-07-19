# Sports Analysis Software

Just a simple tool for coaches to help them analyze their team.

[![Watch the video](https://user-images.githubusercontent.com/23295116/179811907-714b14aa-356c-4dd7-8c95-6577fad69f19.png)](https://youtu.be/s9oEdFQa1OE)

## Screenshots

![Homepage](https://raw.githubusercontent.com/Gsak3l/Sports-Analysis-Software/main/preview_images/home.png)
![Captue Option](https://raw.githubusercontent.com/Gsak3l/Sports-Analysis-Software/main/preview_images/import_video.png)
![Local Import](https://raw.githubusercontent.com/Gsak3l/Sports-Analysis-Software/main/preview_images/import_video_locally.png)
![Cloud Import](https://raw.githubusercontent.com/Gsak3l/Sports-Analysis-Software/main/preview_images/import_cloud_locally.png)
![Lineup Builder](https://raw.githubusercontent.com/Gsak3l/Sports-Analysis-Software/main/preview_images/lineup_builder.png)
![Expert Tool](https://raw.githubusercontent.com/Gsak3l/Sports-Analysis-Software/main/preview_images/expert_tool_i_guess.png)
![Post Game Info](https://raw.githubusercontent.com/Gsak3l/Sports-Analysis-Software/main/preview_images/post_game_details.png)

## Features

- Integrated YoloV5 and DeepSort algorithms
- Automatic Offense/Defense generation
- Graph generation
- Download video directly from YouTube
- Build player lineup with built-in player database
- and many more

## Installation

Installation

```bash
git clone https://github.com/Gsak3l/Sports-Analysis-Software.git
cd Sports-Analysis-Software
pip install -r requirements.txt
python main.py
```

Python 3.8 or newest is recommended for this app to work.

## Custom Dataset
To train the algorithm with your own dataset, navigate to the ./player_detection/yolov5

On this folder create a _custom.yaml_ file with the following code format and a _train_data_ folder
```
# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
# COCO128 dataset https://www.kaggle.com/ultralytics/coco128 (first 128 images from COCO train2017)
# Example usage: python train.py --data coco128.yaml
# parent
# ├── yolov5
# └── datasets
#     └── coco128  ← downloads here


# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
train: train_data/images/train  # train images (relative to 'path') 128 images
val: train_data/images/val # val images (relative to 'path') 128 images
# test:  # test images (optional)

# Classes
nc: 2  # number of objects that appear classes
# Class names
names: [ 'center', 'MyTeam' ]  # your own class names
```

To train your own dataset you need 4 different subfolders inside the _train_data_ folder like shown in the image

![image](https://user-images.githubusercontent.com/23295116/177086159-03d73cdc-2f3b-45d9-990d-2369f37ac974.png)

The images folder contains both train and validation images for your dataset and the folder labels contains .txt files that point to your objects inside the images.

Then use the command `python train.py --img 640 --batch 16 --epochs 3 --data custom.yaml --weights yolov5s.pt`

Adjust the epochs and batch number to suit your needs. 
From my study, the more epochs you add the less significant the batch value is.
For more information about epochs and batch performance difference check yolov5 [#2337](https://github.com/ultralytics/yolov5/issues/2377).

## License

[GNU](https://www.gnu.org/licenses)
