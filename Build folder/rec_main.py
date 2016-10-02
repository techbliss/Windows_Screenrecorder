#Author Storm Shadow www.techbliss.org
import icons
import os
import sys
import re
import time
#import urllib2 // for updater next version
#import json // for updater next version
from time import time, sleep
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QProcess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (QAction, QApplication, QComboBox,
        QDialog, QGroupBox, QLabel, QLineEdit, QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QSplashScreen, QMessageBox)
import time
import datetime
from datetime import datetime
import subprocess
from subprocess import Popen, PIPE
stamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") #next version dont work with time stamp yet
dn = os.getcwd()
sys.path.insert(0, dn)


class Ui_messageformForm(QtWidgets.QWidget):
    def setupUi1(self, messageformForm):
        messageformForm.setObjectName("messageformForm")
        messageformForm.resize(404, 169)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(messageformForm.sizePolicy().hasHeightForWidth())
        messageformForm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        messageformForm.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ico/record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        messageformForm.setWindowIcon(icon2)
        messageformForm.setStyleSheet("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: rgb(226, 53, 46);\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  color: rgb(220,220,220);\n"
"  outline: none;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 1 #e20046);\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.label = QtWidgets.QLabel(messageformForm)
        self.label.setGeometry(QtCore.QRect(40, 20, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(messageformForm)
        QtCore.QMetaObject.connectSlotsByName(messageformForm)

    def retranslateUi(self, messageformForm):
        _translate = QtCore.QCoreApplication.translate
        messageformForm.setWindowTitle(_translate("messageformForm", "Notice"))
        self.label.setText(_translate("messageformForm", "Will Be added in\n"
" future version"))



class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("recorder")
        MainWindow.setGeometry(100, 100, 100, 100)
        MainWindow.resize(400,156)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/1469147602_Python_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.activateWindow()
        MainWindow.setStyleSheet("QToolTip\n"
                                 "{\n"
                                 "     border: 1px solid black;\n"
                                 "     background-color: rgb(226, 53, 46);\n"
                                 "     padding: 1px;\n"
                                 "     border-radius: 3px;\n"
                                 "     opacity: 1000;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget\n"
                                 "{\n"
                                 "  background-color: rgb(80,80,80);\n"
                                 "  color: rgb(220,220,220);\n"
                                 "  font-size: 11px;\n"
                                 "  outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:item:hover\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 1 #ca0619);\n"
                                 "    color: #000000;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:item:selected\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 1 #e20046);\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item\n"
                                 "{\n"
                                 "    background: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item:selected\n"
                                 "{\n"
                                 "    background: transparent;\n"
                                 "    border: 1px solid #e2352e;\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item:pressed\n"
                                 "{\n"
                                 "    background: #444;\n"
                                 "    border: 1px solid #000;\n"
                                 "    background-color: QLinearGradient(\n"
                                 "        x1:0, y1:0,\n"
                                 "        x2:0, y2:1,\n"
                                 "        stop:1 #212121,\n"
                                 "        stop:0.4 #343434/*,\n"
                                 "        stop:0.2 #343434,\n"
                                 "        stop:0.1 #ffaa00*/\n"
                                 "    );\n"
                                 "    margin-bottom:-1px;\n"
                                 "    padding-bottom:1px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu\n"
                                 "{\n"
                                 "    border: 1px solid #000;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item\n"
                                 "{\n"
                                 "    padding: 2px 20px 2px 20px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item:selected\n"
                                 "{\n"
                                 "    color: #000000;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:disabled\n"
                                 "{\n"
                                 "    color: #404040;\n"
                                 "    background-color: #323232;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractItemView\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:focus\n"
                                 "{\n"
                                 "    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
                                 "    padding: 1px;\n"
                                 "    border-style: solid;\n"
                                 "    border: 1px solid #1e1e1e;\n"
                                 "    border-radius: 5;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    border: 1px solid #e2352e;\n"
                                 "    text-align: center;\n"
                                 "    min-height: 20px;\n"
                                 "    min-width: 50px;\n"
                                 "    \n"
                                 "    padding: 0 6px 0 6px;\n"
                                 "}\n"
                                 "QPushButton:pressed\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox\n"
                                 "{\n"
                                 "    selection-background-color: #e2352e;\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                                 "    border-style: solid;\n"
                                 "    border: 1px solid #1e1e1e;\n"
                                 "    border-radius: 5;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QComboBox:hover,QPushButton:hover\n"
                                 "{\n"
                                 "    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 1 #e20046);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QComboBox:on\n"
                                 "{\n"
                                 "    padding-top: 3px;\n"
                                 "    padding-left: 4px;\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                                 "    selection-background-color: #e2352e;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox QAbstractItemView\n"
                                 "{\n"
                                 "    border: 2px solid darkgray;\n"
                                 "    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 1 #e20046);\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::drop-down\n"
                                 "{\n"
                                 "     subcontrol-origin: padding;\n"
                                 "     subcontrol-position: top right;\n"
                                 "     width: 15px;\n"
                                 "\n"
                                 "     border-left-width: 0px;\n"
                                 "     border-left-color: darkgray;\n"
                                 "     border-left-style: solid; /* just a single line */\n"
                                 "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                 "     border-bottom-right-radius: 3px;\n"
                                 " }\n"
                                 "\n"
                                 "QComboBox::down-arrow\n"
                                 "{\n"
                                 "     image: url(:/down_arrow.png);\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox:focus\n"
                                 "{\n"
                                 "border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 1 #e20046);\n"
                                 "}\n"
                                 "\n"
                                 "QTextEdit:focus\n"
                                 "{\n"
                                 "    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 1 #e20046);\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:horizontal {\n"
                                 "     border: 1px solid #222222;\n"
                                 "     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
                                 "     height: 15px;\n"
                                 "     margin: 0px 16px 0 16px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal\n"
                                 "{\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #e2352e, stop: 0.5 #e20046, stop: 1 #e2352e);\n"
                                 "      min-height: 15px;\n"
                                 "      border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:horizontal {\n"
                                 "      border: 1px solid #1b1b19;\n"
                                 "      border-radius: 2px;\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #e2352e, stop: 1 #e20046);\n"
                                 "      width: 15px;\n"
                                 "      subcontrol-position: right;\n"
                                 "      subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:horizontal {\n"
                                 "      border: 1px solid #1b1b19;\n"
                                 "      border-radius: 2px;\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #e2352e, stop: 1 #e20046);\n"
                                 "      width: 15px;\n"
                                 "     subcontrol-position: left;\n"
                                 "     subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
                                 "{\n"
                                 "      border: 1px solid black;\n"
                                 "      width: 1px;\n"
                                 "      height: 1px;\n"
                                 "      background: white;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                 "{\n"
                                 "      background: none;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:vertical\n"
                                 "{\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
                                 "      width: 15px;\n"
                                 "      margin: 16px 0 16px 0;\n"
                                 "      border: 1px solid #222222;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical\n"
                                 "{\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 0.5 #e20046, stop: 1 #e2352e);\n"
                                 "      min-height: 20px;\n"
                                 "      border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:vertical\n"
                                 "{\n"
                                 "      border: 1px solid #1b1b19;\n"
                                 "      border-radius: 2px;\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 1 #e20046);\n"
                                 "      height: 14px;\n"
                                 "      subcontrol-position: bottom;\n"
                                 "      subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:vertical\n"
                                 "{\n"
                                 "      border: 1px solid #1b1b19;\n"
                                 "      border-radius: 2px;\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 1 #e20046);\n"
                                 "      height: 14px;\n"
                                 "      subcontrol-position: top;\n"
                                 "      subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
                                 "{\n"
                                 "      border: 1px solid black;\n"
                                 "      width: 1px;\n"
                                 "      height: 1px;\n"
                                 "      background: white;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
                                 "{\n"
                                 "      background: none;\n"
                                 "}\n"
                                 "\n"
                                 "QTextEdit\n"
                                 "{\n"
                                 "    background-color: #242424;\n"
                                 "}\n"
                                 "\n"
                                 "QPlainTextEdit\n"
                                 "{\n"
                                 "    background-color: #242424;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section\n"
                                 "{\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    border: 1px solid #6c6c6c;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox:disabled\n"
                                 "{\n"
                                 "color: #414141;\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::title\n"
                                 "{\n"
                                 "    text-align: center;\n"
                                 "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button, QDockWidget::float-button\n"
                                 "{\n"
                                 "    text-align: center;\n"
                                 "    spacing: 1px; /* spacing between items in the tool bar */\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
                                 "{\n"
                                 "    background: #242424;\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
                                 "{\n"
                                 "    padding: 1px -1px -1px 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow::separator\n"
                                 "{\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    border: 1px solid #4c4c4c;\n"
                                 "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow::separator:hover\n"
                                 "{\n"
                                 "\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #e2352e, stop:0.5 #e20046\n"
                                 "    stop:1 #e2352e);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    border: 1px solid #6c6c6c;\n"
                                 "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "}\n"
                                 "\n"
                                 "QToolBar::handle\n"
                                 "{\n"
                                 "     spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "     background: url(./icons/handle.png);\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::separator\n"
                                 "{\n"
                                 "    height: 2px;\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    margin-left: 10px;\n"
                                 "    margin-right: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QProgressBar\n"
                                 "{\n"
                                 "    border: 2px solid grey;\n"
                                 "    border-radius: 5px;\n"
                                 "    text-align: center;\n"
                                 "}\n"
                                 "\n"
                                 "QProgressBar::chunk\n"
                                 "{\n"
                                 "    background-color: #e2352e;\n"
                                 "    width: 2.15px;\n"
                                 "    margin: 0.5px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab {\n"
                                 "    color: #b1b1b1;\n"
                                 "    border: 1px solid #444;\n"
                                 "    border-bottom-style: none;\n"
                                 "    background-color: #323232;\n"
                                 "    border-top-right-radius: 12px;\n"
                                 "    padding-left: 10px;\n"
                                 "    padding-right: 10px;\n"
                                 "    padding-top: 3px;\n"
                                 "    padding-bottom: 2px;\n"
                                 "    margin-right: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabWidget::pane {\n"
                                 "    border: 1px solid #444;\n"
                                 "    top: 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:last\n"
                                 "{\n"
                                 "    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
                                 "    border-top-right-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:first:!selected\n"
                                 "{\n"
                                 " margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
                                 "\n"
                                 "\n"
                                 "    border-top-left-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:!selected\n"
                                 "{\n"
                                 "    color: #b1b1b1;\n"
                                 "    border-bottom-style: solid;\n"
                                 "    margin-top: 3px;\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:selected\n"
                                 "{\n"
                                 "    border-top-left-radius: 3px;\n"
                                 "    border-top-right-radius: 3px;\n"
                                 "    margin-bottom: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:!selected:hover\n"
                                 "{\n"
                                 "    /*border-top: 2px solid #ffaa00;\n"
                                 "    padding-bottom: 3px;*/\n"
                                 "    border-top-left-radius: 3px;\n"
                                 "    border-top-right-radius: 3px;\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #e2352e);\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #323232;\n"
                                 "    border: 1px solid #b1b1b1;\n"
                                 "    border-radius: 6px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:checked\n"
                                 "{\n"
                                 "    background-color: qradialgradient(\n"
                                 "        cx: 0.5, cy: 0.5,\n"
                                 "        fx: 0.5, fy: 0.5,\n"
                                 "        radius: 1.0,\n"
                                 "        stop: 0.25 #e2352e,\n"
                                 "        stop: 0.3 #323232\n"
                                 "    );\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #323232;\n"
                                 "    border: 1px solid #b1b1b1;\n"
                                 "    width: 9px;\n"
                                 "    height: 9px;\n"
                                 "}\n"
                                 "QComboBox {\n"
                                 "    border: 1px solid gray;\n"
                                 "    border-radius: 3px;\n"
                                 "    padding: 1px 18px 1px 3px;\n"
                                 "    min-width: 6em;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox:editable {\n"
                                 "    background: white;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                 "     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
                                 "                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
                                 "}\n"
                                 "\n"
                                 "/* QComboBox gets the \"on\" state when the popup is open */\n"
                                 "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
                                 "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                 "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox:on { /* shift the text when the popup opens */\n"
                                 "    padding-top: 3px;\n"
                                 "    padding-left: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox {\n"
                                 "    spacing: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator {\n"
                                 "    width: 13px;\n"
                                 "    height: 13px;\n"
                                 "    border: 1px solid #e2352e;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:unchecked,\n"
                                 "QCheckBox::indicator:unchecked:hover,\n"
                                 "QGroupBox::indicator:unchecked,\n"
                                 "QGroupBox::indicator:unchecked:hover\n"
                                 "{\n"
                                 "    image: url(./icons/checkbox_unchecked.png);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QCheckBox::indicator:checked,\n"
                                 "QCheckBox::indicator:checked:hover,\n"
                                 "QGroupBox::indicator:checked,\n"
                                 "QGroupBox::indicator:checked:hover\n"
                                 "{\n"
                                 "    image: url(./icons/checkbox_checked.png);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                 "    top: 1px;\n"
                                 "    left: 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator\n"
                                 "{\n"
                                 "    border-radius: 6px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
                                 "{\n"
                                 "    border: 1px solid #e2352e;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:checked\n"
                                 "{\n"
                                 "    image:url(./icons/checkbox_checked.png);\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.captureButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.captureButton_2.setGeometry(QtCore.QRect(20, 40, 121, 71))
        self.captureButton_2.setObjectName("captureButton_2")
        self.stopbutton = QtWidgets.QPushButton(self.centralwidget)
        self.stopbutton.setGeometry(QtCore.QRect(170, 40, 121, 71))
        self.stopbutton.setObjectName("stopbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Screen Recorder"))
        self.captureButton_2.setToolTip(_translate("MainWindow",
                                                   "<html><head/><body><p><span style=\" color:#000000;\">Start Recording</span></p></body></html>"))
        self.captureButton_2.setText(_translate("MainWindow", "Record"))
        self.stopbutton.setToolTip(_translate("MainWindow",
                                              "<html><head/><body><p><span style=\" color:#000000;\">Stop Recording and Stop recording thread</span></p></body></html>"))
        self.stopbutton.setText(_translate("MainWindow", "Stop"))
        self.stopbutton.setEnabled(False)
        self.captureButton_2.clicked.connect(self.startrecord)
        self.stopbutton.clicked.connect(self.closeIt)


    def startrecord(self):
        time.sleep(1)
        import subprocess
        from subprocess import Popen, PIPE
        from subprocess import Popen, PIPE
        self.bob = subprocess.Popen(
            'ffmpeg -rtbufsize 1500M -f dshow -i video="Qt-screen-capture" -y Captured.mp4 -s dp -r 60 -vcodec libx264 -threads 0 -crf 0 -preset ultrafast ',
            stdin=PIPE, shell=True)
        self.stopbutton.setEnabled(True)
        QtWidgets.QApplication.setQuitOnLastWindowClosed(False)


    def closeIt(self):
        try:
            self.bob.stdin.write("q")
            time.sleep(1)
            self.stopbutton.setEnabled(False)
            os.system("explorer " + os.getcwd())
            os.rename('Captured.mp4', stamp + '.mp4')
            QtWidgets.QApplication.setQuitOnLastWindowClosed(False)
            print "first"
            time.sleep(3)
            try:
                killer_command = "taskkill /im ffmpeg.exe"
                process = subprocess.Popen(killer_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except OSError:
                pass

            time.sleep(2)
            tray.show()
            time.sleep(1)

        except AttributeError:
            time.sleep(1)
            self.stopbutton.setEnabled(False)
            os.system("explorer " + os.getcwd())
            os.rename('Captured.mp4', stamp + '.mp4')
            tray.show()
            QtWidgets.QApplication.setQuitOnLastWindowClosed(False)
            time.sleep(3)
            try:
                os.system("taskkill /im ffmpeg.exe")
            except OSError:
                pass
            tray.show()
            time.sleep(1)

        except WindowsError:
            new = "new"
            print "second"
            time.sleep(1)
            self.stopbutton.setEnabled(False)
            #os.system("explorer " + os.getcwd())
            #os.rename('Captured.mp4', stamp + '.mp4')
            tray.show()
            QtWidgets.QApplication.setQuitOnLastWindowClosed(False)
            time.sleep(3)
            try:
                killer_command = "taskkill /im ffmpeg.exe"
                process = subprocess.Popen(killer_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except OSError:
                pass
            tray.show()
            time.sleep(1)


class RightClickMenu(QtWidgets.QMenu):
    def __init__(self, parent=None):
        QtWidgets.QMenu.__init__(self, "Edit", parent)

        icon = QtGui.QIcon(":/ico/youtube.png")
        self.youAction = QAction(icon, "Upload to Youtupe", self,
                                      triggered=self.youb)
        self.addAction(self.youAction)

        icon = QtGui.QIcon(":/ico/qt.png")
        self.youAction = QAction(icon, "Show Gui", self,
                                triggered=self.showm)
        self.addAction(self.youAction)

        icon = QtGui.QIcon(":/ico/update.png")
        self.updateAction = QAction(icon, "Check for new version", self,
                                triggered=self.updatev)
        self.addAction(self.updateAction)

        icon = QtGui.QIcon(":/ico/github.png")
        self.devAction = QAction(icon, "developer", self,
                                triggered=self.devv)
        self.addAction(self.devAction)

    def youb(self):
        import webbrowser
        webbrowser.open('https://www.youtube.com/user/Uploads')

    def showm(self):
        MainWindow.show()

    def updatev(self):
        messageformForm.show()

    def devv(self):
        import webbrowser
        webbrowser.open('https://github.com/techbliss/Windows_Screenrecorder')


class LeftClickMenu(QtWidgets.QMenu, QSplashScreen):
    def __init__(self, parent=None):
        QtWidgets.QMenu.__init__(self, "File", parent)

        count = [1, 2, 3, 4, 5]
        _translate = QtCore.QCoreApplication.translate

        icon = QtGui.QIcon(":/ico/record.png")
        self.maximizeAction = QAction(icon, "Start record", self,
                                      triggered=self.bob)
        self.addAction(self.maximizeAction)
        #self.maximizeAction.setToolTip("Start Recording")

        icon = QtGui.QIcon(":/ico/stop.png")
        self.maximizeAction = QAction(icon, "Stop record", self,
                                      triggered=self.bobs)
        self.addAction(self.maximizeAction)

        icon = QtGui.QIcon(":/ico/1475190361_ip_adress.png")
        self.streamAction = QAction(icon, "Stream", self,
                                  triggered=self.streamit)
        self.addAction(self.streamAction)

        icon = QtGui.QIcon(":/ico/stop.png")
        self.quitAction = QAction(icon, "Quit", self,
                                  triggered=QApplication.instance().quit)
        self.addAction(self.quitAction)


    def bob(self):
        splash = QtWidgets.QSplashScreen(QtGui.QPixmap(":ico/23.png"))
        font = splash.font()
        font.setPixelSize(640)
        font.setWeight(QFont.Bold)
        splash.setFont(font)
        splash.show()
        splash.showMessage("1",
                                QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter | QtCore.Qt.WindowStaysOnTopHint,
                                QtCore.Qt.darkRed)
        splash.show()
        app.processEvents()
        time.sleep(1)
        splash.showMessage("2",
                           QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter | QtCore.Qt.WindowStaysOnTopHint,
                           QtCore.Qt.darkRed)
        splash.show()
        app.processEvents()
        time.sleep(1)
        splash.showMessage("3",
                           QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter | QtCore.Qt.WindowStaysOnTopHint,
                           QtCore.Qt.darkRed)
        splash.show()
        app.processEvents()
        time.sleep(1)
        splash.showMessage("4",
                           QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter | QtCore.Qt.WindowStaysOnTopHint,
                           QtCore.Qt.darkRed)
        splash.show()
        app.processEvents()
        time.sleep(1)
        splash.showMessage("5",
                           QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter | QtCore.Qt.WindowStaysOnTopHint,
                           QtCore.Qt.darkRed)
        splash.show()
        time.sleep(1)

        while splash.finish:
            break
        ui.startrecord()
        tray.show()
        QtWidgets.QApplication.setQuitOnLastWindowClosed(False)

    def streamit(self):
        messageformForm.show()

    def bobs(self):
        ui.closeIt()


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, parent)

        self.setIcon(QtGui.QIcon(":/ico/record.png"))
        self.right_menu = RightClickMenu()
        self.setContextMenu(self.right_menu)
        self.left_menu = LeftClickMenu()
        self.activated.connect(self.click_trap)

    def click_trap(self, value):
        if value == self.Trigger:  # left click!
            self.left_menu.exec_(QtGui.QCursor.pos())

    def welcome(self):
        self.showMessage("Hello", "I should be aware of both buttons")

    def show(self):
        QtWidgets.QSystemTrayIcon.show(self)
        #QtCore.QTimer.singleShot(0, self.welcome)

    def noticev(self):
        self.welcome()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Systray",
                "I couldn't detect any system tray on this system.")
        tray = SystemTrayIcon()
        tray.show()
        QApplication.setQuitOnLastWindowClosed(False)

    QApplication.setQuitOnLastWindowClosed(False)
    tray = SystemTrayIcon()
    tray.show()
    QtWidgets.QApplication.setQuitOnLastWindowClosed(False)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    messageformForm = QtWidgets.QWidget()
    ui2 = Ui_messageformForm()
    ui2.setupUi1(messageformForm)
    Form = QtWidgets.QWidget()
    #MainWindow.show()
    sys.exit(app.exec_())

