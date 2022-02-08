import cv2 as cv


def zoom(img, zoom_factor=2):
    return cv.resize(img, None, fx=zoom_factor, fy=zoom_factor)


def manager(img, x, y):
    img = cv.imread(img)
    cropped = img[y - 20: y + 50, x: x + 100]  # from y1 to y2 [y1:y2], from x1 to x2 [x1:x2]
    img = zoom(img, 20)
    zoomed_and_cropped = zoom(cropped, 10)
    cv.imshow('', zoomed_and_cropped)
    cv.waitKey(0)


manager('C:/Users/gsak3/Desktop/frames/scene00046.png', 560, 305)
