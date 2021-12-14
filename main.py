# IMPORT LIBRARIES
import sys
import os
import platform

# IMPORT PYTHON CLASSES
import save_data

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
local_video_page = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global local_video_page
        local_video_page = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Sports Analysis App Name"
        description = "Sports Analysis Slogan"
        # APPLY TEXTS
        self.setWindowTitle(title)
        local_video_page.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        local_video_page.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # local_video_page.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ////////////////////////////////////////////////////////
        local_video_page.btn_local_footage.clicked.connect(self.buttonClick)
        local_video_page.video_file_button.clicked.connect(self.buttonClick)

        # LOCAL VIDEO EMBED BUTTONS PAGE
        local_video_page.previous_page_button_1.clicked.connect(self.buttonClick)
        local_video_page.next_page_button_1.clicked.connect(self.buttonClick)

        # LEFT MENU BUTTONS
        local_video_page.btn_home.clicked.connect(self.buttonClick)
        local_video_page.btn_import_video.clicked.connect(self.buttonClick)

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
        local_video_page.btn_home.setStyleSheet(UIFunctions.selectMenu(local_video_page.btn_home.styleSheet()))
        local_video_page.stackedWidget.setCurrentWidget(local_video_page.home)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            local_video_page.stackedWidget.setCurrentWidget(local_video_page.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_import_video":
            local_video_page.stackedWidget.setCurrentWidget(local_video_page.video_option_menu)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # SHOW VIDEO FROM HARD-DRIVE PAGE
        if btnName == "btn_local_footage":
            local_video_page.stackedWidget.setCurrentWidget(local_video_page.local_video_page)

        # OPEN FILE EXPLORER ON WHEN CLICKING THE LOCAL VIDEO IMPORT
        if btnName == "video_file_button":
            fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:/Users/gsak3/Documents/Projects/v5/',
                                                'MP4 Files (*mp4)')
            local_video_page.video_file_name.setText(fname[0])

        if btnName == "next_page_button_1":
            save_data.save_pre_local_video_data(local_video_page.calendarWidget.selectedDate(),
                                                local_video_page.spots_type_combobox.currentText(),
                                                local_video_page.season_input.text(),
                                                local_video_page.competition_input.text(),
                                                local_video_page.details_input.toPlainText(),
                                                local_video_page.video_file_name.text())

        if btnName == "previous_page_button_1":
            local_video_page.stackedWidget.setCurrentWidget(local_video_page.video_option_menu)

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
