# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ***IMPORT LIBRARIES***
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import sys
import os
import platform
import time
import pandas as pd
import json
import cv2

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ***IMPORT PYTHON CLASSES***
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import filesystem_changes
import save_data as sd
import string_manipulation as sm
import youtube_downloader as yd
import filesystem_changes as fc
import csv_calculations as cc
import distance

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
names = []
actions = []
timestamps = None
date_stamps = None
running_meters = None
distance_meters = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # ***SET AS GLOBAL WIDGETS***
        # -------------------------------------------------------------------------------------------------------------
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        global names
        global actions
        global timestamps
        global date_stamps
        global running_meters
        global distance_meters

        widgets = self.ui
        actions = [
            ['Goal', 'Shot', 'Shot on Target', 'Header', 'Set Piece', 'Right foot', 'Shot Inside the box'],
            ['Pass', 'Short Pass', 'Long Pass', 'Pass above ground', 'Unsuccessful Pass'],
            ['Tackle', 'Tackle Won', 'Tackle in Defensive Zone', 'Foul Conceded',
             'Pass Interception Won', 'Possession Turnover Won']
        ]

        timestamps, running_meters, distance_meters = distance.manager(
            'player_detection/runs/track/exp20/Tactical View- Pixellot C Coaching.txt', 46
        )

        running_meters = pd.DataFrame(running_meters)
        distance_meters = pd.DataFrame(distance_meters)

        distance_meters.to_csv(fc.find_last_created_folder() + 'distance between players.csv')
        running_meters.to_csv(fc.find_last_created_folder() + 'total running distance.csv')

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
        widgets.add_action.clicked.connect(self.buttonClick)
        widgets.return_to_lineup_builder.clicked.connect(self.buttonClick)
        widgets.show_post_game_button.clicked.connect(self.buttonClick)
        # ELEMENTS
        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()
        # OTHERS
        widgets.video_player_slider.valueChanged.connect(self.slider_moved)
        widgets.playback_speed_combo.currentIndexChanged.connect(self.set_video_playback)
        widgets.type_of_action_combobox.currentIndexChanged.connect(self.change_actions)
        widgets.od_combobox.currentIndexChanged.connect(self.change_timestamps)
        widgets.od_timestamps_combobox.currentIndexChanged.connect(self.set_minute)
        self.change_actions()
        self.change_timestamps()

        # ***STATS PAGE***
        # -------------------------------------------------------------------------------------------------------------

        # ***DARK/LIGHT THEME BUTTON***
        # -------------------------------------------------------------------------------------------------------------
        widgets.themeBtn.clicked.connect(self.buttonClick)

        # -------------------------------------------------------------------------------------------------------------
        # SHOW APP
        self.show()

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
        # ***SET CUSTOM THEME***
        if btnName == 'themeBtn':
            if widgets.themeBtn.text() == 'dark_theme':
                UIFunctions.resetStyle(self, btnName)
                UIFunctions.theme(self, 'themes/py_dracula_dark.qss', True)
                AppFunctions.setThemeHack(self)
                widgets.themeBtn.setText('light_theme')
            else:
                UIFunctions.resetStyle(self, btnName)
                UIFunctions.theme(self, 'themes/py_dracula_light.qss', True)
                AppFunctions.setThemeHack(self)
                widgets.themeBtn.setText('dark_theme')

        # -------------------------------------------------------------------------------------------------------------
        # ***RIGHT MENU BUTTONS***
        # .............................................................................................................
        # HOME PAGE
        elif btnName == 'btn_home':  # HOME PAGE
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
            if fc.check_if_file_exists(widgets.local_video_file_name.text()):
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
        elif btnName == 'cloud_next_page_button':
            if fc.check_if_file_exists(widgets.cloud_video_file_name.placeholderText()):
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
            widgets.titleRightInfo.setText('Choose Capture option')
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)

        # -------------------------------------------------------------------------------------------------------------
        # ***FORMATION - LINEUP BUILDER***
        # -------------------------------------------------------------------------------------------------------------
        # SAVE LINEUP BUILDER DATA TO JSON AND GO TO THE COACH TOOL SECTION
        elif btnName == 'formation_next_page_button':
            try:
                self.names = sd.manager(sm.double_backslash_to_slash(fc.find_last_created_folder()), 'lineup.json')
            except FileNotFoundError as fl:
                print(fl)
            self.delete_player_names()
            widgets.player_names_combobox.addItems(self.names)
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
            widgets.titleRightInfo.setText('Choose Capture option')
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)  # SET PAGE
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

        # ADD ACTION FROM THE COMBO BOXES TO A CSV
        # .............................................................................................................

        elif btnName == 'add_action':
            cc.add_to_csv(widgets.player_names_combobox.currentText(),
                          widgets.type_of_action_combobox.currentText(),
                          widgets.action_combobox.currentText(),
                          (self.media_player.position() / 1000))

        # RETURN TO THE LINEUP BUILDER TO CHANGE LINEUP
        # .............................................................................................................
        elif btnName == 'return_to_lineup_builder':
            widgets.titleRightInfo.setText('Build Your Lineup')
            widgets.stackedWidget.setCurrentWidget(widgets.tactics_page)
            UIFunctions.resetStyle(self, widgets.btn_formation.objectName())
            widgets.btn_formation.setStyleSheet(UIFunctions.selectMenu(widgets.btn_formation.styleSheet()))

        # FIXME ADD NEW COMMENTS HERE COMMENDS
        elif btnName == 'show_post_game_button':
            widgets.titleRightInfo.setText('Post Game')
            widgets.stackedWidget.setCurrentWidget(widgets.post_game)
            self.fill_tables()

        # PRINT BTN NAME
        print(f'Button {btnName} pressed!')

    # -----------------------------------------------------------------------------------------------------------------
    # ***MOUSE CLICK EVENTS***
    # -----------------------------------------------------------------------------------------------------------------
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        point = event.globalPosition()
        self.dragPos = point.toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def keyPressEvent(self, event):
        print(event.text())
        print(event)

    # -----------------------------------------------------------------------------------------------------------------
    # ***MEDIA PLAYER NON PLAYBACK RELATED ACTIONS***
    # -----------------------------------------------------------------------------------------------------------------
    # CHANGING THE ACTION OPTIONS ON THE COMBOBOX
    def change_actions(self):
        # deleting current values
        for x in range(10):
            try:
                widgets.action_combobox.removeItem(0)
            except IndexError:
                pass

        index = widgets.type_of_action_combobox.currentIndex()
        widgets.action_combobox.addItems(actions[index])

    # CHANGING THE TIMESTAMPS FOR OFFENSE/DEFENSE/I-B
    def change_timestamps(self):
        # deleting current values
        for x in range(len(timestamps)):
            try:
                widgets.od_timestamps_combobox.removeItem(0)
            except IndexError:
                pass
        # THIS IS GOLD, IT TOOK ABOUT 5 HOURS GIVE OR TAKE, FOR SOMETHING SO SIMPLE
        date_stamps = sm.frame_to_time_list(timestamps, 24)
        for y in range(len(timestamps[0])):
            if timestamps[1][y] == 'OFFENSE' and widgets.od_combobox.currentIndex() == 0:
                widgets.od_timestamps_combobox.addItem(date_stamps[y])
            elif timestamps[1][y] == 'DEFENSE' and widgets.od_combobox.currentIndex() == 1:
                widgets.od_timestamps_combobox.addItem(date_stamps[y])
            elif timestamps[1][y] == 'JUST PLAYING' and widgets.od_combobox.currentIndex() == 2:
                widgets.od_timestamps_combobox.addItem(date_stamps[y])

    # .................................................................................................................
    # CHANGING THE ACTION OPTIONS ON THE COMBOBOX
    def delete_player_names(self):
        # deleting current values
        for x in range(11):
            try:
                widgets.player_names_combobox.removeItem(0)
            except IndexError:
                pass

    # -----------------------------------------------------------------------------------------------------------------
    # ***VIDEO AND AUDIO ACTIONS***
    # -----------------------------------------------------------------------------------------------------------------
    # LOAD VIDEO AND PLAY IT ON THE DEFAULT SPEED OF 1
    def on_loadVideoRequest(self, video_path):
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(widgets.video_player)
        self.media_player.setSource(QUrl(video_path))
        self.media_player.setPlaybackRate(1)
        widgets.play_video_button.setDisabled(False)
        widgets.pause_video_button.setDisabled(True)
        widgets.stop_video_button.setDisabled(False)

    # .................................................................................................................
    def set_minute(self):
        try:
            max_seconds = fc.find_video_sec_length()
            seconds = widgets.od_timestamps_combobox.currentText()
            seconds = sm.date_to_second(seconds)
            seconds -= 10
            duration = self.media_player.duration()
            self.media_player.setPosition(int(duration * seconds / max_seconds))
        except Exception as e:
            print(e)

    # .................................................................................................................
    # SET PLAYBACK SPEED
    def set_video_playback(self):
        self.media_player.setPlaybackRate((widgets.playback_speed_combo.currentIndex() + 1) * 0.25)
        self.fix_audio()

    # .................................................................................................................
    # (DISTORTION ON HIGH AND LOW PLAYBACK)
    def fix_audio(self):
        if self.audio_output.isMuted() and ((widgets.playback_speed_combo.currentIndex() == 3)):
            self.audio_output.setMuted(False)
            self.media_player.setAudioOutput(self.audio_output)
        elif self.audio_output.isMuted():
            pass
        else:
            self.audio_output.setMuted(True)
            self.media_player.setAudioOutput(self.audio_output)

    # .................................................................................................................
    # PLAYBACK AND SLIDER
    def slider_moved(self, position):
        percentage = self.media_player.duration() * position / 100
        self.media_player.setPosition(int(percentage))
        widgets.video_player_progress_bar.setValue(int(position))

    # -----------------------------------------------------------------------------------------------------------------
    # ***POST GAME PAGE***
    # -----------------------------------------------------------------------------------------------------------------
    # FILLING THE AFTERMATH TABLES
    def fill_tables(self):
        # PRE-GAME DETAILS TABLE
        post_game_details = sm.double_backslash_to_slash(fc.find_last_created_folder()) + 'game details.json'
        f = open(post_game_details)
        post_game_details = json.load(f)
        f.close()
        labels = []
        labels_equal_to = []
        # to the moon
        for GME in post_game_details:
            labels.append(GME)
            labels_equal_to.append(post_game_details[GME])
        widgets.pregame_table.setColumnCount(1)
        widgets.pregame_table.setRowCount(len(post_game_details))
        widgets.pregame_table.setVerticalHeaderLabels(labels)
        [widgets.pregame_table.setItem(i, 0, QTableWidgetItem(labels_equal_to[i])) for i in
         range(len(labels_equal_to))]

        # ACTIONS OF PLAYERS, LIKE PASSES, SHOTS, GOALS ETC.
        df_actions = pd.read_csv(sm.double_backslash_to_slash(fc.find_last_created_folder()) + 'actions.csv')
        widgets.actions_table.setRowCount(df_actions.shape[0])
        widgets.actions_table.setColumnCount(df_actions.shape[1])
        # widgets.actions_table.setVerticalHeaderLabels(sm.int_list_to_string_list(df_actions['Name'].tolist()))
        widgets.actions_table.setHorizontalHeaderLabels(['Name', 'Type of Action', 'Action', 'Timestamp'])
        for i in range(df_actions.shape[0]):
            for j in range(df_actions.shape[1]):
                widgets.actions_table.setItem(i, j, QTableWidgetItem(str(df_actions.iloc[i][j])))

        # LINEUPS
        lineups = sm.find_last_folder_lineups()
        lineup_path = []
        row_count = 0
        for i in range(len(lineups)):
            lineup_path.append(sm.double_backslash_to_slash(fc.find_last_created_folder() + lineups[i]))
            df_lineup = pd.read_csv(lineup_path[i])
            row_count += df_lineup.shape[0] + 1  # +1 HEADER FOR EACH LINEUP WITH TIMESTAMP PROBABLY

        widgets.lineup_table.setRowCount(row_count)
        widgets.lineup_table.setColumnCount(3)
        widgets.lineup_table.setHorizontalHeaderLabels(['id', 'Name', 'Positions'])
        y = 0
        for lineup in lineup_path:
            df_lineup = pd.read_csv(lineup)
            for i in range(df_lineup.shape[0]):
                widgets.lineup_table.setItem(y, 0, QTableWidgetItem(str(df_lineup['id'].iloc[i])))
                widgets.lineup_table.setItem(y, 1, QTableWidgetItem(str(df_lineup['name'].iloc[i])))
                widgets.lineup_table.setItem(y, 2, QTableWidgetItem(df_lineup['positions'].iloc[i]))
                y += 1
            widgets.lineup_table.setItem(y, 0, QTableWidgetItem('⚽⚽⚽⚽'))
            widgets.lineup_table.setItem(y, 1, QTableWidgetItem('Next Lineup'))
            widgets.lineup_table.setItem(y, 2, QTableWidgetItem('⚽⚽⚽⚽'))
            y += 1

    # -----------------------------------------------------------------------------------------------------------------
    # ***HANDLE DOWNLOAD REQUESTS FROM WEBSITE***
    # -----------------------------------------------------------------------------------------------------------------
    def on_downloadRequested(self, download):
        download.accept()

    # -----------------------------------------------------------------------------------------------------------------
    # ***RESIZE EVENTS***
    # -----------------------------------------------------------------------------------------------------------------
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# MAIN
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))
    window = MainWindow()
    sys.exit(app.exec())
