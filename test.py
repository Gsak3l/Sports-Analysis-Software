import sys
from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, QMessageBox
from PySide6.QtCore import QUrl


class GraphicsView(QGraphicsView):

    def __init__(self):
        super().__init__()


class mainTester(QMainWindow):

    def __init__(self):
        super().__init__()
        msgBox = QMessageBox()
        msgBox.setIconPixmap(QPixmap('C:/Users/gsak3/Desktop/frames/scene00046.png'))
        msgBox.exec()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainTester = mainTester()
    sys.exit(app.exec())
