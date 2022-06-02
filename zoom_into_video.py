import glob
import cv2
import json

import filesystem_changes as fc
import string_manipulation as sm
import csv_calculations as cc


# CROPS THE GIVEN IMAGE BY THE GIVEN ZOOM FACTOR
def resize_image(img, zoom_factor=2):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)


# CROPS THE ZOOMED IN VERSION OF THE VIDEO
def create_zoom_version(img, x, y):
    img = cv2.imread(img)
    cropped = img[y - 20: y + 50, x - 20: x + 50]  # from y1 to y2 [y1:y2], from x1 to x2 [x1:x2]
    img = resize_image(img, 20)
    zoomed_and_cropped = resize_image(cropped, 10)
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

    image_nums = []
    for image in glob.glob('./Exported Frames/*.jpg'):
        image_nums.append(int(sm.keep_numbers(image)))
    image_nums.sort()

    for num in image_nums:
        try:
            print(f'Generating zoomed-in frame, Frame: {num}')
            img = create_zoom_version('./Exported Frames/frame%d.jpg' % num, x[num], y[num])
            cv2.imwrite('./Exported Frames/zoomed images/zoom%d.jpg' % num, img)
        except IndexError as ie:
            print(ie)

    print('Converting frames into video, type:DIVX-mp4')
    fc.create_zoom_video_folder()
    out = cv2.VideoWriter('./Zoomed-in Video/output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 25, (700, 700))
    for num in image_nums:
        try:
            print(f'Converting zoomed-in frame into type:DIVX-mp4, Frame: {num}')
            img = glob.glob('./Exported Frames/zoomed images/zoom%d.jpg' % num)[0]
            img = cv2.imread(img)
            out.write(img)
        except IndexError as ie:
            print(ie)

    out.release()


# EXPORT 10 SECONDS WORTH OF FRAMES
def export_10_seconds_frames(video, frame):
    print('Exporting 10 Seconds')
    fc.delete_files_and_folder('./Exported Frames')
    fc.create_exported_frames_folder()
    vid_cap = cv2.VideoCapture(video)
    fps_ = get_video_fps(video)
    success, image = vid_cap.read()
    count = 0

    while success:
        if frame - (fps_ * 3) <= count <= frame + (fps_ * 7):
            print(f'Exporting frames, Frame Count: {count}')
            cv2.imwrite('./Exported Frames/frame%d.jpg' % count, image)
        elif count > frame + (fps_ * 7):
            break

        success, image = vid_cap.read()
        count += 1


# EXPORTS FRAMES TO A SUB-PROJECT FOLDER NAMED "Exported Frames"
def export_all_frames(video):
    fc.delete_files_and_folder('./Exported Frames')
    fc.create_exported_frames_folder()
    vid_cap = cv2.VideoCapture(video)
    success, image = vid_cap.read()
    count = 0

    while success:
        print('Exporting several images:')
        if count % 10 == 0:
            print(f'Exporting frames, Frame Count: {count}')
            cv2.imwrite('./Exported Frames/frame%d.jpg' % count, image)

        success, image = vid_cap.read()
        count += 1


# FIND VIDEO LENGTH SECONDS
def find_video_sec_length():
    duration = 1
    path = ''

    try:
        f = open(sm.double_backslash_to_slash(fc.find_last_created_folder()) + 'game details.json')
        path = json.load(f)
        path = path['Video Path']
        f.close()
    except FileNotFoundError as fe:
        print(fe)

    if path != '':
        cap = cv2.VideoCapture(path)
        fps = cap.get(cv2.CAP_PROP_FPS)  # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps

    return duration


# RETURNS THE FPS OF THE VIDEO, 24, 30 ETC.
def get_video_fps(video):
    video = cv2.VideoCapture(video)
    return int(video.get(cv2.CAP_PROP_FPS))
