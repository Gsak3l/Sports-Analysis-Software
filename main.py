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
        # ////////////////////////////////////////////////////////
        widgets.btn_local_footage.clicked.connect(self.buttonClick)
        widgets.video_file_button.clicked.connect(self.buttonClick)
        widgets.btn_cloud_footage.clicked.connect(self.buttonClick)

        # LOCAL VIDEO EMBED BUTTONS PAGE
        widgets.previous_page_button_1.clicked.connect(self.buttonClick)
        widgets.next_page_button_1.clicked.connect(self.buttonClick)

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

        elif btnName == "video_file_button":  # OPEN FILE EXPLORER ON WHEN CLICKING THE LOCAL VIDEO IMPORT
            fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:/Users/gsak3/Documents/Projects/v5/',
                                                'MP4 Files (*mp4)')
            widgets.video_file_name.setText(fname[0])

        elif btnName == "next_page_button_1":  # SAVE DATA FROM INPUT FIELDS INTO A JSON FILE
            save_data.save_pre_local_video_data(widgets.calendarWidget.selectedDate(),
                                                widgets.spots_type_combobox.currentText(),
                                                widgets.season_input.text(),
                                                widgets.competition_input.text(),
                                                widgets.details_input.toPlainText(),
                                                widgets.video_file_name.text())

        elif btnName == "previous_page_button_1":  # BUTTON THAT GOES BACK TO THE VIDEO TYPE SELECTION
            widgets.stackedWidget.setCurrentWidget(widgets.video_option_menu)
        # -------------------------------------------------------------------------------------------------------------

        # EMBED VIDEO FROM A CLOUD LINK
        elif btnName == "btn_cloud_footage":
            widgets.stackedWidget.setCurrentWidget(widgets.cloud_video_page)

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
