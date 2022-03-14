# import sys
#
# from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
#     QPushButton
# from PySide6.QtGui import QIcon
#
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
#
# import random
#
#
# class App(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.left = 10
#         self.top = 10
#         self.title = 'PyQt5 matplotlib example - pythonspot.com'
#         self.width = 640
#         self.height = 400
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         m = PlotCanvas(self, width=5, height=4)
#         m.move(0, 0)
#
#         button = QPushButton('PyQt5 button', self)
#         button.setToolTip('This s an example button')
#         button.move(500, 0)
#         button.resize(140, 100)
#
#         self.show()
#
#
# class PlotCanvas(FigureCanvas):
#
#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#
#         FigureCanvas.__init__(self, fig)
#         self.setParent(parent)
#
#         FigureCanvas.setSizePolicy(self,
#                                    QSizePolicy.Expanding,
#                                    QSizePolicy.Expanding)
#         FigureCanvas.updateGeometry(self)
#         self.plot()
#
#     def plot(self):
#         data = [random.random() for i in range(25)]
#         ax = self.figure.add_subplot(111)
#         ax.plot(data, 'r-')
#         ax.set_title('PyQt Matplotlib Example')
#         self.draw()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())

## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ##

# import os
#
# os.chdir('./player_detection')
#
#
# os.system('C:/Users/gsak3/AppData/Local/Programs/Python/Python39/python track.py --yolo_mode '
#           'yolov5/runs/train/exp55/weights/last.pt --source videos/Tactical View- Pixellot C Coaching.mp4 '
#           '--classes 0 1 --save-vid --save-txt')

## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ##

# import cv2
#
#
# def distance_to_object(img):
#     fmm = 1.9  # mm
#     real_height = 170  # mm
#     image_height = 4032  # pixels
#     object_height = 2879  # pixels
#     sensor_height = 2.55  # mm
#
#     divisor = fmm * real_height * image_height
#     dividend = object_height * sensor_height
#
#     distance = divisor / dividend
#     print(distance)
#
#
# distance_to_object('C:/Users/gsak3/Desktop/PXL_20220304_094907852.jpg')

## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ##


























