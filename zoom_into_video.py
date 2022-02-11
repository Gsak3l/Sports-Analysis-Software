import glob

import filesystem_changes as fc
import cv2 as cv
import numpy as np

import csv_calculations as cc


# CREATES A ZOOMED IN VERSION OF THE VIDEO
def zoom(img, zoom_factor=2):
    return cv.resize(img, None, fx=zoom_factor, fy=zoom_factor)


# CROPS THE ZOOMED IN VERSION OF THE VIDEO
def create_zoom_version(img, x, y):
    img = cv.imread(img)
    cropped = img[y - 20: y + 50, x - 20: x + 50]  # from y1 to y2 [y1:y2], from x1 to x2 [x1:x2]
    img = zoom(img, 20)
    zoomed_and_cropped = zoom(cropped, 10)
    return zoomed_and_cropped


# EXPORTS WHERE A PLAYER IS AT THE GIVEN FRAME
def zoom_frame_player(frame, player_id, runs_path):
    df = cc.read_and_clean(runs_path)
    player = df.loc[(df['Frame'] == frame) & (df['ID'] == player_id)]

    x = int(player['x'])
    y = int(player['y'])
    create_zoom_version('./Exported Frames/frame%d.jpg' % frame, frame, x, y)


def zoom_player(player_id, runs_path):
    df = cc.read_and_clean(runs_path)
    player = df.loc[df['ID'] == player_id]
    # player = player.iloc[::30, :]  # basically one every 30 frames aka 1 every second on a 30fps video,

    frame, x, y = list(player['Frame']), list(player['x']), list(player['y'])

    for i in range(len(frame)):
        img = create_zoom_version('./Exported Frames/frame%d.jpg' % frame[i], x[i], y[i])
        cv.imwrite('./Exported Frames/zoomed images/zoom%d.jpg' % i, img)

    out = cv.VideoWriter('output_video.avi', cv.VideoWriter_fourcc(*'DIVX'), 5, (700, 700))
    for image in glob.glob('./Exported Frames/zoomed images/*.jpg'):
        img = cv.imread(image)
        out.write(img)

    out.release()


# EXPORTS FRAMES TO A SUB-PROJECT FOLDER NAMED "Exported Frames"
def export_frames(video):
    fc.delete_files_and_folder('./Exported Frames')
    fc.create_exported_frames_folder()
    vid_cap = cv.VideoCapture(video)
    success, image = vid_cap.read()
    count = 0

    while success:
        cv.imwrite('./Exported Frames/frame%d.jpg' % count, image)
        success, image = vid_cap.read()
        count += 1


export_frames('C:/Users/gsak3/Downloads/Tactical View- Pixellot C Coaching.mp4')
zoom_player(5, 'player_detection/runs/track/exp22/Tactical View- Pixellot C Coaching.txt')
