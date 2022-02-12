import sys
from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, QMessageBox
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QGraphicsVideoItem


class GraphicsView(QGraphicsView):

    def __init__(self):
        super().__init__()


class mainTester(QMainWindow):

    def __init__(self):
        super().__init__()
        # msgBox = QMessageBox()
        # msgBox.setIconPixmap(QPixmap('C:/Users/gsak3/Desktop/frames/scene00046.png'))
        # msgBox.exec()

        player = QMediaPlayer()
        player.setSource(QtCore.QUrl('C:/Users/gsak3/Downloads/Tactical View- Pixellot C Coaching.mp4'))

        video_item = QGraphicsVideoItem()
        player.setVideoOutput(video_item)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainTester = mainTester()
    sys.exit(app.exec())
