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
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

tactics_counter_1 = 0
tactics_counter_2 = 1


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

        # LOCAL VIDEO PAGE BUTTON CONNECTION
        widgets.btn_local_footage.clicked.connect(self.buttonClick)
        widgets.local_video_file_button.clicked.connect(self.buttonClick)
        widgets.local_previous_page_button.clicked.connect(self.buttonClick)
        widgets.local_next_page_button.clicked.connect(self.buttonClick)

        # TACTICS PAGE
        widgets.tactics_1.textChanged.connect(self.textChanged)
        widgets.tactics_2.textChanged.connect(self.textChanged)

        widgets.textBrowser.setOpenExternalLinks(True)
        str_html = (file_manipulation.open_html_file(''))
        widgets.textBrowser.setText(str_html)
        widgets.textBrowser.show()
        widgets.textBrowser.raise_()

        # -------------------------------------------------------------------------------------------------------------

        # CLOUD VIDEO PAGE BUTTON CONNECTION
        widgets.btn_cloud_footage.clicked.connect(self.buttonClick)
        widgets.cloud_video_file_button.clicked.connect(self.buttonClick)
        widgets.cloud_next_page_button.clicked.connect(self.buttonClick)
        widgets.cloud_previous_page_button.clicked.connect(self.buttonClick)

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

    # TEXT CHANGED
    def textChanged(self):
        inp = self.sender()
        inpName = inp.objectName()

        # checking sport to calculate players and tactics that could work
        if widgets.local_sports_type_combobox.currentText() == 'Football':
            # in the first case user types a letter, in the second types random numbers
            # in football you cannot have more than 4 positions, so the input should only be something like 1-4-3-3 etc.
            if inpName == 'tactics_1':
                if (not string_manipulation.allow_dash_number(widgets.tactics_1.text()) or
                        (int(string_manipulation.count_numbers_in_string(widgets.tactics_1.text())) >= 4 and
                         int(string_manipulation.sum_digits_string(widgets.tactics_1.text()) != 11))):
                    widgets.tactics_1.setText('')
            # in the first case user types a letter, in the second types random numbers
            # in football you cannot have more than 4 positions, so the input should only be something like 1-4-3-3 etc.
            elif inpName == 'tactics_2':
                if (not string_manipulation.allow_dash_number(widgets.tactics_2.text()) or
                        (int(string_manipulation.count_numbers_in_string(widgets.tactics_2.text())) >= 4 and
                         int(string_manipulation.sum_digits_string(widgets.tactics_2.text()) != 11))):
                    widgets.tactics_2.setText('')

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

        # LOCALLY EMBED VIDEOS

        elif btnName == "btn_local_footage":  # SHOW THE AVAILABLE OPTIONS FOR LOCAL VIDEO
            widgets.stackedWidget.setCurrentWidget(widgets.local_video_page)

        elif btnName == "local_video_file_button":  # OPEN FILE EXPLORER ON WHEN CLICKING THE LOCAL VIDEO IMPORT
            fname = QFileDialog.getOpenFileName(self, 'Open Video', 'C:/Users/gsak3/Downloads',
                                                'MP4 Files (*mp4)')
            widgets.local_video_file_name.setText(fname[0])

        elif btnName == "local_next_page_button":  # SAVE DATA FROM INPUT FIELDS INTO A JSON FILE
            if save_data.check_if_file_exists(widgets.local_video_file_name.text()):  # FILE VALIDATION FOR THE PATH
                save_data.save_pre_local_video_data(widgets.local_calendar.selectedDate(),
                                                    widgets.local_sports_type_combobox.currentText(),
                                                    widgets.local_season_input.text(),
                                                    widgets.local_competition_input.text(),
                                                    widgets.local_details_input.toPlainText(),
                                                    widgets.local_video_file_name.text())
                # NEXT PAGE BUTTON
                widgets.stackedWidget.setCurrentWidget(widgets.tactics_page)
            else:
                widgets.local_video_file_name.setText('Please select a valid video file by pressing the Open button'
                                                      'and navigating to a .mp4 file')

        elif btnName == "local_previous_page_button":  # BUTTON THAT GOES BACK TO THE VIDEO TYPE SELECTION
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)

        # -------------------------------------------------------------------------------------------------------------

        # EMBED VIDEO FROM A CLOUD LINK

        elif btnName == "btn_cloud_footage":  # SHOW THE AVAILABLE OPTIONS FOR CLOUD VIDEO
            widgets.stackedWidget.setCurrentWidget(widgets.cloud_video_page)

        elif btnName == "cloud_video_file_button":  # DOWNLOAD VIDEO BUTTON
            # FAKE PROGRESS BAR
            try:
                widgets.cloud_progress_bar.setTextVisible(True)  # VISIBLE %
                for i in range(0, 100):
                    if i == 14:
                        url = youtube_downloader.save_video_to_downloads(widgets.cloud_video_file_name.text())
                    else:
                        time.sleep(0.05)
                        widgets.cloud_progress_bar.setValue(i)
                widgets.cloud_progress_bar.setValue(100)
                widgets.cloud_video_file_name.setPlaceholderText(string_manipulation.double_backslash_to_slash(url))
                widgets.cloud_video_file_name.setText('COMPLETED')
            except Exception as e:  # just in case the url is not valid
                widgets.cloud_progress_bar.setValue(0)
                widgets.cloud_video_file_name.setText('')
                widgets.cloud_video_file_name.setPlaceholderText('Please enter a valid URL...')
                print(e.__cause__)

        elif btnName == "cloud_next_page_button":  # SAVE DATA FROM INPUT FIELDS INTO A JSON FILE
            # FILE VALIDATION FOR THE PATH
            if save_data.check_if_file_exists(widgets.cloud_video_file_name.placeholderText()):
                save_data.save_pre_local_video_data(widgets.cloud_calendar.selectedDate(),
                                                    widgets.cloud_sports_type_combobox.currentText(),
                                                    widgets.cloud_season_input.text(),
                                                    widgets.cloud_competition_input.text(),
                                                    widgets.cloud_details_input.toPlainText(),
                                                    widgets.cloud_video_file_name.placeholderText())
                # NEXT PAGE BUTTON
                widgets.stackedWidget.setCurrentWidget(widgets.tactics_page)
            else:
                widgets.cloud_video_file_name.setText('Error while validating the existance of the video, please'
                                                      'try to downloaded again...')
        elif btnName == "cloud_previous_page_button":
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)

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
