# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2142, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
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
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
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
"/* CHECKBOX */\n"
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
"	background-image: url(cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
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
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(facebook logo32.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setBold(True)
        font2.setWeight(75)
        self.label_top_info_2.setFont(font2)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.label_user_icon.setFont(font3)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_dives = QWidget()
        self.page_dives.setObjectName(u"page_dives")
        self.verticalLayout_10 = QVBoxLayout(self.page_dives)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.update_courses_button = QPushButton(self.page_dives)
        self.update_courses_button.setObjectName(u"update_courses_button")

        self.gridLayout_3.addWidget(self.update_courses_button, 4, 14, 1, 1)

        self.z_remove_diver_button = QPushButton(self.page_dives)
        self.z_remove_diver_button.setObjectName(u"z_remove_diver_button")

        self.gridLayout_3.addWidget(self.z_remove_diver_button, 5, 9, 1, 1)

        self.z_das_combo = QComboBox(self.page_dives)
        self.z_das_combo.setObjectName(u"z_das_combo")
        self.z_das_combo.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.z_das_combo, 3, 10, 1, 2)

        self.calendar_widget = QCalendarWidget(self.page_dives)
        self.calendar_widget.setObjectName(u"calendar_widget")

        self.gridLayout_3.addWidget(self.calendar_widget, 0, 11, 1, 3)

        self.am_das_combo = QComboBox(self.page_dives)
        self.am_das_combo.setObjectName(u"am_das_combo")
        self.am_das_combo.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.am_das_combo, 3, 1, 1, 2)

        self.am_delete_diver_entry = QLineEdit(self.page_dives)
        self.am_delete_diver_entry.setObjectName(u"am_delete_diver_entry")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.am_delete_diver_entry.sizePolicy().hasHeightForWidth())
        self.am_delete_diver_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.am_delete_diver_entry, 5, 1, 1, 1)

        self.label_6 = QLabel(self.page_dives)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 3, 3, 1, 1)

        self.label_5 = QLabel(self.page_dives)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 3, 1, 1)

        self.co_delete_diver_entry = QLineEdit(self.page_dives)
        self.co_delete_diver_entry.setObjectName(u"co_delete_diver_entry")
        sizePolicy5.setHeightForWidth(self.co_delete_diver_entry.sizePolicy().hasHeightForWidth())
        self.co_delete_diver_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.co_delete_diver_entry, 5, 13, 1, 1)

        self.zenobia_table = QTableWidget(self.page_dives)
        if (self.zenobia_table.columnCount() < 7):
            self.zenobia_table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.zenobia_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.zenobia_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.zenobia_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.zenobia_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.zenobia_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.zenobia_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.zenobia_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.zenobia_table.setObjectName(u"zenobia_table")
        self.zenobia_table.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.zenobia_table, 6, 9, 1, 3)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_16 = QLabel(self.page_dives)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_7.addWidget(self.label_16, 0, 0, 1, 1)

        self.z_print_button = QPushButton(self.page_dives)
        self.z_print_button.setObjectName(u"z_print_button")

        self.gridLayout_7.addWidget(self.z_print_button, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_7, 5, 11, 1, 1)

        self.mam_delete_diver_entry = QLineEdit(self.page_dives)
        self.mam_delete_diver_entry.setObjectName(u"mam_delete_diver_entry")
        sizePolicy5.setHeightForWidth(self.mam_delete_diver_entry.sizePolicy().hasHeightForWidth())
        self.mam_delete_diver_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.mam_delete_diver_entry, 5, 4, 1, 1)

        self.pm_dive_site_combo = QComboBox(self.page_dives)
        self.pm_dive_site_combo.setObjectName(u"pm_dive_site_combo")
        self.pm_dive_site_combo.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.pm_dive_site_combo, 2, 7, 1, 2)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.refresh_button = QPushButton(self.page_dives)
        self.refresh_button.setObjectName(u"refresh_button")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.refresh_button.sizePolicy().hasHeightForWidth())
        self.refresh_button.setSizePolicy(sizePolicy6)

        self.gridLayout_9.addWidget(self.refresh_button, 0, 0, 1, 1)

        self.todays_dive_button = QPushButton(self.page_dives)
        self.todays_dive_button.setObjectName(u"todays_dive_button")

        self.gridLayout_9.addWidget(self.todays_dive_button, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_9, 0, 14, 1, 1)

        self.label = QLabel(self.page_dives)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.add_new_course_button = QPushButton(self.page_dives)
        self.add_new_course_button.setObjectName(u"add_new_course_button")

        self.gridLayout_3.addWidget(self.add_new_course_button, 4, 13, 1, 1)

        self.update_zenobia_button = QPushButton(self.page_dives)
        self.update_zenobia_button.setObjectName(u"update_zenobia_button")

        self.gridLayout_3.addWidget(self.update_zenobia_button, 4, 11, 1, 1)

        self.label_10 = QLabel(self.page_dives)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 3, 6, 1, 1)

        self.am_remove_diver_button = QPushButton(self.page_dives)
        self.am_remove_diver_button.setObjectName(u"am_remove_diver_button")

        self.gridLayout_3.addWidget(self.am_remove_diver_button, 5, 0, 1, 1)

        self.z_dive_site_combo = QComboBox(self.page_dives)
        self.z_dive_site_combo.setObjectName(u"z_dive_site_combo")
        self.z_dive_site_combo.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.z_dive_site_combo, 2, 10, 1, 2)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.mam_print_button = QPushButton(self.page_dives)
        self.mam_print_button.setObjectName(u"mam_print_button")

        self.gridLayout_5.addWidget(self.mam_print_button, 0, 1, 1, 1)

        self.label_8 = QLabel(self.page_dives)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 5, 5, 1, 1)

        self.mam_dive_site_combo = QComboBox(self.page_dives)
        self.mam_dive_site_combo.setObjectName(u"mam_dive_site_combo")
        self.mam_dive_site_combo.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.mam_dive_site_combo, 2, 4, 1, 2)

        self.pm_delete_diver_entry = QLineEdit(self.page_dives)
        self.pm_delete_diver_entry.setObjectName(u"pm_delete_diver_entry")
        sizePolicy5.setHeightForWidth(self.pm_delete_diver_entry.sizePolicy().hasHeightForWidth())
        self.pm_delete_diver_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.pm_delete_diver_entry, 5, 7, 1, 1)

        self.label_9 = QLabel(self.page_dives)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 2, 6, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.page_dives)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.am_print_button = QPushButton(self.page_dives)
        self.am_print_button.setObjectName(u"am_print_button")

        self.gridLayout_4.addWidget(self.am_print_button, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 5, 2, 1, 1)

        self.add_new_pm_dive_button = QPushButton(self.page_dives)
        self.add_new_pm_dive_button.setObjectName(u"add_new_pm_dive_button")

        self.gridLayout_3.addWidget(self.add_new_pm_dive_button, 4, 7, 1, 1)

        self.update_am_dive_button = QPushButton(self.page_dives)
        self.update_am_dive_button.setObjectName(u"update_am_dive_button")

        self.gridLayout_3.addWidget(self.update_am_dive_button, 4, 2, 1, 1)

        self.label_2 = QLabel(self.page_dives)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)

        self.update_mid_am_dive_button = QPushButton(self.page_dives)
        self.update_mid_am_dive_button.setObjectName(u"update_mid_am_dive_button")

        self.gridLayout_3.addWidget(self.update_mid_am_dive_button, 4, 5, 1, 1)

        self.courses_table = QTableWidget(self.page_dives)
        if (self.courses_table.columnCount() < 7):
            self.courses_table.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.courses_table.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.courses_table.setObjectName(u"courses_table")
        self.courses_table.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.courses_table, 6, 12, 1, 3)

        self.pm_remove_diver_button = QPushButton(self.page_dives)
        self.pm_remove_diver_button.setObjectName(u"pm_remove_diver_button")

        self.gridLayout_3.addWidget(self.pm_remove_diver_button, 5, 6, 1, 1)

        self.update_pm_dive_button = QPushButton(self.page_dives)
        self.update_pm_dive_button.setObjectName(u"update_pm_dive_button")

        self.gridLayout_3.addWidget(self.update_pm_dive_button, 4, 8, 1, 1)

        self.label_14 = QLabel(self.page_dives)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 3, 9, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pm_print_button = QPushButton(self.page_dives)
        self.pm_print_button.setObjectName(u"pm_print_button")

        self.gridLayout_6.addWidget(self.pm_print_button, 0, 1, 1, 1)

        self.label_12 = QLabel(self.page_dives)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_6, 5, 8, 1, 1)

        self.co_das_combo = QComboBox(self.page_dives)
        self.co_das_combo.setObjectName(u"co_das_combo")
        self.co_das_combo.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.co_das_combo, 3, 13, 1, 2)

        self.ci_remove_diver_button = QPushButton(self.page_dives)
        self.ci_remove_diver_button.setObjectName(u"ci_remove_diver_button")

        self.gridLayout_3.addWidget(self.ci_remove_diver_button, 5, 12, 1, 1)

        self.am_dive_site_combo = QComboBox(self.page_dives)
        self.am_dive_site_combo.setObjectName(u"am_dive_site_combo")
        self.am_dive_site_combo.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.am_dive_site_combo, 2, 1, 1, 2)

        self.pm_dive_table = QTableWidget(self.page_dives)
        if (self.pm_dive_table.columnCount() < 7):
            self.pm_dive_table.setColumnCount(7)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.pm_dive_table.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.pm_dive_table.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.pm_dive_table.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.pm_dive_table.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.pm_dive_table.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.pm_dive_table.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.pm_dive_table.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        self.pm_dive_table.setObjectName(u"pm_dive_table")
        self.pm_dive_table.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.pm_dive_table, 6, 6, 1, 3)

        self.co_dive_site_combo = QComboBox(self.page_dives)
        self.co_dive_site_combo.setObjectName(u"co_dive_site_combo")
        self.co_dive_site_combo.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.co_dive_site_combo, 2, 13, 1, 2)

        self.label_17 = QLabel(self.page_dives)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 2, 12, 1, 1)

        self.mam_das_combo = QComboBox(self.page_dives)
        self.mam_das_combo.setObjectName(u"mam_das_combo")
        self.mam_das_combo.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.mam_das_combo, 3, 4, 1, 2)

        self.label_18 = QLabel(self.page_dives)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 3, 12, 1, 1)

        self.add_new_am_dive_button = QPushButton(self.page_dives)
        self.add_new_am_dive_button.setObjectName(u"add_new_am_dive_button")

        self.gridLayout_3.addWidget(self.add_new_am_dive_button, 4, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.co_print_button = QPushButton(self.page_dives)
        self.co_print_button.setObjectName(u"co_print_button")

        self.gridLayout_8.addWidget(self.co_print_button, 0, 1, 1, 1)

        self.label_20 = QLabel(self.page_dives)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_8.addWidget(self.label_20, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_8, 5, 14, 1, 1)

        self.mam_remove_diver_button = QPushButton(self.page_dives)
        self.mam_remove_diver_button.setObjectName(u"mam_remove_diver_button")

        self.gridLayout_3.addWidget(self.mam_remove_diver_button, 5, 3, 1, 1)

        self.add_new_zenobia_button = QPushButton(self.page_dives)
        self.add_new_zenobia_button.setObjectName(u"add_new_zenobia_button")

        self.gridLayout_3.addWidget(self.add_new_zenobia_button, 4, 10, 1, 1)

        self.add_new_mid_dive_button = QPushButton(self.page_dives)
        self.add_new_mid_dive_button.setObjectName(u"add_new_mid_dive_button")

        self.gridLayout_3.addWidget(self.add_new_mid_dive_button, 4, 4, 1, 1)

        self.pm_das_combo = QComboBox(self.page_dives)
        self.pm_das_combo.setObjectName(u"pm_das_combo")
        self.pm_das_combo.setAutoFillBackground(False)

        self.gridLayout_3.addWidget(self.pm_das_combo, 3, 7, 1, 2)

        self.z_delete_diver_entry = QLineEdit(self.page_dives)
        self.z_delete_diver_entry.setObjectName(u"z_delete_diver_entry")
        sizePolicy5.setHeightForWidth(self.z_delete_diver_entry.sizePolicy().hasHeightForWidth())
        self.z_delete_diver_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.z_delete_diver_entry, 5, 10, 1, 1)

        self.mid_am_dive_table = QTableWidget(self.page_dives)
        if (self.mid_am_dive_table.columnCount() < 7):
            self.mid_am_dive_table.setColumnCount(7)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.mid_am_dive_table.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.mid_am_dive_table.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.mid_am_dive_table.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.mid_am_dive_table.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.mid_am_dive_table.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.mid_am_dive_table.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.mid_am_dive_table.setHorizontalHeaderItem(6, __qtablewidgetitem27)
        self.mid_am_dive_table.setObjectName(u"mid_am_dive_table")
        self.mid_am_dive_table.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.mid_am_dive_table, 6, 3, 1, 3)

        self.am_dive_table = QTableWidget(self.page_dives)
        if (self.am_dive_table.columnCount() < 7):
            self.am_dive_table.setColumnCount(7)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.am_dive_table.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.am_dive_table.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.am_dive_table.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.am_dive_table.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.am_dive_table.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.am_dive_table.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.am_dive_table.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        self.am_dive_table.setObjectName(u"am_dive_table")
        self.am_dive_table.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.am_dive_table, 6, 0, 1, 3)

        self.label_13 = QLabel(self.page_dives)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 2, 9, 1, 1)

        self.label_3 = QLabel(self.page_dives)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setFamily(u"DejaVu Sans")
        font4.setPointSize(13)
        self.label_3.setFont(font4)

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_7 = QLabel(self.page_dives)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.gridLayout_3.addWidget(self.label_7, 1, 3, 1, 1)

        self.label_11 = QLabel(self.page_dives)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.gridLayout_3.addWidget(self.label_11, 1, 6, 1, 1)

        self.label_15 = QLabel(self.page_dives)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)

        self.gridLayout_3.addWidget(self.label_15, 1, 9, 1, 1)

        self.label_19 = QLabel(self.page_dives)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)

        self.gridLayout_3.addWidget(self.label_19, 1, 12, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_3)

        self.stackedWidget.addWidget(self.page_dives)
        self.page_add_new_customer = QWidget()
        self.page_add_new_customer.setObjectName(u"page_add_new_customer")
        self.verticalLayout_6 = QVBoxLayout(self.page_add_new_customer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cert_seen_label = QLabel(self.page_add_new_customer)
        self.cert_seen_label.setObjectName(u"cert_seen_label")
        font5 = QFont()
        font5.setFamily(u"DejaVu Sans")
        font5.setPointSize(16)
        self.cert_seen_label.setFont(font5)

        self.gridLayout_2.addWidget(self.cert_seen_label, 4, 1, 1, 1)

        self.dob_entry = QLineEdit(self.page_add_new_customer)
        self.dob_entry.setObjectName(u"dob_entry")

        self.gridLayout_2.addWidget(self.dob_entry, 2, 2, 1, 1)

        self.liab_check = QCheckBox(self.page_add_new_customer)
        self.liab_check.setObjectName(u"liab_check")

        self.gridLayout_2.addWidget(self.liab_check, 7, 2, 1, 1)

        self.no_dives__label = QLabel(self.page_add_new_customer)
        self.no_dives__label.setObjectName(u"no_dives__label")
        self.no_dives__label.setFont(font5)

        self.gridLayout_2.addWidget(self.no_dives__label, 5, 1, 1, 1)

        self.pushButton = QPushButton(self.page_add_new_customer)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.pushButton, 8, 1, 1, 2)

        self.last_dive_entry = QLineEdit(self.page_add_new_customer)
        self.last_dive_entry.setObjectName(u"last_dive_entry")

        self.gridLayout_2.addWidget(self.last_dive_entry, 6, 2, 1, 1)

        self.no_dives_entry = QLineEdit(self.page_add_new_customer)
        self.no_dives_entry.setObjectName(u"no_dives_entry")

        self.gridLayout_2.addWidget(self.no_dives_entry, 5, 2, 1, 1)

        self.label_22 = QLabel(self.page_add_new_customer)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 6, 3, 1, 1)

        self.f_name_entry = QLineEdit(self.page_add_new_customer)
        self.f_name_entry.setObjectName(u"f_name_entry")

        self.gridLayout_2.addWidget(self.f_name_entry, 0, 2, 1, 1)

        self.cert_check = QCheckBox(self.page_add_new_customer)
        self.cert_check.setObjectName(u"cert_check")

        self.gridLayout_2.addWidget(self.cert_check, 4, 2, 1, 1)

        self.dob_label = QLabel(self.page_add_new_customer)
        self.dob_label.setObjectName(u"dob_label")
        self.dob_label.setFont(font5)

        self.gridLayout_2.addWidget(self.dob_label, 2, 1, 1, 1)

        self.cert_combo = QComboBox(self.page_add_new_customer)
        self.cert_combo.setObjectName(u"cert_combo")

        self.gridLayout_2.addWidget(self.cert_combo, 3, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.l_name_label = QLabel(self.page_add_new_customer)
        self.l_name_label.setObjectName(u"l_name_label")
        self.l_name_label.setFont(font5)

        self.gridLayout_2.addWidget(self.l_name_label, 1, 1, 1, 1)

        self.label_21 = QLabel(self.page_add_new_customer)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 2, 3, 1, 1)

        self.last_dive__label = QLabel(self.page_add_new_customer)
        self.last_dive__label.setObjectName(u"last_dive__label")
        self.last_dive__label.setFont(font5)

        self.gridLayout_2.addWidget(self.last_dive__label, 6, 1, 1, 1)

        self.f_name_label = QLabel(self.page_add_new_customer)
        self.f_name_label.setObjectName(u"f_name_label")
        self.f_name_label.setFont(font5)

        self.gridLayout_2.addWidget(self.f_name_label, 0, 1, 1, 1)

        self.liab__label = QLabel(self.page_add_new_customer)
        self.liab__label.setObjectName(u"liab__label")
        self.liab__label.setFont(font5)

        self.gridLayout_2.addWidget(self.liab__label, 7, 1, 1, 1)

        self.cert_label = QLabel(self.page_add_new_customer)
        self.cert_label.setObjectName(u"cert_label")
        self.cert_label.setFont(font5)

        self.gridLayout_2.addWidget(self.cert_label, 3, 1, 1, 1)

        self.l_name_entry = QLineEdit(self.page_add_new_customer)
        self.l_name_entry.setObjectName(u"l_name_entry")

        self.gridLayout_2.addWidget(self.l_name_entry, 1, 2, 1, 1)

        self.new_customer_added_label = QLabel(self.page_add_new_customer)
        self.new_customer_added_label.setObjectName(u"new_customer_added_label")

        self.gridLayout_2.addWidget(self.new_customer_added_label, 8, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.page_add_new_customer)
        self.page_find_customer = QWidget()
        self.page_find_customer.setObjectName(u"page_find_customer")
        self.gridLayout_10 = QGridLayout(self.page_find_customer)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.cert_check_2 = QCheckBox(self.page_find_customer)
        self.cert_check_2.setObjectName(u"cert_check_2")

        self.gridLayout_10.addWidget(self.cert_check_2, 5, 8, 1, 1)

        self.cert_combo_2 = QComboBox(self.page_find_customer)
        self.cert_combo_2.setObjectName(u"cert_combo_2")

        self.gridLayout_10.addWidget(self.cert_combo_2, 4, 8, 1, 1)

        self.liab_check_2 = QCheckBox(self.page_find_customer)
        self.liab_check_2.setObjectName(u"liab_check_2")

        self.gridLayout_10.addWidget(self.liab_check_2, 8, 8, 1, 1)

        self.no_dives_entry_2 = QLineEdit(self.page_find_customer)
        self.no_dives_entry_2.setObjectName(u"no_dives_entry_2")

        self.gridLayout_10.addWidget(self.no_dives_entry_2, 6, 8, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_3, 10, 8, 1, 1)

        self.no_dives__label_2 = QLabel(self.page_find_customer)
        self.no_dives__label_2.setObjectName(u"no_dives__label_2")
        self.no_dives__label_2.setFont(font5)

        self.gridLayout_10.addWidget(self.no_dives__label_2, 6, 7, 1, 1)

        self.cert_seen_label_2 = QLabel(self.page_find_customer)
        self.cert_seen_label_2.setObjectName(u"cert_seen_label_2")
        self.cert_seen_label_2.setFont(font5)

        self.gridLayout_10.addWidget(self.cert_seen_label_2, 5, 7, 1, 1)

        self.l_name_search_label_2 = QLabel(self.page_find_customer)
        self.l_name_search_label_2.setObjectName(u"l_name_search_label_2")

        self.gridLayout_10.addWidget(self.l_name_search_label_2, 2, 3, 1, 1)

        self.label_25 = QLabel(self.page_find_customer)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_10.addWidget(self.label_25, 7, 9, 1, 1)

        self.oid_search_label = QLabel(self.page_find_customer)
        self.oid_search_label.setObjectName(u"oid_search_label")

        self.gridLayout_10.addWidget(self.oid_search_label, 2, 0, 1, 1)

        self.l_name_label_4 = QLabel(self.page_find_customer)
        self.l_name_label_4.setObjectName(u"l_name_label_4")
        self.l_name_label_4.setFont(font5)

        self.gridLayout_10.addWidget(self.l_name_label_4, 2, 7, 1, 1)

        self.oid_search_results_label = QLabel(self.page_find_customer)
        self.oid_search_results_label.setObjectName(u"oid_search_results_label")

        self.gridLayout_10.addWidget(self.oid_search_results_label, 3, 0, 1, 1)

        self.dob_search_label = QLabel(self.page_find_customer)
        self.dob_search_label.setObjectName(u"dob_search_label")

        self.gridLayout_10.addWidget(self.dob_search_label, 2, 4, 1, 1)

        self.f_name_entry_2 = QLineEdit(self.page_find_customer)
        self.f_name_entry_2.setObjectName(u"f_name_entry_2")

        self.gridLayout_10.addWidget(self.f_name_entry_2, 1, 8, 1, 1)

        self.l_name_entry_2 = QLineEdit(self.page_find_customer)
        self.l_name_entry_2.setObjectName(u"l_name_entry_2")

        self.gridLayout_10.addWidget(self.l_name_entry_2, 2, 8, 1, 1)

        self.update_customer_button = QPushButton(self.page_find_customer)
        self.update_customer_button.setObjectName(u"update_customer_button")
        sizePolicy3.setHeightForWidth(self.update_customer_button.sizePolicy().hasHeightForWidth())
        self.update_customer_button.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush15 = QBrush(QColor(210, 210, 210, 128))
        brush15.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.update_customer_button.setPalette(palette1)

        self.gridLayout_10.addWidget(self.update_customer_button, 8, 9, 1, 1)

        self.list_all_button = QPushButton(self.page_find_customer)
        self.list_all_button.setObjectName(u"list_all_button")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush18)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush19 = QBrush(QColor(210, 210, 210, 128))
        brush19.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush19)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush20 = QBrush(QColor(210, 210, 210, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush20)
#endif
        self.list_all_button.setPalette(palette2)

        self.gridLayout_10.addWidget(self.list_all_button, 2, 5, 1, 1)

        self.l_name_search_label = QLabel(self.page_find_customer)
        self.l_name_search_label.setObjectName(u"l_name_search_label")
        self.l_name_search_label.setFont(font5)

        self.gridLayout_10.addWidget(self.l_name_search_label, 0, 0, 1, 1)

        self.label_24 = QLabel(self.page_find_customer)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_10.addWidget(self.label_24, 3, 9, 1, 1)

        self.f_name_search_label = QLabel(self.page_find_customer)
        self.f_name_search_label.setObjectName(u"f_name_search_label")

        self.gridLayout_10.addWidget(self.f_name_search_label, 2, 1, 1, 1)

        self.delete_customer_button = QPushButton(self.page_find_customer)
        self.delete_customer_button.setObjectName(u"delete_customer_button")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush21 = QBrush(QColor(210, 210, 210, 128))
        brush21.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush21)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush22 = QBrush(QColor(210, 210, 210, 128))
        brush22.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush22)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush23 = QBrush(QColor(210, 210, 210, 128))
        brush23.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush23)
#endif
        self.delete_customer_button.setPalette(palette3)

        self.gridLayout_10.addWidget(self.delete_customer_button, 1, 4, 1, 1)

        self.last_dive_entry_2 = QLineEdit(self.page_find_customer)
        self.last_dive_entry_2.setObjectName(u"last_dive_entry_2")

        self.gridLayout_10.addWidget(self.last_dive_entry_2, 7, 8, 1, 1)

        self.id_label = QLabel(self.page_find_customer)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setFont(font5)

        self.gridLayout_10.addWidget(self.id_label, 1, 0, 1, 1)

        self.dob_entry_2 = QLineEdit(self.page_find_customer)
        self.dob_entry_2.setObjectName(u"dob_entry_2")

        self.gridLayout_10.addWidget(self.dob_entry_2, 3, 8, 1, 1)

        self.f_name_label_4 = QLabel(self.page_find_customer)
        self.f_name_label_4.setObjectName(u"f_name_label_4")
        self.f_name_label_4.setFont(font5)

        self.gridLayout_10.addWidget(self.f_name_label_4, 1, 7, 1, 1)

        self.id_entry = QLineEdit(self.page_find_customer)
        self.id_entry.setObjectName(u"id_entry")
        sizePolicy5.setHeightForWidth(self.id_entry.sizePolicy().hasHeightForWidth())
        self.id_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_10.addWidget(self.id_entry, 1, 1, 1, 1)

        self.last_dive__label_2 = QLabel(self.page_find_customer)
        self.last_dive__label_2.setObjectName(u"last_dive__label_2")
        self.last_dive__label_2.setFont(font5)

        self.gridLayout_10.addWidget(self.last_dive__label_2, 7, 7, 1, 1)

        self.cert_label_2 = QLabel(self.page_find_customer)
        self.cert_label_2.setObjectName(u"cert_label_2")
        self.cert_label_2.setFont(font5)

        self.gridLayout_10.addWidget(self.cert_label_2, 4, 7, 1, 1)

        self.f_name_search_results_label = QLabel(self.page_find_customer)
        self.f_name_search_results_label.setObjectName(u"f_name_search_results_label")

        self.gridLayout_10.addWidget(self.f_name_search_results_label, 3, 1, 1, 1)

        self.dob_label_2 = QLabel(self.page_find_customer)
        self.dob_label_2.setObjectName(u"dob_label_2")
        self.dob_label_2.setFont(font5)

        self.gridLayout_10.addWidget(self.dob_label_2, 3, 7, 1, 1)

        self.liab__label_2 = QLabel(self.page_find_customer)
        self.liab__label_2.setObjectName(u"liab__label_2")
        self.liab__label_2.setFont(font5)

        self.gridLayout_10.addWidget(self.liab__label_2, 8, 7, 1, 1)

        self.l_name_search_results_label = QLabel(self.page_find_customer)
        self.l_name_search_results_label.setObjectName(u"l_name_search_results_label")

        self.gridLayout_10.addWidget(self.l_name_search_results_label, 3, 3, 1, 1)

        self.l_name_search_results_label_2 = QLabel(self.page_find_customer)
        self.l_name_search_results_label_2.setObjectName(u"l_name_search_results_label_2")

        self.gridLayout_10.addWidget(self.l_name_search_results_label_2, 3, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_4, 1, 6, 1, 1)

        self.l_name_search_entry = QLineEdit(self.page_find_customer)
        self.l_name_search_entry.setObjectName(u"l_name_search_entry")
        sizePolicy5.setHeightForWidth(self.l_name_search_entry.sizePolicy().hasHeightForWidth())
        self.l_name_search_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_10.addWidget(self.l_name_search_entry, 0, 1, 1, 1)

        self.search_customer_button = QPushButton(self.page_find_customer)
        self.search_customer_button.setObjectName(u"search_customer_button")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush24 = QBrush(QColor(210, 210, 210, 128))
        brush24.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush24)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush25 = QBrush(QColor(210, 210, 210, 128))
        brush25.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush25)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush26 = QBrush(QColor(210, 210, 210, 128))
        brush26.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush26)
#endif
        self.search_customer_button.setPalette(palette4)

        self.gridLayout_10.addWidget(self.search_customer_button, 0, 3, 1, 2)

        self.search_customer_id_button_ = QPushButton(self.page_find_customer)
        self.search_customer_id_button_.setObjectName(u"search_customer_id_button_")

        self.gridLayout_10.addWidget(self.search_customer_id_button_, 1, 3, 1, 1)

        self.record_updated_label = QLabel(self.page_find_customer)
        self.record_updated_label.setObjectName(u"record_updated_label")

        self.gridLayout_10.addWidget(self.record_updated_label, 9, 9, 1, 1)

        self.stackedWidget.addWidget(self.page_find_customer)
        self.page_staff = QWidget()
        self.page_staff.setObjectName(u"page_staff")
        self.gridLayout_11 = QGridLayout(self.page_staff)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pb_check = QCheckBox(self.page_staff)
        self.pb_check.setObjectName(u"pb_check")

        self.gridLayout_11.addWidget(self.pb_check, 7, 12, 1, 1)

        self.insurance_no_label = QLabel(self.page_staff)
        self.insurance_no_label.setObjectName(u"insurance_no_label")

        self.gridLayout_11.addWidget(self.insurance_no_label, 4, 4, 1, 1)

        self.xr_check = QCheckBox(self.page_staff)
        self.xr_check.setObjectName(u"xr_check")

        self.gridLayout_11.addWidget(self.xr_check, 7, 13, 1, 1)

        self.l_name_label_3 = QLabel(self.page_staff)
        self.l_name_label_3.setObjectName(u"l_name_label_3")

        self.gridLayout_11.addWidget(self.l_name_label_3, 1, 10, 1, 1)

        self.delete_staff_button = QPushButton(self.page_staff)
        self.delete_staff_button.setObjectName(u"delete_staff_button")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush27 = QBrush(QColor(210, 210, 210, 128))
        brush27.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush27)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush28 = QBrush(QColor(210, 210, 210, 128))
        brush28.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush28)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush29 = QBrush(QColor(210, 210, 210, 128))
        brush29.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush29)
#endif
        self.delete_staff_button.setPalette(palette5)

        self.gridLayout_11.addWidget(self.delete_staff_button, 1, 6, 1, 1)

        self.lineEdit = QLineEdit(self.page_staff)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy5.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy5)

        self.gridLayout_11.addWidget(self.lineEdit, 0, 11, 1, 1)

        self.pro_no_label_2 = QLabel(self.page_staff)
        self.pro_no_label_2.setObjectName(u"pro_no_label_2")

        self.gridLayout_11.addWidget(self.pro_no_label_2, 2, 10, 1, 1)

        self.highest_label = QLabel(self.page_staff)
        self.highest_label.setObjectName(u"highest_label")

        self.gridLayout_11.addWidget(self.highest_label, 4, 6, 1, 1)

        self.f_name_results_label = QLabel(self.page_staff)
        self.f_name_results_label.setObjectName(u"f_name_results_label")
        font6 = QFont()
        font6.setFamily(u"DejaVu Sans")
        font6.setPointSize(11)
        self.f_name_results_label.setFont(font6)

        self.gridLayout_11.addWidget(self.f_name_results_label, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_2, 9, 10, 1, 1)

        self.pro_no_label = QLabel(self.page_staff)
        self.pro_no_label.setObjectName(u"pro_no_label")

        self.gridLayout_11.addWidget(self.pro_no_label, 4, 3, 1, 1)

        self.oid_entry = QLineEdit(self.page_staff)
        self.oid_entry.setObjectName(u"oid_entry")
        sizePolicy5.setHeightForWidth(self.oid_entry.sizePolicy().hasHeightForWidth())
        self.oid_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_11.addWidget(self.oid_entry, 2, 8, 1, 1)

        self.l_name_results_label = QLabel(self.page_staff)
        self.l_name_results_label.setObjectName(u"l_name_results_label")
        self.l_name_results_label.setFont(font6)

        self.gridLayout_11.addWidget(self.l_name_results_label, 5, 2, 1, 1)

        self.eanx_check = QCheckBox(self.page_staff)
        self.eanx_check.setObjectName(u"eanx_check")

        self.gridLayout_11.addWidget(self.eanx_check, 0, 13, 1, 1)

        self.insurance_exp_results_label = QLabel(self.page_staff)
        self.insurance_exp_results_label.setObjectName(u"insurance_exp_results_label")
        self.insurance_exp_results_label.setFont(font6)

        self.gridLayout_11.addWidget(self.insurance_exp_results_label, 5, 5, 1, 1)

        self.id_label_2 = QLabel(self.page_staff)
        self.id_label_2.setObjectName(u"id_label_2")

        self.gridLayout_11.addWidget(self.id_label_2, 4, 0, 1, 1)

        self.sod_check = QCheckBox(self.page_staff)
        self.sod_check.setObjectName(u"sod_check")

        self.gridLayout_11.addWidget(self.sod_check, 5, 13, 1, 1)

        self.insurance_no_results_label = QLabel(self.page_staff)
        self.insurance_no_results_label.setObjectName(u"insurance_no_results_label")
        self.insurance_no_results_label.setFont(font6)

        self.gridLayout_11.addWidget(self.insurance_no_results_label, 5, 4, 1, 1)

        self.lineEdit_3 = QLineEdit(self.page_staff)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy5.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy5)

        self.gridLayout_11.addWidget(self.lineEdit_3, 2, 11, 1, 1)

        self.highest_label_2 = QLabel(self.page_staff)
        self.highest_label_2.setObjectName(u"highest_label_2")

        self.gridLayout_11.addWidget(self.highest_label_2, 7, 10, 1, 1)

        self.add_search_staff_button = QPushButton(self.page_staff)
        self.add_search_staff_button.setObjectName(u"add_search_staff_button")

        self.gridLayout_11.addWidget(self.add_search_staff_button, 2, 6, 1, 1)

        self.f_name_label_2 = QLabel(self.page_staff)
        self.f_name_label_2.setObjectName(u"f_name_label_2")

        self.gridLayout_11.addWidget(self.f_name_label_2, 4, 1, 1, 1)

        self.insurance_exp_label = QLabel(self.page_staff)
        self.insurance_exp_label.setObjectName(u"insurance_exp_label")

        self.gridLayout_11.addWidget(self.insurance_exp_label, 4, 5, 1, 1)

        self.update_button = QPushButton(self.page_staff)
        self.update_button.setObjectName(u"update_button")

        self.gridLayout_11.addWidget(self.update_button, 8, 11, 1, 1)

        self.lineEdit_2 = QLineEdit(self.page_staff)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy5.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy5)

        self.gridLayout_11.addWidget(self.lineEdit_2, 1, 11, 1, 1)

        self.insurance_no_label_2 = QLabel(self.page_staff)
        self.insurance_no_label_2.setObjectName(u"insurance_no_label_2")

        self.gridLayout_11.addWidget(self.insurance_no_label_2, 4, 10, 1, 1)

        self.id_results_label = QLabel(self.page_staff)
        self.id_results_label.setObjectName(u"id_results_label")
        self.id_results_label.setFont(font6)

        self.gridLayout_11.addWidget(self.id_results_label, 5, 0, 1, 1)

        self.nav_check = QCheckBox(self.page_staff)
        self.nav_check.setObjectName(u"nav_check")

        self.gridLayout_11.addWidget(self.nav_check, 2, 13, 1, 1)

        self.pushButton_2 = QPushButton(self.page_staff)
        self.pushButton_2.setObjectName(u"pushButton_2")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush30 = QBrush(QColor(210, 210, 210, 128))
        brush30.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush30)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush31 = QBrush(QColor(210, 210, 210, 128))
        brush31.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush31)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush32 = QBrush(QColor(210, 210, 210, 128))
        brush32.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush32)
#endif
        self.pushButton_2.setPalette(palette6)

        self.gridLayout_11.addWidget(self.pushButton_2, 8, 12, 1, 1)

        self.wreck_check = QCheckBox(self.page_staff)
        self.wreck_check.setObjectName(u"wreck_check")

        self.gridLayout_11.addWidget(self.wreck_check, 4, 12, 1, 1)

        self.pro_number_results_label = QLabel(self.page_staff)
        self.pro_number_results_label.setObjectName(u"pro_number_results_label")
        self.pro_number_results_label.setFont(font6)

        self.gridLayout_11.addWidget(self.pro_number_results_label, 5, 3, 1, 1)

        self.adv_wreck_check = QCheckBox(self.page_staff)
        self.adv_wreck_check.setObjectName(u"adv_wreck_check")

        self.gridLayout_11.addWidget(self.adv_wreck_check, 5, 12, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page_staff)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy5.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy5)

        self.gridLayout_11.addWidget(self.lineEdit_4, 4, 11, 1, 1)

        self.boat_check = QCheckBox(self.page_staff)
        self.boat_check.setObjectName(u"boat_check")

        self.gridLayout_11.addWidget(self.boat_check, 1, 13, 1, 1)

        self.clear_staff_button = QPushButton(self.page_staff)
        self.clear_staff_button.setObjectName(u"clear_staff_button")

        self.gridLayout_11.addWidget(self.clear_staff_button, 8, 10, 1, 1)

        self.highest_results_label = QLabel(self.page_staff)
        self.highest_results_label.setObjectName(u"highest_results_label")
        self.highest_results_label.setFont(font6)

        self.gridLayout_11.addWidget(self.highest_results_label, 5, 6, 1, 1)

        self.deep_check = QCheckBox(self.page_staff)
        self.deep_check.setObjectName(u"deep_check")

        self.gridLayout_11.addWidget(self.deep_check, 2, 12, 1, 1)

        self.lineEdit_6 = QLineEdit(self.page_staff)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy5.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy5)

        self.gridLayout_11.addWidget(self.lineEdit_6, 7, 11, 1, 1)

        self.night_check = QCheckBox(self.page_staff)
        self.night_check.setObjectName(u"night_check")

        self.gridLayout_11.addWidget(self.night_check, 4, 13, 1, 1)

        self.sidemount_check = QCheckBox(self.page_staff)
        self.sidemount_check.setObjectName(u"sidemount_check")

        self.gridLayout_11.addWidget(self.sidemount_check, 8, 13, 1, 1)

        self.l_name_label_2 = QLabel(self.page_staff)
        self.l_name_label_2.setObjectName(u"l_name_label_2")

        self.gridLayout_11.addWidget(self.l_name_label_2, 4, 2, 1, 1)

        self.insurance_exp_label_2 = QLabel(self.page_staff)
        self.insurance_exp_label_2.setObjectName(u"insurance_exp_label_2")

        self.gridLayout_11.addWidget(self.insurance_exp_label_2, 5, 10, 1, 1)

        self.owi_check = QCheckBox(self.page_staff)
        self.owi_check.setObjectName(u"owi_check")

        self.gridLayout_11.addWidget(self.owi_check, 1, 12, 1, 1)

        self.dm_check = QCheckBox(self.page_staff)
        self.dm_check.setObjectName(u"dm_check")

        self.gridLayout_11.addWidget(self.dm_check, 0, 12, 1, 1)

        self.lineEdit_5 = QLineEdit(self.page_staff)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy5.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy5)

        self.gridLayout_11.addWidget(self.lineEdit_5, 5, 11, 1, 1)

        self.f_name_label_3 = QLabel(self.page_staff)
        self.f_name_label_3.setObjectName(u"f_name_label_3")

        self.gridLayout_11.addWidget(self.f_name_label_3, 0, 10, 1, 1)

        self.label_23 = QLabel(self.page_staff)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_11.addWidget(self.label_23, 2, 7, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_7, 2, 9, 1, 1)

        self.stackedWidget.addWidget(self.page_staff)
        self.page_accounts = QWidget()
        self.page_accounts.setObjectName(u"page_accounts")
        self.gridLayout_12 = QGridLayout(self.page_accounts)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.search_button = QPushButton(self.page_accounts)
        self.search_button.setObjectName(u"search_button")

        self.gridLayout_12.addWidget(self.search_button, 0, 14, 1, 1)

        self.total_mount_results = QLabel(self.page_accounts)
        self.total_mount_results.setObjectName(u"total_mount_results")
        font7 = QFont()
        font7.setFamily(u"DejaVu Serif")
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setWeight(75)
        self.total_mount_results.setFont(font7)

        self.gridLayout_12.addWidget(self.total_mount_results, 4, 4, 1, 1)

        self.amount_paid_label = QLabel(self.page_accounts)
        self.amount_paid_label.setObjectName(u"amount_paid_label")
        self.amount_paid_label.setFont(font4)

        self.gridLayout_12.addWidget(self.amount_paid_label, 5, 3, 1, 1)

        self.dob_search_label_2 = QLabel(self.page_accounts)
        self.dob_search_label_2.setObjectName(u"dob_search_label_2")

        self.gridLayout_12.addWidget(self.dob_search_label_2, 1, 5, 1, 1)

        self.l_name_search_results_label_4 = QLabel(self.page_accounts)
        self.l_name_search_results_label_4.setObjectName(u"l_name_search_results_label_4")

        self.gridLayout_12.addWidget(self.l_name_search_results_label_4, 2, 5, 1, 1)

        self.oid_search_label_2 = QLabel(self.page_accounts)
        self.oid_search_label_2.setObjectName(u"oid_search_label_2")

        self.gridLayout_12.addWidget(self.oid_search_label_2, 1, 0, 1, 1)

        self.total_amount_owed_label = QLabel(self.page_accounts)
        self.total_amount_owed_label.setObjectName(u"total_amount_owed_label")
        self.total_amount_owed_label.setFont(font4)

        self.gridLayout_12.addWidget(self.total_amount_owed_label, 4, 3, 1, 1)

        self.l_name_search_entry_2 = QLineEdit(self.page_accounts)
        self.l_name_search_entry_2.setObjectName(u"l_name_search_entry_2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.l_name_search_entry_2.sizePolicy().hasHeightForWidth())
        self.l_name_search_entry_2.setSizePolicy(sizePolicy8)

        self.gridLayout_12.addWidget(self.l_name_search_entry_2, 0, 3, 1, 2)

        self.id_search_entry = QLineEdit(self.page_accounts)
        self.id_search_entry.setObjectName(u"id_search_entry")
        sizePolicy5.setHeightForWidth(self.id_search_entry.sizePolicy().hasHeightForWidth())
        self.id_search_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_12.addWidget(self.id_search_entry, 0, 10, 1, 1)

        self.balance_label = QLabel(self.page_accounts)
        self.balance_label.setObjectName(u"balance_label")
        self.balance_label.setFont(font4)

        self.gridLayout_12.addWidget(self.balance_label, 6, 3, 1, 1)

        self.f_l_name_label = QLabel(self.page_accounts)
        self.f_l_name_label.setObjectName(u"f_l_name_label")
        font8 = QFont()
        font8.setFamily(u"DejaVu Sans")
        font8.setPointSize(19)
        self.f_l_name_label.setFont(font8)

        self.gridLayout_12.addWidget(self.f_l_name_label, 3, 4, 1, 1)

        self.search_customer_button_2 = QPushButton(self.page_accounts)
        self.search_customer_button_2.setObjectName(u"search_customer_button_2")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush33 = QBrush(QColor(210, 210, 210, 128))
        brush33.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush33)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush34 = QBrush(QColor(210, 210, 210, 128))
        brush34.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush34)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush35 = QBrush(QColor(210, 210, 210, 128))
        brush35.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush35)
#endif
        self.search_customer_button_2.setPalette(palette7)

        self.gridLayout_12.addWidget(self.search_customer_button_2, 0, 5, 1, 1)

        self.make_payment_button = QPushButton(self.page_accounts)
        self.make_payment_button.setObjectName(u"make_payment_button")

        self.gridLayout_12.addWidget(self.make_payment_button, 4, 14, 1, 1)

        self.amount_paid_results = QLabel(self.page_accounts)
        self.amount_paid_results.setObjectName(u"amount_paid_results")
        self.amount_paid_results.setFont(font7)

        self.gridLayout_12.addWidget(self.amount_paid_results, 5, 4, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_16, 0, 7, 1, 1)

        self.f_name_search_results_label_2 = QLabel(self.page_accounts)
        self.f_name_search_results_label_2.setObjectName(u"f_name_search_results_label_2")

        self.gridLayout_12.addWidget(self.f_name_search_results_label_2, 2, 3, 1, 1)

        self.l_name_search_results_label_3 = QLabel(self.page_accounts)
        self.l_name_search_results_label_3.setObjectName(u"l_name_search_results_label_3")

        self.gridLayout_12.addWidget(self.l_name_search_results_label_3, 2, 4, 1, 1)

        self.l_name_search_label_4 = QLabel(self.page_accounts)
        self.l_name_search_label_4.setObjectName(u"l_name_search_label_4")

        self.gridLayout_12.addWidget(self.l_name_search_label_4, 1, 4, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_4, 2, 7, 1, 1)

        self.f_name_search_label_2 = QLabel(self.page_accounts)
        self.f_name_search_label_2.setObjectName(u"f_name_search_label_2")

        self.gridLayout_12.addWidget(self.f_name_search_label_2, 1, 3, 1, 1)

        self.balance_results = QLabel(self.page_accounts)
        self.balance_results.setObjectName(u"balance_results")
        self.balance_results.setFont(font7)
        self.balance_results.setFrameShape(QFrame.StyledPanel)
        self.balance_results.setFrameShadow(QFrame.Raised)
        self.balance_results.setLineWidth(1)

        self.gridLayout_12.addWidget(self.balance_results, 6, 4, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_66 = QLabel(self.page_accounts)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_9.addWidget(self.label_66)


        self.gridLayout_12.addLayout(self.horizontalLayout_9, 3, 10, 1, 1)

        self.tab_table = QTableWidget(self.page_accounts)
        if (self.tab_table.columnCount() < 42):
            self.tab_table.setColumnCount(42)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(5, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(6, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(7, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(8, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(9, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(10, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(11, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(12, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(13, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(14, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(15, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(16, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(17, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(18, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(19, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(20, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(21, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(22, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(23, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(24, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(25, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(26, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(27, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(28, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(29, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(30, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(31, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(32, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(33, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(34, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(35, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(36, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(37, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(38, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(39, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(40, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tab_table.setHorizontalHeaderItem(41, __qtablewidgetitem76)
        if (self.tab_table.rowCount() < 1):
            self.tab_table.setRowCount(1)
        self.tab_table.setObjectName(u"tab_table")
        self.tab_table.setFrameShadow(QFrame.Raised)
        self.tab_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tab_table.setAlternatingRowColors(False)
        self.tab_table.setWordWrap(True)
        self.tab_table.setRowCount(1)
        self.tab_table.horizontalHeader().setVisible(False)
        self.tab_table.horizontalHeader().setStretchLastSection(False)
        self.tab_table.verticalHeader().setVisible(False)

        self.gridLayout_12.addWidget(self.tab_table, 7, 3, 1, 8)

        self.id_number_label = QLabel(self.page_accounts)
        self.id_number_label.setObjectName(u"id_number_label")
        self.id_number_label.setFont(font8)

        self.gridLayout_12.addWidget(self.id_number_label, 3, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_5, 4, 15, 1, 1)

        self.oid_search_results_label_2 = QLabel(self.page_accounts)
        self.oid_search_results_label_2.setObjectName(u"oid_search_results_label_2")

        self.gridLayout_12.addWidget(self.oid_search_results_label_2, 2, 0, 1, 1)

        self.l_name_search_label_3 = QLabel(self.page_accounts)
        self.l_name_search_label_3.setObjectName(u"l_name_search_label_3")
        self.l_name_search_label_3.setFont(font5)

        self.gridLayout_12.addWidget(self.l_name_search_label_3, 0, 0, 1, 1)

        self.list_all_button_2 = QPushButton(self.page_accounts)
        self.list_all_button_2.setObjectName(u"list_all_button_2")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush36 = QBrush(QColor(210, 210, 210, 128))
        brush36.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush36)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush37 = QBrush(QColor(210, 210, 210, 128))
        brush37.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush37)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush38 = QBrush(QColor(210, 210, 210, 128))
        brush38.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush38)
#endif
        self.list_all_button_2.setPalette(palette8)

        self.gridLayout_12.addWidget(self.list_all_button_2, 1, 6, 1, 1)

        self.tableWidget = QTableWidget(self.page_accounts)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem78)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(28)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.gridLayout_12.addWidget(self.tableWidget, 4, 8, 3, 6)

        self.id_search_label = QLabel(self.page_accounts)
        self.id_search_label.setObjectName(u"id_search_label")

        self.gridLayout_12.addWidget(self.id_search_label, 0, 9, 1, 1)

        self.label_26 = QLabel(self.page_accounts)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_12.addWidget(self.label_26, 3, 8, 1, 1)

        self.lineEdit_7 = QLineEdit(self.page_accounts)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy5.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy5)

        self.gridLayout_12.addWidget(self.lineEdit_7, 3, 14, 1, 1)

        self.stackedWidget.addWidget(self.page_accounts)
        self.page_activities = QWidget()
        self.page_activities.setObjectName(u"page_activities")
        self.gridLayout_14 = QGridLayout(self.page_activities)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.computer_entry = QLineEdit(self.page_activities)
        self.computer_entry.setObjectName(u"computer_entry")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.computer_entry.sizePolicy().hasHeightForWidth())
        self.computer_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.computer_entry, 3, 6, 1, 1)

        self.label_35 = QLabel(self.page_activities)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_14.addWidget(self.label_35, 8, 5, 1, 1)

        self.reg_dive_entry = QLineEdit(self.page_activities)
        self.reg_dive_entry.setObjectName(u"reg_dive_entry")
        sizePolicy9.setHeightForWidth(self.reg_dive_entry.sizePolicy().hasHeightForWidth())
        self.reg_dive_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.reg_dive_entry, 8, 6, 1, 1)

        self.list_activities_button = QPushButton(self.page_activities)
        self.list_activities_button.setObjectName(u"list_activities_button")

        self.gridLayout_14.addWidget(self.list_activities_button, 4, 0, 1, 1)

        self.activity_name_label = QLabel(self.page_activities)
        self.activity_name_label.setObjectName(u"activity_name_label")

        self.gridLayout_14.addWidget(self.activity_name_label, 0, 0, 1, 1)

        self.label_41 = QLabel(self.page_activities)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_14.addWidget(self.label_41, 14, 5, 1, 1)

        self.wreck_reel_entry = QLineEdit(self.page_activities)
        self.wreck_reel_entry.setObjectName(u"wreck_reel_entry")
        sizePolicy9.setHeightForWidth(self.wreck_reel_entry.sizePolicy().hasHeightForWidth())
        self.wreck_reel_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.wreck_reel_entry, 13, 8, 1, 1)

        self.t_6_50_entry = QLineEdit(self.page_activities)
        self.t_6_50_entry.setObjectName(u"t_6_50_entry")
        sizePolicy9.setHeightForWidth(self.t_6_50_entry.sizePolicy().hasHeightForWidth())
        self.t_6_50_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.t_6_50_entry, 1, 8, 1, 1)

        self.bcd_dive_entry = QLineEdit(self.page_activities)
        self.bcd_dive_entry.setObjectName(u"bcd_dive_entry")
        sizePolicy9.setHeightForWidth(self.bcd_dive_entry.sizePolicy().hasHeightForWidth())
        self.bcd_dive_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.bcd_dive_entry, 5, 6, 1, 1)

        self.is_course_check = QCheckBox(self.page_activities)
        self.is_course_check.setObjectName(u"is_course_check")
        self.is_course_check.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_14.addWidget(self.is_course_check, 3, 1, 1, 1)

        self.tech_computer_entry = QLineEdit(self.page_activities)
        self.tech_computer_entry.setObjectName(u"tech_computer_entry")
        sizePolicy9.setHeightForWidth(self.tech_computer_entry.sizePolicy().hasHeightForWidth())
        self.tech_computer_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.tech_computer_entry, 11, 8, 1, 1)

        self.full_equip_dive_entry = QLineEdit(self.page_activities)
        self.full_equip_dive_entry.setObjectName(u"full_equip_dive_entry")
        sizePolicy9.setHeightForWidth(self.full_equip_dive_entry.sizePolicy().hasHeightForWidth())
        self.full_equip_dive_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.full_equip_dive_entry, 0, 6, 1, 1)

        self.reg_upgrade_entry = QLineEdit(self.page_activities)
        self.reg_upgrade_entry.setObjectName(u"reg_upgrade_entry")
        sizePolicy9.setHeightForWidth(self.reg_upgrade_entry.sizePolicy().hasHeightForWidth())
        self.reg_upgrade_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.reg_upgrade_entry, 10, 6, 1, 1)

        self.inst_cert_combo = QComboBox(self.page_activities)
        self.inst_cert_combo.setObjectName(u"inst_cert_combo")
        sizePolicy9.setHeightForWidth(self.inst_cert_combo.sizePolicy().hasHeightForWidth())
        self.inst_cert_combo.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.inst_cert_combo, 1, 1, 1, 1)

        self.t_6_100_entry = QLineEdit(self.page_activities)
        self.t_6_100_entry.setObjectName(u"t_6_100_entry")
        sizePolicy9.setHeightForWidth(self.t_6_100_entry.sizePolicy().hasHeightForWidth())
        self.t_6_100_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.t_6_100_entry, 2, 8, 1, 1)

        self.back_plate_entry = QLineEdit(self.page_activities)
        self.back_plate_entry.setObjectName(u"back_plate_entry")
        sizePolicy9.setHeightForWidth(self.back_plate_entry.sizePolicy().hasHeightForWidth())
        self.back_plate_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.back_plate_entry, 8, 8, 1, 1)

        self.rebreather_entry = QLineEdit(self.page_activities)
        self.rebreather_entry.setObjectName(u"rebreather_entry")
        sizePolicy9.setHeightForWidth(self.rebreather_entry.sizePolicy().hasHeightForWidth())
        self.rebreather_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.rebreather_entry, 17, 8, 1, 1)

        self.o2_reg_entry = QLineEdit(self.page_activities)
        self.o2_reg_entry.setObjectName(u"o2_reg_entry")
        sizePolicy9.setHeightForWidth(self.o2_reg_entry.sizePolicy().hasHeightForWidth())
        self.o2_reg_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.o2_reg_entry, 10, 8, 1, 1)

        self.oid_entry_2 = QLineEdit(self.page_activities)
        self.oid_entry_2.setObjectName(u"oid_entry_2")
        sizePolicy5.setHeightForWidth(self.oid_entry_2.sizePolicy().hasHeightForWidth())
        self.oid_entry_2.setSizePolicy(sizePolicy5)

        self.gridLayout_14.addWidget(self.oid_entry_2, 5, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.page_activities)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy9.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.pushButton_3, 19, 8, 1, 1)

        self.full_equip_day_entry = QLineEdit(self.page_activities)
        self.full_equip_day_entry.setObjectName(u"full_equip_day_entry")
        sizePolicy9.setHeightForWidth(self.full_equip_day_entry.sizePolicy().hasHeightForWidth())
        self.full_equip_day_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.full_equip_day_entry, 1, 6, 1, 1)

        self.label_45 = QLabel(self.page_activities)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_14.addWidget(self.label_45, 18, 5, 1, 2)

        self.label_40 = QLabel(self.page_activities)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_14.addWidget(self.label_40, 13, 5, 1, 1)

        self.activity_name_entry = QLineEdit(self.page_activities)
        self.activity_name_entry.setObjectName(u"activity_name_entry")
        sizePolicy9.setHeightForWidth(self.activity_name_entry.sizePolicy().hasHeightForWidth())
        self.activity_name_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.activity_name_entry, 0, 1, 1, 1)

        self.torch_entry = QLineEdit(self.page_activities)
        self.torch_entry.setObjectName(u"torch_entry")
        sizePolicy9.setHeightForWidth(self.torch_entry.sizePolicy().hasHeightForWidth())
        self.torch_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.torch_entry, 4, 6, 1, 1)

        self.bcd_upgrade_entry = QLineEdit(self.page_activities)
        self.bcd_upgrade_entry.setObjectName(u"bcd_upgrade_entry")
        sizePolicy9.setHeightForWidth(self.bcd_upgrade_entry.sizePolicy().hasHeightForWidth())
        self.bcd_upgrade_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.bcd_upgrade_entry, 7, 6, 1, 1)

        self.full_equip_upgrade_entry = QLineEdit(self.page_activities)
        self.full_equip_upgrade_entry.setObjectName(u"full_equip_upgrade_entry")
        sizePolicy9.setHeightForWidth(self.full_equip_upgrade_entry.sizePolicy().hasHeightForWidth())
        self.full_equip_upgrade_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.full_equip_upgrade_entry, 2, 6, 1, 1)

        self.label_56 = QLabel(self.page_activities)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_14.addWidget(self.label_56, 10, 7, 1, 1)

        self.reg_day_entry = QLineEdit(self.page_activities)
        self.reg_day_entry.setObjectName(u"reg_day_entry")
        sizePolicy9.setHeightForWidth(self.reg_day_entry.sizePolicy().hasHeightForWidth())
        self.reg_day_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.reg_day_entry, 9, 6, 1, 1)

        self.activity_name_label_2 = QLabel(self.page_activities)
        self.activity_name_label_2.setObjectName(u"activity_name_label_2")

        self.gridLayout_14.addWidget(self.activity_name_label_2, 6, 1, 1, 1)

        self.t_15l_entry = QLineEdit(self.page_activities)
        self.t_15l_entry.setObjectName(u"t_15l_entry")
        sizePolicy9.setHeightForWidth(self.t_15l_entry.sizePolicy().hasHeightForWidth())
        self.t_15l_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.t_15l_entry, 15, 6, 1, 1)

        self.label_46 = QLabel(self.page_activities)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_14.addWidget(self.label_46, 0, 7, 1, 1)

        self.label_30 = QLabel(self.page_activities)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_14.addWidget(self.label_30, 3, 5, 1, 1)

        self.label_55 = QLabel(self.page_activities)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_14.addWidget(self.label_55, 9, 7, 1, 1)

        self.t_12_50_entry = QLineEdit(self.page_activities)
        self.t_12_50_entry.setObjectName(u"t_12_50_entry")
        sizePolicy9.setHeightForWidth(self.t_12_50_entry.sizePolicy().hasHeightForWidth())
        self.t_12_50_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.t_12_50_entry, 3, 8, 1, 1)

        self.label_60 = QLabel(self.page_activities)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_14.addWidget(self.label_60, 14, 7, 1, 1)

        self.sorb_entry = QLineEdit(self.page_activities)
        self.sorb_entry.setObjectName(u"sorb_entry")
        sizePolicy9.setHeightForWidth(self.sorb_entry.sizePolicy().hasHeightForWidth())
        self.sorb_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.sorb_entry, 18, 8, 1, 1)

        self.t_3l_100_entry = QLineEdit(self.page_activities)
        self.t_3l_100_entry.setObjectName(u"t_3l_100_entry")
        sizePolicy9.setHeightForWidth(self.t_3l_100_entry.sizePolicy().hasHeightForWidth())
        self.t_3l_100_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.t_3l_100_entry, 0, 8, 1, 1)

        self.reel_entry = QLineEdit(self.page_activities)
        self.reel_entry.setObjectName(u"reel_entry")
        sizePolicy9.setHeightForWidth(self.reel_entry.sizePolicy().hasHeightForWidth())
        self.reel_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.reel_entry, 15, 8, 1, 1)

        self.label_65 = QLabel(self.page_activities)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_14.addWidget(self.label_65, 18, 9, 1, 1)

        self.label_47 = QLabel(self.page_activities)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_14.addWidget(self.label_47, 1, 7, 1, 1)

        self.label_33 = QLabel(self.page_activities)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_14.addWidget(self.label_33, 6, 5, 1, 1)

        self.eanx_upgrade_entry = QLineEdit(self.page_activities)
        self.eanx_upgrade_entry.setObjectName(u"eanx_upgrade_entry")
        sizePolicy9.setHeightForWidth(self.eanx_upgrade_entry.sizePolicy().hasHeightForWidth())
        self.eanx_upgrade_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.eanx_upgrade_entry, 14, 6, 1, 1)

        self.add_activity_button = QPushButton(self.page_activities)
        self.add_activity_button.setObjectName(u"add_activity_button")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush39 = QBrush(QColor(210, 210, 210, 128))
        brush39.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush39)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush40 = QBrush(QColor(210, 210, 210, 128))
        brush40.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush40)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush41 = QBrush(QColor(210, 210, 210, 128))
        brush41.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush41)
#endif
        self.add_activity_button.setPalette(palette9)

        self.gridLayout_14.addWidget(self.add_activity_button, 3, 0, 1, 1)

        self.label_54 = QLabel(self.page_activities)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_14.addWidget(self.label_54, 8, 7, 1, 1)

        self.label_36 = QLabel(self.page_activities)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_14.addWidget(self.label_36, 9, 5, 1, 1)

        self.label_48 = QLabel(self.page_activities)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_14.addWidget(self.label_48, 2, 7, 1, 1)

        self.t_12l_100_entry = QLineEdit(self.page_activities)
        self.t_12l_100_entry.setObjectName(u"t_12l_100_entry")
        sizePolicy9.setHeightForWidth(self.t_12l_100_entry.sizePolicy().hasHeightForWidth())
        self.t_12l_100_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.t_12l_100_entry, 4, 8, 1, 1)

        self.label_58 = QLabel(self.page_activities)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_14.addWidget(self.label_58, 12, 7, 1, 1)

        self.soft_day_entry = QLineEdit(self.page_activities)
        self.soft_day_entry.setObjectName(u"soft_day_entry")
        sizePolicy9.setHeightForWidth(self.soft_day_entry.sizePolicy().hasHeightForWidth())
        self.soft_day_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.soft_day_entry, 12, 6, 1, 1)

        self.label_43 = QLabel(self.page_activities)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_14.addWidget(self.label_43, 16, 5, 1, 1)

        self.price_label = QLabel(self.page_activities)
        self.price_label.setObjectName(u"price_label")

        self.gridLayout_14.addWidget(self.price_label, 2, 0, 1, 1)

        self.soft_upgrade_entry = QLineEdit(self.page_activities)
        self.soft_upgrade_entry.setObjectName(u"soft_upgrade_entry")
        sizePolicy9.setHeightForWidth(self.soft_upgrade_entry.sizePolicy().hasHeightForWidth())
        self.soft_upgrade_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.soft_upgrade_entry, 13, 6, 1, 1)

        self.label_50 = QLabel(self.page_activities)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_14.addWidget(self.label_50, 4, 7, 1, 1)

        self.tech_torch_entry = QLineEdit(self.page_activities)
        self.tech_torch_entry.setObjectName(u"tech_torch_entry")
        sizePolicy9.setHeightForWidth(self.tech_torch_entry.sizePolicy().hasHeightForWidth())
        self.tech_torch_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.tech_torch_entry, 12, 8, 1, 1)

        self.label_39 = QLabel(self.page_activities)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_14.addWidget(self.label_39, 12, 5, 1, 1)

        self.label_57 = QLabel(self.page_activities)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_14.addWidget(self.label_57, 11, 7, 1, 1)

        self.id_label_3 = QLabel(self.page_activities)
        self.id_label_3.setObjectName(u"id_label_3")

        self.gridLayout_14.addWidget(self.id_label_3, 6, 0, 1, 1)

        self.label_49 = QLabel(self.page_activities)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_14.addWidget(self.label_49, 3, 7, 1, 1)

        self.label_52 = QLabel(self.page_activities)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_14.addWidget(self.label_52, 6, 7, 1, 1)

        self.wing_entry = QLineEdit(self.page_activities)
        self.wing_entry.setObjectName(u"wing_entry")
        sizePolicy9.setHeightForWidth(self.wing_entry.sizePolicy().hasHeightForWidth())
        self.wing_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.wing_entry, 9, 8, 1, 1)

        self.inst_cert_label_2 = QLabel(self.page_activities)
        self.inst_cert_label_2.setObjectName(u"inst_cert_label_2")

        self.gridLayout_14.addWidget(self.inst_cert_label_2, 6, 2, 1, 1)

        self.label_61 = QLabel(self.page_activities)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_14.addWidget(self.label_61, 15, 7, 1, 1)

        self.label_29 = QLabel(self.page_activities)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_14.addWidget(self.label_29, 2, 5, 1, 1)

        self.label_64 = QLabel(self.page_activities)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_14.addWidget(self.label_64, 18, 7, 1, 1)

        self.label_59 = QLabel(self.page_activities)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_14.addWidget(self.label_59, 13, 7, 1, 1)

        self.label_37 = QLabel(self.page_activities)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_14.addWidget(self.label_37, 10, 5, 1, 1)

        self.twin_air_entry = QLineEdit(self.page_activities)
        self.twin_air_entry.setObjectName(u"twin_air_entry")
        sizePolicy9.setHeightForWidth(self.twin_air_entry.sizePolicy().hasHeightForWidth())
        self.twin_air_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.twin_air_entry, 5, 8, 1, 1)

        self.t_3l_air_entry = QLineEdit(self.page_activities)
        self.t_3l_air_entry.setObjectName(u"t_3l_air_entry")
        sizePolicy9.setHeightForWidth(self.t_3l_air_entry.sizePolicy().hasHeightForWidth())
        self.t_3l_air_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.t_3l_air_entry, 17, 6, 1, 1)

        self.label_27 = QLabel(self.page_activities)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_14.addWidget(self.label_27, 0, 5, 1, 1)

        self.label_62 = QLabel(self.page_activities)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_14.addWidget(self.label_62, 16, 7, 1, 1)

        self.price_entry = QLineEdit(self.page_activities)
        self.price_entry.setObjectName(u"price_entry")
        sizePolicy9.setHeightForWidth(self.price_entry.sizePolicy().hasHeightForWidth())
        self.price_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.price_entry, 2, 1, 1, 1)

        self.label_44 = QLabel(self.page_activities)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_14.addWidget(self.label_44, 17, 5, 1, 1)

        self.label_28 = QLabel(self.page_activities)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_14.addWidget(self.label_28, 1, 5, 1, 1)

        self.soft_dive_entry = QLineEdit(self.page_activities)
        self.soft_dive_entry.setObjectName(u"soft_dive_entry")
        sizePolicy9.setHeightForWidth(self.soft_dive_entry.sizePolicy().hasHeightForWidth())
        self.soft_dive_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.soft_dive_entry, 11, 6, 1, 1)

        self.price_label_2 = QLabel(self.page_activities)
        self.price_label_2.setObjectName(u"price_label_2")

        self.gridLayout_14.addWidget(self.price_label_2, 6, 3, 1, 1)

        self.label_34 = QLabel(self.page_activities)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_14.addWidget(self.label_34, 7, 5, 1, 1)

        self.delete_record_button = QPushButton(self.page_activities)
        self.delete_record_button.setObjectName(u"delete_record_button")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush42 = QBrush(QColor(210, 210, 210, 128))
        brush42.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush42)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush43 = QBrush(QColor(210, 210, 210, 128))
        brush43.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush43)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush44 = QBrush(QColor(210, 210, 210, 128))
        brush44.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush44)
#endif
        self.delete_record_button.setPalette(palette10)

        self.gridLayout_14.addWidget(self.delete_record_button, 5, 2, 1, 1)

        self.label_51 = QLabel(self.page_activities)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_14.addWidget(self.label_51, 5, 7, 1, 1)

        self.label_32 = QLabel(self.page_activities)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_14.addWidget(self.label_32, 5, 5, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_6, 1, 4, 1, 1)

        self.label_63 = QLabel(self.page_activities)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_14.addWidget(self.label_63, 17, 7, 1, 1)

        self.tech_reg_entry = QLineEdit(self.page_activities)
        self.tech_reg_entry.setObjectName(u"tech_reg_entry")
        sizePolicy9.setHeightForWidth(self.tech_reg_entry.sizePolicy().hasHeightForWidth())
        self.tech_reg_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.tech_reg_entry, 7, 8, 1, 1)

        self.label_42 = QLabel(self.page_activities)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_14.addWidget(self.label_42, 15, 5, 1, 1)

        self.label_31 = QLabel(self.page_activities)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_14.addWidget(self.label_31, 4, 5, 1, 1)

        self.label_38 = QLabel(self.page_activities)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_14.addWidget(self.label_38, 11, 5, 1, 1)

        self.label_53 = QLabel(self.page_activities)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_14.addWidget(self.label_53, 7, 7, 1, 1)

        self.twin_eanx_entry = QLineEdit(self.page_activities)
        self.twin_eanx_entry.setObjectName(u"twin_eanx_entry")
        sizePolicy9.setHeightForWidth(self.twin_eanx_entry.sizePolicy().hasHeightForWidth())
        self.twin_eanx_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.twin_eanx_entry, 6, 8, 1, 1)

        self.inst_cert_label = QLabel(self.page_activities)
        self.inst_cert_label.setObjectName(u"inst_cert_label")

        self.gridLayout_14.addWidget(self.inst_cert_label, 1, 0, 1, 1)

        self.slate_entry = QLineEdit(self.page_activities)
        self.slate_entry.setObjectName(u"slate_entry")
        sizePolicy9.setHeightForWidth(self.slate_entry.sizePolicy().hasHeightForWidth())
        self.slate_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.slate_entry, 16, 8, 1, 1)

        self.t_18__entry = QLineEdit(self.page_activities)
        self.t_18__entry.setObjectName(u"t_18__entry")
        sizePolicy9.setHeightForWidth(self.t_18__entry.sizePolicy().hasHeightForWidth())
        self.t_18__entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.t_18__entry, 16, 6, 1, 1)

        self.smb_entry = QLineEdit(self.page_activities)
        self.smb_entry.setObjectName(u"smb_entry")
        sizePolicy9.setHeightForWidth(self.smb_entry.sizePolicy().hasHeightForWidth())
        self.smb_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.smb_entry, 14, 8, 1, 1)

        self.bcd_day_entry = QLineEdit(self.page_activities)
        self.bcd_day_entry.setObjectName(u"bcd_day_entry")
        sizePolicy9.setHeightForWidth(self.bcd_day_entry.sizePolicy().hasHeightForWidth())
        self.bcd_day_entry.setSizePolicy(sizePolicy9)

        self.gridLayout_14.addWidget(self.bcd_day_entry, 6, 6, 1, 1)

        self.inst_cert_list_results = QLabel(self.page_activities)
        self.inst_cert_list_results.setObjectName(u"inst_cert_list_results")

        self.gridLayout_14.addWidget(self.inst_cert_list_results, 7, 2, 2, 1)

        self.activity_list_results = QLabel(self.page_activities)
        self.activity_list_results.setObjectName(u"activity_list_results")

        self.gridLayout_14.addWidget(self.activity_list_results, 7, 1, 2, 1)

        self.id_list_results_ = QLabel(self.page_activities)
        self.id_list_results_.setObjectName(u"id_list_results_")

        self.gridLayout_14.addWidget(self.id_list_results_, 7, 0, 2, 1)

        self.price_list_results = QLabel(self.page_activities)
        self.price_list_results.setObjectName(u"price_list_results")

        self.gridLayout_14.addWidget(self.price_list_results, 7, 3, 2, 1)

        self.stackedWidget.addWidget(self.page_activities)
        self.page_am_dive_add = QWidget()
        self.page_am_dive_add.setObjectName(u"page_am_dive_add")
        self.gridLayout_13 = QGridLayout(self.page_am_dive_add)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.dob_search_label_3 = QLabel(self.page_am_dive_add)
        self.dob_search_label_3.setObjectName(u"dob_search_label_3")

        self.gridLayout_13.addWidget(self.dob_search_label_3, 2, 8, 1, 1)

        self.l_name_search_label_5 = QLabel(self.page_am_dive_add)
        self.l_name_search_label_5.setObjectName(u"l_name_search_label_5")
        self.l_name_search_label_5.setFont(font5)

        self.gridLayout_13.addWidget(self.l_name_search_label_5, 0, 5, 1, 1)

        self.l_name_search_label_6 = QLabel(self.page_am_dive_add)
        self.l_name_search_label_6.setObjectName(u"l_name_search_label_6")

        self.gridLayout_13.addWidget(self.l_name_search_label_6, 2, 7, 1, 1)

        self.f_name_search_label_3 = QLabel(self.page_am_dive_add)
        self.f_name_search_label_3.setObjectName(u"f_name_search_label_3")

        self.gridLayout_13.addWidget(self.f_name_search_label_3, 2, 6, 1, 1)

        self.groupBox_3 = QGroupBox(self.page_am_dive_add)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.am_soft_dive_check_2 = QCheckBox(self.groupBox_3)
        self.am_soft_dive_check_2.setObjectName(u"am_soft_dive_check_2")
        self.am_soft_dive_check_2.setGeometry(QRect(220, 120, 101, 23))
        self.am_torch_check_2 = QCheckBox(self.groupBox_3)
        self.am_torch_check_2.setObjectName(u"am_torch_check_2")
        self.am_torch_check_2.setGeometry(QRect(10, 150, 151, 23))
        self.am_full_equip_dive_check = QCheckBox(self.groupBox_3)
        self.am_full_equip_dive_check.setObjectName(u"am_full_equip_dive_check")
        self.am_full_equip_dive_check.setGeometry(QRect(10, 30, 171, 23))
        self.am_reg_dive_check_2 = QCheckBox(self.groupBox_3)
        self.am_reg_dive_check_2.setObjectName(u"am_reg_dive_check_2")
        self.am_reg_dive_check_2.setGeometry(QRect(220, 30, 111, 23))
        self.am_reg_upgrade_check_2 = QCheckBox(self.groupBox_3)
        self.am_reg_upgrade_check_2.setObjectName(u"am_reg_upgrade_check_2")
        self.am_reg_upgrade_check_2.setGeometry(QRect(220, 90, 131, 23))
        self.am_full_equip_day_check = QCheckBox(self.groupBox_3)
        self.am_full_equip_day_check.setObjectName(u"am_full_equip_day_check")
        self.am_full_equip_day_check.setGeometry(QRect(10, 60, 161, 23))
        self.am_computer_check = QCheckBox(self.groupBox_3)
        self.am_computer_check.setObjectName(u"am_computer_check")
        self.am_computer_check.setGeometry(QRect(10, 120, 161, 23))
        self.am_bcd_dive_check_2 = QCheckBox(self.groupBox_3)
        self.am_bcd_dive_check_2.setObjectName(u"am_bcd_dive_check_2")
        self.am_bcd_dive_check_2.setGeometry(QRect(10, 180, 131, 23))
        self.am_bcd_day_check_2 = QCheckBox(self.groupBox_3)
        self.am_bcd_day_check_2.setObjectName(u"am_bcd_day_check_2")
        self.am_bcd_day_check_2.setGeometry(QRect(10, 210, 121, 23))
        self.am_full_equip_upgrade_check = QCheckBox(self.groupBox_3)
        self.am_full_equip_upgrade_check.setObjectName(u"am_full_equip_upgrade_check")
        self.am_full_equip_upgrade_check.setGeometry(QRect(10, 90, 181, 23))
        self.am_soft_upgrade_check_2 = QCheckBox(self.groupBox_3)
        self.am_soft_upgrade_check_2.setObjectName(u"am_soft_upgrade_check_2")
        self.am_soft_upgrade_check_2.setGeometry(QRect(220, 180, 151, 23))
        self.am_soft_day_check_2 = QCheckBox(self.groupBox_3)
        self.am_soft_day_check_2.setObjectName(u"am_soft_day_check_2")
        self.am_soft_day_check_2.setGeometry(QRect(220, 150, 90, 23))
        self.am_bcd_upgrade_check_2 = QCheckBox(self.groupBox_3)
        self.am_bcd_upgrade_check_2.setObjectName(u"am_bcd_upgrade_check_2")
        self.am_bcd_upgrade_check_2.setGeometry(QRect(10, 240, 131, 23))
        self.am_reg_day_check_2 = QCheckBox(self.groupBox_3)
        self.am_reg_day_check_2.setObjectName(u"am_reg_day_check_2")
        self.am_reg_day_check_2.setGeometry(QRect(220, 60, 111, 23))
        self.am_add_to_dive_button = QPushButton(self.groupBox_3)
        self.am_add_to_dive_button.setObjectName(u"am_add_to_dive_button")
        self.am_add_to_dive_button.setGeometry(QRect(20, 390, 151, 91))

        self.gridLayout_13.addWidget(self.groupBox_3, 3, 0, 3, 2)

        self.am_id_entry = QLineEdit(self.page_am_dive_add)
        self.am_id_entry.setObjectName(u"am_id_entry")
        sizePolicy5.setHeightForWidth(self.am_id_entry.sizePolicy().hasHeightForWidth())
        self.am_id_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_13.addWidget(self.am_id_entry, 0, 1, 1, 1)

        self.am_l_name_search_entry = QLineEdit(self.page_am_dive_add)
        self.am_l_name_search_entry.setObjectName(u"am_l_name_search_entry")
        sizePolicy5.setHeightForWidth(self.am_l_name_search_entry.sizePolicy().hasHeightForWidth())
        self.am_l_name_search_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_13.addWidget(self.am_l_name_search_entry, 0, 7, 1, 1)

        self.am_oid_search_results_label = QLabel(self.page_am_dive_add)
        self.am_oid_search_results_label.setObjectName(u"am_oid_search_results_label")

        self.gridLayout_13.addWidget(self.am_oid_search_results_label, 3, 5, 1, 1)

        self.am_l_name_search_results_label_2 = QLabel(self.page_am_dive_add)
        self.am_l_name_search_results_label_2.setObjectName(u"am_l_name_search_results_label_2")

        self.gridLayout_13.addWidget(self.am_l_name_search_results_label_2, 3, 8, 1, 1)

        self.am_search_customer_button = QPushButton(self.page_am_dive_add)
        self.am_search_customer_button.setObjectName(u"am_search_customer_button")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush45 = QBrush(QColor(210, 210, 210, 128))
        brush45.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush45)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush46 = QBrush(QColor(210, 210, 210, 128))
        brush46.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush46)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush47 = QBrush(QColor(210, 210, 210, 128))
        brush47.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush47)
#endif
        self.am_search_customer_button.setPalette(palette11)

        self.gridLayout_13.addWidget(self.am_search_customer_button, 0, 8, 1, 1)

        self.oid_search_label_3 = QLabel(self.page_am_dive_add)
        self.oid_search_label_3.setObjectName(u"oid_search_label_3")

        self.gridLayout_13.addWidget(self.oid_search_label_3, 2, 5, 1, 1)

        self.am_l_name_search_results_label = QLabel(self.page_am_dive_add)
        self.am_l_name_search_results_label.setObjectName(u"am_l_name_search_results_label")

        self.gridLayout_13.addWidget(self.am_l_name_search_results_label, 3, 7, 1, 1)

        self.label_68 = QLabel(self.page_am_dive_add)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font4)

        self.gridLayout_13.addWidget(self.label_68, 2, 0, 1, 1)

        self.am_f_name_search_results_label = QLabel(self.page_am_dive_add)
        self.am_f_name_search_results_label.setObjectName(u"am_f_name_search_results_label")

        self.gridLayout_13.addWidget(self.am_f_name_search_results_label, 3, 6, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_9, 2, 3, 1, 1)

        self.label_67 = QLabel(self.page_am_dive_add)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font4)

        self.gridLayout_13.addWidget(self.label_67, 0, 0, 1, 1)

        self.am_activity_combo = QComboBox(self.page_am_dive_add)
        self.am_activity_combo.setObjectName(u"am_activity_combo")
        sizePolicy5.setHeightForWidth(self.am_activity_combo.sizePolicy().hasHeightForWidth())
        self.am_activity_combo.setSizePolicy(sizePolicy5)

        self.gridLayout_13.addWidget(self.am_activity_combo, 2, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.page_am_dive_add)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.am_twin_air_check = QCheckBox(self.groupBox_2)
        self.am_twin_air_check.setObjectName(u"am_twin_air_check")
        self.am_twin_air_check.setGeometry(QRect(20, 300, 111, 23))
        self.am_6l_50_check = QCheckBox(self.groupBox_2)
        self.am_6l_50_check.setObjectName(u"am_6l_50_check")
        self.am_6l_50_check.setGeometry(QRect(20, 180, 90, 23))
        self.am_twin_eanx_check = QCheckBox(self.groupBox_2)
        self.am_twin_eanx_check.setObjectName(u"am_twin_eanx_check")
        self.am_twin_eanx_check.setGeometry(QRect(20, 330, 131, 23))
        self.am_12l_100_check = QCheckBox(self.groupBox_2)
        self.am_12l_100_check.setObjectName(u"am_12l_100_check")
        self.am_12l_100_check.setGeometry(QRect(20, 270, 90, 23))
        self.am_6l_100_check = QCheckBox(self.groupBox_2)
        self.am_6l_100_check.setObjectName(u"am_6l_100_check")
        self.am_6l_100_check.setGeometry(QRect(20, 210, 90, 23))
        self.am_15l_upgrade_check = QCheckBox(self.groupBox_2)
        self.am_15l_upgrade_check.setObjectName(u"am_15l_upgrade_check")
        self.am_15l_upgrade_check.setGeometry(QRect(20, 60, 131, 23))
        self.am_18l_upgrade_check = QCheckBox(self.groupBox_2)
        self.am_18l_upgrade_check.setObjectName(u"am_18l_upgrade_check")
        self.am_18l_upgrade_check.setGeometry(QRect(20, 90, 121, 23))
        self.am_12l_50_check = QCheckBox(self.groupBox_2)
        self.am_12l_50_check.setObjectName(u"am_12l_50_check")
        self.am_12l_50_check.setGeometry(QRect(20, 240, 90, 23))
        self.am_eanx_upgrade_check = QCheckBox(self.groupBox_2)
        self.am_eanx_upgrade_check.setObjectName(u"am_eanx_upgrade_check")
        self.am_eanx_upgrade_check.setGeometry(QRect(20, 30, 121, 23))
        self.am_no_tank_check = QCheckBox(self.groupBox_2)
        self.am_no_tank_check.setObjectName(u"am_no_tank_check")
        self.am_no_tank_check.setGeometry(QRect(20, 360, 131, 23))
        self.am_3l_100_check = QCheckBox(self.groupBox_2)
        self.am_3l_100_check.setObjectName(u"am_3l_100_check")
        self.am_3l_100_check.setGeometry(QRect(20, 150, 121, 23))
        self.am_3l_air_check = QCheckBox(self.groupBox_2)
        self.am_3l_air_check.setObjectName(u"am_3l_air_check")
        self.am_3l_air_check.setGeometry(QRect(20, 120, 121, 23))

        self.gridLayout_13.addWidget(self.groupBox_2, 3, 2, 3, 1)

        self.groupBox = QGroupBox(self.page_am_dive_add)
        self.groupBox.setObjectName(u"groupBox")
        self.am_smb_check = QCheckBox(self.groupBox)
        self.am_smb_check.setObjectName(u"am_smb_check")
        self.am_smb_check.setGeometry(QRect(20, 240, 90, 23))
        self.am_tech_torch_check = QCheckBox(self.groupBox)
        self.am_tech_torch_check.setObjectName(u"am_tech_torch_check")
        self.am_tech_torch_check.setGeometry(QRect(20, 180, 90, 23))
        self.am_o2_reg_check = QCheckBox(self.groupBox)
        self.am_o2_reg_check.setObjectName(u"am_o2_reg_check")
        self.am_o2_reg_check.setGeometry(QRect(20, 120, 251, 23))
        self.am_back_plate_check = QCheckBox(self.groupBox)
        self.am_back_plate_check.setObjectName(u"am_back_plate_check")
        self.am_back_plate_check.setGeometry(QRect(20, 60, 191, 23))
        self.am_reel_check = QCheckBox(self.groupBox)
        self.am_reel_check.setObjectName(u"am_reel_check")
        self.am_reel_check.setGeometry(QRect(20, 270, 90, 23))
        self.am_slate_check = QCheckBox(self.groupBox)
        self.am_slate_check.setObjectName(u"am_slate_check")
        self.am_slate_check.setGeometry(QRect(20, 300, 111, 23))
        self.am_tech_computer_check = QCheckBox(self.groupBox)
        self.am_tech_computer_check.setObjectName(u"am_tech_computer_check")
        self.am_tech_computer_check.setGeometry(QRect(20, 150, 121, 23))
        self.am_tech_reg_check = QCheckBox(self.groupBox)
        self.am_tech_reg_check.setObjectName(u"am_tech_reg_check")
        self.am_tech_reg_check.setGeometry(QRect(20, 30, 141, 23))
        self.am_wing_check = QCheckBox(self.groupBox)
        self.am_wing_check.setObjectName(u"am_wing_check")
        self.am_wing_check.setGeometry(QRect(20, 90, 151, 23))
        self.am_wreck_reel_check = QCheckBox(self.groupBox)
        self.am_wreck_reel_check.setObjectName(u"am_wreck_reel_check")
        self.am_wreck_reel_check.setGeometry(QRect(20, 210, 151, 23))
        self.label_69 = QLabel(self.groupBox)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(160, 365, 31, 17))
        self.label_70 = QLabel(self.groupBox)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(40, 365, 41, 17))
        self.am_rebreather_check = QCheckBox(self.groupBox)
        self.am_rebreather_check.setObjectName(u"am_rebreather_check")
        self.am_rebreather_check.setGeometry(QRect(20, 330, 111, 23))
        self.am_sorb_entry = QLineEdit(self.groupBox)
        self.am_sorb_entry.setObjectName(u"am_sorb_entry")
        self.am_sorb_entry.setGeometry(QRect(90, 360, 61, 31))
        self.label_71 = QLabel(self.groupBox)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(10, 410, 411, 31))
        sizePolicy9.setHeightForWidth(self.label_71.sizePolicy().hasHeightForWidth())
        self.label_71.setSizePolicy(sizePolicy9)

        self.gridLayout_13.addWidget(self.groupBox, 3, 3, 3, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_10, 3, 4, 1, 1)

        self.stackedWidget.addWidget(self.page_am_dive_add)
        self.page_mam_dive_add = QWidget()
        self.page_mam_dive_add.setObjectName(u"page_mam_dive_add")
        self.gridLayout_15 = QGridLayout(self.page_mam_dive_add)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.dob_search_label_4 = QLabel(self.page_mam_dive_add)
        self.dob_search_label_4.setObjectName(u"dob_search_label_4")

        self.gridLayout_15.addWidget(self.dob_search_label_4, 1, 10, 1, 1)

        self.label_73 = QLabel(self.page_mam_dive_add)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font4)

        self.gridLayout_15.addWidget(self.label_73, 1, 0, 1, 1)

        self.mam_activity_combo = QComboBox(self.page_mam_dive_add)
        self.mam_activity_combo.setObjectName(u"mam_activity_combo")
        sizePolicy5.setHeightForWidth(self.mam_activity_combo.sizePolicy().hasHeightForWidth())
        self.mam_activity_combo.setSizePolicy(sizePolicy5)

        self.gridLayout_15.addWidget(self.mam_activity_combo, 1, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.page_mam_dive_add)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.mam_soft_dive_check = QCheckBox(self.groupBox_4)
        self.mam_soft_dive_check.setObjectName(u"mam_soft_dive_check")
        self.mam_soft_dive_check.setGeometry(QRect(210, 120, 90, 23))
        self.mam_torch_check = QCheckBox(self.groupBox_4)
        self.mam_torch_check.setObjectName(u"mam_torch_check")
        self.mam_torch_check.setGeometry(QRect(20, 150, 151, 23))
        self.mam_full_equip_dive_check = QCheckBox(self.groupBox_4)
        self.mam_full_equip_dive_check.setObjectName(u"mam_full_equip_dive_check")
        self.mam_full_equip_dive_check.setGeometry(QRect(20, 30, 171, 23))
        self.mam_reg_dive_check = QCheckBox(self.groupBox_4)
        self.mam_reg_dive_check.setObjectName(u"mam_reg_dive_check")
        self.mam_reg_dive_check.setGeometry(QRect(210, 30, 111, 23))
        self.mam_reg_upgrade_check = QCheckBox(self.groupBox_4)
        self.mam_reg_upgrade_check.setObjectName(u"mam_reg_upgrade_check")
        self.mam_reg_upgrade_check.setGeometry(QRect(210, 90, 131, 23))
        self.mam_full_equip_day_check = QCheckBox(self.groupBox_4)
        self.mam_full_equip_day_check.setObjectName(u"mam_full_equip_day_check")
        self.mam_full_equip_day_check.setGeometry(QRect(20, 60, 161, 23))
        self.mam_computer_check = QCheckBox(self.groupBox_4)
        self.mam_computer_check.setObjectName(u"mam_computer_check")
        self.mam_computer_check.setGeometry(QRect(20, 120, 161, 23))
        self.mam_bcd_dive_check = QCheckBox(self.groupBox_4)
        self.mam_bcd_dive_check.setObjectName(u"mam_bcd_dive_check")
        self.mam_bcd_dive_check.setGeometry(QRect(20, 180, 131, 23))
        self.mam_bcd_day_check = QCheckBox(self.groupBox_4)
        self.mam_bcd_day_check.setObjectName(u"mam_bcd_day_check")
        self.mam_bcd_day_check.setGeometry(QRect(20, 210, 121, 23))
        self.mam_full_equip_upgrade_check = QCheckBox(self.groupBox_4)
        self.mam_full_equip_upgrade_check.setObjectName(u"mam_full_equip_upgrade_check")
        self.mam_full_equip_upgrade_check.setGeometry(QRect(20, 90, 181, 23))
        self.mam_soft_upgrade_check = QCheckBox(self.groupBox_4)
        self.mam_soft_upgrade_check.setObjectName(u"mam_soft_upgrade_check")
        self.mam_soft_upgrade_check.setGeometry(QRect(210, 180, 151, 23))
        self.mam_soft_day_check = QCheckBox(self.groupBox_4)
        self.mam_soft_day_check.setObjectName(u"mam_soft_day_check")
        self.mam_soft_day_check.setGeometry(QRect(210, 150, 90, 23))
        self.mam_bcd_upgrade_check = QCheckBox(self.groupBox_4)
        self.mam_bcd_upgrade_check.setObjectName(u"mam_bcd_upgrade_check")
        self.mam_bcd_upgrade_check.setGeometry(QRect(20, 240, 131, 23))
        self.mam_reg_day_check = QCheckBox(self.groupBox_4)
        self.mam_reg_day_check.setObjectName(u"mam_reg_day_check")
        self.mam_reg_day_check.setGeometry(QRect(210, 60, 111, 23))
        self.mam_add_to_dive_button = QPushButton(self.groupBox_4)
        self.mam_add_to_dive_button.setObjectName(u"mam_add_to_dive_button")
        self.mam_add_to_dive_button.setGeometry(QRect(20, 350, 141, 81))

        self.gridLayout_15.addWidget(self.groupBox_4, 2, 0, 2, 2)

        self.label_72 = QLabel(self.page_mam_dive_add)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font4)

        self.gridLayout_15.addWidget(self.label_72, 0, 0, 1, 1)

        self.l_name_search_label_8 = QLabel(self.page_mam_dive_add)
        self.l_name_search_label_8.setObjectName(u"l_name_search_label_8")

        self.gridLayout_15.addWidget(self.l_name_search_label_8, 1, 9, 1, 1)

        self.l_name_search_label_7 = QLabel(self.page_mam_dive_add)
        self.l_name_search_label_7.setObjectName(u"l_name_search_label_7")
        self.l_name_search_label_7.setFont(font5)

        self.gridLayout_15.addWidget(self.l_name_search_label_7, 0, 6, 1, 1)

        self.groupBox_5 = QGroupBox(self.page_mam_dive_add)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.mam_twin_air_check = QCheckBox(self.groupBox_5)
        self.mam_twin_air_check.setObjectName(u"mam_twin_air_check")
        self.mam_twin_air_check.setGeometry(QRect(10, 300, 111, 23))
        self.mam_6l_50_check = QCheckBox(self.groupBox_5)
        self.mam_6l_50_check.setObjectName(u"mam_6l_50_check")
        self.mam_6l_50_check.setGeometry(QRect(10, 180, 90, 23))
        self.mam_twin_eanx_check = QCheckBox(self.groupBox_5)
        self.mam_twin_eanx_check.setObjectName(u"mam_twin_eanx_check")
        self.mam_twin_eanx_check.setGeometry(QRect(10, 330, 131, 23))
        self.mam_12l_100_check = QCheckBox(self.groupBox_5)
        self.mam_12l_100_check.setObjectName(u"mam_12l_100_check")
        self.mam_12l_100_check.setGeometry(QRect(10, 270, 90, 23))
        self.mam_6l_100_check = QCheckBox(self.groupBox_5)
        self.mam_6l_100_check.setObjectName(u"mam_6l_100_check")
        self.mam_6l_100_check.setGeometry(QRect(10, 210, 90, 23))
        self.mam_15l_upgrade_check = QCheckBox(self.groupBox_5)
        self.mam_15l_upgrade_check.setObjectName(u"mam_15l_upgrade_check")
        self.mam_15l_upgrade_check.setGeometry(QRect(10, 60, 131, 23))
        self.mam_18l_upgrade_check = QCheckBox(self.groupBox_5)
        self.mam_18l_upgrade_check.setObjectName(u"mam_18l_upgrade_check")
        self.mam_18l_upgrade_check.setGeometry(QRect(10, 90, 121, 23))
        self.mam_12l_50_check = QCheckBox(self.groupBox_5)
        self.mam_12l_50_check.setObjectName(u"mam_12l_50_check")
        self.mam_12l_50_check.setGeometry(QRect(10, 240, 90, 23))
        self.mam_eanx_upgrade_check = QCheckBox(self.groupBox_5)
        self.mam_eanx_upgrade_check.setObjectName(u"mam_eanx_upgrade_check")
        self.mam_eanx_upgrade_check.setGeometry(QRect(10, 30, 121, 23))
        self.mam_no_tank_check = QCheckBox(self.groupBox_5)
        self.mam_no_tank_check.setObjectName(u"mam_no_tank_check")
        self.mam_no_tank_check.setGeometry(QRect(10, 360, 131, 23))
        self.mam_3l_100_check = QCheckBox(self.groupBox_5)
        self.mam_3l_100_check.setObjectName(u"mam_3l_100_check")
        self.mam_3l_100_check.setGeometry(QRect(10, 150, 121, 23))
        self.mam_3l_air_check = QCheckBox(self.groupBox_5)
        self.mam_3l_air_check.setObjectName(u"mam_3l_air_check")
        self.mam_3l_air_check.setGeometry(QRect(10, 120, 121, 23))

        self.gridLayout_15.addWidget(self.groupBox_5, 2, 2, 2, 1)

        self.f_name_search_label_4 = QLabel(self.page_mam_dive_add)
        self.f_name_search_label_4.setObjectName(u"f_name_search_label_4")

        self.gridLayout_15.addWidget(self.f_name_search_label_4, 1, 8, 1, 1)

        self.groupBox_6 = QGroupBox(self.page_mam_dive_add)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.mam_smb_check_2 = QCheckBox(self.groupBox_6)
        self.mam_smb_check_2.setObjectName(u"mam_smb_check_2")
        self.mam_smb_check_2.setGeometry(QRect(20, 240, 90, 23))
        self.mam_tech_torch_check_2 = QCheckBox(self.groupBox_6)
        self.mam_tech_torch_check_2.setObjectName(u"mam_tech_torch_check_2")
        self.mam_tech_torch_check_2.setGeometry(QRect(20, 180, 90, 23))
        self.mam_o2_reg_check_2 = QCheckBox(self.groupBox_6)
        self.mam_o2_reg_check_2.setObjectName(u"mam_o2_reg_check_2")
        self.mam_o2_reg_check_2.setGeometry(QRect(20, 120, 251, 23))
        self.mam_back_plate_check_2 = QCheckBox(self.groupBox_6)
        self.mam_back_plate_check_2.setObjectName(u"mam_back_plate_check_2")
        self.mam_back_plate_check_2.setGeometry(QRect(20, 60, 191, 23))
        self.mam_reel_check_2 = QCheckBox(self.groupBox_6)
        self.mam_reel_check_2.setObjectName(u"mam_reel_check_2")
        self.mam_reel_check_2.setGeometry(QRect(20, 270, 90, 23))
        self.mam_slate_check_2 = QCheckBox(self.groupBox_6)
        self.mam_slate_check_2.setObjectName(u"mam_slate_check_2")
        self.mam_slate_check_2.setGeometry(QRect(20, 300, 111, 23))
        self.mam_tech_computer_check_2 = QCheckBox(self.groupBox_6)
        self.mam_tech_computer_check_2.setObjectName(u"mam_tech_computer_check_2")
        self.mam_tech_computer_check_2.setGeometry(QRect(20, 150, 121, 23))
        self.mam_tech_reg_check_2 = QCheckBox(self.groupBox_6)
        self.mam_tech_reg_check_2.setObjectName(u"mam_tech_reg_check_2")
        self.mam_tech_reg_check_2.setGeometry(QRect(20, 30, 141, 23))
        self.mam_wing_check_2 = QCheckBox(self.groupBox_6)
        self.mam_wing_check_2.setObjectName(u"mam_wing_check_2")
        self.mam_wing_check_2.setGeometry(QRect(20, 90, 151, 23))
        self.mam_wreck_reel_check_2 = QCheckBox(self.groupBox_6)
        self.mam_wreck_reel_check_2.setObjectName(u"mam_wreck_reel_check_2")
        self.mam_wreck_reel_check_2.setGeometry(QRect(20, 210, 151, 23))
        self.mam_rebreather_check_2 = QCheckBox(self.groupBox_6)
        self.mam_rebreather_check_2.setObjectName(u"mam_rebreather_check_2")
        self.mam_rebreather_check_2.setGeometry(QRect(20, 330, 111, 23))
        self.label_76 = QLabel(self.groupBox_6)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(30, 360, 41, 17))
        self.mam_sorb_entry_2 = QLineEdit(self.groupBox_6)
        self.mam_sorb_entry_2.setObjectName(u"mam_sorb_entry_2")
        self.mam_sorb_entry_2.setGeometry(QRect(80, 355, 61, 31))
        self.label_77 = QLabel(self.groupBox_6)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(150, 360, 31, 17))
        self.label_78 = QLabel(self.groupBox_6)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(10, 420, 321, 51))

        self.gridLayout_15.addWidget(self.groupBox_6, 2, 3, 2, 2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_11, 2, 5, 1, 1)

        self.oid_search_label_4 = QLabel(self.page_mam_dive_add)
        self.oid_search_label_4.setObjectName(u"oid_search_label_4")

        self.gridLayout_15.addWidget(self.oid_search_label_4, 1, 6, 1, 1)

        self.mam_id_entry = QLineEdit(self.page_mam_dive_add)
        self.mam_id_entry.setObjectName(u"mam_id_entry")
        sizePolicy5.setHeightForWidth(self.mam_id_entry.sizePolicy().hasHeightForWidth())
        self.mam_id_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_15.addWidget(self.mam_id_entry, 0, 1, 1, 1)

        self.mam_search_customer_button = QPushButton(self.page_mam_dive_add)
        self.mam_search_customer_button.setObjectName(u"mam_search_customer_button")
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush48 = QBrush(QColor(210, 210, 210, 128))
        brush48.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush48)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush49 = QBrush(QColor(210, 210, 210, 128))
        brush49.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush49)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush50 = QBrush(QColor(210, 210, 210, 128))
        brush50.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush50)
#endif
        self.mam_search_customer_button.setPalette(palette12)

        self.gridLayout_15.addWidget(self.mam_search_customer_button, 0, 10, 1, 1)

        self.mam_l_name_search_entry = QLineEdit(self.page_mam_dive_add)
        self.mam_l_name_search_entry.setObjectName(u"mam_l_name_search_entry")
        sizePolicy5.setHeightForWidth(self.mam_l_name_search_entry.sizePolicy().hasHeightForWidth())
        self.mam_l_name_search_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_15.addWidget(self.mam_l_name_search_entry, 0, 9, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_12, 1, 3, 1, 1)

        self.mam_oid_search_results_label = QLabel(self.page_mam_dive_add)
        self.mam_oid_search_results_label.setObjectName(u"mam_oid_search_results_label")

        self.gridLayout_15.addWidget(self.mam_oid_search_results_label, 2, 6, 1, 1)

        self.mam_l_name_search_results_label = QLabel(self.page_mam_dive_add)
        self.mam_l_name_search_results_label.setObjectName(u"mam_l_name_search_results_label")

        self.gridLayout_15.addWidget(self.mam_l_name_search_results_label, 2, 9, 1, 1)

        self.mam_f_name_search_results_label = QLabel(self.page_mam_dive_add)
        self.mam_f_name_search_results_label.setObjectName(u"mam_f_name_search_results_label")

        self.gridLayout_15.addWidget(self.mam_f_name_search_results_label, 2, 8, 1, 1)

        self.mam_l_name_search_results_label_2 = QLabel(self.page_mam_dive_add)
        self.mam_l_name_search_results_label_2.setObjectName(u"mam_l_name_search_results_label_2")

        self.gridLayout_15.addWidget(self.mam_l_name_search_results_label_2, 2, 10, 1, 1)

        self.stackedWidget.addWidget(self.page_mam_dive_add)
        self.page_pm_dive_add = QWidget()
        self.page_pm_dive_add.setObjectName(u"page_pm_dive_add")
        self.gridLayout_17 = QGridLayout(self.page_pm_dive_add)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.dob_search_label_5 = QLabel(self.page_pm_dive_add)
        self.dob_search_label_5.setObjectName(u"dob_search_label_5")

        self.gridLayout_17.addWidget(self.dob_search_label_5, 1, 10, 1, 1)

        self.groupBox_8 = QGroupBox(self.page_pm_dive_add)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.pm_twin_air_check = QCheckBox(self.groupBox_8)
        self.pm_twin_air_check.setObjectName(u"pm_twin_air_check")
        self.pm_twin_air_check.setGeometry(QRect(10, 300, 111, 23))
        self.pm_6l_50_check = QCheckBox(self.groupBox_8)
        self.pm_6l_50_check.setObjectName(u"pm_6l_50_check")
        self.pm_6l_50_check.setGeometry(QRect(10, 180, 90, 23))
        self.pm_twin_eanx_check = QCheckBox(self.groupBox_8)
        self.pm_twin_eanx_check.setObjectName(u"pm_twin_eanx_check")
        self.pm_twin_eanx_check.setGeometry(QRect(10, 330, 131, 23))
        self.pm_12l_100_check = QCheckBox(self.groupBox_8)
        self.pm_12l_100_check.setObjectName(u"pm_12l_100_check")
        self.pm_12l_100_check.setGeometry(QRect(10, 270, 90, 23))
        self.pm_6l_100_check = QCheckBox(self.groupBox_8)
        self.pm_6l_100_check.setObjectName(u"pm_6l_100_check")
        self.pm_6l_100_check.setGeometry(QRect(10, 210, 90, 23))
        self.pm_15l_upgrade_check = QCheckBox(self.groupBox_8)
        self.pm_15l_upgrade_check.setObjectName(u"pm_15l_upgrade_check")
        self.pm_15l_upgrade_check.setGeometry(QRect(10, 60, 131, 23))
        self.pm_18l_upgrade_check = QCheckBox(self.groupBox_8)
        self.pm_18l_upgrade_check.setObjectName(u"pm_18l_upgrade_check")
        self.pm_18l_upgrade_check.setGeometry(QRect(10, 90, 121, 23))
        self.pm_12l_50_check = QCheckBox(self.groupBox_8)
        self.pm_12l_50_check.setObjectName(u"pm_12l_50_check")
        self.pm_12l_50_check.setGeometry(QRect(10, 240, 90, 23))
        self.pm_eanx_upgrade_check = QCheckBox(self.groupBox_8)
        self.pm_eanx_upgrade_check.setObjectName(u"pm_eanx_upgrade_check")
        self.pm_eanx_upgrade_check.setGeometry(QRect(10, 30, 121, 23))
        self.pm_no_tank_check = QCheckBox(self.groupBox_8)
        self.pm_no_tank_check.setObjectName(u"pm_no_tank_check")
        self.pm_no_tank_check.setGeometry(QRect(10, 360, 131, 21))
        self.pm_3l_air_check = QCheckBox(self.groupBox_8)
        self.pm_3l_air_check.setObjectName(u"pm_3l_air_check")
        self.pm_3l_air_check.setGeometry(QRect(10, 120, 121, 23))
        self.pm_3l_100_check = QCheckBox(self.groupBox_8)
        self.pm_3l_100_check.setObjectName(u"pm_3l_100_check")
        self.pm_3l_100_check.setGeometry(QRect(10, 150, 121, 23))

        self.gridLayout_17.addWidget(self.groupBox_8, 2, 3, 1, 1)

        self.pm_oid_search_results_label = QLabel(self.page_pm_dive_add)
        self.pm_oid_search_results_label.setObjectName(u"pm_oid_search_results_label")

        self.gridLayout_17.addWidget(self.pm_oid_search_results_label, 2, 7, 1, 1)

        self.pm_l_name_search_entry = QLineEdit(self.page_pm_dive_add)
        self.pm_l_name_search_entry.setObjectName(u"pm_l_name_search_entry")
        sizePolicy5.setHeightForWidth(self.pm_l_name_search_entry.sizePolicy().hasHeightForWidth())
        self.pm_l_name_search_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_17.addWidget(self.pm_l_name_search_entry, 0, 9, 1, 1)

        self.f_name_search_label_5 = QLabel(self.page_pm_dive_add)
        self.f_name_search_label_5.setObjectName(u"f_name_search_label_5")

        self.gridLayout_17.addWidget(self.f_name_search_label_5, 1, 8, 1, 1)

        self.pm_search_customer_button = QPushButton(self.page_pm_dive_add)
        self.pm_search_customer_button.setObjectName(u"pm_search_customer_button")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush51 = QBrush(QColor(210, 210, 210, 128))
        brush51.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush51)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush52 = QBrush(QColor(210, 210, 210, 128))
        brush52.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush52)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush53 = QBrush(QColor(210, 210, 210, 128))
        brush53.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush53)
#endif
        self.pm_search_customer_button.setPalette(palette13)

        self.gridLayout_17.addWidget(self.pm_search_customer_button, 0, 10, 1, 1)

        self.groupBox_9 = QGroupBox(self.page_pm_dive_add)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.pm_smb_check = QCheckBox(self.groupBox_9)
        self.pm_smb_check.setObjectName(u"pm_smb_check")
        self.pm_smb_check.setGeometry(QRect(20, 240, 90, 23))
        self.pm_tech_torch_check = QCheckBox(self.groupBox_9)
        self.pm_tech_torch_check.setObjectName(u"pm_tech_torch_check")
        self.pm_tech_torch_check.setGeometry(QRect(20, 180, 90, 23))
        self.pm_o2_reg_check = QCheckBox(self.groupBox_9)
        self.pm_o2_reg_check.setObjectName(u"pm_o2_reg_check")
        self.pm_o2_reg_check.setGeometry(QRect(20, 120, 251, 23))
        self.pm_back_plate_check = QCheckBox(self.groupBox_9)
        self.pm_back_plate_check.setObjectName(u"pm_back_plate_check")
        self.pm_back_plate_check.setGeometry(QRect(20, 60, 191, 23))
        self.pm_reel_check = QCheckBox(self.groupBox_9)
        self.pm_reel_check.setObjectName(u"pm_reel_check")
        self.pm_reel_check.setGeometry(QRect(20, 270, 90, 23))
        self.pm_slate_check = QCheckBox(self.groupBox_9)
        self.pm_slate_check.setObjectName(u"pm_slate_check")
        self.pm_slate_check.setGeometry(QRect(20, 300, 111, 23))
        self.pm_tech_computer_check = QCheckBox(self.groupBox_9)
        self.pm_tech_computer_check.setObjectName(u"pm_tech_computer_check")
        self.pm_tech_computer_check.setGeometry(QRect(20, 150, 121, 23))
        self.pm_tech_reg_check = QCheckBox(self.groupBox_9)
        self.pm_tech_reg_check.setObjectName(u"pm_tech_reg_check")
        self.pm_tech_reg_check.setGeometry(QRect(20, 30, 141, 23))
        self.pm_wing_check = QCheckBox(self.groupBox_9)
        self.pm_wing_check.setObjectName(u"pm_wing_check")
        self.pm_wing_check.setGeometry(QRect(20, 90, 151, 23))
        self.pm_wreck_reel_check = QCheckBox(self.groupBox_9)
        self.pm_wreck_reel_check.setObjectName(u"pm_wreck_reel_check")
        self.pm_wreck_reel_check.setGeometry(QRect(20, 210, 151, 23))
        self.pm_rebreather_check = QCheckBox(self.groupBox_9)
        self.pm_rebreather_check.setObjectName(u"pm_rebreather_check")
        self.pm_rebreather_check.setGeometry(QRect(20, 330, 111, 23))
        self.label_81 = QLabel(self.groupBox_9)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(40, 365, 41, 17))
        self.pm_sorb_entry = QLineEdit(self.groupBox_9)
        self.pm_sorb_entry.setObjectName(u"pm_sorb_entry")
        self.pm_sorb_entry.setGeometry(QRect(90, 360, 61, 31))
        self.label_82 = QLabel(self.groupBox_9)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(160, 365, 31, 17))
        self.label_83 = QLabel(self.groupBox_9)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(10, 450, 511, 31))

        self.gridLayout_17.addWidget(self.groupBox_9, 2, 4, 1, 2)

        self.oid_search_label_5 = QLabel(self.page_pm_dive_add)
        self.oid_search_label_5.setObjectName(u"oid_search_label_5")

        self.gridLayout_17.addWidget(self.oid_search_label_5, 1, 7, 1, 1)

        self.pm_l_name_search_results_label = QLabel(self.page_pm_dive_add)
        self.pm_l_name_search_results_label.setObjectName(u"pm_l_name_search_results_label")

        self.gridLayout_17.addWidget(self.pm_l_name_search_results_label, 2, 9, 1, 1)

        self.pm_activity_combo = QComboBox(self.page_pm_dive_add)
        self.pm_activity_combo.setObjectName(u"pm_activity_combo")
        sizePolicy5.setHeightForWidth(self.pm_activity_combo.sizePolicy().hasHeightForWidth())
        self.pm_activity_combo.setSizePolicy(sizePolicy5)

        self.gridLayout_17.addWidget(self.pm_activity_combo, 1, 1, 1, 1)

        self.l_name_search_label_9 = QLabel(self.page_pm_dive_add)
        self.l_name_search_label_9.setObjectName(u"l_name_search_label_9")
        self.l_name_search_label_9.setFont(font5)

        self.gridLayout_17.addWidget(self.l_name_search_label_9, 0, 7, 1, 1)

        self.pm_id_entry = QLineEdit(self.page_pm_dive_add)
        self.pm_id_entry.setObjectName(u"pm_id_entry")
        sizePolicy5.setHeightForWidth(self.pm_id_entry.sizePolicy().hasHeightForWidth())
        self.pm_id_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_17.addWidget(self.pm_id_entry, 0, 1, 1, 1)

        self.label_79 = QLabel(self.page_pm_dive_add)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font4)

        self.gridLayout_17.addWidget(self.label_79, 0, 0, 1, 1)

        self.l_name_search_label_10 = QLabel(self.page_pm_dive_add)
        self.l_name_search_label_10.setObjectName(u"l_name_search_label_10")

        self.gridLayout_17.addWidget(self.l_name_search_label_10, 1, 9, 1, 1)

        self.groupBox_7 = QGroupBox(self.page_pm_dive_add)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.pm_soft_dive_check = QCheckBox(self.groupBox_7)
        self.pm_soft_dive_check.setObjectName(u"pm_soft_dive_check")
        self.pm_soft_dive_check.setGeometry(QRect(210, 120, 101, 23))
        self.pm_torch_check = QCheckBox(self.groupBox_7)
        self.pm_torch_check.setObjectName(u"pm_torch_check")
        self.pm_torch_check.setGeometry(QRect(10, 150, 151, 23))
        self.pm_full_equip_dive_check = QCheckBox(self.groupBox_7)
        self.pm_full_equip_dive_check.setObjectName(u"pm_full_equip_dive_check")
        self.pm_full_equip_dive_check.setGeometry(QRect(10, 30, 171, 23))
        self.pm_reg_dive_check = QCheckBox(self.groupBox_7)
        self.pm_reg_dive_check.setObjectName(u"pm_reg_dive_check")
        self.pm_reg_dive_check.setGeometry(QRect(210, 30, 111, 23))
        self.pm_reg_upgrade_check = QCheckBox(self.groupBox_7)
        self.pm_reg_upgrade_check.setObjectName(u"pm_reg_upgrade_check")
        self.pm_reg_upgrade_check.setGeometry(QRect(210, 90, 131, 23))
        self.pm_full_equip_day_check = QCheckBox(self.groupBox_7)
        self.pm_full_equip_day_check.setObjectName(u"pm_full_equip_day_check")
        self.pm_full_equip_day_check.setGeometry(QRect(10, 60, 161, 23))
        self.pm_computer_check = QCheckBox(self.groupBox_7)
        self.pm_computer_check.setObjectName(u"pm_computer_check")
        self.pm_computer_check.setGeometry(QRect(10, 120, 161, 23))
        self.pm_bcd_dive_check = QCheckBox(self.groupBox_7)
        self.pm_bcd_dive_check.setObjectName(u"pm_bcd_dive_check")
        self.pm_bcd_dive_check.setGeometry(QRect(10, 180, 131, 23))
        self.pm_bcd_day_check = QCheckBox(self.groupBox_7)
        self.pm_bcd_day_check.setObjectName(u"pm_bcd_day_check")
        self.pm_bcd_day_check.setGeometry(QRect(10, 210, 121, 23))
        self.pm_full_equip_upgrade_check = QCheckBox(self.groupBox_7)
        self.pm_full_equip_upgrade_check.setObjectName(u"pm_full_equip_upgrade_check")
        self.pm_full_equip_upgrade_check.setGeometry(QRect(10, 90, 181, 23))
        self.pm_soft_upgrade_check = QCheckBox(self.groupBox_7)
        self.pm_soft_upgrade_check.setObjectName(u"pm_soft_upgrade_check")
        self.pm_soft_upgrade_check.setGeometry(QRect(210, 180, 151, 23))
        self.pm_soft_day_check = QCheckBox(self.groupBox_7)
        self.pm_soft_day_check.setObjectName(u"pm_soft_day_check")
        self.pm_soft_day_check.setGeometry(QRect(210, 150, 90, 23))
        self.pm_bcd_upgrade_check = QCheckBox(self.groupBox_7)
        self.pm_bcd_upgrade_check.setObjectName(u"pm_bcd_upgrade_check")
        self.pm_bcd_upgrade_check.setGeometry(QRect(10, 240, 131, 23))
        self.pm_reg_day_check = QCheckBox(self.groupBox_7)
        self.pm_reg_day_check.setObjectName(u"pm_reg_day_check")
        self.pm_reg_day_check.setGeometry(QRect(210, 60, 111, 23))
        self.pm_add_to_dive_button = QPushButton(self.groupBox_7)
        self.pm_add_to_dive_button.setObjectName(u"pm_add_to_dive_button")
        self.pm_add_to_dive_button.setGeometry(QRect(20, 340, 151, 91))

        self.gridLayout_17.addWidget(self.groupBox_7, 2, 0, 1, 2)

        self.label_80 = QLabel(self.page_pm_dive_add)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font4)

        self.gridLayout_17.addWidget(self.label_80, 1, 0, 1, 1)

        self.pm_l_name_search_results_label_2 = QLabel(self.page_pm_dive_add)
        self.pm_l_name_search_results_label_2.setObjectName(u"pm_l_name_search_results_label_2")

        self.gridLayout_17.addWidget(self.pm_l_name_search_results_label_2, 2, 10, 1, 1)

        self.pm_f_name_search_results_label = QLabel(self.page_pm_dive_add)
        self.pm_f_name_search_results_label.setObjectName(u"pm_f_name_search_results_label")

        self.gridLayout_17.addWidget(self.pm_f_name_search_results_label, 2, 8, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_13, 2, 6, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_14, 1, 4, 1, 1)

        self.stackedWidget.addWidget(self.page_pm_dive_add)
        self.page_zen_dive_add = QWidget()
        self.page_zen_dive_add.setObjectName(u"page_zen_dive_add")
        self.gridLayout_18 = QGridLayout(self.page_zen_dive_add)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.z_id_entry = QLineEdit(self.page_zen_dive_add)
        self.z_id_entry.setObjectName(u"z_id_entry")
        sizePolicy5.setHeightForWidth(self.z_id_entry.sizePolicy().hasHeightForWidth())
        self.z_id_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_18.addWidget(self.z_id_entry, 0, 1, 1, 1)

        self.oid_search_label_6 = QLabel(self.page_zen_dive_add)
        self.oid_search_label_6.setObjectName(u"oid_search_label_6")

        self.gridLayout_18.addWidget(self.oid_search_label_6, 1, 6, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_15, 3, 5, 1, 1)

        self.z_search_customer_button = QPushButton(self.page_zen_dive_add)
        self.z_search_customer_button.setObjectName(u"z_search_customer_button")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush54 = QBrush(QColor(210, 210, 210, 128))
        brush54.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush54)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush55 = QBrush(QColor(210, 210, 210, 128))
        brush55.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush55)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush56 = QBrush(QColor(210, 210, 210, 128))
        brush56.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush56)
#endif
        self.z_search_customer_button.setPalette(palette14)

        self.gridLayout_18.addWidget(self.z_search_customer_button, 0, 9, 1, 1)

        self.groupBox_12 = QGroupBox(self.page_zen_dive_add)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.z_smb_check = QCheckBox(self.groupBox_12)
        self.z_smb_check.setObjectName(u"z_smb_check")
        self.z_smb_check.setGeometry(QRect(20, 240, 90, 23))
        self.z_tech_torch_check = QCheckBox(self.groupBox_12)
        self.z_tech_torch_check.setObjectName(u"z_tech_torch_check")
        self.z_tech_torch_check.setGeometry(QRect(20, 180, 90, 23))
        self.z_o2_reg_check = QCheckBox(self.groupBox_12)
        self.z_o2_reg_check.setObjectName(u"z_o2_reg_check")
        self.z_o2_reg_check.setGeometry(QRect(20, 120, 251, 23))
        self.z_back_plate_check = QCheckBox(self.groupBox_12)
        self.z_back_plate_check.setObjectName(u"z_back_plate_check")
        self.z_back_plate_check.setGeometry(QRect(20, 60, 191, 23))
        self.z_reel_check = QCheckBox(self.groupBox_12)
        self.z_reel_check.setObjectName(u"z_reel_check")
        self.z_reel_check.setGeometry(QRect(20, 270, 90, 23))
        self.z_slate_check = QCheckBox(self.groupBox_12)
        self.z_slate_check.setObjectName(u"z_slate_check")
        self.z_slate_check.setGeometry(QRect(20, 300, 111, 23))
        self.z_tech_computer_check = QCheckBox(self.groupBox_12)
        self.z_tech_computer_check.setObjectName(u"z_tech_computer_check")
        self.z_tech_computer_check.setGeometry(QRect(20, 150, 121, 23))
        self.z_tech_reg_check = QCheckBox(self.groupBox_12)
        self.z_tech_reg_check.setObjectName(u"z_tech_reg_check")
        self.z_tech_reg_check.setGeometry(QRect(20, 30, 141, 23))
        self.z_wing_check = QCheckBox(self.groupBox_12)
        self.z_wing_check.setObjectName(u"z_wing_check")
        self.z_wing_check.setGeometry(QRect(20, 90, 151, 23))
        self.z_wreck_reel_check = QCheckBox(self.groupBox_12)
        self.z_wreck_reel_check.setObjectName(u"z_wreck_reel_check")
        self.z_wreck_reel_check.setGeometry(QRect(20, 210, 151, 23))
        self.z_rebreather_check = QCheckBox(self.groupBox_12)
        self.z_rebreather_check.setObjectName(u"z_rebreather_check")
        self.z_rebreather_check.setGeometry(QRect(20, 330, 111, 23))
        self.label_86 = QLabel(self.groupBox_12)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(40, 360, 41, 17))
        self.label_87 = QLabel(self.groupBox_12)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(160, 360, 31, 17))
        self.z_sorb_entry = QLineEdit(self.groupBox_12)
        self.z_sorb_entry.setObjectName(u"z_sorb_entry")
        self.z_sorb_entry.setGeometry(QRect(90, 355, 61, 31))
        self.label_88 = QLabel(self.groupBox_12)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(10, 440, 331, 51))

        self.gridLayout_18.addWidget(self.groupBox_12, 2, 3, 3, 2)

        self.dob_search_label_6 = QLabel(self.page_zen_dive_add)
        self.dob_search_label_6.setObjectName(u"dob_search_label_6")

        self.gridLayout_18.addWidget(self.dob_search_label_6, 1, 9, 1, 1)

        self.z_activity_combo = QComboBox(self.page_zen_dive_add)
        self.z_activity_combo.setObjectName(u"z_activity_combo")
        sizePolicy5.setHeightForWidth(self.z_activity_combo.sizePolicy().hasHeightForWidth())
        self.z_activity_combo.setSizePolicy(sizePolicy5)

        self.gridLayout_18.addWidget(self.z_activity_combo, 1, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_16, 0, 3, 1, 1)

        self.label_84 = QLabel(self.page_zen_dive_add)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font4)

        self.gridLayout_18.addWidget(self.label_84, 0, 0, 1, 1)

        self.f_name_search_label_6 = QLabel(self.page_zen_dive_add)
        self.f_name_search_label_6.setObjectName(u"f_name_search_label_6")

        self.gridLayout_18.addWidget(self.f_name_search_label_6, 1, 7, 1, 1)

        self.l_name_search_label_11 = QLabel(self.page_zen_dive_add)
        self.l_name_search_label_11.setObjectName(u"l_name_search_label_11")
        self.l_name_search_label_11.setFont(font5)

        self.gridLayout_18.addWidget(self.l_name_search_label_11, 0, 6, 1, 1)

        self.z_l_name_search_entry = QLineEdit(self.page_zen_dive_add)
        self.z_l_name_search_entry.setObjectName(u"z_l_name_search_entry")
        sizePolicy5.setHeightForWidth(self.z_l_name_search_entry.sizePolicy().hasHeightForWidth())
        self.z_l_name_search_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_18.addWidget(self.z_l_name_search_entry, 0, 8, 1, 1)

        self.groupBox_11 = QGroupBox(self.page_zen_dive_add)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.z_twin_air_check = QCheckBox(self.groupBox_11)
        self.z_twin_air_check.setObjectName(u"z_twin_air_check")
        self.z_twin_air_check.setGeometry(QRect(10, 300, 111, 23))
        self.z_6l_50_check = QCheckBox(self.groupBox_11)
        self.z_6l_50_check.setObjectName(u"z_6l_50_check")
        self.z_6l_50_check.setGeometry(QRect(10, 180, 90, 23))
        self.z_twin_eanx_check = QCheckBox(self.groupBox_11)
        self.z_twin_eanx_check.setObjectName(u"z_twin_eanx_check")
        self.z_twin_eanx_check.setGeometry(QRect(10, 330, 131, 23))
        self.z_12l_100_check = QCheckBox(self.groupBox_11)
        self.z_12l_100_check.setObjectName(u"z_12l_100_check")
        self.z_12l_100_check.setGeometry(QRect(10, 270, 90, 23))
        self.z_6l_100_check = QCheckBox(self.groupBox_11)
        self.z_6l_100_check.setObjectName(u"z_6l_100_check")
        self.z_6l_100_check.setGeometry(QRect(10, 210, 90, 23))
        self.z_15l_upgrade_check = QCheckBox(self.groupBox_11)
        self.z_15l_upgrade_check.setObjectName(u"z_15l_upgrade_check")
        self.z_15l_upgrade_check.setGeometry(QRect(10, 60, 131, 23))
        self.z_18l_upgrade_check = QCheckBox(self.groupBox_11)
        self.z_18l_upgrade_check.setObjectName(u"z_18l_upgrade_check")
        self.z_18l_upgrade_check.setGeometry(QRect(10, 90, 121, 23))
        self.z_12l_50_check = QCheckBox(self.groupBox_11)
        self.z_12l_50_check.setObjectName(u"z_12l_50_check")
        self.z_12l_50_check.setGeometry(QRect(10, 240, 90, 23))
        self.z_eanx_upgrade_check = QCheckBox(self.groupBox_11)
        self.z_eanx_upgrade_check.setObjectName(u"z_eanx_upgrade_check")
        self.z_eanx_upgrade_check.setGeometry(QRect(10, 30, 121, 23))
        self.z_no_tank_check = QCheckBox(self.groupBox_11)
        self.z_no_tank_check.setObjectName(u"z_no_tank_check")
        self.z_no_tank_check.setGeometry(QRect(10, 360, 131, 23))
        self.z_3l_100_check = QCheckBox(self.groupBox_11)
        self.z_3l_100_check.setObjectName(u"z_3l_100_check")
        self.z_3l_100_check.setGeometry(QRect(10, 150, 121, 23))
        self.z_3l_air_check = QCheckBox(self.groupBox_11)
        self.z_3l_air_check.setObjectName(u"z_3l_air_check")
        self.z_3l_air_check.setGeometry(QRect(10, 120, 121, 23))

        self.gridLayout_18.addWidget(self.groupBox_11, 2, 2, 3, 1)

        self.l_name_search_label_12 = QLabel(self.page_zen_dive_add)
        self.l_name_search_label_12.setObjectName(u"l_name_search_label_12")

        self.gridLayout_18.addWidget(self.l_name_search_label_12, 1, 8, 1, 1)

        self.label_85 = QLabel(self.page_zen_dive_add)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font4)

        self.gridLayout_18.addWidget(self.label_85, 1, 0, 1, 1)

        self.groupBox_10 = QGroupBox(self.page_zen_dive_add)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.z_soft_dive_check = QCheckBox(self.groupBox_10)
        self.z_soft_dive_check.setObjectName(u"z_soft_dive_check")
        self.z_soft_dive_check.setGeometry(QRect(210, 120, 101, 23))
        self.z_torch_check = QCheckBox(self.groupBox_10)
        self.z_torch_check.setObjectName(u"z_torch_check")
        self.z_torch_check.setGeometry(QRect(10, 150, 151, 23))
        self.z_full_equip_dive_check = QCheckBox(self.groupBox_10)
        self.z_full_equip_dive_check.setObjectName(u"z_full_equip_dive_check")
        self.z_full_equip_dive_check.setGeometry(QRect(10, 30, 171, 23))
        self.z_reg_dive_check = QCheckBox(self.groupBox_10)
        self.z_reg_dive_check.setObjectName(u"z_reg_dive_check")
        self.z_reg_dive_check.setGeometry(QRect(210, 30, 111, 23))
        self.z_reg_upgrade_check = QCheckBox(self.groupBox_10)
        self.z_reg_upgrade_check.setObjectName(u"z_reg_upgrade_check")
        self.z_reg_upgrade_check.setGeometry(QRect(210, 90, 131, 23))
        self.z_full_equip_day_check = QCheckBox(self.groupBox_10)
        self.z_full_equip_day_check.setObjectName(u"z_full_equip_day_check")
        self.z_full_equip_day_check.setGeometry(QRect(10, 60, 161, 23))
        self.z_computer_check = QCheckBox(self.groupBox_10)
        self.z_computer_check.setObjectName(u"z_computer_check")
        self.z_computer_check.setGeometry(QRect(10, 120, 161, 23))
        self.z_bcd_dive_check = QCheckBox(self.groupBox_10)
        self.z_bcd_dive_check.setObjectName(u"z_bcd_dive_check")
        self.z_bcd_dive_check.setGeometry(QRect(10, 180, 131, 23))
        self.z_bcd_day_check = QCheckBox(self.groupBox_10)
        self.z_bcd_day_check.setObjectName(u"z_bcd_day_check")
        self.z_bcd_day_check.setGeometry(QRect(10, 210, 121, 23))
        self.z_full_equip_upgrade_check = QCheckBox(self.groupBox_10)
        self.z_full_equip_upgrade_check.setObjectName(u"z_full_equip_upgrade_check")
        self.z_full_equip_upgrade_check.setGeometry(QRect(10, 90, 181, 23))
        self.z_soft_upgrade_check = QCheckBox(self.groupBox_10)
        self.z_soft_upgrade_check.setObjectName(u"z_soft_upgrade_check")
        self.z_soft_upgrade_check.setGeometry(QRect(210, 180, 151, 23))
        self.z_soft_day_check = QCheckBox(self.groupBox_10)
        self.z_soft_day_check.setObjectName(u"z_soft_day_check")
        self.z_soft_day_check.setGeometry(QRect(210, 150, 90, 23))
        self.z_bcd_upgrade_check = QCheckBox(self.groupBox_10)
        self.z_bcd_upgrade_check.setObjectName(u"z_bcd_upgrade_check")
        self.z_bcd_upgrade_check.setGeometry(QRect(10, 240, 131, 23))
        self.z_reg_day_check = QCheckBox(self.groupBox_10)
        self.z_reg_day_check.setObjectName(u"z_reg_day_check")
        self.z_reg_day_check.setGeometry(QRect(210, 60, 111, 23))
        self.z_add_to_dive_button = QPushButton(self.groupBox_10)
        self.z_add_to_dive_button.setObjectName(u"z_add_to_dive_button")
        self.z_add_to_dive_button.setGeometry(QRect(20, 340, 151, 91))

        self.gridLayout_18.addWidget(self.groupBox_10, 2, 0, 3, 2)

        self.z_oid_search_results_label = QLabel(self.page_zen_dive_add)
        self.z_oid_search_results_label.setObjectName(u"z_oid_search_results_label")

        self.gridLayout_18.addWidget(self.z_oid_search_results_label, 2, 6, 1, 1)

        self.z_f_name_search_results_label = QLabel(self.page_zen_dive_add)
        self.z_f_name_search_results_label.setObjectName(u"z_f_name_search_results_label")

        self.gridLayout_18.addWidget(self.z_f_name_search_results_label, 2, 7, 1, 1)

        self.z_l_name_search_results_label = QLabel(self.page_zen_dive_add)
        self.z_l_name_search_results_label.setObjectName(u"z_l_name_search_results_label")

        self.gridLayout_18.addWidget(self.z_l_name_search_results_label, 2, 8, 1, 1)

        self.z_l_name_search_results_label_2 = QLabel(self.page_zen_dive_add)
        self.z_l_name_search_results_label_2.setObjectName(u"z_l_name_search_results_label_2")

        self.gridLayout_18.addWidget(self.z_l_name_search_results_label_2, 2, 9, 1, 1)

        self.stackedWidget.addWidget(self.page_zen_dive_add)
        self.page_co_add = QWidget()
        self.page_co_add.setObjectName(u"page_co_add")
        self.gridLayout_19 = QGridLayout(self.page_co_add)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_90 = QLabel(self.page_co_add)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font4)

        self.gridLayout_19.addWidget(self.label_90, 2, 0, 1, 1)

        self.co_l_name_search_results_label_2 = QLabel(self.page_co_add)
        self.co_l_name_search_results_label_2.setObjectName(u"co_l_name_search_results_label_2")

        self.gridLayout_19.addWidget(self.co_l_name_search_results_label_2, 3, 9, 1, 1)

        self.co_l_name_search_entry = QLineEdit(self.page_co_add)
        self.co_l_name_search_entry.setObjectName(u"co_l_name_search_entry")
        sizePolicy5.setHeightForWidth(self.co_l_name_search_entry.sizePolicy().hasHeightForWidth())
        self.co_l_name_search_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_19.addWidget(self.co_l_name_search_entry, 0, 8, 1, 1)

        self.groupBox_14 = QGroupBox(self.page_co_add)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.co_twin_air_check = QCheckBox(self.groupBox_14)
        self.co_twin_air_check.setObjectName(u"co_twin_air_check")
        self.co_twin_air_check.setGeometry(QRect(10, 300, 111, 23))
        self.co_6l_50_check = QCheckBox(self.groupBox_14)
        self.co_6l_50_check.setObjectName(u"co_6l_50_check")
        self.co_6l_50_check.setGeometry(QRect(10, 180, 90, 23))
        self.co_twin_eanx_check = QCheckBox(self.groupBox_14)
        self.co_twin_eanx_check.setObjectName(u"co_twin_eanx_check")
        self.co_twin_eanx_check.setGeometry(QRect(10, 330, 131, 23))
        self.co_12l_100_check = QCheckBox(self.groupBox_14)
        self.co_12l_100_check.setObjectName(u"co_12l_100_check")
        self.co_12l_100_check.setGeometry(QRect(10, 270, 90, 23))
        self.co_6l_100_check = QCheckBox(self.groupBox_14)
        self.co_6l_100_check.setObjectName(u"co_6l_100_check")
        self.co_6l_100_check.setGeometry(QRect(10, 210, 90, 23))
        self.co_15l_upgrade_check = QCheckBox(self.groupBox_14)
        self.co_15l_upgrade_check.setObjectName(u"co_15l_upgrade_check")
        self.co_15l_upgrade_check.setGeometry(QRect(10, 60, 131, 23))
        self.co_18l_upgrade_check = QCheckBox(self.groupBox_14)
        self.co_18l_upgrade_check.setObjectName(u"co_18l_upgrade_check")
        self.co_18l_upgrade_check.setGeometry(QRect(10, 90, 121, 23))
        self.co_12l_50_check = QCheckBox(self.groupBox_14)
        self.co_12l_50_check.setObjectName(u"co_12l_50_check")
        self.co_12l_50_check.setGeometry(QRect(10, 240, 90, 23))
        self.co_eanx_upgrade_check = QCheckBox(self.groupBox_14)
        self.co_eanx_upgrade_check.setObjectName(u"co_eanx_upgrade_check")
        self.co_eanx_upgrade_check.setGeometry(QRect(10, 30, 121, 23))
        self.co_no_tank_check = QCheckBox(self.groupBox_14)
        self.co_no_tank_check.setObjectName(u"co_no_tank_check")
        self.co_no_tank_check.setGeometry(QRect(10, 360, 131, 23))
        self.co_3l_100_check = QCheckBox(self.groupBox_14)
        self.co_3l_100_check.setObjectName(u"co_3l_100_check")
        self.co_3l_100_check.setGeometry(QRect(10, 150, 121, 23))
        self.co_3l_air_check = QCheckBox(self.groupBox_14)
        self.co_3l_air_check.setObjectName(u"co_3l_air_check")
        self.co_3l_air_check.setGeometry(QRect(10, 120, 121, 23))

        self.gridLayout_19.addWidget(self.groupBox_14, 3, 2, 1, 1)

        self.oid_search_label_7 = QLabel(self.page_co_add)
        self.oid_search_label_7.setObjectName(u"oid_search_label_7")

        self.gridLayout_19.addWidget(self.oid_search_label_7, 2, 6, 1, 1)

        self.groupBox_15 = QGroupBox(self.page_co_add)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.co_smb_check = QCheckBox(self.groupBox_15)
        self.co_smb_check.setObjectName(u"co_smb_check")
        self.co_smb_check.setGeometry(QRect(10, 240, 90, 23))
        self.co_tech_torch_check = QCheckBox(self.groupBox_15)
        self.co_tech_torch_check.setObjectName(u"co_tech_torch_check")
        self.co_tech_torch_check.setGeometry(QRect(10, 180, 101, 23))
        self.co_o2_reg_check = QCheckBox(self.groupBox_15)
        self.co_o2_reg_check.setObjectName(u"co_o2_reg_check")
        self.co_o2_reg_check.setGeometry(QRect(10, 120, 251, 23))
        self.co_back_plate_check = QCheckBox(self.groupBox_15)
        self.co_back_plate_check.setObjectName(u"co_back_plate_check")
        self.co_back_plate_check.setGeometry(QRect(10, 60, 191, 23))
        self.co_reel_check = QCheckBox(self.groupBox_15)
        self.co_reel_check.setObjectName(u"co_reel_check")
        self.co_reel_check.setGeometry(QRect(10, 270, 90, 23))
        self.co_slate_check = QCheckBox(self.groupBox_15)
        self.co_slate_check.setObjectName(u"co_slate_check")
        self.co_slate_check.setGeometry(QRect(10, 300, 111, 23))
        self.co_tech_computer_check = QCheckBox(self.groupBox_15)
        self.co_tech_computer_check.setObjectName(u"co_tech_computer_check")
        self.co_tech_computer_check.setGeometry(QRect(10, 150, 121, 23))
        self.co_tech_reg_check = QCheckBox(self.groupBox_15)
        self.co_tech_reg_check.setObjectName(u"co_tech_reg_check")
        self.co_tech_reg_check.setGeometry(QRect(10, 30, 141, 23))
        self.co_wing_check = QCheckBox(self.groupBox_15)
        self.co_wing_check.setObjectName(u"co_wing_check")
        self.co_wing_check.setGeometry(QRect(10, 90, 151, 23))
        self.co_wreck_reel_check = QCheckBox(self.groupBox_15)
        self.co_wreck_reel_check.setObjectName(u"co_wreck_reel_check")
        self.co_wreck_reel_check.setGeometry(QRect(10, 210, 151, 23))
        self.co_rebreather_check = QCheckBox(self.groupBox_15)
        self.co_rebreather_check.setObjectName(u"co_rebreather_check")
        self.co_rebreather_check.setGeometry(QRect(10, 330, 111, 23))
        self.label_91 = QLabel(self.groupBox_15)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(40, 370, 41, 17))
        self.label_92 = QLabel(self.groupBox_15)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(160, 370, 31, 17))
        self.co_sorb_entry = QLineEdit(self.groupBox_15)
        self.co_sorb_entry.setObjectName(u"co_sorb_entry")
        self.co_sorb_entry.setGeometry(QRect(90, 365, 61, 31))
        self.label_93 = QLabel(self.groupBox_15)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(30, 430, 321, 41))

        self.gridLayout_19.addWidget(self.groupBox_15, 3, 3, 1, 2)

        self.l_name_search_label_13 = QLabel(self.page_co_add)
        self.l_name_search_label_13.setObjectName(u"l_name_search_label_13")
        self.l_name_search_label_13.setFont(font5)

        self.gridLayout_19.addWidget(self.l_name_search_label_13, 0, 6, 1, 1)

        self.co_search_customer_button = QPushButton(self.page_co_add)
        self.co_search_customer_button.setObjectName(u"co_search_customer_button")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush57 = QBrush(QColor(210, 210, 210, 128))
        brush57.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush57)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush58 = QBrush(QColor(210, 210, 210, 128))
        brush58.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush58)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush59 = QBrush(QColor(210, 210, 210, 128))
        brush59.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush59)
#endif
        self.co_search_customer_button.setPalette(palette15)

        self.gridLayout_19.addWidget(self.co_search_customer_button, 0, 9, 1, 1)

        self.co_f_name_search_results_label = QLabel(self.page_co_add)
        self.co_f_name_search_results_label.setObjectName(u"co_f_name_search_results_label")

        self.gridLayout_19.addWidget(self.co_f_name_search_results_label, 3, 7, 1, 1)

        self.co_l_name_search_results_label = QLabel(self.page_co_add)
        self.co_l_name_search_results_label.setObjectName(u"co_l_name_search_results_label")

        self.gridLayout_19.addWidget(self.co_l_name_search_results_label, 3, 8, 1, 1)

        self.groupBox_13 = QGroupBox(self.page_co_add)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.co_soft_dive_check = QCheckBox(self.groupBox_13)
        self.co_soft_dive_check.setObjectName(u"co_soft_dive_check")
        self.co_soft_dive_check.setGeometry(QRect(210, 120, 101, 23))
        self.co_torch_check = QCheckBox(self.groupBox_13)
        self.co_torch_check.setObjectName(u"co_torch_check")
        self.co_torch_check.setGeometry(QRect(10, 150, 151, 23))
        self.co_full_equip_dive_check = QCheckBox(self.groupBox_13)
        self.co_full_equip_dive_check.setObjectName(u"co_full_equip_dive_check")
        self.co_full_equip_dive_check.setGeometry(QRect(10, 30, 171, 23))
        self.co_reg_dive_check = QCheckBox(self.groupBox_13)
        self.co_reg_dive_check.setObjectName(u"co_reg_dive_check")
        self.co_reg_dive_check.setGeometry(QRect(210, 30, 111, 23))
        self.co_reg_upgrade_check = QCheckBox(self.groupBox_13)
        self.co_reg_upgrade_check.setObjectName(u"co_reg_upgrade_check")
        self.co_reg_upgrade_check.setGeometry(QRect(210, 90, 131, 23))
        self.co_full_equip_day_check = QCheckBox(self.groupBox_13)
        self.co_full_equip_day_check.setObjectName(u"co_full_equip_day_check")
        self.co_full_equip_day_check.setGeometry(QRect(10, 60, 161, 23))
        self.co_computer_check = QCheckBox(self.groupBox_13)
        self.co_computer_check.setObjectName(u"co_computer_check")
        self.co_computer_check.setGeometry(QRect(10, 120, 161, 23))
        self.co_bcd_dive_check = QCheckBox(self.groupBox_13)
        self.co_bcd_dive_check.setObjectName(u"co_bcd_dive_check")
        self.co_bcd_dive_check.setGeometry(QRect(10, 180, 131, 23))
        self.co_bcd_day_check = QCheckBox(self.groupBox_13)
        self.co_bcd_day_check.setObjectName(u"co_bcd_day_check")
        self.co_bcd_day_check.setGeometry(QRect(10, 210, 121, 23))
        self.co_full_equip_upgrade_check = QCheckBox(self.groupBox_13)
        self.co_full_equip_upgrade_check.setObjectName(u"co_full_equip_upgrade_check")
        self.co_full_equip_upgrade_check.setGeometry(QRect(10, 90, 181, 23))
        self.co_soft_upgrade_check = QCheckBox(self.groupBox_13)
        self.co_soft_upgrade_check.setObjectName(u"co_soft_upgrade_check")
        self.co_soft_upgrade_check.setGeometry(QRect(210, 180, 151, 23))
        self.co_soft_day_check = QCheckBox(self.groupBox_13)
        self.co_soft_day_check.setObjectName(u"co_soft_day_check")
        self.co_soft_day_check.setGeometry(QRect(210, 150, 90, 23))
        self.co_bcd_upgrade_check = QCheckBox(self.groupBox_13)
        self.co_bcd_upgrade_check.setObjectName(u"co_bcd_upgrade_check")
        self.co_bcd_upgrade_check.setGeometry(QRect(10, 240, 131, 23))
        self.co_reg_day_check = QCheckBox(self.groupBox_13)
        self.co_reg_day_check.setObjectName(u"co_reg_day_check")
        self.co_reg_day_check.setGeometry(QRect(210, 60, 111, 23))
        self.co_add_to_dive_button = QPushButton(self.groupBox_13)
        self.co_add_to_dive_button.setObjectName(u"co_add_to_dive_button")
        self.co_add_to_dive_button.setGeometry(QRect(10, 330, 151, 91))

        self.gridLayout_19.addWidget(self.groupBox_13, 3, 0, 1, 2)

        self.label_89 = QLabel(self.page_co_add)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font4)

        self.gridLayout_19.addWidget(self.label_89, 0, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_17, 0, 4, 1, 1)

        self.dob_search_label_7 = QLabel(self.page_co_add)
        self.dob_search_label_7.setObjectName(u"dob_search_label_7")

        self.gridLayout_19.addWidget(self.dob_search_label_7, 2, 9, 1, 1)

        self.l_name_search_label_14 = QLabel(self.page_co_add)
        self.l_name_search_label_14.setObjectName(u"l_name_search_label_14")

        self.gridLayout_19.addWidget(self.l_name_search_label_14, 2, 8, 1, 1)

        self.co_oid_search_results_label = QLabel(self.page_co_add)
        self.co_oid_search_results_label.setObjectName(u"co_oid_search_results_label")

        self.gridLayout_19.addWidget(self.co_oid_search_results_label, 3, 6, 1, 1)

        self.co_activity_combo = QComboBox(self.page_co_add)
        self.co_activity_combo.setObjectName(u"co_activity_combo")
        sizePolicy5.setHeightForWidth(self.co_activity_combo.sizePolicy().hasHeightForWidth())
        self.co_activity_combo.setSizePolicy(sizePolicy5)

        self.gridLayout_19.addWidget(self.co_activity_combo, 2, 1, 1, 1)

        self.f_name_search_label_7 = QLabel(self.page_co_add)
        self.f_name_search_label_7.setObjectName(u"f_name_search_label_7")

        self.gridLayout_19.addWidget(self.f_name_search_label_7, 2, 7, 1, 1)

        self.co_id_entry = QLineEdit(self.page_co_add)
        self.co_id_entry.setObjectName(u"co_id_entry")
        sizePolicy5.setHeightForWidth(self.co_id_entry.sizePolicy().hasHeightForWidth())
        self.co_id_entry.setSizePolicy(sizePolicy5)

        self.gridLayout_19.addWidget(self.co_id_entry, 0, 1, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_18, 3, 5, 1, 1)

        self.stackedWidget.addWidget(self.page_co_add)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        self.label_credits.setFont(font9)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font9)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"WM", None))
        self.update_courses_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.z_remove_diver_button.setText(QCoreApplication.translate("MainWindow", u"remove diver", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DAS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Dive Site", None))
        ___qtablewidgetitem = self.zenobia_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.zenobia_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Activity", None));
        ___qtablewidgetitem2 = self.zenobia_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"guide", None));
        ___qtablewidgetitem3 = self.zenobia_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Card", None));
        ___qtablewidgetitem4 = self.zenobia_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Paperwork", None));
        ___qtablewidgetitem5 = self.zenobia_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Balance", None));
        ___qtablewidgetitem6 = self.zenobia_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.z_print_button.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.todays_dive_button.setText(QCoreApplication.translate("MainWindow", u"Todays dive", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dive Site", None))
        self.add_new_course_button.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.update_zenobia_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"DAS", None))
        self.am_remove_diver_button.setText(QCoreApplication.translate("MainWindow", u"remove diver", None))
        self.mam_print_button.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Dive Site", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.am_print_button.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.add_new_pm_dive_button.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.update_am_dive_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DAS", None))
        self.update_mid_am_dive_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        ___qtablewidgetitem7 = self.courses_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem8 = self.courses_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Activity", None));
        ___qtablewidgetitem9 = self.courses_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"guide", None));
        ___qtablewidgetitem10 = self.courses_table.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Card", None));
        ___qtablewidgetitem11 = self.courses_table.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Paperwork", None));
        ___qtablewidgetitem12 = self.courses_table.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Balance", None));
        ___qtablewidgetitem13 = self.courses_table.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        self.pm_remove_diver_button.setText(QCoreApplication.translate("MainWindow", u"remove diver", None))
        self.update_pm_dive_button.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"DAS", None))
        self.pm_print_button.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u" ID", None))
        self.ci_remove_diver_button.setText(QCoreApplication.translate("MainWindow", u"remove diver", None))
        ___qtablewidgetitem14 = self.pm_dive_table.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem15 = self.pm_dive_table.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Activity", None));
        ___qtablewidgetitem16 = self.pm_dive_table.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"guide", None));
        ___qtablewidgetitem17 = self.pm_dive_table.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Card", None));
        ___qtablewidgetitem18 = self.pm_dive_table.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Paperwork", None));
        ___qtablewidgetitem19 = self.pm_dive_table.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Balance", None));
        ___qtablewidgetitem20 = self.pm_dive_table.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Dive Site", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"DAS", None))
        self.add_new_am_dive_button.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.co_print_button.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u" ID", None))
        self.mam_remove_diver_button.setText(QCoreApplication.translate("MainWindow", u"remove diver", None))
        self.add_new_zenobia_button.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        self.add_new_mid_dive_button.setText(QCoreApplication.translate("MainWindow", u"Add New", None))
        ___qtablewidgetitem21 = self.mid_am_dive_table.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem22 = self.mid_am_dive_table.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Activity", None));
        ___qtablewidgetitem23 = self.mid_am_dive_table.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"guide", None));
        ___qtablewidgetitem24 = self.mid_am_dive_table.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Card", None));
        ___qtablewidgetitem25 = self.mid_am_dive_table.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Paperwork", None));
        ___qtablewidgetitem26 = self.mid_am_dive_table.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Balance", None));
        ___qtablewidgetitem27 = self.mid_am_dive_table.horizontalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem28 = self.am_dive_table.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem29 = self.am_dive_table.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Activity", None));
        ___qtablewidgetitem30 = self.am_dive_table.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"guide", None));
        ___qtablewidgetitem31 = self.am_dive_table.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Card", None));
        ___qtablewidgetitem32 = self.am_dive_table.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Paperwork", None));
        ___qtablewidgetitem33 = self.am_dive_table.horizontalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Balance", None));
        ___qtablewidgetitem34 = self.am_dive_table.horizontalHeaderItem(6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Dive Site", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Am Dive", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Mid Am", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"PM Dive", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Zenobia", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Courses", None))
        self.cert_seen_label.setText(QCoreApplication.translate("MainWindow", u"Certification seen?", None))
        self.liab_check.setText("")
        self.no_dives__label.setText(QCoreApplication.translate("MainWindow", u"Number of dives:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create new customer", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"in months", None))
        self.cert_check.setText("")
        self.dob_label.setText(QCoreApplication.translate("MainWindow", u"Date of birth:", None))
        self.l_name_label.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"dd/mm/yyyy", None))
        self.last_dive__label.setText(QCoreApplication.translate("MainWindow", u"Last Dive:", None))
        self.f_name_label.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.liab__label.setText(QCoreApplication.translate("MainWindow", u"Liability form complete?", None))
        self.cert_label.setText(QCoreApplication.translate("MainWindow", u"Certification:", None))
        self.new_customer_added_label.setText("")
        self.cert_check_2.setText("")
        self.liab_check_2.setText("")
        self.no_dives__label_2.setText(QCoreApplication.translate("MainWindow", u"Number of dives:", None))
        self.cert_seen_label_2.setText(QCoreApplication.translate("MainWindow", u"Certification seen?", None))
        self.l_name_search_label_2.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"in months", None))
        self.oid_search_label.setText(QCoreApplication.translate("MainWindow", u"ID number", None))
        self.l_name_label_4.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.oid_search_results_label.setText("")
        self.dob_search_label.setText(QCoreApplication.translate("MainWindow", u"DoB", None))
        self.update_customer_button.setText(QCoreApplication.translate("MainWindow", u"Update customer", None))
        self.list_all_button.setText(QCoreApplication.translate("MainWindow", u"List all", None))
        self.l_name_search_label.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"dd/mm/yyyy", None))
        self.f_name_search_label.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.delete_customer_button.setText(QCoreApplication.translate("MainWindow", u"Delete customer", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"ID Number:", None))
        self.f_name_label_4.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.last_dive__label_2.setText(QCoreApplication.translate("MainWindow", u"Last Dive:", None))
        self.cert_label_2.setText(QCoreApplication.translate("MainWindow", u"Certification:", None))
        self.f_name_search_results_label.setText("")
        self.dob_label_2.setText(QCoreApplication.translate("MainWindow", u"Date of birth:", None))
        self.liab__label_2.setText(QCoreApplication.translate("MainWindow", u"Liability form complete?", None))
        self.l_name_search_results_label.setText("")
        self.l_name_search_results_label_2.setText("")
        self.search_customer_button.setText(QCoreApplication.translate("MainWindow", u" Search for customer", None))
        self.search_customer_id_button_.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.record_updated_label.setText("")
        self.pb_check.setText(QCoreApplication.translate("MainWindow", u"PB", None))
        self.insurance_no_label.setText(QCoreApplication.translate("MainWindow", u"Insurance No", None))
        self.xr_check.setText(QCoreApplication.translate("MainWindow", u"XR", None))
        self.l_name_label_3.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.delete_staff_button.setText(QCoreApplication.translate("MainWindow", u"Delete Staff", None))
        self.pro_no_label_2.setText(QCoreApplication.translate("MainWindow", u"Pro Number", None))
        self.highest_label.setText(QCoreApplication.translate("MainWindow", u"Highest cert level", None))
        self.f_name_results_label.setText("")
        self.pro_no_label.setText(QCoreApplication.translate("MainWindow", u"Pro Number", None))
        self.l_name_results_label.setText("")
        self.eanx_check.setText(QCoreApplication.translate("MainWindow", u"EANX", None))
        self.insurance_exp_results_label.setText("")
        self.id_label_2.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.sod_check.setText(QCoreApplication.translate("MainWindow", u"SOD", None))
        self.insurance_no_results_label.setText("")
        self.highest_label_2.setText(QCoreApplication.translate("MainWindow", u"Highest cert level", None))
        self.add_search_staff_button.setText(QCoreApplication.translate("MainWindow", u"Search staff", None))
        self.f_name_label_2.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.insurance_exp_label.setText(QCoreApplication.translate("MainWindow", u"Insurance Exp", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"update Staff", None))
        self.insurance_no_label_2.setText(QCoreApplication.translate("MainWindow", u"Insurance No", None))
        self.id_results_label.setText("")
        self.nav_check.setText(QCoreApplication.translate("MainWindow", u"NAV", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add Staff", None))
        self.wreck_check.setText(QCoreApplication.translate("MainWindow", u"WRECK", None))
        self.pro_number_results_label.setText("")
        self.adv_wreck_check.setText(QCoreApplication.translate("MainWindow", u"ADV WRECK", None))
        self.boat_check.setText(QCoreApplication.translate("MainWindow", u"BOAT", None))
        self.clear_staff_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.highest_results_label.setText("")
        self.deep_check.setText(QCoreApplication.translate("MainWindow", u"DEEP", None))
        self.night_check.setText(QCoreApplication.translate("MainWindow", u"NIGHT", None))
        self.sidemount_check.setText(QCoreApplication.translate("MainWindow", u"SIDEMOUNT", None))
        self.l_name_label_2.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.insurance_exp_label_2.setText(QCoreApplication.translate("MainWindow", u"Insurance Exp\u02d8 ", None))
        self.owi_check.setText(QCoreApplication.translate("MainWindow", u"OWI", None))
        self.dm_check.setText(QCoreApplication.translate("MainWindow", u"DM", None))
        self.f_name_label_3.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Staff ID", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.total_mount_results.setText(QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.amount_paid_label.setText(QCoreApplication.translate("MainWindow", u"Amount paid to date:", None))
        self.dob_search_label_2.setText(QCoreApplication.translate("MainWindow", u"DoB", None))
        self.l_name_search_results_label_4.setText("")
        self.oid_search_label_2.setText(QCoreApplication.translate("MainWindow", u"ID number", None))
        self.total_amount_owed_label.setText(QCoreApplication.translate("MainWindow", u"Total amount owed:", None))
        self.balance_label.setText(QCoreApplication.translate("MainWindow", u"Balance:", None))
        self.f_l_name_label.setText("")
        self.search_customer_button_2.setText(QCoreApplication.translate("MainWindow", u" Search for customer", None))
        self.make_payment_button.setText(QCoreApplication.translate("MainWindow", u"Make payment", None))
        self.amount_paid_results.setText(QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.f_name_search_results_label_2.setText("")
        self.l_name_search_results_label_3.setText("")
        self.l_name_search_label_4.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.f_name_search_label_2.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.balance_results.setText(QCoreApplication.translate("MainWindow", u"\u20ac", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Enter amount in Euros:", None))
        ___qtablewidgetitem35 = self.tab_table.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem36 = self.tab_table.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Activity", None));
        ___qtablewidgetitem37 = self.tab_table.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Dive Site", None));
        ___qtablewidgetitem38 = self.tab_table.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Guide", None));
        ___qtablewidgetitem39 = self.tab_table.horizontalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem40 = self.tab_table.horizontalHeaderItem(5)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"full equipment/dive", None));
        ___qtablewidgetitem41 = self.tab_table.horizontalHeaderItem(6)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"full equipment/day", None));
        ___qtablewidgetitem42 = self.tab_table.horizontalHeaderItem(7)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"full equipment upgrde", None));
        ___qtablewidgetitem43 = self.tab_table.horizontalHeaderItem(8)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"computer/day", None));
        ___qtablewidgetitem44 = self.tab_table.horizontalHeaderItem(9)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Torch/day", None));
        ___qtablewidgetitem45 = self.tab_table.horizontalHeaderItem(10)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"BCD/dive", None));
        ___qtablewidgetitem46 = self.tab_table.horizontalHeaderItem(11)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"BCD/day", None));
        ___qtablewidgetitem47 = self.tab_table.horizontalHeaderItem(12)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"BCD upgrade", None));
        ___qtablewidgetitem48 = self.tab_table.horizontalHeaderItem(13)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"REG/dive", None));
        ___qtablewidgetitem49 = self.tab_table.horizontalHeaderItem(14)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"REG/day", None));
        ___qtablewidgetitem50 = self.tab_table.horizontalHeaderItem(15)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"REG upgrade", None));
        ___qtablewidgetitem51 = self.tab_table.horizontalHeaderItem(16)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"soft/dive", None));
        ___qtablewidgetitem52 = self.tab_table.horizontalHeaderItem(17)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"soft/day", None));
        ___qtablewidgetitem53 = self.tab_table.horizontalHeaderItem(18)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"soft upgrade", None));
        ___qtablewidgetitem54 = self.tab_table.horizontalHeaderItem(19)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"EANx upgrade", None));
        ___qtablewidgetitem55 = self.tab_table.horizontalHeaderItem(20)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"15L upgrade", None));
        ___qtablewidgetitem56 = self.tab_table.horizontalHeaderItem(21)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"18L upgrade", None));
        ___qtablewidgetitem57 = self.tab_table.horizontalHeaderItem(22)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"3L air", None));
        ___qtablewidgetitem58 = self.tab_table.horizontalHeaderItem(23)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"3L 100%", None));
        ___qtablewidgetitem59 = self.tab_table.horizontalHeaderItem(24)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"6L 50%", None));
        ___qtablewidgetitem60 = self.tab_table.horizontalHeaderItem(25)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"6L 100%", None));
        ___qtablewidgetitem61 = self.tab_table.horizontalHeaderItem(26)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"12L 50%", None));
        ___qtablewidgetitem62 = self.tab_table.horizontalHeaderItem(27)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"12L 100%", None));
        ___qtablewidgetitem63 = self.tab_table.horizontalHeaderItem(28)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"twin set air", None));
        ___qtablewidgetitem64 = self.tab_table.horizontalHeaderItem(29)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Twin set EANx", None));
        ___qtablewidgetitem65 = self.tab_table.horizontalHeaderItem(30)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"tech REG", None));
        ___qtablewidgetitem66 = self.tab_table.horizontalHeaderItem(31)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Back plate", None));
        ___qtablewidgetitem67 = self.tab_table.horizontalHeaderItem(32)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Wing", None));
        ___qtablewidgetitem68 = self.tab_table.horizontalHeaderItem(33)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"O2 reg", None));
        ___qtablewidgetitem69 = self.tab_table.horizontalHeaderItem(34)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Tech Computer", None));
        ___qtablewidgetitem70 = self.tab_table.horizontalHeaderItem(35)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Tech Torch", None));
        ___qtablewidgetitem71 = self.tab_table.horizontalHeaderItem(36)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Wreck reel", None));
        ___qtablewidgetitem72 = self.tab_table.horizontalHeaderItem(37)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"SMB", None));
        ___qtablewidgetitem73 = self.tab_table.horizontalHeaderItem(38)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"reel", None));
        ___qtablewidgetitem74 = self.tab_table.horizontalHeaderItem(39)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Slate", None));
        ___qtablewidgetitem75 = self.tab_table.horizontalHeaderItem(40)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Rebreather", None));
        ___qtablewidgetitem76 = self.tab_table.horizontalHeaderItem(41)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Sorb", None));
        self.id_number_label.setText("")
        self.oid_search_results_label_2.setText("")
        self.l_name_search_label_3.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.list_all_button_2.setText(QCoreApplication.translate("MainWindow", u"List all", None))
        ___qtablewidgetitem77 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem78 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Amount paid", None));
        self.id_search_label.setText(QCoreApplication.translate("MainWindow", u"Search by ID", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Payments made", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"REG / dive", None))
        self.list_activities_button.setText(QCoreApplication.translate("MainWindow", u"List Activities", None))
        self.activity_name_label.setText(QCoreApplication.translate("MainWindow", u"Activity name", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"EANx upgrade", None))
        self.is_course_check.setText(QCoreApplication.translate("MainWindow", u"Is this a course?", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Set extras", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"*** upgrades price is (day price - dive price)", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Soft upgrade", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"O2 clean REG with stage rigging", None))
        self.activity_name_label_2.setText(QCoreApplication.translate("MainWindow", u"Activity name", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"3L 100%", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Computer / day", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Tech Wing", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"SMB", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"/Kg", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"6L 50%", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"BCD / day", None))
        self.add_activity_button.setText(QCoreApplication.translate("MainWindow", u"Add Activity", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Back plate with harness", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"REG / day", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"6L 100%", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Tech torch", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"18L upgrade", None))
        self.price_label.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"12L 100%", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Soft / day", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Tech Computer", None))
        self.id_label_3.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"12L 50%", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Twin set EANx", None))
        self.inst_cert_label_2.setText(QCoreApplication.translate("MainWindow", u"Instructor cert required", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Reel", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Full Equipment upgrade", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Sorb", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Tech/Wreck reel", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"REG upgrade", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Full Equpiment / dive", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Wrist slate", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"3L Air", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Full Equipment / day", None))
        self.price_label_2.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"BCD upgrade", None))
        self.delete_record_button.setText(QCoreApplication.translate("MainWindow", u"Delete activity", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Twin set air", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"BCD / dive", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Rebreather", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"15L upgrade", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Torch / day", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Soft / dive", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Tech REG", None))
        self.inst_cert_label.setText(QCoreApplication.translate("MainWindow", u"Instructor cert required", None))
        self.inst_cert_list_results.setText("")
        self.activity_list_results.setText("")
        self.id_list_results_.setText("")
        self.price_list_results.setText("")
        self.dob_search_label_3.setText(QCoreApplication.translate("MainWindow", u"DoB", None))
        self.l_name_search_label_5.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.l_name_search_label_6.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.f_name_search_label_3.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Recreational Equipment", None))
        self.am_soft_dive_check_2.setText(QCoreApplication.translate("MainWindow", u"Soft / dive", None))
        self.am_torch_check_2.setText(QCoreApplication.translate("MainWindow", u"torch / day", None))
        self.am_full_equip_dive_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment / dive", None))
        self.am_reg_dive_check_2.setText(QCoreApplication.translate("MainWindow", u"REG / dive", None))
        self.am_reg_upgrade_check_2.setText(QCoreApplication.translate("MainWindow", u"REG upgrade", None))
        self.am_full_equip_day_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment / day", None))
        self.am_computer_check.setText(QCoreApplication.translate("MainWindow", u"computer / day", None))
        self.am_bcd_dive_check_2.setText(QCoreApplication.translate("MainWindow", u"BCD / dive", None))
        self.am_bcd_day_check_2.setText(QCoreApplication.translate("MainWindow", u"BCD / day", None))
        self.am_full_equip_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment upgrade", None))
        self.am_soft_upgrade_check_2.setText(QCoreApplication.translate("MainWindow", u"Soft upgrade", None))
        self.am_soft_day_check_2.setText(QCoreApplication.translate("MainWindow", u"Soft / day", None))
        self.am_bcd_upgrade_check_2.setText(QCoreApplication.translate("MainWindow", u"BCD upgrade", None))
        self.am_reg_day_check_2.setText(QCoreApplication.translate("MainWindow", u"REG / day", None))
        self.am_add_to_dive_button.setText(QCoreApplication.translate("MainWindow", u"Add to AM dive", None))
        self.am_oid_search_results_label.setText("")
        self.am_l_name_search_results_label_2.setText("")
        self.am_search_customer_button.setText(QCoreApplication.translate("MainWindow", u" Search for customer", None))
        self.oid_search_label_3.setText(QCoreApplication.translate("MainWindow", u"ID number", None))
        self.am_l_name_search_results_label.setText("")
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.am_f_name_search_results_label.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Customer ID number", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Tanks and gasses", None))
        self.am_twin_air_check.setText(QCoreApplication.translate("MainWindow", u"Twin set air", None))
        self.am_6l_50_check.setText(QCoreApplication.translate("MainWindow", u"6L 50%", None))
        self.am_twin_eanx_check.setText(QCoreApplication.translate("MainWindow", u"Twin set EANx", None))
        self.am_12l_100_check.setText(QCoreApplication.translate("MainWindow", u"12L 100%", None))
        self.am_6l_100_check.setText(QCoreApplication.translate("MainWindow", u"6L 100%", None))
        self.am_15l_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"15L upgrade", None))
        self.am_18l_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"18L upgrade", None))
        self.am_12l_50_check.setText(QCoreApplication.translate("MainWindow", u"12L 50%", None))
        self.am_eanx_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"EANx upgrade", None))
        self.am_no_tank_check.setText(QCoreApplication.translate("MainWindow", u"NO TANK", None))
        self.am_3l_100_check.setText(QCoreApplication.translate("MainWindow", u"3L 100%", None))
        self.am_3l_air_check.setText(QCoreApplication.translate("MainWindow", u"3L Air", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Tech equipment", None))
        self.am_smb_check.setText(QCoreApplication.translate("MainWindow", u"SMB", None))
        self.am_tech_torch_check.setText(QCoreApplication.translate("MainWindow", u"Tech torch", None))
        self.am_o2_reg_check.setText(QCoreApplication.translate("MainWindow", u"O2 clean REG with stage rigging", None))
        self.am_back_plate_check.setText(QCoreApplication.translate("MainWindow", u"Back plate with harness", None))
        self.am_reel_check.setText(QCoreApplication.translate("MainWindow", u"Reel", None))
        self.am_slate_check.setText(QCoreApplication.translate("MainWindow", u"Wrist slate", None))
        self.am_tech_computer_check.setText(QCoreApplication.translate("MainWindow", u"Tech computer", None))
        self.am_tech_reg_check.setText(QCoreApplication.translate("MainWindow", u"Primary REG", None))
        self.am_wing_check.setText(QCoreApplication.translate("MainWindow", u"Tech Wing", None))
        self.am_wreck_reel_check.setText(QCoreApplication.translate("MainWindow", u"Tech/Wreck reel", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Sorb:", None))
        self.am_rebreather_check.setText(QCoreApplication.translate("MainWindow", u"Rebreather", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"*** equipment upgrade price is upgrading from single dive \n"
" rental to full day", None))
        self.dob_search_label_4.setText(QCoreApplication.translate("MainWindow", u"DoB", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Recreational Equipment", None))
        self.mam_soft_dive_check.setText(QCoreApplication.translate("MainWindow", u"Soft / dive", None))
        self.mam_torch_check.setText(QCoreApplication.translate("MainWindow", u"torch / day", None))
        self.mam_full_equip_dive_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment / dive", None))
        self.mam_reg_dive_check.setText(QCoreApplication.translate("MainWindow", u"REG / dive", None))
        self.mam_reg_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"REG upgrade", None))
        self.mam_full_equip_day_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment / day", None))
        self.mam_computer_check.setText(QCoreApplication.translate("MainWindow", u"computer / day", None))
        self.mam_bcd_dive_check.setText(QCoreApplication.translate("MainWindow", u"BCD / dive", None))
        self.mam_bcd_day_check.setText(QCoreApplication.translate("MainWindow", u"BCD / day", None))
        self.mam_full_equip_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment upgrade", None))
        self.mam_soft_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"Soft upgrade", None))
        self.mam_soft_day_check.setText(QCoreApplication.translate("MainWindow", u"Soft / day", None))
        self.mam_bcd_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"BCD upgrade", None))
        self.mam_reg_day_check.setText(QCoreApplication.translate("MainWindow", u"REG / day", None))
        self.mam_add_to_dive_button.setText(QCoreApplication.translate("MainWindow", u"Add to MID -AM dive", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Customer ID number", None))
        self.l_name_search_label_8.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.l_name_search_label_7.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Tanks and gasses", None))
        self.mam_twin_air_check.setText(QCoreApplication.translate("MainWindow", u"Twin set air", None))
        self.mam_6l_50_check.setText(QCoreApplication.translate("MainWindow", u"6L 50%", None))
        self.mam_twin_eanx_check.setText(QCoreApplication.translate("MainWindow", u"Twin set EANx", None))
        self.mam_12l_100_check.setText(QCoreApplication.translate("MainWindow", u"12L 100%", None))
        self.mam_6l_100_check.setText(QCoreApplication.translate("MainWindow", u"6L 100%", None))
        self.mam_15l_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"15L upgrade", None))
        self.mam_18l_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"18L upgrade", None))
        self.mam_12l_50_check.setText(QCoreApplication.translate("MainWindow", u"12L 50%", None))
        self.mam_eanx_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"EANx upgrade", None))
        self.mam_no_tank_check.setText(QCoreApplication.translate("MainWindow", u"NO TANK", None))
        self.mam_3l_100_check.setText(QCoreApplication.translate("MainWindow", u"3L 100%", None))
        self.mam_3l_air_check.setText(QCoreApplication.translate("MainWindow", u"3L Air", None))
        self.f_name_search_label_4.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Tech equipment", None))
        self.mam_smb_check_2.setText(QCoreApplication.translate("MainWindow", u"SMB", None))
        self.mam_tech_torch_check_2.setText(QCoreApplication.translate("MainWindow", u"Tech torch", None))
        self.mam_o2_reg_check_2.setText(QCoreApplication.translate("MainWindow", u"O2 clean REG with stage rigging", None))
        self.mam_back_plate_check_2.setText(QCoreApplication.translate("MainWindow", u"Back plate with harness", None))
        self.mam_reel_check_2.setText(QCoreApplication.translate("MainWindow", u"Reel", None))
        self.mam_slate_check_2.setText(QCoreApplication.translate("MainWindow", u"Wrist slate", None))
        self.mam_tech_computer_check_2.setText(QCoreApplication.translate("MainWindow", u"Tech computer", None))
        self.mam_tech_reg_check_2.setText(QCoreApplication.translate("MainWindow", u"Primary REG", None))
        self.mam_wing_check_2.setText(QCoreApplication.translate("MainWindow", u"Tech Wing", None))
        self.mam_wreck_reel_check_2.setText(QCoreApplication.translate("MainWindow", u"Tech/Wreck reel", None))
        self.mam_rebreather_check_2.setText(QCoreApplication.translate("MainWindow", u"Rebreather", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Sorb:", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"*** equipment upgrade price is upgrading from \n"
" single dive rental to full day", None))
        self.oid_search_label_4.setText(QCoreApplication.translate("MainWindow", u"ID number", None))
        self.mam_search_customer_button.setText(QCoreApplication.translate("MainWindow", u" Search for customer", None))
        self.mam_oid_search_results_label.setText("")
        self.mam_l_name_search_results_label.setText("")
        self.mam_f_name_search_results_label.setText("")
        self.mam_l_name_search_results_label_2.setText("")
        self.dob_search_label_5.setText(QCoreApplication.translate("MainWindow", u"DoB", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Tanks and gasses", None))
        self.pm_twin_air_check.setText(QCoreApplication.translate("MainWindow", u"Twin set air", None))
        self.pm_6l_50_check.setText(QCoreApplication.translate("MainWindow", u"6L 50%", None))
        self.pm_twin_eanx_check.setText(QCoreApplication.translate("MainWindow", u"Twin set EANx", None))
        self.pm_12l_100_check.setText(QCoreApplication.translate("MainWindow", u"12L 100%", None))
        self.pm_6l_100_check.setText(QCoreApplication.translate("MainWindow", u"6L 100%", None))
        self.pm_15l_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"15L upgrade", None))
        self.pm_18l_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"18L upgrade", None))
        self.pm_12l_50_check.setText(QCoreApplication.translate("MainWindow", u"12L 50%", None))
        self.pm_eanx_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"EANx upgrade", None))
        self.pm_no_tank_check.setText(QCoreApplication.translate("MainWindow", u"NO TANK", None))
        self.pm_3l_air_check.setText(QCoreApplication.translate("MainWindow", u"3L Air", None))
        self.pm_3l_100_check.setText(QCoreApplication.translate("MainWindow", u"3L 100%", None))
        self.pm_oid_search_results_label.setText("")
        self.f_name_search_label_5.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.pm_search_customer_button.setText(QCoreApplication.translate("MainWindow", u" Search for customer", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Tech equipment", None))
        self.pm_smb_check.setText(QCoreApplication.translate("MainWindow", u"SMB", None))
        self.pm_tech_torch_check.setText(QCoreApplication.translate("MainWindow", u"Tech torch", None))
        self.pm_o2_reg_check.setText(QCoreApplication.translate("MainWindow", u"O2 clean REG with stage rigging", None))
        self.pm_back_plate_check.setText(QCoreApplication.translate("MainWindow", u"Back plate with harness", None))
        self.pm_reel_check.setText(QCoreApplication.translate("MainWindow", u"Reel", None))
        self.pm_slate_check.setText(QCoreApplication.translate("MainWindow", u"Wrist slate", None))
        self.pm_tech_computer_check.setText(QCoreApplication.translate("MainWindow", u"Tech computer", None))
        self.pm_tech_reg_check.setText(QCoreApplication.translate("MainWindow", u"Primary REG", None))
        self.pm_wing_check.setText(QCoreApplication.translate("MainWindow", u"Tech Wing", None))
        self.pm_wreck_reel_check.setText(QCoreApplication.translate("MainWindow", u"Tech/Wreck reel", None))
        self.pm_rebreather_check.setText(QCoreApplication.translate("MainWindow", u"Rebreather", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Sorb:", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"*** equipment upgrade price is upgrading from \n"
" single dive rental to full day", None))
        self.oid_search_label_5.setText(QCoreApplication.translate("MainWindow", u"ID number", None))
        self.pm_l_name_search_results_label.setText("")
        self.l_name_search_label_9.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Customer ID number", None))
        self.l_name_search_label_10.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Recreational Equipment", None))
        self.pm_soft_dive_check.setText(QCoreApplication.translate("MainWindow", u"Soft / dive", None))
        self.pm_torch_check.setText(QCoreApplication.translate("MainWindow", u"torch / day", None))
        self.pm_full_equip_dive_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment / dive", None))
        self.pm_reg_dive_check.setText(QCoreApplication.translate("MainWindow", u"REG / dive", None))
        self.pm_reg_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"REG upgrade", None))
        self.pm_full_equip_day_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment / day", None))
        self.pm_computer_check.setText(QCoreApplication.translate("MainWindow", u"computer / day", None))
        self.pm_bcd_dive_check.setText(QCoreApplication.translate("MainWindow", u"BCD / dive", None))
        self.pm_bcd_day_check.setText(QCoreApplication.translate("MainWindow", u"BCD / day", None))
        self.pm_full_equip_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment upgrade", None))
        self.pm_soft_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"Soft upgrade", None))
        self.pm_soft_day_check.setText(QCoreApplication.translate("MainWindow", u"Soft / day", None))
        self.pm_bcd_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"BCD upgrade", None))
        self.pm_reg_day_check.setText(QCoreApplication.translate("MainWindow", u"REG / day", None))
        self.pm_add_to_dive_button.setText(QCoreApplication.translate("MainWindow", u"Add to PM dive", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.pm_l_name_search_results_label_2.setText("")
        self.pm_f_name_search_results_label.setText("")
        self.oid_search_label_6.setText(QCoreApplication.translate("MainWindow", u"ID number", None))
        self.z_search_customer_button.setText(QCoreApplication.translate("MainWindow", u" Search for customer", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Tech equipment", None))
        self.z_smb_check.setText(QCoreApplication.translate("MainWindow", u"SMB", None))
        self.z_tech_torch_check.setText(QCoreApplication.translate("MainWindow", u"Tech torch", None))
        self.z_o2_reg_check.setText(QCoreApplication.translate("MainWindow", u"O2 clean REG with stage rigging", None))
        self.z_back_plate_check.setText(QCoreApplication.translate("MainWindow", u"Back plate with harness", None))
        self.z_reel_check.setText(QCoreApplication.translate("MainWindow", u"Reel", None))
        self.z_slate_check.setText(QCoreApplication.translate("MainWindow", u"Wrist slate", None))
        self.z_tech_computer_check.setText(QCoreApplication.translate("MainWindow", u"Tech computer", None))
        self.z_tech_reg_check.setText(QCoreApplication.translate("MainWindow", u"Primary REG", None))
        self.z_wing_check.setText(QCoreApplication.translate("MainWindow", u"Tech Wing", None))
        self.z_wreck_reel_check.setText(QCoreApplication.translate("MainWindow", u"Tech/Wreck reel", None))
        self.z_rebreather_check.setText(QCoreApplication.translate("MainWindow", u"Rebreather", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Sorb:", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"*** equipment upgrade price is upgrading from \n"
" single dive rental to full day", None))
        self.dob_search_label_6.setText(QCoreApplication.translate("MainWindow", u"DoB", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Customer ID number", None))
        self.f_name_search_label_6.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.l_name_search_label_11.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Tanks and gasses", None))
        self.z_twin_air_check.setText(QCoreApplication.translate("MainWindow", u"Twin set air", None))
        self.z_6l_50_check.setText(QCoreApplication.translate("MainWindow", u"6L 50%", None))
        self.z_twin_eanx_check.setText(QCoreApplication.translate("MainWindow", u"Twin set EANx", None))
        self.z_12l_100_check.setText(QCoreApplication.translate("MainWindow", u"12L 100%", None))
        self.z_6l_100_check.setText(QCoreApplication.translate("MainWindow", u"6L 100%", None))
        self.z_15l_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"15L upgrade", None))
        self.z_18l_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"18L upgrade", None))
        self.z_12l_50_check.setText(QCoreApplication.translate("MainWindow", u"12L 50%", None))
        self.z_eanx_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"EANx upgrade", None))
        self.z_no_tank_check.setText(QCoreApplication.translate("MainWindow", u"NO TANK", None))
        self.z_3l_100_check.setText(QCoreApplication.translate("MainWindow", u"3L 100%", None))
        self.z_3l_air_check.setText(QCoreApplication.translate("MainWindow", u"3L Air", None))
        self.l_name_search_label_12.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Recreational Equipment", None))
        self.z_soft_dive_check.setText(QCoreApplication.translate("MainWindow", u"Soft / dive", None))
        self.z_torch_check.setText(QCoreApplication.translate("MainWindow", u"torch / day", None))
        self.z_full_equip_dive_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment / dive", None))
        self.z_reg_dive_check.setText(QCoreApplication.translate("MainWindow", u"REG / dive", None))
        self.z_reg_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"REG upgrade", None))
        self.z_full_equip_day_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment / day", None))
        self.z_computer_check.setText(QCoreApplication.translate("MainWindow", u"computer / day", None))
        self.z_bcd_dive_check.setText(QCoreApplication.translate("MainWindow", u"BCD / dive", None))
        self.z_bcd_day_check.setText(QCoreApplication.translate("MainWindow", u"BCD / day", None))
        self.z_full_equip_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment upgrade", None))
        self.z_soft_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"Soft upgrade", None))
        self.z_soft_day_check.setText(QCoreApplication.translate("MainWindow", u"Soft / day", None))
        self.z_bcd_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"BCD upgrade", None))
        self.z_reg_day_check.setText(QCoreApplication.translate("MainWindow", u"REG / day", None))
        self.z_add_to_dive_button.setText(QCoreApplication.translate("MainWindow", u"Add to Zenobia dive", None))
        self.z_oid_search_results_label.setText("")
        self.z_f_name_search_results_label.setText("")
        self.z_l_name_search_results_label.setText("")
        self.z_l_name_search_results_label_2.setText("")
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.co_l_name_search_results_label_2.setText("")
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Tanks and gasses", None))
        self.co_twin_air_check.setText(QCoreApplication.translate("MainWindow", u"Twin set air", None))
        self.co_6l_50_check.setText(QCoreApplication.translate("MainWindow", u"6L 50%", None))
        self.co_twin_eanx_check.setText(QCoreApplication.translate("MainWindow", u"Twin set EANx", None))
        self.co_12l_100_check.setText(QCoreApplication.translate("MainWindow", u"12L 100%", None))
        self.co_6l_100_check.setText(QCoreApplication.translate("MainWindow", u"6L 100%", None))
        self.co_15l_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"15L upgrade", None))
        self.co_18l_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"18L upgrade", None))
        self.co_12l_50_check.setText(QCoreApplication.translate("MainWindow", u"12L 50%", None))
        self.co_eanx_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"EANx upgrade", None))
        self.co_no_tank_check.setText(QCoreApplication.translate("MainWindow", u"NO TANK", None))
        self.co_3l_100_check.setText(QCoreApplication.translate("MainWindow", u"3L 100%", None))
        self.co_3l_air_check.setText(QCoreApplication.translate("MainWindow", u"3L Air", None))
        self.oid_search_label_7.setText(QCoreApplication.translate("MainWindow", u"ID number", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Tech equipment", None))
        self.co_smb_check.setText(QCoreApplication.translate("MainWindow", u"SMB", None))
        self.co_tech_torch_check.setText(QCoreApplication.translate("MainWindow", u"Tech torch", None))
        self.co_o2_reg_check.setText(QCoreApplication.translate("MainWindow", u"O2 clean REG with stage rigging", None))
        self.co_back_plate_check.setText(QCoreApplication.translate("MainWindow", u"Back plate with harness", None))
        self.co_reel_check.setText(QCoreApplication.translate("MainWindow", u"Reel", None))
        self.co_slate_check.setText(QCoreApplication.translate("MainWindow", u"Wrist slate", None))
        self.co_tech_computer_check.setText(QCoreApplication.translate("MainWindow", u"Tech computer", None))
        self.co_tech_reg_check.setText(QCoreApplication.translate("MainWindow", u"Primary REG", None))
        self.co_wing_check.setText(QCoreApplication.translate("MainWindow", u"Tech Wing", None))
        self.co_wreck_reel_check.setText(QCoreApplication.translate("MainWindow", u"Tech/Wreck reel", None))
        self.co_rebreather_check.setText(QCoreApplication.translate("MainWindow", u"Rebreather", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Sorb:", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"KG", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"*** equipment upgrade price is upgrading from \n"
" single dive rental to full day", None))
        self.l_name_search_label_13.setText(QCoreApplication.translate("MainWindow", u"Last Name:", None))
        self.co_search_customer_button.setText(QCoreApplication.translate("MainWindow", u" Search for customer", None))
        self.co_f_name_search_results_label.setText("")
        self.co_l_name_search_results_label.setText("")
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Recreational Equipment", None))
        self.co_soft_dive_check.setText(QCoreApplication.translate("MainWindow", u"Soft / dive", None))
        self.co_torch_check.setText(QCoreApplication.translate("MainWindow", u"torch / day", None))
        self.co_full_equip_dive_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment / dive", None))
        self.co_reg_dive_check.setText(QCoreApplication.translate("MainWindow", u"REG / dive", None))
        self.co_reg_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"REG upgrade", None))
        self.co_full_equip_day_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment / day", None))
        self.co_computer_check.setText(QCoreApplication.translate("MainWindow", u"computer / day", None))
        self.co_bcd_dive_check.setText(QCoreApplication.translate("MainWindow", u"BCD / dive", None))
        self.co_bcd_day_check.setText(QCoreApplication.translate("MainWindow", u"BCD / day", None))
        self.co_full_equip_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"Full equipment upgrade", None))
        self.co_soft_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"Soft upgrade", None))
        self.co_soft_day_check.setText(QCoreApplication.translate("MainWindow", u"Soft / day", None))
        self.co_bcd_upgrade_check.setText(QCoreApplication.translate("MainWindow", u"BCD upgrade", None))
        self.co_reg_day_check.setText(QCoreApplication.translate("MainWindow", u"REG / day", None))
        self.co_add_to_dive_button.setText(QCoreApplication.translate("MainWindow", u"Add to Courses", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Customer ID number", None))
        self.dob_search_label_7.setText(QCoreApplication.translate("MainWindow", u"DoB", None))
        self.l_name_search_label_14.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.co_oid_search_results_label.setText("")
        self.f_name_search_label_7.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Get Wet Divers booking system designed by Ben Wrench", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

