import glob
import cv2

import filesystem_changes as fc
import string_manipulation as sm
import csv_calculations as cc


# CREATES A ZOOMED IN VERSION OF THE VIDEO
def zoom(img, zoom_factor=2):
    return cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor)


# CROPS THE ZOOMED IN VERSION OF THE VIDEO
def create_zoom_version(img, x, y):
    img = cv2.imread(img)
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
        try:
            img = create_zoom_version('./Exported Frames/frame%d.jpg' % num, x[num], y[num])
            cv2.imwrite('./Exported Frames/zoomed images/zoom%d.jpg' % num, img)
        except IndexError as i:
            print(i)

    fc.created_zoom_video_folder()
    out = cv2.VideoWriter('./Zoomed-in Video/output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 25, (700, 700))
    for num in image_nums:
        try:
            img = glob.glob('./Exported Frames/zoomed images/zoom%d.jpg' % num)[0]
            img = cv2.imread(img)
            out.write(img)
        except IndexError as i:
            print(i)

    out.release()


# EXPORT 10 SECONDS WORTH OF FRAMES
def export_frames(video, frame):
    fc.delete_files_and_folder('./Exported Frames')
    fc.create_exported_frames_folder()
    vid_cap = cv2.VideoCapture(video)
    fps_ = get_video_fps(video)
    success, image = vid_cap.read()
    count = 0

    while success:
        if frame - (fps_ * 3) <= count <= frame + (fps_ * 7):
            cv2.imwrite('./Exported Frames/frame%d.jpg' % count, image)

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
        if count % 10 == 0:
            cv2.imwrite('./Exported Frames/frame%d.jpg' % count, image)

        success, image = vid_cap.read()
        count += 1


def get_video_fps(video):
    video = cv2.VideoCapture(video)
    return int(video.get(cv2.CAP_PROP_FPS))

# export_frames('C:/Users/gsak3/Downloads/Tactical View- Pixellot C Coaching.mp4', 300)
# zoom_player(5, 'player_detection/runs/track/exp22/Tactical View- Pixellot C Coaching.txt')
# import cv2
# if __name__ == '__main__' :
#
#     video = cv2.VideoCapture("test.mp4");
#
#     # Find OpenCV version
#     (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
#
#     if int(major_ver)  < 3 :
#         fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
#         print "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)
#     else :
#         fps = video.get(cv2.CAP_PROP_FPS)
#         print "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps)
#
#     video.release();
