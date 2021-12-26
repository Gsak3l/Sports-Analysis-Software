# IMPORT LIBRARIES
import sys
import os
import platform

# IMPORT PYTHON CLASSES
import time

import string_manipulation
import save_data
import string_manipulation
import youtube_downloader
import file_manipulation
import test
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%


# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        UIFunctions.uiDefinitions(self)

        self.ui.formation.load(QUrl('https://google.com'))

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
