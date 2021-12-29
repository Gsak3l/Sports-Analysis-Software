import os
from PySide6 import QtCore, QtWidgets, QtWebEngineWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.page().profile().downloadRequested.connect(
            self.on_downloadRequested
        )
        url = "file:///C:/Users/gsak3/Documents/Projects/SportsAnalysisSoftware/football-formation-creator/11-builder/build/index.html"
        self.view.load(QtCore.QUrl(url))
        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.view)

    def on_downloadRequested(self, download):
        old_path = file_path()
        path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", old_path, "*.json")
        download.accept()


def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
