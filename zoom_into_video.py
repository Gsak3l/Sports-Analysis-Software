import glob
import cv2 as cv
import pkg_resources

import filesystem_changes as fc
import string_manipulation as sm
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

    image_nums = []
    for image in glob.glob('./Exported Frames/*.jpg'):
        image_nums.append(int(sm.keep_numbers(image)))
    image_nums.sort()

    for num in image_nums:
        img = create_zoom_version('./Exported Frames/frame%d.jpg' % num, x[num], y[num])
        cv.imwrite('./Exported Frames/zoomed images/zoom%d.jpg' % num, img)

    out = cv.VideoWriter('./Exported Frames/output_video.avi', cv.VideoWriter_fourcc(*'DIVX'), 5, (700, 700))
    for num in image_nums:
        img = glob.glob('./Exported Frames/zoomed images/zoom%d.jpg' % num)[0]
        img = cv.imread(img)
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
        if count % 25 == 0:
            cv.imwrite('./Exported Frames/frame%d.jpg' % count, image)

        success, image = vid_cap.read()
        count += 1


# export_frames('C:/Users/gsak3/Downloads/Tactical View- Pixellot C Coaching.mp4')
# zoom_player(5, 'player_detection/runs/track/exp22/Tactical View- Pixellot C Coaching.txt')
