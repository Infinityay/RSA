# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE_changeINBfgR.ui'
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
        MainWindow.resize(1202, 818)
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
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
        # endif
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
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
        # endif
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
        # if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
        # endif
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
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
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
                                      "	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
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
                                      "	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
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
                                           "	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
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
                                              "background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
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
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

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
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
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
        self.verticalLayout_24 = QVBoxLayout(self.frame_content)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(200, 100))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(26)
        self.stackedWidget.setFont(font5)
        self.stackedWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_rsa = QWidget()
        self.page_rsa.setObjectName(u"page_rsa")
        self.verticalLayout_12 = QVBoxLayout(self.page_rsa)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_rsa = QVBoxLayout()
        self.verticalLayout_rsa.setObjectName(u"verticalLayout_rsa")
        self.horizontalLayout_001 = QHBoxLayout()
        self.horizontalLayout_001.setObjectName(u"horizontalLayout_001")
        self.label_3 = QLabel(self.page_rsa)
        self.label_3.setObjectName(u"label_3")
        font6 = QFont()
        font6.setFamily(u"Microsoft YaHei")
        font6.setPointSize(14)
        self.label_3.setFont(font6)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_001.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_001.addItem(self.horizontalSpacer_5)

        self.plainTextEdit_8 = QPlainTextEdit(self.page_rsa)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setMinimumSize(QSize(200, 45))
        font7 = QFont()
        font7.setFamily(u"Arial")
        font7.setPointSize(12)
        self.plainTextEdit_8.setFont(font7)
        self.plainTextEdit_8.setStyleSheet(u"QPlainTextEdit {\n"
                                           "	background-color: rgb(27, 29, 35);\n"
                                           "	border-radius: 5px;\n"
                                           "	padding: 10px;\n"
                                           "}\n"
                                           "QPlainTextEdit:hover {\n"
                                           "	border: 2px solid rgb(64, 71, 88);\n"
                                           "}\n"
                                           "QPlainTextEdit:focus {\n"
                                           "	border: 2px solid rgb(91, 101, 124);\n"
                                           "}")

        self.horizontalLayout_001.addWidget(self.plainTextEdit_8)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_001.addItem(self.horizontalSpacer_54)

        self.pushButton_20 = QPushButton(self.page_rsa)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(90, 60))
        font8 = QFont()
        font8.setFamily(u"Arial")
        font8.setPointSize(14)
        self.pushButton_20.setFont(font8)
        self.pushButton_20.setStyleSheet(u"QPushButton {\n"
                                         "	border: 2px solid rgb(52, 59, 72);\n"
                                         "	border-radius: 5px;	\n"
                                         "	background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(57, 65, 80);\n"
                                         "	border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color: rgb(35, 40, 49);\n"
                                         "	border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        self.horizontalLayout_001.addWidget(self.pushButton_20)

        self.verticalLayout_rsa.addLayout(self.horizontalLayout_001)

        self.horizontalLayout_002 = QHBoxLayout()
        self.horizontalLayout_002.setObjectName(u"horizontalLayout_002")
        self.label = QLabel(self.page_rsa)
        self.label.setObjectName(u"label")
        self.label.setFont(font6)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_002.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_002.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.page_rsa)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font6)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_002.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.page_rsa)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
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
                                    "}")

        self.horizontalLayout_002.addWidget(self.lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_002.addItem(self.horizontalSpacer_3)

        self.label_7 = QLabel(self.page_rsa)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_002.addWidget(self.label_7)

        self.lineEdit_2 = QLineEdit(self.page_rsa)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(300, 30))
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
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
                                      "}")

        self.horizontalLayout_002.addWidget(self.lineEdit_2)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_002.addItem(self.horizontalSpacer_49)

        self.pushButton_19 = QPushButton(self.page_rsa)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(90, 60))
        self.pushButton_19.setFont(font8)
        self.pushButton_19.setStyleSheet(u"QPushButton {\n"
                                         "	border: 2px solid rgb(52, 59, 72);\n"
                                         "	border-radius: 5px;	\n"
                                         "	background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(57, 65, 80);\n"
                                         "	border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color: rgb(35, 40, 49);\n"
                                         "	border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        self.horizontalLayout_002.addWidget(self.pushButton_19)

        self.verticalLayout_rsa.addLayout(self.horizontalLayout_002)

        self.horizontalLayout_003 = QHBoxLayout()
        self.horizontalLayout_003.setObjectName(u"horizontalLayout_003")
        self.label_8 = QLabel(self.page_rsa)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font6)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_003.addWidget(self.label_8)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_003.addItem(self.horizontalSpacer_2)

        self.label_9 = QLabel(self.page_rsa)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font6)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_003.addWidget(self.label_9)

        self.plainTextEdit_7 = QPlainTextEdit(self.page_rsa)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_7.setFont(font7)
        self.plainTextEdit_7.setStyleSheet(u"QPlainTextEdit {\n"
                                           "	background-color: rgb(27, 29, 35);\n"
                                           "	border-radius: 5px;\n"
                                           "	padding: 10px;\n"
                                           "}\n"
                                           "QPlainTextEdit:hover {\n"
                                           "	border: 2px solid rgb(64, 71, 88);\n"
                                           "}\n"
                                           "QPlainTextEdit:focus {\n"
                                           "	border: 2px solid rgb(91, 101, 124);\n"
                                           "}")
        self.plainTextEdit_7.setReadOnly(True)

        self.horizontalLayout_003.addWidget(self.plainTextEdit_7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_003.addItem(self.horizontalSpacer_6)

        self.label_14 = QLabel(self.page_rsa)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font6)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_003.addWidget(self.label_14)

        self.plainTextEdit_11 = QPlainTextEdit(self.page_rsa)
        self.plainTextEdit_11.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_11.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_11.setFont(font7)
        self.plainTextEdit_11.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_11.setReadOnly(True)

        self.horizontalLayout_003.addWidget(self.plainTextEdit_11)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_003.addItem(self.horizontalSpacer_4)

        self.pushButton_3 = QPushButton(self.page_rsa)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(90, 60))
        self.pushButton_3.setFont(font8)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
                                        "	border: 2px solid rgb(52, 59, 72);\n"
                                        "	border-radius: 5px;	\n"
                                        "	background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(57, 65, 80);\n"
                                        "	border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "	background-color: rgb(35, 40, 49);\n"
                                        "	border: 2px solid rgb(43, 50, 61);\n"
                                        "}")

        self.horizontalLayout_003.addWidget(self.pushButton_3)

        self.verticalLayout_rsa.addLayout(self.horizontalLayout_003)

        self.horizontalLayout_004 = QHBoxLayout()
        self.horizontalLayout_004.setObjectName(u"horizontalLayout_004")
        self.label_15 = QLabel(self.page_rsa)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font6)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_004.addWidget(self.label_15)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_004.addItem(self.horizontalSpacer_7)

        self.plainTextEdit_31 = QPlainTextEdit(self.page_rsa)
        self.plainTextEdit_31.setObjectName(u"plainTextEdit_31")
        self.plainTextEdit_31.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_31.setFont(font7)
        self.plainTextEdit_31.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_31.setReadOnly(True)

        self.horizontalLayout_004.addWidget(self.plainTextEdit_31)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_004.addItem(self.horizontalSpacer_47)

        self.pushButton_18 = QPushButton(self.page_rsa)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(90, 60))
        self.pushButton_18.setFont(font8)
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
                                         "	border: 2px solid rgb(52, 59, 72);\n"
                                         "	border-radius: 5px;	\n"
                                         "	background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(57, 65, 80);\n"
                                         "	border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color: rgb(35, 40, 49);\n"
                                         "	border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        self.horizontalLayout_004.addWidget(self.pushButton_18)

        self.verticalLayout_rsa.addLayout(self.horizontalLayout_004)

        self.horizontalLayout_005 = QHBoxLayout()
        self.horizontalLayout_005.setObjectName(u"horizontalLayout_005")
        self.label_17 = QLabel(self.page_rsa)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font6)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_005.addWidget(self.label_17)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_005.addItem(self.horizontalSpacer_8)

        self.plainTextEdit_29 = QPlainTextEdit(self.page_rsa)
        self.plainTextEdit_29.setObjectName(u"plainTextEdit_29")
        self.plainTextEdit_29.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_29.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_29.setFont(font7)
        self.plainTextEdit_29.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_29.setReadOnly(True)

        self.horizontalLayout_005.addWidget(self.plainTextEdit_29)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_005.addItem(self.horizontalSpacer_11)

        self.pushButton_5 = QPushButton(self.page_rsa)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(90, 60))
        self.pushButton_5.setFont(font8)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
                                        "	border: 2px solid rgb(52, 59, 72);\n"
                                        "	border-radius: 5px;	\n"
                                        "	background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(57, 65, 80);\n"
                                        "	border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "	background-color: rgb(35, 40, 49);\n"
                                        "	border: 2px solid rgb(43, 50, 61);\n"
                                        "}")

        self.horizontalLayout_005.addWidget(self.pushButton_5)

        self.verticalLayout_rsa.addLayout(self.horizontalLayout_005)

        self.horizontalLayout_006 = QHBoxLayout()
        self.horizontalLayout_006.setObjectName(u"horizontalLayout_006")
        self.label_31 = QLabel(self.page_rsa)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font6)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_006.addWidget(self.label_31)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_006.addItem(self.horizontalSpacer_20)

        self.label_32 = QLabel(self.page_rsa)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font6)
        self.label_32.setAutoFillBackground(False)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_006.addWidget(self.label_32)

        self.plainTextEdit_38 = QPlainTextEdit(self.page_rsa)
        self.plainTextEdit_38.setObjectName(u"plainTextEdit_38")
        self.plainTextEdit_38.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_38.setFont(font7)
        self.plainTextEdit_38.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_38.setReadOnly(True)
        self.plainTextEdit_38.setCenterOnScroll(False)

        self.horizontalLayout_006.addWidget(self.plainTextEdit_38)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_006.addItem(self.horizontalSpacer_21)

        self.label_33 = QLabel(self.page_rsa)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font6)
        self.label_33.setAutoFillBackground(False)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_006.addWidget(self.label_33)

        self.plainTextEdit_39 = QPlainTextEdit(self.page_rsa)
        self.plainTextEdit_39.setObjectName(u"plainTextEdit_39")
        self.plainTextEdit_39.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_39.setFont(font7)
        self.plainTextEdit_39.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_39.setReadOnly(True)

        self.horizontalLayout_006.addWidget(self.plainTextEdit_39)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_006.addItem(self.horizontalSpacer_53)

        self.pushButton_10 = QPushButton(self.page_rsa)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(90, 60))
        self.pushButton_10.setFont(font8)
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
                                         "	border: 2px solid rgb(52, 59, 72);\n"
                                         "	border-radius: 5px;	\n"
                                         "	background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(57, 65, 80);\n"
                                         "	border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color: rgb(35, 40, 49);\n"
                                         "	border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        self.horizontalLayout_006.addWidget(self.pushButton_10)

        self.verticalLayout_rsa.addLayout(self.horizontalLayout_006)

        self.horizontalLayout_007 = QHBoxLayout()
        self.horizontalLayout_007.setObjectName(u"horizontalLayout_007")
        self.label_5 = QLabel(self.page_rsa)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font6)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_007.addWidget(self.label_5)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_007.addItem(self.horizontalSpacer_22)

        self.plainTextEdit_9 = QPlainTextEdit(self.page_rsa)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        self.plainTextEdit_9.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_9.setFont(font7)
        self.plainTextEdit_9.setStyleSheet(u"QPlainTextEdit {\n"
                                           "	background-color: rgb(27, 29, 35);\n"
                                           "	border-radius: 5px;\n"
                                           "	padding: 10px;\n"
                                           "}\n"
                                           "QPlainTextEdit:hover {\n"
                                           "	border: 2px solid rgb(64, 71, 88);\n"
                                           "}\n"
                                           "QPlainTextEdit:focus {\n"
                                           "	border: 2px solid rgb(91, 101, 124);\n"
                                           "}")
        self.plainTextEdit_9.setReadOnly(True)

        self.horizontalLayout_007.addWidget(self.plainTextEdit_9)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_007.addItem(self.horizontalSpacer_55)

        self.pushButton_21 = QPushButton(self.page_rsa)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(90, 60))
        self.pushButton_21.setFont(font8)
        self.pushButton_21.setStyleSheet(u"QPushButton {\n"
                                         "	border: 2px solid rgb(52, 59, 72);\n"
                                         "	border-radius: 5px;	\n"
                                         "	background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(57, 65, 80);\n"
                                         "	border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color: rgb(35, 40, 49);\n"
                                         "	border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        self.horizontalLayout_007.addWidget(self.pushButton_21)

        self.verticalLayout_rsa.addLayout(self.horizontalLayout_007)

        self.horizontalLayout_008 = QHBoxLayout()
        self.horizontalLayout_008.setObjectName(u"horizontalLayout_008")
        self.label_10 = QLabel(self.page_rsa)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font6)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_008.addWidget(self.label_10)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_008.addItem(self.horizontalSpacer_24)

        self.plainTextEdit_10 = QPlainTextEdit(self.page_rsa)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")
        self.plainTextEdit_10.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_10.setFont(font7)
        self.plainTextEdit_10.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_10.setReadOnly(True)

        self.horizontalLayout_008.addWidget(self.plainTextEdit_10)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_008.addItem(self.horizontalSpacer_56)

        self.pushButton_22 = QPushButton(self.page_rsa)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(90, 60))
        self.pushButton_22.setFont(font8)
        self.pushButton_22.setStyleSheet(u"QPushButton {\n"
                                         "	border: 2px solid rgb(52, 59, 72);\n"
                                         "	border-radius: 5px;	\n"
                                         "	background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(57, 65, 80);\n"
                                         "	border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color: rgb(35, 40, 49);\n"
                                         "	border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        self.horizontalLayout_008.addWidget(self.pushButton_22)

        self.verticalLayout_rsa.addLayout(self.horizontalLayout_008)

        self.horizontalLayout_009 = QHBoxLayout()
        self.horizontalLayout_009.setObjectName(u"horizontalLayout_009")
        self.label_11 = QLabel(self.page_rsa)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font6)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_009.addWidget(self.label_11)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_009.addItem(self.horizontalSpacer_10)

        self.plainTextEdit_13 = QPlainTextEdit(self.page_rsa)
        self.plainTextEdit_13.setObjectName(u"plainTextEdit_13")
        self.plainTextEdit_13.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_13.setFont(font7)
        self.plainTextEdit_13.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_13.setReadOnly(True)

        self.horizontalLayout_009.addWidget(self.plainTextEdit_13)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_009.addItem(self.horizontalSpacer_23)

        self.pushButton_4 = QPushButton(self.page_rsa)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(90, 60))
        self.pushButton_4.setFont(font8)
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
                                        "	border: 2px solid rgb(52, 59, 72);\n"
                                        "	border-radius: 5px;	\n"
                                        "	background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "	background-color: rgb(57, 65, 80);\n"
                                        "	border: 2px solid rgb(61, 70, 86);\n"
                                        "}\n"
                                        "QPushButton:pressed {	\n"
                                        "	background-color: rgb(35, 40, 49);\n"
                                        "	border: 2px solid rgb(43, 50, 61);\n"
                                        "}")

        self.horizontalLayout_009.addWidget(self.pushButton_4)

        self.verticalLayout_rsa.addLayout(self.horizontalLayout_009)

        self.verticalLayout_12.addLayout(self.verticalLayout_rsa)

        self.stackedWidget.addWidget(self.page_rsa)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_8 = QVBoxLayout(self.page_home)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.page_home)
        self.label_4.setObjectName(u"label_4")
        font9 = QFont()
        font9.setFamily(u"Microsoft YaHei")
        font9.setPointSize(72)
        self.label_4.setFont(font9)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)

        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font10 = QFont()
        font10.setFamily(u"Microsoft YaHei")
        font10.setPointSize(26)
        self.label_6.setFont(font10)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)

        self.label_12 = QLabel(self.page_home)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font10)
        urlDisplay = "urlAddressDisPlay";
        urlStyle = "<a href=www.baidu.com style=\"color:red;text-decoration:none;\">";
        self.label_12.setText('More details: '
                              '<a href="https://github.com/Infinityay/RSA">'
                              'RSA</a>')
        self.label_12.setOpenExternalLinks(True)
        self.label_12.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_12)

        self.verticalLayout_8.addLayout(self.verticalLayout_6)

        self.stackedWidget.addWidget(self.page_home)
        self.page_signature = QWidget()
        self.page_signature.setObjectName(u"page_signature")
        self.verticalLayout_10 = QVBoxLayout(self.page_signature)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_16 = QLabel(self.page_signature)
        self.label_16.setObjectName(u"label_16")
        font_lab = QFont()
        font_lab.setFamily(u"Microsoft YaHei")
        font_lab.setPointSize(20)
        self.label_16.setFont(font_lab)
        self.verticalLayout_9.addWidget(self.label_16)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_13 = QLabel(self.page_signature)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font6)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_13)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.plainTextEdit_12 = QPlainTextEdit(self.page_signature)
        self.plainTextEdit_12.setObjectName(u"plainTextEdit_12")
        self.plainTextEdit_12.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_12.setFont(font7)
        self.plainTextEdit_12.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_12.setPlaceholderText("Fill in the plainText that the sender wants to send")
        self.horizontalLayout.addWidget(self.plainTextEdit_12)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_57)

        self.pushButton_23 = QPushButton(self.page_signature)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(90, 60))
        self.pushButton_23.setFont(font8)
        self.pushButton_23.setStyleSheet(u"QPushButton {\n"
                                         "	border: 2px solid rgb(52, 59, 72);\n"
                                         "	border-radius: 5px;	\n"
                                         "	background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(57, 65, 80);\n"
                                         "	border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color: rgb(35, 40, 49);\n"
                                         "	border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        self.horizontalLayout.addWidget(self.pushButton_23)

        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_34 = QLabel(self.page_signature)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font6)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_34)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_25)

        self.label_36 = QLabel(self.page_signature)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font6)
        self.label_36.setAutoFillBackground(False)
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_36)

        self.plainTextEdit_41 = QPlainTextEdit(self.page_signature)
        self.plainTextEdit_41.setObjectName(u"plainTextEdit_41")
        self.plainTextEdit_41.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_41.setFont(font7)
        self.plainTextEdit_41.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_41.setReadOnly(True)
        self.plainTextEdit_41.setCenterOnScroll(False)

        self.horizontalLayout_14.addWidget(self.plainTextEdit_41)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)

        self.label_35 = QLabel(self.page_signature)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font6)
        self.label_35.setAutoFillBackground(False)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_35)

        self.plainTextEdit_40 = QPlainTextEdit(self.page_signature)
        self.plainTextEdit_40.setObjectName(u"plainTextEdit_40")
        self.plainTextEdit_40.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_40.setFont(font7)
        self.plainTextEdit_40.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_40.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.plainTextEdit_40)

        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_62)

        self.pushButton_11 = QPushButton(self.page_signature)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(90, 60))
        self.pushButton_11.setFont(font8)
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
                                         "	border: 2px solid rgb(52, 59, 72);\n"
                                         "	border-radius: 5px;	\n"
                                         "	background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(57, 65, 80);\n"
                                         "	border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color: rgb(35, 40, 49);\n"
                                         "	border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        self.horizontalLayout_14.addWidget(self.pushButton_11)

        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_19 = QLabel(self.page_signature)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font6)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)

        self.plainTextEdit_16 = QPlainTextEdit(self.page_signature)
        self.plainTextEdit_16.setObjectName(u"plainTextEdit_16")
        self.plainTextEdit_16.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_16.setFont(font7)
        self.plainTextEdit_16.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_16.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.plainTextEdit_16)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_60)

        self.pushButton_26 = QPushButton(self.page_signature)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(90, 60))
        self.pushButton_26.setFont(font8)
        self.pushButton_26.setStyleSheet(u"QPushButton {\n"
                                         "	border: 2px solid rgb(52, 59, 72);\n"
                                         "	border-radius: 5px;	\n"
                                         "	background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(57, 65, 80);\n"
                                         "	border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color: rgb(35, 40, 49);\n"
                                         "	border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        self.horizontalLayout_12.addWidget(self.pushButton_26)

        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.label_18 = QLabel(self.page_signature)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font_lab)
        self.verticalLayout_9.addWidget(self.label_18)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_21 = QLabel(self.page_signature)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font6)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_21)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)

        self.plainTextEdit_18 = QPlainTextEdit(self.page_signature)
        self.plainTextEdit_18.setObjectName(u"plainTextEdit_18")
        self.plainTextEdit_18.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_18.setFont(font7)
        self.plainTextEdit_18.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_18.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.plainTextEdit_18)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_63)

        self.pushButton_28 = QPushButton(self.page_signature)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(90, 60))
        self.pushButton_28.setFont(font8)
        self.pushButton_28.setStyleSheet(u"QPushButton {\n"
                                         "	border: 2px solid rgb(52, 59, 72);\n"
                                         "	border-radius: 5px;	\n"
                                         "	background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(57, 65, 80);\n"
                                         "	border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color: rgb(35, 40, 49);\n"
                                         "	border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        self.horizontalLayout_15.addWidget(self.pushButton_28)

        self.verticalLayout_9.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_20 = QLabel(self.page_signature)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font6)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_20)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_15)

        self.plainTextEdit_17 = QPlainTextEdit(self.page_signature)
        self.plainTextEdit_17.setObjectName(u"plainTextEdit_17")
        self.plainTextEdit_17.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_17.setFont(font7)
        self.plainTextEdit_17.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_17.setPlaceholderText("Fill in the plaintext obtained by the recipient")
        self.horizontalLayout_9.addWidget(self.plainTextEdit_17)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_61)

        self.pushButton_27 = QPushButton(self.page_signature)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(90, 60))
        self.pushButton_27.setFont(font8)
        self.pushButton_27.setStyleSheet(u"QPushButton {\n"
                                         "	border: 2px solid rgb(52, 59, 72);\n"
                                         "	border-radius: 5px;	\n"
                                         "	background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(57, 65, 80);\n"
                                         "	border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color: rgb(35, 40, 49);\n"
                                         "	border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        self.horizontalLayout_9.addWidget(self.pushButton_27)

        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_22 = QLabel(self.page_signature)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font6)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_22)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_17)

        self.plainTextEdit_19 = QPlainTextEdit(self.page_signature)
        self.plainTextEdit_19.setObjectName(u"plainTextEdit_19")
        self.plainTextEdit_19.setMinimumSize(QSize(200, 45))
        self.plainTextEdit_19.setFont(font7)
        self.plainTextEdit_19.setStyleSheet(u"QPlainTextEdit {\n"
                                            "	background-color: rgb(27, 29, 35);\n"
                                            "	border-radius: 5px;\n"
                                            "	padding: 10px;\n"
                                            "}\n"
                                            "QPlainTextEdit:hover {\n"
                                            "	border: 2px solid rgb(64, 71, 88);\n"
                                            "}\n"
                                            "QPlainTextEdit:focus {\n"
                                            "	border: 2px solid rgb(91, 101, 124);\n"
                                            "}")
        self.plainTextEdit_19.setReadOnly(True)
        self.plainTextEdit_19.setPlaceholderText("verify the signature")
        self.horizontalLayout_11.addWidget(self.plainTextEdit_19)

        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_64)

        self.pushButton_29 = QPushButton(self.page_signature)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(90, 60))
        self.pushButton_29.setFont(font8)
        self.pushButton_29.setStyleSheet(u"QPushButton {\n"
                                         "	border: 2px solid rgb(52, 59, 72);\n"
                                         "	border-radius: 5px;	\n"
                                         "	background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "	background-color: rgb(57, 65, 80);\n"
                                         "	border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {	\n"
                                         "	background-color: rgb(35, 40, 49);\n"
                                         "	border: 2px solid rgb(43, 50, 61);\n"
                                         "}")

        self.horizontalLayout_11.addWidget(self.pushButton_29)

        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.stackedWidget.addWidget(self.page_signature)

        self.verticalLayout_24.addWidget(self.stackedWidget)

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
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)

        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
                                           "	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
                                           "	background-position: center;\n"
                                           "	background-repeat: no-reperat;\n"
                                           "}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)

        self.verticalLayout_4.addWidget(self.frame_grip)

        self.horizontalLayout_2.addWidget(self.frame_content_right)

        self.verticalLayout.addWidget(self.frame_center)

        self.verticalLayout_7.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
        # if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
        # if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(
            QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"RSA", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Step 1: input plainText", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"encode", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Step 2: Select Primes", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"p:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"q:", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"generate", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Step 3: Key length", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"n =", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u03c6(n) = ", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"do", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Step 4: Public exponent", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"generate", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Step 5:Private exponent", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"do", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Step 6: get Keys", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"PublicKey = ", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"PublicKey = ", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"get", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Step 7: encrypt by Public", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"encrypt", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Step 8:decrypt by Private", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"decrypt", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Step 9: output plaintext  ", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"decode", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", u"Just click left menu and start RSA experiment!", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Sender", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Step 1: Message Digest ", None))
        self.plainTextEdit_12.setPlainText("")

        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Hash", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Step 2: RSA                ", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"    e = ", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u" d = ", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"get", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Step 3:Signature by d     ", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"signature", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Recipient", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Step 4:Decrypt signature ", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"decrypt", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Step 5:Message Digest    ", None))
        self.plainTextEdit_17.setPlainText("")

        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Hash", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Step 6: Verify signature   ", None))
        self.plainTextEdit_19.setPlainText("")

        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"verify", None))
        self.label_credits.setText(
            QCoreApplication.translate("MainWindow", u"Registered by: Wanderson M. Pimenta", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi
