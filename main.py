# IMPORT LIBRARIES
import sys
import os
import platform
import time

# IMPORT PYTHON CLASSES
import string_manipulation
import save_data
import string_manipulation
import youtube_downloader
import file_manipulation
import filesystem_changes
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWebEngineCore import QWebEngineProfile
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

os.environ['QT_FONT_DPI'] = '96'  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # -------------------------------------------------------------------------------------------------------------
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS 'False' FOR MAC OR LINUX
        # -------------------------------------------------------------------------------------------------------------
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # -------------------------------------------------------------------------------------------------------------
        title = 'Sports Analysis App Name'
        description = 'Sports Analysis Slogan'
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # -------------------------------------------------------------------------------------------------------------
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # -------------------------------------------------------------------------------------------------------------
        UIFunctions.uiDefinitions(self)

        # CREATING FOLDERS WHERE DATA WILL BE SAVED
        # -------------------------------------------------------------------------------------------------------------
        filesystem_changes.create_root_save_directory()
        path = filesystem_changes.create_sub_save_folder()

        # QTableWidget PARAMETERS
        # -------------------------------------------------------------------------------------------------------------
        # local_video_page.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # -------------------------------------------------------------------------------------------------------------
        # LEFT MENU BUTTONS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_import_video.clicked.connect(self.buttonClick)
        widgets.btn_formation.clicked.connect(self.buttonClick)

        # LOCAL VIDEO PAGE BUTTON CONNECTION
        # -------------------------------------------------------------------------------------------------------------
        widgets.btn_local_footage.clicked.connect(self.buttonClick)
        widgets.local_video_file_button.clicked.connect(self.buttonClick)
        widgets.local_previous_page_button.clicked.connect(self.buttonClick)
        widgets.local_next_page_button.clicked.connect(self.buttonClick)

        # TACTICS PAGE
        # -------------------------------------------------------------------------------------------------------------
        # saving the information for the formation/tactics/lineup website to a json file
        widgets.formation.page().profile().setDownloadPath(path)
        widgets.formation.page().profile().downloadRequested.connect(self.on_downloadRequested)
        widgets.formation.load(QUrl('file:///football-formation-creator/11-builder/build/index.html'))
        # BUTTONS
        widgets.formation_next_page_button.clicked.connect(self.buttonClick)
        widgets.formation_previous_page_button.clicked.connect(self.buttonClick)

        # CLOUD VIDEO PAGE BUTTON CONNECTION
        # -------------------------------------------------------------------------------------------------------------
        widgets.btn_cloud_footage.clicked.connect(self.buttonClick)
        widgets.cloud_video_file_button.clicked.connect(self.buttonClick)
        widgets.cloud_next_page_button.clicked.connect(self.buttonClick)
        widgets.cloud_previous_page_button.clicked.connect(self.buttonClick)

        # VIDEO PLAYER PAGE
        # -------------------------------------------------------------------------------------------------------------
        # BUTTONS
        widgets.play_video_button.clicked.connect(self.buttonClick)
        widgets.pause_video_button.clicked.connect(self.buttonClick)
        widgets.stop_video_button.clicked.connect(self.buttonClick)
        # ELEMENTS
        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()

        # -------------------------------------------------------------------------------------------------------------
        # SHOW APP
        self.show()

        # -------------------------------------------------------------------------------------------------------------
        # SET CUSTOM THEME
        useCustomTheme = False
        themeFile = 'themes/py_dracula_dark.qss'

        # -------------------------------------------------------------------------------------------------------------
        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # -------------------------------------------------------------------------------------------------------------
        # SET HOME PAGE AND SELECT MENU
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        widgets.stackedWidget.setCurrentWidget(widgets.home)

    # -----------------------------------------------------------------------------------------------------------------
    # BUTTONS CLICK
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # --------------------------------------------------------------------------------------------------------------
        # RIGHT MENU BUTTONS
        if btnName == 'btn_home':  # HOME PAGE
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        elif btnName == 'btn_import_video':  # EMBED VIDEO MENU
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # LINEUP BUILDER BUTTON
        elif btnName == 'btn_formation':
            widgets.stackedWidget.setCurrentWidget(widgets.tactics_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # -------------------------------------------------------------------------------------------------------------
        # LOCALLY EMBED VIDEOS
        elif btnName == 'btn_local_footage':  # SHOW THE AVAILABLE OPTIONS FOR LOCAL VIDEO
            widgets.stackedWidget.setCurrentWidget(widgets.local_video_page)

        elif btnName == 'local_video_file_button':  # OPEN FILE EXPLORER ON WHEN CLICKING THE LOCAL VIDEO IMPORT
            fname = QFileDialog.getOpenFileName(self, 'Open Video', filesystem_changes.downloads_path(),
                                                'Video File (*.avi, *.mpg, *.mp4)')
            widgets.local_video_file_name.setText(fname[0])

        elif btnName == 'local_next_page_button':  # SAVE DATA FROM INPUT FIELDS INTO A JSON FILE
            if save_data.check_if_file_exists(widgets.local_video_file_name.text()):  # FILE VALIDATION FOR THE PATH
                save_data.save_pre_local_video_data(widgets.local_calendar.selectedDate(),
                                                    widgets.local_sports_type_combobox.currentText(),
                                                    widgets.local_season_input.text(),
                                                    widgets.local_competition_input.text(),
                                                    widgets.local_details_input.toPlainText(),
                                                    widgets.local_video_file_name.text())
                # NEXT PAGE BUTTON
                widgets.stackedWidget.setCurrentWidget(widgets.tactics_page)
                # ACTIVE FORMATION MENU
                UIFunctions.resetStyle(self, widgets.btn_formation.objectName())
                widgets.btn_formation.setStyleSheet(UIFunctions.selectMenu(widgets.btn_formation.styleSheet()))
            else:
                widgets.local_video_file_name.setText('Please select a valid video file by pressing the Open button'
                                                      'and navigating to a .mp4 file')

        elif btnName == 'local_previous_page_button':  # BUTTON THAT GOES BACK TO THE VIDEO TYPE SELECTION
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)

        # -------------------------------------------------------------------------------------------------------------
        # EMBED VIDEO FROM A CLOUD LINK
        elif btnName == 'btn_cloud_footage':  # SHOW THE AVAILABLE OPTIONS FOR CLOUD VIDEO
            widgets.stackedWidget.setCurrentWidget(widgets.cloud_video_page)

        elif btnName == 'cloud_video_file_button':  # DOWNLOAD VIDEO BUTTON
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

        elif btnName == 'cloud_next_page_button':  # SAVE DATA FROM INPUT FIELDS INTO A JSON FILE
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
                # ACTIVE FORMATION MENU
                UIFunctions.resetStyle(self, widgets.btn_formation.objectName())
                widgets.btn_formation.setStyleSheet(UIFunctions.selectMenu(widgets.btn_formation.styleSheet()))
            else:
                widgets.cloud_video_file_name.setText('')
                widgets.cloud_video_file_name.setPlaceholderText(
                    'Error while validating the existance of the video, please'
                    'try to downloaded again...')
        elif btnName == 'cloud_previous_page_button':
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)

        # -------------------------------------------------------------------------------------------------------------
        # FORMATION - LINEUP BUILDER BUTTONS
        elif btnName == 'formation_next_page_button':
            save_data.json_data_cleanup(filesystem_changes.find_last_created_folder(), 'lineup.json')
            # CHANGING ACTIVE WIDGET PAGE
            widgets.stackedWidget.setCurrentWidget(widgets.video_page)
            # SETTING A VIDEO FOR THE VIDEO PLAYER
            self.on_loadVideoRequest(widgets.local_video_file_name.text())
        elif btnName == 'formation_previous_page_button':
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)  # SET PAGE
            # ACTIVE EMBED VIDEO MENU
            UIFunctions.resetStyle(self, widgets.btn_import_video.objectName())
            widgets.btn_import_video.setStyleSheet(UIFunctions.selectMenu(widgets.btn_import_video.styleSheet()))

        # -------------------------------------------------------------------------------------------------------------
        # VIDEO PLAYER PAGE
        elif btnName == 'play_video_button':
            self.media_player.play()
            btn.setDisabled(True)
            widgets.pause_video_button.setDisabled(False)
            widgets.stop_video_button.setDisabled(False)
        elif btnName == 'pause_video_button':
            self.media_player.pause()
            btn.setDisabled(True)
            widgets.play_video_button.setDisabled(False)
            widgets.stop_video_button.setDisabled(False)
        elif btnName == 'stop_video_button':
            self.media_player.stop()
            btn.setDisabled(True)
            widgets.play_video_button.setDisabled(False)
            widgets.pause_video_button.setDisabled(False)

        # PRINT BTN NAME
        print(f'Button {btnName} pressed!')

    # -----------------------------------------------------------------------------------------------------------------
    # HANDLE DOWNLOAD REQUESTS FROM WEBSITE
    def on_loadVideoRequest(self, video_path):
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(widgets.video_player)
        self.media_player.setSource(QUrl(video_path))
        self.media_player.play()

    # DOWNLOADING WITHOUT DIALOG QWEBENGINEVIEW
    def on_downloadRequested(self, download):
        download.accept()

    # -----------------------------------------------------------------------------------------------------------------
    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # -----------------------------------------------------------------------------------------------------------------
    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def keyPressEvent(self, event):
        print(event.text())
        print(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))
    window = MainWindow()
    sys.exit(app.exec_())
