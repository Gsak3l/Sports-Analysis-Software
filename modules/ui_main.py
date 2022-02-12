# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
                               QGridLayout, QHBoxLayout, QHeaderView, QLabel,
                               QLineEdit, QMainWindow, QPlainTextEdit, QProgressBar,
                               QPushButton, QSizePolicy, QSlider, QStackedWidget,
                               QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
                               QWidget, QAbstractItemView)
from .resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        MainWindow.setMinimumSize(QSize(900, 800))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(
            u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "\n"
            "SET APP STYLESHEET - FULL STYLES HERE\n"
            "DARK THEME - DRACULA COLOR BASED\n"
            "\n"
            "///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
            "\n"
            "QWidget{\n"
            "	color: rgb(221, 221, 221);\n"
            "	font: 10pt \"Segoe UI\";\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Tooltip */\n"
            "QToolTip {\n"
            "	color: #ffffff;\n"
            "	background-color: rgba(33, 37, 43, 180);\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "	background-image: none;\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 2px solid rgb(255, 121, 198);\n"
            "	text-align: left;\n"
            "	padding-left: 8px;\n"
            "	margin: 0px;\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Bg App */\n"
            "#bgApp {	\n"
            "	background"
            "-color: rgb(40, 44, 52);\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Left Menu */\n"
            "#leftMenuBg {	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#topLogo {\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	background-image: url(:/images/images/images/PyDracula.png);\n"
            "	background-position: centered;\n"
            "	background-repeat: no-repeat;\n"
            "}\n"
            "#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
            "#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
            "\n"
            "/* MENUS */\n"
            "#topMenu .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid transparent;\n"
            "	background-color: transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#topMenu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#topMenu .QPushButton:pressed {	\n"
            "	background-color: rgb(18"
            "9, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "#bottomMenu .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 20px solid transparent;\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#bottomMenu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#bottomMenu .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "#leftMenuFrame{\n"
            "	border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Toggle Button */\n"
            "#toggleButton {\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 20px solid transparent;\n"
            "	background-color: rgb(37, 41, 48);\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "	color: rgb(113, 126, 149);\n"
            "}\n"
            "#toggleButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#toggleButton:pressed {\n"
            "	background-color: rgb("
            "189, 147, 249);\n"
            "}\n"
            "\n"
            "/* Title Menu */\n"
            "#titleRightInfo { padding-left: 10px; }\n"
            "\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Extra Tab */\n"
            "#extraLeftBox {	\n"
            "	background-color: rgb(44, 49, 58);\n"
            "}\n"
            "#extraTopBg{	\n"
            "	background-color: rgb(189, 147, 249)\n"
            "}\n"
            "\n"
            "/* Icon */\n"
            "#extraIcon {\n"
            "	background-position: center;\n"
            "	background-repeat: no-repeat;\n"
            "	background-image: url(:/icons/images/icons/icon_settings.png);\n"
            "}\n"
            "\n"
            "/* Label */\n"
            "#extraLabel { color: rgb(255, 255, 255); }\n"
            "\n"
            "/* Btn Close */\n"
            "#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
            "#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "/* Extra Content */\n"
            "#extraContent{\n"
            "	border"
            "-top: 3px solid rgb(40, 44, 52);\n"
            "}\n"
            "\n"
            "/* Extra Top Menus */\n"
            "#extraTopMenu .QPushButton {\n"
            "background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid transparent;\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#extraTopMenu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#extraTopMenu .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Content App */\n"
            "#contentTopBg{	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#contentBottom{\n"
            "	border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Top Buttons */\n"
            "#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
            "le: solid; border-radius: 4px; }\n"
            "#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "/* Theme Settings */\n"
            "#extraRightBox { background-color: rgb(44, 49, 58); }\n"
            "#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
            "\n"
            "/* Bottom Bar */\n"
            "#bottomBar { background-color: rgb(44, 49, 58); }\n"
            "#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
            "\n"
            "/* CONTENT SETTINGS */\n"
            "/* MENUS */\n"
            "#contentSettings .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid transparent;\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#contentSettings .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#contentSettings .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb"
            "(255, 255, 255);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "QTableWidget */\n"
            "QTableWidget {	\n"
            "	background-color: transparent;\n"
            "	padding: 10px;\n"
            "	border-radius: 5px;\n"
            "	gridline-color: rgb(44, 49, 58);\n"
            "	border-bottom: 1px solid rgb(44, 49, 60);\n"
            "}\n"
            "QTableWidget::item{\n"
            "	border-color: rgb(44, 49, 60);\n"
            "	padding-left: 5px;\n"
            "	padding-right: 5px;\n"
            "	gridline-color: rgb(44, 49, 60);\n"
            "}\n"
            "QTableWidget::item:selected{\n"
            "	background-color: rgb(189, 147, 249);\n"
            "}\n"
            "QHeaderView::section{\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	max-width: 30px;\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "	border-style: none;\n"
            "    border-bottom: 1px solid rgb(44, 49, 60);\n"
            "    border-right: 1px solid rgb(44, 49, 60);\n"
            "}\n"
            "QTableWidget::horizontalHeader {	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "QHeaderView::section:horizontal\n"
            "{\n"
            "    border: 1px solid rgb(33, 37, 43);\n"
            "	background-co"
            "lor: rgb(33, 37, 43);\n"
            "	padding: 3px;\n"
            "	border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "}\n"
            "QHeaderView::section:vertical\n"
            "{\n"
            "    border: 1px solid rgb(44, 49, 60);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "LineEdit */\n"
            "QLineEdit {\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(33, 37, 43);\n"
            "	padding-left: 10px;\n"
            "	selection-color: rgb(255, 255, 255);\n"
            "	selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "PlainTextEdit */\n"
            "QPlainTextEdit {\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	padding: 10px;\n"
            "	selection-color: rgb(255, 255, 255);\n"
            "	selection-background-c"
            "olor: rgb(255, 121, 198);\n"
            "}\n"
            "QPlainTextEdit  QScrollBar:vertical {\n"
            "    width: 8px;\n"
            " }\n"
            "QPlainTextEdit  QScrollBar:horizontal {\n"
            "    height: 8px;\n"
            " }\n"
            "QPlainTextEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QPlainTextEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "ScrollBars */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    height: 8px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "	border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: rgb(189, 147, 249);\n"
            "    min-width: 25px;\n"
            "	border-radius: 4px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-right-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            ""
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-left-radius: 4px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "	border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 8px;\n"
            "    margin: 21px 0 21px 0;\n"
            "	border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {	\n"
            "	background: rgb(189, 147, 249);\n"
            "    min-height: 25px;\n"
            "	border-radius: 4px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-bottom-left-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "     subcontrol-position: bottom;\n"
            "     su"
            "bcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "	border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-top-left-radius: 4px;\n"
            "    border-top-right-radius: 4px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "CheckBox */\n"
            "QCheckBox::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QCheckBox::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "    background: 3px solid rgb(52, 59, 72);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "	back"
            "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "RadioButton */\n"
            "QRadioButton::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QRadioButton::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QRadioButton::indicator:checked {\n"
            "    background: 3px solid rgb(94, 106, 130);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "ComboBox */\n"
            "QComboBox{\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(33, 37, 43);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;\n"
            "}\n"
            "QComboBox:hover{\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "	subcontrol-origin: padding;\n"
            "	subco"
            "ntrol-position: top right;\n"
            "	width: 25px; \n"
            "	border-left-width: 3px;\n"
            "	border-left-color: rgba(39, 44, 54, 150);\n"
            "	border-left-style: solid;\n"
            "	border-top-right-radius: 3px;\n"
            "	border-bottom-right-radius: 3px;	\n"
            "	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
            "	background-position: center;\n"
            "	background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "	color: rgb(255, 121, 198);	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	padding: 10px;\n"
            "	selection-background-color: rgb(39, 44, 54);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Sliders */\n"
            "QSlider::groove:horizontal {\n"
            "    border-radius: 5px;\n"
            "    height: 10px;\n"
            "	margin: 0px;\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:horizontal:hover {\n"
            "	background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:horizontal {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "    border: none;\n"
            "    h"
            "eight: 10px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "QSlider::handle:horizontal:hover {\n"
            "    background-color: rgb(195, 155, 255);\n"
            "}\n"
            "QSlider::handle:horizontal:pressed {\n"
            "    background-color: rgb(255, 121, 198);\n"
            "}\n"
            "\n"
            "QSlider::groove:vertical {\n"
            "    border-radius: 5px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:vertical:hover {\n"
            "	background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:vertical {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "	border: none;\n"
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "QSlider::handle:vertical:hover {\n"
            "    background-color: rgb(195, 155, 255);\n"
            "}\n"
            "QSlider::handle:vertical:pressed {\n"
            "    background-color: rgb(255, 121, 198);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "CommandLinkButton */\n"
            "QCommandLi"
            "nkButton {	\n"
            "	color: rgb(255, 121, 198);\n"
            "	border-radius: 5px;\n"
            "	padding: 5px;\n"
            "	color: rgb(255, 170, 255);\n"
            "}\n"
            "QCommandLinkButton:hover {	\n"
            "	color: rgb(255, 170, 255);\n"
            "	background-color: rgb(44, 49, 60);\n"
            "}\n"
            "QCommandLinkButton:pressed {	\n"
            "	color: rgb(189, 147, 249);\n"
            "	background-color: rgb(52, 58, 71);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Button */\n"
            "#pagesContainer QPushButton {\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "#pagesContainer QPushButton:hover {\n"
            "	background-color: rgb(57, 65, 80);\n"
            "	border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "#pagesContainer QPushButton:pressed {	\n"
            "	background-color: rgb(35, 40, 49);\n"
            "	border: 2px solid rgb(43, 50, 61);\n"
            "}\n"
            "\n"
            "")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image:url(:/images/images/images/ball_logo.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)

        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_import_video = QPushButton(self.topMenu)
        self.btn_import_video.setObjectName(u"btn_import_video")
        sizePolicy.setHeightForWidth(self.btn_import_video.sizePolicy().hasHeightForWidth())
        self.btn_import_video.setSizePolicy(sizePolicy)
        self.btn_import_video.setMinimumSize(QSize(0, 45))
        self.btn_import_video.setFont(font)
        self.btn_import_video.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_import_video.setLayoutDirection(Qt.LeftToRight)
        self.btn_import_video.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-image-plus.png);")

        self.verticalLayout_8.addWidget(self.btn_import_video)

        self.btn_formation = QPushButton(self.topMenu)
        self.btn_formation.setObjectName(u"btn_formation")
        sizePolicy.setHeightForWidth(self.btn_formation.sizePolicy().hasHeightForWidth())
        self.btn_formation.setSizePolicy(sizePolicy)
        self.btn_formation.setMinimumSize(QSize(0, 45))
        self.btn_formation.setFont(font)
        self.btn_formation.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_formation.setLayoutDirection(Qt.LeftToRight)
        self.btn_formation.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-people.png);")

        self.verticalLayout_8.addWidget(self.btn_formation)

        self.btn_video_player = QPushButton(self.topMenu)
        self.btn_video_player.setObjectName(u"btn_video_player")
        self.btn_video_player.setMinimumSize(QSize(0, 45))
        self.btn_video_player.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_video_player.setStyleSheet(u"background-image:url(:/icons/images/icons/cil-movie.png);")

        self.verticalLayout_8.addWidget(self.btn_video_player)

        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu)

        self.verticalLayout_3.addWidget(self.leftMenuFrame)

        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"font-weight:bold;\n"
                                          "font-size:18px;")
        self.titleRightInfo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)

        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.themeBtn = QToolButton(self.rightButtons)
        self.themeBtn.setObjectName(u"themeBtn")
        self.themeBtn.setStyleSheet(u"background-color: transparent;\n"
                                    "border:none;")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-lightbulb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.themeBtn.setIcon(icon)
        self.themeBtn.setIconSize(QSize(20, 20))
        self.themeBtn.setCheckable(False)
        self.themeBtn.setChecked(False)

        self.horizontalLayout_2.addWidget(self.themeBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)

        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image:url(:/images/images/images/logo640x320.png);\n"
                                "background-position: center;\n"
                                "background-repeat: no-repeat;\n"
                                "")
        self.stackedWidget.addWidget(self.home)
        self.local_video_page = QWidget()
        self.local_video_page.setObjectName(u"local_video_page")
        self.local_video_page.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.local_video_page)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.local_video_page)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_11 = QFrame(self.row_1)
        self.frame_div_content_11.setObjectName(u"frame_div_content_11")
        self.frame_div_content_11.setMinimumSize(QSize(0, 110))
        self.frame_div_content_11.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_11.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_11)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_11 = QFrame(self.frame_div_content_11)
        self.frame_title_wid_11.setObjectName(u"frame_title_wid_11")
        self.frame_title_wid_11.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_11.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_181 = QVBoxLayout(self.frame_title_wid_11)
        self.verticalLayout_181.setObjectName(u"verticalLayout_181")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_11)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_181.addWidget(self.labelBoxBlenderInstalation)

        self.verticalLayout_17.addWidget(self.frame_title_wid_11)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_11)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout1 = QGridLayout()
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.gridLayout1.setContentsMargins(-1, -1, -1, 0)
        self.local_video_file_button = QPushButton(self.frame_content_wid_1)
        self.local_video_file_button.setObjectName(u"local_video_file_button")
        self.local_video_file_button.setMinimumSize(QSize(150, 30))
        self.local_video_file_button.setFont(font)
        self.local_video_file_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.local_video_file_button.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.local_video_file_button.setIcon(icon4)

        self.gridLayout1.addWidget(self.local_video_file_button, 0, 1, 1, 1)

        self.local_video_file_name = QLineEdit(self.frame_content_wid_1)
        self.local_video_file_name.setObjectName(u"local_video_file_name")
        self.local_video_file_name.setMinimumSize(QSize(0, 30))
        self.local_video_file_name.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout1.addWidget(self.local_video_file_name, 0, 0, 1, 1)

        self.horizontalLayout_9.addLayout(self.gridLayout1)

        self.verticalLayout_17.addWidget(self.frame_content_wid_1)

        self.verticalLayout_16.addWidget(self.frame_div_content_11)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.local_competition_input = QLineEdit(self.row_1)
        self.local_competition_input.setObjectName(u"local_competition_input")
        self.local_competition_input.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.local_competition_input, 1, 1, 1, 1)

        self.local_season_input = QLineEdit(self.row_1)
        self.local_season_input.setObjectName(u"local_season_input")
        self.local_season_input.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.local_season_input, 1, 0, 1, 1)

        self.local_sports_type_combobox = QComboBox(self.row_1)
        self.local_sports_type_combobox.addItem("")
        self.local_sports_type_combobox.addItem("")
        self.local_sports_type_combobox.addItem("")
        self.local_sports_type_combobox.addItem("")
        self.local_sports_type_combobox.addItem("")
        self.local_sports_type_combobox.setObjectName(u"local_sports_type_combobox")
        self.local_sports_type_combobox.setMinimumSize(QSize(0, 25))
        self.local_sports_type_combobox.setEditable(False)

        self.gridLayout_2.addWidget(self.local_sports_type_combobox, 0, 0, 1, 2)

        self.verticalLayout_16.addLayout(self.gridLayout_2)

        self.verticalLayout.addWidget(self.row_1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.local_details_input = QPlainTextEdit(self.local_video_page)
        self.local_details_input.setObjectName(u"local_details_input")

        self.gridLayout_3.addWidget(self.local_details_input, 0, 0, 1, 1)

        self.local_calendar = QCalendarWidget(self.local_video_page)
        self.local_calendar.setObjectName(u"local_calendar")
        self.local_calendar.setStyleSheet(u"QCalendarWidget QAbstractItemView{\n"
                                          "	background-color: #21252b; \n"
                                          "	selection-background-color: #bd93f9;\n"
                                          "	selection-color: #21252b; \n"
                                          "}\n"
                                          "QCalendarWidget QWidget {background-color:#21252b;}\n"
                                          "QCalendarWidget QTableView{background-color:#21252b;}")
        self.local_calendar.setHorizontalHeaderFormat(QCalendarWidget.NoHorizontalHeader)
        self.local_calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        self.gridLayout_3.addWidget(self.local_calendar, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.local_previous_page_button = QPushButton(self.local_video_page)
        self.local_previous_page_button.setObjectName(u"local_previous_page_button")
        self.local_previous_page_button.setMaximumSize(QSize(80, 80))
        self.local_previous_page_button.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                                      "::active{border:none}")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/images/previous_purple.png", QSize(), QIcon.Normal, QIcon.Off)
        self.local_previous_page_button.setIcon(icon5)
        self.local_previous_page_button.setIconSize(QSize(48, 48))

        self.horizontalLayout_7.addWidget(self.local_previous_page_button, 0, Qt.AlignLeft)

        self.local_next_page_button = QPushButton(self.local_video_page)
        self.local_next_page_button.setObjectName(u"local_next_page_button")
        self.local_next_page_button.setMaximumSize(QSize(80, 80))
        self.local_next_page_button.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                                  "::active{border:none}")
        icon6 = QIcon()
        icon6.addFile(u":/images/images/images/next_purple.png", QSize(), QIcon.Normal, QIcon.Off)
        self.local_next_page_button.setIcon(icon6)
        self.local_next_page_button.setIconSize(QSize(48, 48))

        self.horizontalLayout_7.addWidget(self.local_next_page_button, 0, Qt.AlignRight)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.stackedWidget.addWidget(self.local_video_page)
        self.cloud_video_page = QWidget()
        self.cloud_video_page.setObjectName(u"cloud_video_page")
        self.cloud_video_page.setStyleSheet(u"b")
        self.verticalLayout1 = QVBoxLayout(self.cloud_video_page)
        self.verticalLayout1.setSpacing(10)
        self.verticalLayout1.setObjectName(u"verticalLayout1")
        self.verticalLayout1.setContentsMargins(10, 10, 10, 10)
        self.row_11 = QFrame(self.cloud_video_page)
        self.row_11.setObjectName(u"row_11")
        self.row_11.setFrameShape(QFrame.StyledPanel)
        self.row_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.row_11)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_11)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_171.setSpacing(0)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.verticalLayout_171.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation1 = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation1.setObjectName(u"labelBoxBlenderInstalation1")
        self.labelBoxBlenderInstalation1.setFont(font)
        self.labelBoxBlenderInstalation1.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation1)

        self.verticalLayout_171.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_11 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_11.setObjectName(u"frame_content_wid_11")
        self.frame_content_wid_11.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_content_wid_11)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.cloud_video_file_name = QLineEdit(self.frame_content_wid_11)
        self.cloud_video_file_name.setObjectName(u"cloud_video_file_name")
        self.cloud_video_file_name.setMinimumSize(QSize(0, 30))
        self.cloud_video_file_name.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.cloud_video_file_name, 0, 0, 1, 1)

        self.cloud_video_file_button = QPushButton(self.frame_content_wid_11)
        self.cloud_video_file_button.setObjectName(u"cloud_video_file_button")
        self.cloud_video_file_button.setMinimumSize(QSize(150, 30))
        self.cloud_video_file_button.setFont(font)
        self.cloud_video_file_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cloud_video_file_button.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-cloud-download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cloud_video_file_button.setIcon(icon7)

        self.gridLayout.addWidget(self.cloud_video_file_button, 0, 1, 1, 1)

        self.cloud_progress_bar = QProgressBar(self.frame_content_wid_11)
        self.cloud_progress_bar.setObjectName(u"cloud_progress_bar")
        self.cloud_progress_bar.setStyleSheet(u"QProgressBar {\n"
                                              "     border: 2px solid #BD93F9;\n"
                                              "     border-radius: 5px;\n"
                                              "     background-color: #21252b;\n"
                                              "	 text-align: center;\n"
                                              "	 font-weight: bold;\n"
                                              " }\n"
                                              "\n"
                                              " QProgressBar::chunk {\n"
                                              "     background-color: #BD93F9;\n"
                                              " }")
        self.cloud_progress_bar.setValue(0)
        self.cloud_progress_bar.setTextVisible(False)
        self.cloud_progress_bar.setOrientation(Qt.Horizontal)
        self.cloud_progress_bar.setInvertedAppearance(False)
        self.cloud_progress_bar.setTextDirection(QProgressBar.BottomToTop)

        self.gridLayout.addWidget(self.cloud_progress_bar, 1, 0, 1, 2)

        self.horizontalLayout_91.addLayout(self.gridLayout)

        self.verticalLayout_171.addWidget(self.frame_content_wid_11)

        self.verticalLayout_161.addWidget(self.frame_div_content_1)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setSpacing(6)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.cloud_competition_input = QLineEdit(self.row_11)
        self.cloud_competition_input.setObjectName(u"cloud_competition_input")
        self.cloud_competition_input.setMinimumSize(QSize(0, 30))

        self.gridLayout_21.addWidget(self.cloud_competition_input, 1, 1, 1, 1)

        self.cloud_season_input = QLineEdit(self.row_11)
        self.cloud_season_input.setObjectName(u"cloud_season_input")
        self.cloud_season_input.setMinimumSize(QSize(0, 30))

        self.gridLayout_21.addWidget(self.cloud_season_input, 1, 0, 1, 1)

        self.cloud_sports_type_combobox = QComboBox(self.row_11)
        self.cloud_sports_type_combobox.addItem("")
        self.cloud_sports_type_combobox.addItem("")
        self.cloud_sports_type_combobox.addItem("")
        self.cloud_sports_type_combobox.addItem("")
        self.cloud_sports_type_combobox.addItem("")
        self.cloud_sports_type_combobox.setObjectName(u"cloud_sports_type_combobox")
        self.cloud_sports_type_combobox.setMinimumSize(QSize(0, 25))
        self.cloud_sports_type_combobox.setEditable(False)

        self.gridLayout_21.addWidget(self.cloud_sports_type_combobox, 0, 0, 1, 2)

        self.verticalLayout_161.addLayout(self.gridLayout_21)

        self.verticalLayout1.addWidget(self.row_11)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.cloud_details_input = QPlainTextEdit(self.cloud_video_page)
        self.cloud_details_input.setObjectName(u"cloud_details_input")

        self.gridLayout_31.addWidget(self.cloud_details_input, 0, 0, 1, 1)

        self.cloud_calendar = QCalendarWidget(self.cloud_video_page)
        self.cloud_calendar.setObjectName(u"cloud_calendar")
        self.cloud_calendar.setStyleSheet(u"QCalendarWidget QAbstractItemView{\n"
                                          "	background-color: #21252b; \n"
                                          "	selection-background-color: #bd93f9;\n"
                                          "	selection-color: #21252b; \n"
                                          "}\n"
                                          "QCalendarWidget QWidget {background-color:#21252b;}\n"
                                          "QCalendarWidget QTableView{background-color:#21252b;}")
        self.cloud_calendar.setGridVisible(False)
        self.cloud_calendar.setHorizontalHeaderFormat(QCalendarWidget.NoHorizontalHeader)
        self.cloud_calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.cloud_calendar.setNavigationBarVisible(True)
        self.cloud_calendar.setDateEditEnabled(True)

        self.gridLayout_31.addWidget(self.cloud_calendar, 0, 1, 1, 1)

        self.verticalLayout1.addLayout(self.gridLayout_31)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.cloud_previous_page_button = QPushButton(self.cloud_video_page)
        self.cloud_previous_page_button.setObjectName(u"cloud_previous_page_button")
        self.cloud_previous_page_button.setMaximumSize(QSize(80, 60))
        self.cloud_previous_page_button.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                                      "::active{border:none}")
        self.cloud_previous_page_button.setIcon(icon5)
        self.cloud_previous_page_button.setIconSize(QSize(48, 48))

        self.horizontalLayout_71.addWidget(self.cloud_previous_page_button, 0, Qt.AlignLeft)

        self.cloud_next_page_button = QPushButton(self.cloud_video_page)
        self.cloud_next_page_button.setObjectName(u"cloud_next_page_button")
        self.cloud_next_page_button.setMaximumSize(QSize(80, 60))
        self.cloud_next_page_button.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                                  "::active{border:none}")
        self.cloud_next_page_button.setIcon(icon6)
        self.cloud_next_page_button.setIconSize(QSize(48, 48))

        self.horizontalLayout_71.addWidget(self.cloud_next_page_button, 0, Qt.AlignRight)

        self.verticalLayout1.addLayout(self.horizontalLayout_71)

        self.stackedWidget.addWidget(self.cloud_video_page)
        self.tactics_page = QWidget()
        self.tactics_page.setObjectName(u"tactics_page")
        self.tactics_page.setStyleSheet(u"b")
        self.verticalLayout2 = QVBoxLayout(self.tactics_page)
        self.verticalLayout2.setSpacing(10)
        self.verticalLayout2.setObjectName(u"verticalLayout2")
        self.verticalLayout2.setContentsMargins(10, 10, 10, 10)
        self.formation = QWebEngineView(self.tactics_page)
        self.formation.setObjectName(u"formation")

        self.verticalLayout2.addWidget(self.formation)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.formation_previous_page_button = QPushButton(self.tactics_page)
        self.formation_previous_page_button.setObjectName(u"formation_previous_page_button")
        self.formation_previous_page_button.setMaximumSize(QSize(80, 60))
        self.formation_previous_page_button.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                                          "::active{border:none}")
        self.formation_previous_page_button.setIcon(icon5)
        self.formation_previous_page_button.setIconSize(QSize(48, 48))

        self.horizontalLayout_17.addWidget(self.formation_previous_page_button, 0, Qt.AlignLeft)

        self.formation_next_page_button = QPushButton(self.tactics_page)
        self.formation_next_page_button.setObjectName(u"formation_next_page_button")
        self.formation_next_page_button.setMaximumSize(QSize(80, 60))
        self.formation_next_page_button.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                                      "::active{border:none}")
        self.formation_next_page_button.setIcon(icon6)
        self.formation_next_page_button.setIconSize(QSize(48, 48))

        self.horizontalLayout_17.addWidget(self.formation_next_page_button, 0, Qt.AlignRight)

        self.verticalLayout2.addLayout(self.horizontalLayout_17)

        self.stackedWidget.addWidget(self.tactics_page)
        self.video_page = QWidget()
        self.video_page.setObjectName(u"video_page")
        self.video_page.setStyleSheet(u"b")
        self.verticalLayout21 = QVBoxLayout(self.video_page)
        self.verticalLayout21.setSpacing(10)
        self.verticalLayout21.setObjectName(u"verticalLayout21")
        self.verticalLayout21.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.return_to_lineup_builder = QPushButton(self.video_page)
        self.return_to_lineup_builder.setObjectName(u"return_to_lineup_builder")
        self.return_to_lineup_builder.setMaximumSize(QSize(80, 16777215))
        self.return_to_lineup_builder.setSizeIncrement(QSize(50, 0))
        self.return_to_lineup_builder.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                                    "::active{border:none}")
        icon8 = QIcon()
        icon8.addFile(u":/images/images/images/swap_players.png", QSize(), QIcon.Normal, QIcon.Off)
        self.return_to_lineup_builder.setIcon(icon8)
        self.return_to_lineup_builder.setIconSize(QSize(64, 64))

        self.horizontalLayout_11.addWidget(self.return_to_lineup_builder)

        self.zoom_into_player_button = QPushButton(self.video_page)
        self.zoom_into_player_button.setObjectName(u"zoom_into_player_button")
        self.zoom_into_player_button.setMaximumSize(QSize(80, 16777215))
        self.zoom_into_player_button.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                                   "::active{border:none}")
        icon9 = QIcon()
        icon9.addFile(u":/images/images/images/zoom-buttons.png", QSize(), QIcon.Normal, QIcon.Off)
        self.zoom_into_player_button.setIcon(icon9)
        self.zoom_into_player_button.setIconSize(QSize(64, 64))

        self.horizontalLayout_11.addWidget(self.zoom_into_player_button)

        self.player_zoom_selection_lineedit = QLineEdit(self.video_page)
        self.player_zoom_selection_lineedit.setObjectName(u"player_zoom_selection_lineedit")
        self.player_zoom_selection_lineedit.setMinimumSize(QSize(0, 32))
        self.player_zoom_selection_lineedit.setMaximumSize(QSize(40, 16777215))
        self.player_zoom_selection_lineedit.setStyleSheet(u"background-color:#bd93f9 ;\n"
                                                          "font-weight:bold;\n"
                                                          "color:#fff;")

        self.horizontalLayout_11.addWidget(self.player_zoom_selection_lineedit)

        self.player_names_combobox = QComboBox(self.video_page)
        self.player_names_combobox.setObjectName(u"player_names_combobox")
        self.player_names_combobox.setStyleSheet(u"background-color:#bd93f9 ;\n"
                                                 "font-weight:bold;\n"
                                                 "color:#fff;\n"
                                                 "border:none;")

        self.horizontalLayout_11.addWidget(self.player_names_combobox)

        self.type_of_action_combobox = QComboBox(self.video_page)
        self.type_of_action_combobox.addItem("")
        self.type_of_action_combobox.addItem("")
        self.type_of_action_combobox.addItem("")
        self.type_of_action_combobox.setObjectName(u"type_of_action_combobox")
        self.type_of_action_combobox.setStyleSheet(u"background-color:#bd93f9 ;\n"
                                                   "font-weight:bold;\n"
                                                   "color:#fff;")

        self.horizontalLayout_11.addWidget(self.type_of_action_combobox)

        self.action_combobox = QComboBox(self.video_page)
        self.action_combobox.setObjectName(u"action_combobox")
        self.action_combobox.setStyleSheet(u"background-color:#bd93f9 ;\n"
                                           "font-weight:bold;\n"
                                           "color:#fff;")

        self.horizontalLayout_11.addWidget(self.action_combobox)

        self.add_action = QPushButton(self.video_page)
        self.add_action.setObjectName(u"add_action")
        self.add_action.setMaximumSize(QSize(50, 16777215))
        self.add_action.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_action.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                      "::active{border:none}")
        icon10 = QIcon()
        icon10.addFile(u":/images/images/images/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_action.setIcon(icon10)
        self.add_action.setIconSize(QSize(40, 40))

        self.horizontalLayout_11.addWidget(self.add_action)

        self.od_combobox = QComboBox(self.video_page)
        self.od_combobox.addItem("")
        self.od_combobox.addItem("")
        self.od_combobox.addItem("")
        self.od_combobox.setObjectName(u"od_combobox")
        self.od_combobox.setStyleSheet(u"background-color:#bd93f9 ;\n"
                                       "font-weight:bold;\n"
                                       "color:#fff;")

        self.horizontalLayout_11.addWidget(self.od_combobox)

        self.od_timestamps_combobox = QComboBox(self.video_page)
        self.od_timestamps_combobox.setObjectName(u"od_timestamps_combobox")
        self.od_timestamps_combobox.setMaximumSize(QSize(100, 16777215))
        self.od_timestamps_combobox.setStyleSheet(u"background-color:#bd93f9 ;\n"
                                                  "font-weight:bold;\n"
                                                  "color:#fff;\n"
                                                  "width:70%")

        self.horizontalLayout_11.addWidget(self.od_timestamps_combobox)

        self.verticalLayout21.addLayout(self.horizontalLayout_11)

        self.video_player = QVideoWidget(self.video_page)
        self.video_player.setObjectName(u"video_player")

        self.verticalLayout21.addWidget(self.video_player)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.play_video_button = QPushButton(self.video_page)
        self.play_video_button.setObjectName(u"play_video_button")
        self.play_video_button.setMaximumSize(QSize(80, 16777215))
        self.play_video_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.play_video_button.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                             "::active{border:none}")
        icon11 = QIcon()
        icon11.addFile(u":/images/images/images/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_video_button.setIcon(icon11)
        self.play_video_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.play_video_button)

        self.pause_video_button = QPushButton(self.video_page)
        self.pause_video_button.setObjectName(u"pause_video_button")
        self.pause_video_button.setMaximumSize(QSize(80, 16777215))
        self.pause_video_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.pause_video_button.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                              "::active{border:none}")
        icon12 = QIcon()
        icon12.addFile(u":/images/images/images/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_video_button.setIcon(icon12)
        self.pause_video_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.pause_video_button)

        self.stop_video_button = QPushButton(self.video_page)
        self.stop_video_button.setObjectName(u"stop_video_button")
        self.stop_video_button.setMaximumSize(QSize(80, 16777215))
        self.stop_video_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_video_button.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                             "::active{border:none}")
        icon13 = QIcon()
        icon13.addFile(u":/images/images/images/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_video_button.setIcon(icon13)
        self.stop_video_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.stop_video_button)

        self.playback_speed_combo = QComboBox(self.video_page)
        self.playback_speed_combo.addItem("")
        self.playback_speed_combo.addItem("")
        self.playback_speed_combo.addItem("")
        self.playback_speed_combo.addItem("")
        self.playback_speed_combo.addItem("")
        self.playback_speed_combo.addItem("")
        self.playback_speed_combo.addItem("")
        self.playback_speed_combo.addItem("")
        self.playback_speed_combo.setObjectName(u"playback_speed_combo")
        self.playback_speed_combo.setStyleSheet(u"background-color:#bd93f9 ;\n"
                                                "font-weight:bold;\n"
                                                "color:#fff;")

        self.horizontalLayout_8.addWidget(self.playback_speed_combo)

        self.video_player_progress_bar = QProgressBar(self.video_page)
        self.video_player_progress_bar.setObjectName(u"video_player_progress_bar")
        self.video_player_progress_bar.setStyleSheet(u"QProgressBar {\n"
                                                     "     border: 2px solid #BD93F9;\n"
                                                     "     border-radius: 5px;\n"
                                                     "     background-color: #21252b;\n"
                                                     "	 text-align: center;\n"
                                                     "	 font-weight: bold;\n"
                                                     " }\n"
                                                     "\n"
                                                     " QProgressBar::chunk {\n"
                                                     "     background-color: #BD93F9;\n"
                                                     " }")
        self.video_player_progress_bar.setMinimum(1)
        self.video_player_progress_bar.setValue(1)

        self.horizontalLayout_8.addWidget(self.video_player_progress_bar)

        self.video_player_slider = QSlider(self.video_page)
        self.video_player_slider.setObjectName(u"video_player_slider")
        self.video_player_slider.setFont(font)
        self.video_player_slider.setCursor(QCursor(Qt.OpenHandCursor))
        self.video_player_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
                                               "    width: 50px;\n"
                                               "}")
        self.video_player_slider.setMinimum(1)
        self.video_player_slider.setMaximum(100)
        self.video_player_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.video_player_slider)

        self.show_post_game_button = QPushButton(self.video_page)
        self.show_post_game_button.setObjectName(u"show_post_game_button")
        self.show_post_game_button.setMaximumSize(QSize(80, 16777215))
        self.show_post_game_button.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                                 "::active{border:none}")
        icon14 = QIcon()
        icon14.addFile(u":/images/images/images/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.show_post_game_button.setIcon(icon14)
        self.show_post_game_button.setIconSize(QSize(64, 64))

        self.horizontalLayout_8.addWidget(self.show_post_game_button)

        self.verticalLayout21.addLayout(self.horizontalLayout_8)

        self.stackedWidget.addWidget(self.video_page)
        self.video_option_menu = QWidget()
        self.video_option_menu.setObjectName(u"video_option_menu")
        self.verticalLayout_20 = QVBoxLayout(self.video_option_menu)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_local_footage = QPushButton(self.video_option_menu)
        self.btn_local_footage.setObjectName(u"btn_local_footage")
        self.btn_local_footage.setMaximumSize(QSize(80, 80))
        self.btn_local_footage.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_local_footage.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                             "::active{border:none}")
        icon15 = QIcon()
        icon15.addFile(u":/images/images/images/folder_purple.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_local_footage.setIcon(icon15)
        self.btn_local_footage.setIconSize(QSize(64, 64))
        self.btn_local_footage.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.btn_local_footage)

        self.btn_cloud_footage = QPushButton(self.video_option_menu)
        self.btn_cloud_footage.setObjectName(u"btn_cloud_footage")
        self.btn_cloud_footage.setMaximumSize(QSize(80, 80))
        self.btn_cloud_footage.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cloud_footage.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                             "::active{border:none}")
        icon16 = QIcon()
        icon16.addFile(u":/images/images/images/cloud_purple.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cloud_footage.setIcon(icon16)
        self.btn_cloud_footage.setIconSize(QSize(80, 80))

        self.horizontalLayout_6.addWidget(self.btn_cloud_footage)

        self.btn_camera_footage = QPushButton(self.video_option_menu)
        self.btn_camera_footage.setObjectName(u"btn_camera_footage")
        self.btn_camera_footage.setMaximumSize(QSize(80, 80))
        self.btn_camera_footage.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_camera_footage.setStyleSheet(u"::pressed{background-color: #ff79c6}\n"
                                              "::active{border:none}")
        icon17 = QIcon()
        icon17.addFile(u":/images/images/images/camera_purple.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_camera_footage.setIcon(icon17)
        self.btn_camera_footage.setIconSize(QSize(64, 64))

        self.horizontalLayout_6.addWidget(self.btn_camera_footage)

        self.verticalLayout_20.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.video_option_menu)
        self.post_game = QWidget()
        self.post_game.setObjectName(u"post_game")
        self.verticalLayout_21 = QVBoxLayout(self.post_game)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pregame_table = QTableWidget(self.post_game)
        self.pregame_table.setObjectName(u"pregame_table")
        self.pregame_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pregame_table.setDragEnabled(False)
        self.pregame_table.horizontalHeader().setVisible(False)
        self.pregame_table.horizontalHeader().setCascadingSectionResizes(False)
        self.pregame_table.horizontalHeader().setHighlightSections(False)
        self.pregame_table.horizontalHeader().setStretchLastSection(True)
        self.pregame_table.verticalHeader().setVisible(True)
        self.pregame_table.verticalHeader().setHighlightSections(True)
        self.pregame_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_10.addWidget(self.pregame_table)

        self.lineup_table = QTableWidget(self.post_game)
        self.lineup_table.setObjectName(u"lineup_table")
        self.lineup_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lineup_table.setDragEnabled(False)
        self.lineup_table.horizontalHeader().setVisible(True)
        self.lineup_table.horizontalHeader().setHighlightSections(False)
        self.lineup_table.horizontalHeader().setStretchLastSection(False)
        self.lineup_table.verticalHeader().setVisible(False)
        self.lineup_table.verticalHeader().setHighlightSections(False)
        self.lineup_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_10.addWidget(self.lineup_table)

        self.actions_table = QTableWidget(self.post_game)
        self.actions_table.setObjectName(u"actions_table")
        self.actions_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.actions_table.setDragEnabled(False)
        self.actions_table.horizontalHeader().setVisible(True)
        self.actions_table.horizontalHeader().setHighlightSections(False)
        self.actions_table.horizontalHeader().setStretchLastSection(True)
        self.actions_table.verticalHeader().setVisible(False)
        self.actions_table.verticalHeader().setHighlightSections(True)
        self.actions_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_10.addWidget(self.actions_table)

        self.verticalLayout_21.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.post_game)

        self.verticalLayout_15.addWidget(self.stackedWidget)

        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)

        self.verticalLayout_6.addWidget(self.bottomBar)

        self.verticalLayout_2.addWidget(self.contentBottom)

        self.appLayout.addWidget(self.contentBox)

        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)
        self.type_of_action_combobox.setCurrentIndex(2)
        self.playback_speed_combo.setCurrentIndex(3)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Advanced Software", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"for Coaches and Players", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_import_video.setText(QCoreApplication.translate("MainWindow", u"Import Video", None))
        self.btn_formation.setText(QCoreApplication.translate("MainWindow", u"Lineup Builder", None))
        self.btn_video_player.setText(QCoreApplication.translate("MainWindow", u"Match Page", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Sports Analysis Software", None))
        self.themeBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        # endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        # endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        # endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"VIDEO BOX", None))
        self.local_video_file_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.local_video_file_name.setText("")
        self.local_video_file_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here...", None))
        self.local_competition_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Competition", None))
        self.local_season_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Season", None))
        self.local_sports_type_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Football", None))
        self.local_sports_type_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Baskeball", None))
        self.local_sports_type_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Volleyball", None))
        self.local_sports_type_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"Cricket", None))
        self.local_sports_type_combobox.setItemText(4, QCoreApplication.translate("MainWindow", u"Other", None))

        self.local_sports_type_combobox.setCurrentText("")
        self.local_sports_type_combobox.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Select a Sport", None))
        self.local_details_input.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"More details about the game", None))
        self.local_previous_page_button.setText("")
        self.local_next_page_button.setText("")
        self.labelBoxBlenderInstalation1.setText(QCoreApplication.translate("MainWindow", u"VIDEO BOX", None))
        self.cloud_video_file_name.setText("")
        self.cloud_video_file_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste URL here", None))
        self.cloud_video_file_button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.cloud_competition_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Competition", None))
        self.cloud_season_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Season", None))
        self.cloud_sports_type_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Football", None))
        self.cloud_sports_type_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Baskeball", None))
        self.cloud_sports_type_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Volleyball", None))
        self.cloud_sports_type_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"Cricket", None))
        self.cloud_sports_type_combobox.setItemText(4, QCoreApplication.translate("MainWindow", u"Other", None))

        self.cloud_sports_type_combobox.setCurrentText("")
        self.cloud_sports_type_combobox.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Select a Sport", None))
        self.cloud_details_input.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"More details about the game", None))
        self.cloud_previous_page_button.setText("")
        self.cloud_next_page_button.setText("")
        self.formation_previous_page_button.setText("")
        self.formation_next_page_button.setText("")
        self.return_to_lineup_builder.setText("")
        self.zoom_into_player_button.setText("")
        self.type_of_action_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Shooting Game", None))
        self.type_of_action_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Passing Game", None))
        self.type_of_action_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Defensive Game", None))

        self.add_action.setText("")
        self.od_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Offense Timestamps", None))
        self.od_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Defense Timestamps", None))
        self.od_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"In-Between", None))

        self.play_video_button.setText("")
        self.pause_video_button.setText("")
        self.stop_video_button.setText("")
        self.playback_speed_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"x0.25", None))
        self.playback_speed_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"x0.50", None))
        self.playback_speed_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"x0.75", None))
        self.playback_speed_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"x1.00", None))
        self.playback_speed_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"x1.25", None))
        self.playback_speed_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"x1.50", None))
        self.playback_speed_combo.setItemText(6, QCoreApplication.translate("MainWindow", u"x1.75", None))
        self.playback_speed_combo.setItemText(7, QCoreApplication.translate("MainWindow", u"x2.00", None))

        self.show_post_game_button.setText("")
        self.btn_local_footage.setText("")
        self.btn_cloud_footage.setText("")
        self.btn_camera_footage.setText("")
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Sakellariou G.", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v2.0.1", None))
    # retranslateUi
