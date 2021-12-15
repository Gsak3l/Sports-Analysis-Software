# IMPORT LIBRARIES
import sys
import os
import platform

# IMPORT PYTHON CLASSES
import time

import save_data
import youtube_downloader
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Sports Analysis App Name"
        description = "Sports Analysis Slogan"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # local_video_page.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # CONNECTING BUTTONS

        # LOCAL VIDEO PAGE
        widgets.btn_local_footage.clicked.connect(self.buttonClick)
        widgets.local_video_file_button.clicked.connect(self.buttonClick)
        widgets.local_previous_page_button.clicked.connect(self.buttonClick)
        widgets.local_next_page_button.clicked.connect(self.buttonClick)

        # -------------------------------------------------------------------------------------------------------------

        widgets.btn_cloud_footage.clicked.connect(self.buttonClick)
        widgets.cloud_video_file_button.clicked.connect(self.buttonClick)
        # widgets.video_url_button.clicked.connect(self.buttonClick)

        # LEFT MENU BUTTONS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_import_video.clicked.connect(self.buttonClick)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes/py_dracula_dark.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        widgets.stackedWidget.setCurrentWidget(widgets.home)

    # BUTTONS CLICK
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # RIGHT MENU BUTTONS
        if btnName == "btn_home":  # HOME PAGE
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btnName == "btn_import_video":  # EMBED VIDEO MENU
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # -------------------------------------------------------------------------------------------------------------

        # LOCALLY EMBED VIDEO BUTTONS
        elif btnName == "btn_local_footage":  # SHOW THE AVAILABLE OPTIONS FOR
            widgets.stackedWidget.setCurrentWidget(widgets.local_video_page)

        elif btnName == "local_video_file_button":  # OPEN FILE EXPLORER ON WHEN CLICKING THE LOCAL VIDEO IMPORT
            fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:/Users/gsak3/Documents/Projects/v5/',
                                                'MP4 Files (*mp4)')
            widgets.local_video_file_name.setText(fname[0])

        elif btnName == "local_next_page_button":  # SAVE DATA FROM INPUT FIELDS INTO A JSON FILE
            save_data.save_pre_local_video_data(widgets.local_calendar.selectedDate(),
                                                widgets.local_sports_type_combobox.currentText(),
                                                widgets.local_season_input.text(),
                                                widgets.local_competition_input.text(),
                                                widgets.local_details_input.toPlainText(),
                                                widgets.local_video_file_name.text())

        elif btnName == "local_previous_page_button":  # BUTTON THAT GOES BACK TO THE VIDEO TYPE SELECTION
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)

        # -------------------------------------------------------------------------------------------------------------

        # EMBED VIDEO FROM A CLOUD LINK
        elif btnName == "btn_cloud_footage":
            widgets.stackedWidget.setCurrentWidget(widgets.cloud_video_page)
            widgets.progressBar.setValue(0)

        # DOWNLOAD VIDEO BUTTON
        elif btnName == "cloud_video_file_button":
            # FAKE PROGRESS BAR
            try:
                for i in range(0, 100):
                    if i == 14:
                        url = youtube_downloader.save_video_to_downloads(widgets.cloud_video_file_name.text())
                    else:
                        time.sleep(0.1)
                        widgets.progressBar.setValue(i)
                widgets.progressBar.setValue(100)
                widgets.cloud_video_file_name.setText(url)
            except Exception as e:
                widgets.progressBar.setValue(0)
                widgets.cloud_video_file_name.setText('')
                widgets.cloud_video_file_name.setPlaceholderText('Please enter a valid URL...')
                print(e.__cause__)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
