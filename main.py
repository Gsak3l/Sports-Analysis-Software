# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ***IMPORT LIBRARIES***
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import sys
import os
import platform
import time

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ***IMPORT PYTHON CLASSES***
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import save_data as sd
import string_manipulation as sm
import youtube_downloader as yd
import filesystem_changes as fc

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ***IMPORT / GUI AND MODULES AND WIDGETS***
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from modules import *
from widgets import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWebEngineCore import QWebEngineProfile
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

os.environ['QT_FONT_DPI'] = '96'  # FIX Problem for High DPI and Scale above 100%

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SET AS GLOBAL WIDGETS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # ***SET AS GLOBAL WIDGETS***
        # -------------------------------------------------------------------------------------------------------------
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # ***USE CUSTOM TITLE BAR***
        # -------------------------------------------------------------------------------------------------------------
        # USE AS 'False' FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # ***APP NAME***
        # -------------------------------------------------------------------------------------------------------------
        title = 'Sports Analysis App Name'
        description = 'Sports Analysis Slogan'
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # ***TOGGLE MENU***
        # -------------------------------------------------------------------------------------------------------------
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # ***SET UI DEFINITIONS***
        # -------------------------------------------------------------------------------------------------------------
        UIFunctions.uiDefinitions(self)

        # ***CREATING FOLDERS WHERE DATA WILL BE SAVED***
        # -------------------------------------------------------------------------------------------------------------
        fc.create_root_save_directory()
        path = fc.create_sub_save_folder()

        # -------------------------------------------------------------------------------------------------------------
        # ***LEFT MENU BUTTONS***
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_import_video.clicked.connect(self.buttonClick)
        widgets.btn_formation.clicked.connect(self.buttonClick)
        widgets.btn_video_player.clicked.connect(self.buttonClick)

        # ***LOCAL VIDEO PAGE BUTTON CONNECTION***
        # -------------------------------------------------------------------------------------------------------------
        widgets.btn_local_footage.clicked.connect(self.buttonClick)
        widgets.local_video_file_button.clicked.connect(self.buttonClick)
        widgets.local_previous_page_button.clicked.connect(self.buttonClick)
        widgets.local_next_page_button.clicked.connect(self.buttonClick)

        # ***TACTICS PAGE***
        # -------------------------------------------------------------------------------------------------------------
        # saving the information for the formation/tactics/lineup website to a json file
        widgets.formation.page().profile().setDownloadPath(path)
        widgets.formation.page().profile().downloadRequested.connect(self.on_downloadRequested)
        widgets.formation.load(QUrl('file:///football-formation-creator/11-builder/build/index.html'))
        # BUTTONS
        widgets.formation_next_page_button.clicked.connect(self.buttonClick)
        widgets.formation_previous_page_button.clicked.connect(self.buttonClick)

        # ***CLOUD VIDEO PAGE BUTTON CONNECTION***
        # -------------------------------------------------------------------------------------------------------------
        widgets.btn_cloud_footage.clicked.connect(self.buttonClick)
        widgets.cloud_video_file_button.clicked.connect(self.buttonClick)
        widgets.cloud_next_page_button.clicked.connect(self.buttonClick)
        widgets.cloud_previous_page_button.clicked.connect(self.buttonClick)

        # ***VIDEO PLAYER PAGE***
        # -------------------------------------------------------------------------------------------------------------
        # BUTTONS
        widgets.play_video_button.clicked.connect(self.buttonClick)
        widgets.pause_video_button.clicked.connect(self.buttonClick)
        widgets.stop_video_button.clicked.connect(self.buttonClick)
        widgets.increase_video_speed.clicked.connect(self.buttonClick)
        widgets.decrease_video_speed.clicked.connect(self.buttonClick)
        # ELEMENTS
        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()
        # PROGRESS BAR
        widgets.video_player_slider.valueChanged.connect(self.slider_moved)

        # -------------------------------------------------------------------------------------------------------------
        # SHOW APP
        self.show()

        # -------------------------------------------------------------------------------------------------------------
        # ***SET CUSTOM THEME***
        # UIFunctions.theme(self, 'themes/py_dracula_dark.qss', True)
        # AppFunctions.setThemeHack(self)

        # -------------------------------------------------------------------------------------------------------------
        # ***SET HOME PAGE AND SELECT MENU***
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        widgets.stackedWidget.setCurrentWidget(widgets.home)

    # =================================================================================================================
    # ***BUTTONS CLICK***
    # =================================================================================================================
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # -------------------------------------------------------------------------------------------------------------
        # ***RIGHT MENU BUTTONS***
        # .............................................................................................................
        # HOME PAGE
        if btnName == 'btn_home':  # HOME PAGE
            widgets.titleRightInfo.setText('Sports Analysis Software')
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # .............................................................................................................
        # EMBED VIDEO PAGE
        elif btnName == 'btn_import_video':
            widgets.titleRightInfo.setText('Choose Capture option')
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # .............................................................................................................
        # LINEUP BUILDER BUTTON
        elif btnName == 'btn_formation':
            widgets.titleRightInfo.setText('Build Your Lineup')
            widgets.stackedWidget.setCurrentWidget(widgets.tactics_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        # .............................................................................................................
        # VIDEO VIEWER AND COACH TOOL
        elif btnName == 'btn_video_player':
            widgets.titleRightInfo.setText('Expert Tool')
            widgets.stackedWidget.setCurrentWidget(widgets.video_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # -------------------------------------------------------------------------------------------------------------
        # ***LOCALLY EMBED VIDEOS***
        # -------------------------------------------------------------------------------------------------------------
        # SHOW LOCAL VIDEO PAGE
        elif btnName == 'btn_local_footage':
            widgets.titleRightInfo.setText('Local Video Page')
            widgets.stackedWidget.setCurrentWidget(widgets.local_video_page)
        # .............................................................................................................
        # FILE EXPLORER FOR VIDEO SELECTOR
        elif btnName == 'local_video_file_button':
            supported_formats = 'Video File (*.avi, *.mpg, *.mp4)'
            fname = QFileDialog.getOpenFileName(self, 'Open Video', fc.downloads_path(), supported_formats)
            widgets.local_video_file_name.setText(fname[0])
        # .............................................................................................................
        # SAVE DATA FROM INPUT FIELDS INTO A JSON AFTER VALIDATING FILE AND CHANGE PAGE
        elif btnName == 'local_next_page_button':
            # FILE VALIDATION FOR THE PATH
            if sd.check_if_file_exists(widgets.local_video_file_name.text()):
                sd.save_pre_local_video_data(widgets.local_calendar.selectedDate(),
                                             widgets.local_sports_type_combobox.currentText(),
                                             widgets.local_season_input.text(),
                                             widgets.local_competition_input.text(),
                                             widgets.local_details_input.toPlainText(),
                                             widgets.local_video_file_name.text())
                widgets.titleRightInfo.setText('Build Your Lineup')
                widgets.stackedWidget.setCurrentWidget(widgets.tactics_page)
                UIFunctions.resetStyle(self, widgets.btn_formation.objectName())
                widgets.btn_formation.setStyleSheet(UIFunctions.selectMenu(widgets.btn_formation.styleSheet()))
            else:
                widgets.local_video_file_name.setText('Please select a valid video file by pressing the Open button'
                                                      'and navigating to a .mp4 file')
        # .............................................................................................................
        # BUTTON THAT GOES BACK TO THE VIDEO TYPE SELECTION
        elif btnName == 'local_previous_page_button':
            # CHANGE HEADER TEXT
            widgets.titleRightInfo.setText('Choose Capture Video Option')
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)

        # -------------------------------------------------------------------------------------------------------------
        # ***EMBED VIDEO FROM A CLOUD LINK***
        # -------------------------------------------------------------------------------------------------------------
        # SHOW CLOUD PAGE
        elif btnName == 'btn_cloud_footage':
            widgets.titleRightInfo.setText('Cloud Video Page')
            widgets.stackedWidget.setCurrentWidget(widgets.cloud_video_page)
        # .............................................................................................................
        # DOWNLOAD BUTTON
        elif btnName == 'cloud_video_file_button':
            # FAKE PROGRESS BAR
            try:
                widgets.cloud_progress_bar.setTextVisible(True)  # VISIBLE %
                for i in range(0, 100):
                    if i == 14:
                        url = yd.save_video_to_downloads(widgets.cloud_video_file_name.text())
                    else:
                        time.sleep(0.05)
                        widgets.cloud_progress_bar.setValue(i)
                widgets.cloud_progress_bar.setValue(100)
                widgets.cloud_video_file_name.setPlaceholderText(sm.double_backslash_to_slash(url))
                widgets.cloud_video_file_name.setText('COMPLETED')
            except Exception as e:  # just in case the url is not valid
                widgets.cloud_progress_bar.setValue(0)
                widgets.cloud_video_file_name.setText('')
                widgets.cloud_video_file_name.setPlaceholderText('Please enter a valid URL...')
                print(e.__cause__)
        # .............................................................................................................
        # SAVE DATA FROM INPUT FIELDS INTO A JSON AFTER VALIDATING FILE AND CHANGE PAGE
        elif btnName == 'cloud_next_page_button':  # SAVE DATA FROM INPUT FIELDS INTO A JSON FILE
            if sd.check_if_file_exists(widgets.cloud_video_file_name.placeholderText()):
                sd.save_pre_local_video_data(widgets.cloud_calendar.selectedDate(),
                                             widgets.cloud_sports_type_combobox.currentText(),
                                             widgets.cloud_season_input.text(),
                                             widgets.cloud_competition_input.text(),
                                             widgets.cloud_details_input.toPlainText(),
                                             widgets.cloud_video_file_name.placeholderText())
                widgets.titleRightInfo.setText('Build Your Lineup')
                widgets.stackedWidget.setCurrentWidget(widgets.tactics_page)
                UIFunctions.resetStyle(self, widgets.btn_formation.objectName())
                widgets.btn_formation.setStyleSheet(UIFunctions.selectMenu(widgets.btn_formation.styleSheet()))
            else:
                widgets.cloud_video_file_name.setText('')
                widgets.cloud_video_file_name.setPlaceholderText('Error while validating the existence of the video, '
                                                                 'please try to downloaded again...')
        # .............................................................................................................
        # BUTTON THAT GOES BACK TO THE VIDEO TYPE SELECTION
        elif btnName == 'cloud_previous_page_button':
            widgets.titleRightInfo.setText('Choose Capture option')  # CHANGE HEADER TEXT
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)

        # -------------------------------------------------------------------------------------------------------------
        # ***FORMATION - LINEUP BUILDER***
        # -------------------------------------------------------------------------------------------------------------
        # SAVE LINEUP BUILDER DATA TO JSON AND GO TO THE COACH TOOL SECTION
        elif btnName == 'formation_next_page_button':
            sd.json_data_cleanup(sm.double_backslash_to_slash(fc.find_last_created_folder()), 'lineup.json')
            widgets.titleRightInfo.setText('Expert Tool')
            widgets.stackedWidget.setCurrentWidget(widgets.video_page)
            # DECIDE WHAT VIDEO TO DISPLAY, BAD PRACTICE
            if (widgets.cloud_video_file_name.text() == 'COMPLETED'):
                self.on_loadVideoRequest(widgets.cloud_video_file_name.placeholderText())
            else:
                self.on_loadVideoRequest(widgets.local_video_file_name.text())
        # .............................................................................................................
        # GO BACK PAGE
        elif btnName == 'formation_previous_page_button':
            # CHANGE HEADER TEXT
            widgets.titleRightInfo.setText('Choose Capture option')
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)  # SET PAGE
            # ACTIVE EMBED VIDEO MENU
            UIFunctions.resetStyle(self, widgets.btn_import_video.objectName())
            widgets.btn_import_video.setStyleSheet(UIFunctions.selectMenu(widgets.btn_import_video.styleSheet()))

        # -------------------------------------------------------------------------------------------------------------
        # ***VIDEO PLAYER PAGE***
        # -------------------------------------------------------------------------------------------------------------
        # PLAY VIDEO
        elif btnName == 'play_video_button':
            self.media_player.play()
            btn.setDisabled(True)
            widgets.pause_video_button.setDisabled(False)
            widgets.stop_video_button.setDisabled(False)
        # .............................................................................................................
        # PAUSE VIDEO
        elif btnName == 'pause_video_button':
            self.media_player.pause()
            btn.setDisabled(True)
            widgets.play_video_button.setDisabled(False)
            widgets.stop_video_button.setDisabled(False)
        # .............................................................................................................
        # STOP VIDEO
        elif btnName == 'stop_video_button':
            self.media_player.stop()
            btn.setDisabled(True)
            widgets.play_video_button.setDisabled(False)
            widgets.pause_video_button.setDisabled(False)
        # .............................................................................................................
        # INCREASE VIDEO PLAYBACK RATE
        elif btnName == 'increase_video_speed':
            self.fix_audio(btnName)
            self.media_player.setPlaybackRate(self.media_player.playbackRate() + 0.25)
        # .............................................................................................................
        # DECREASE VIDEO PLAYBACK SPEED
        elif btnName == 'decrease_video_speed':
            self.fix_audio(btnName)
            self.media_player.setPlaybackRate(self.media_player.playbackRate() - 0.25)

        # PRINT BTN NAME
        print(f'Button {btnName} pressed!')

    # -----------------------------------------------------------------------------------------------------------------
    # ***MOUSE CLICK EVENTS***
    # -----------------------------------------------------------------------------------------------------------------
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

    # -----------------------------------------------------------------------------------------------------------------
    # ***MEDIA PLAYER ACTIONS***
    # -----------------------------------------------------------------------------------------------------------------
    def slider_moved(self, position):
        percentage = self.media_player.duration() * position / 100
        self.media_player.setPosition(int(percentage))
        widgets.video_player_progress_bar.setValue(int(position))

    # -----------------------------------------------------------------------------------------------------------------
    # ***HANDLE DOWNLOAD REQUESTS FROM WEBSITE***
    # -----------------------------------------------------------------------------------------------------------------
    def on_loadVideoRequest(self, video_path):
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(widgets.video_player)
        self.media_player.setSource(QUrl(video_path))
        self.media_player.setPlaybackRate(1)
        self.media_player.play()

    # -----------------------------------------------------------------------------------------------------------------
    # ***DOWNLOADING WITHOUT DIALOG QWEBENGINEVIEW***
    # -----------------------------------------------------------------------------------------------------------------
    def on_downloadRequested(self, download):
        download.accept()

    # -----------------------------------------------------------------------------------------------------------------
    # ***RESIZE EVENTS***
    # -----------------------------------------------------------------------------------------------------------------
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # -----------------------------------------------------------------------------------------------------------------
    # ***REMOVE OR RESTORE AUDIO FROM VIDEO***
    # -----------------------------------------------------------------------------------------------------------------
    # (DISTORTION ON HIGH AND LOW PLAYBACK)
    def fix_audio(self, btn_):
        if (self.audio_output.isMuted()) and \
                ((btn_ == 'increase_video_speed' and (self.media_player.playbackRate() + 0.20) == 1) or
                 (btn_ == 'decrease_video_speed' and (self.media_player.playbackRate() - 0.20) == 1)):
            self.audio_output.setMuted(False)
            self.media_player.setAudioOutput(self.audio_output)
        elif self.audio_output.isMuted():
            pass
        else:
            self.audio_output.setMuted(True)
            self.media_player.setAudioOutput(self.audio_output)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# MAIN
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))
    window = MainWindow()
    sys.exit(app.exec_())
