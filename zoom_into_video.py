import filesystem_changes as fc
import cv2 as cv


# CREATES A ZOOMED IN VERSION OF THE VIDEO
def zoom(img, zoom_factor=2):
    return cv.resize(img, None, fx=zoom_factor, fy=zoom_factor)


# CROPS THE ZOOMED IN VERSION OF THE VIDEO
def create_zoom_version(img, x, y):
    img = cv.imread(img)
    cropped = img[y - 20: y + 50, x: x + 100]  # from y1 to y2 [y1:y2], from x1 to x2 [x1:x2]
    img = zoom(img, 20)
    zoomed_and_cropped = zoom(cropped, 10)
    cv.imshow('', zoomed_and_cropped)
    cv.waitKey(0)


#  EXPORTS FRAMES TO A SUB-PROJECT FOLDER NAMED "Exported Frames"
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
