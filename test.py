import sys
from PySide6.QtCore import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)

web = QWebEngineView()
web.load(QUrl('file:///football-formation-creator/index.html'))
web.show()

sys.exit(app.exec())
