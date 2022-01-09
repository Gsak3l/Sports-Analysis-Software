import os

os.getcwd()


def rename_files(path):
    for i, filename in enumerate(os.listdir(path)):
        os.rename(path + '/' + filename, path + '/' + str(i + 1) + ".jpg")


def reset_names(path):
    for i, filename in enumerate(os.listdir(path)):
        os.rename(path + '/' + filename, path + '/' + 'res' + str(i + 1) + ".jpg")


# reset_names('C:/Users/gsak3/Documents/Projects/trainy images/trian')
# rename_files('C:/Users/gsak3/Documents/Projects/trainy images/trian')

# reset_names('C:/Users/gsak3/Documents/Projects/trainy images/val')

reset_names('./yolov5/train_data/images/train/')
reset_names('./yolov5/train_data/images/val/')
rename_files('./yolov5/train_data/images/train/')
rename_files('./yolov5/train_data/images/val/')
