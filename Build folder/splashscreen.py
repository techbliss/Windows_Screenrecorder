from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QProcess
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QSplashScreen
import os
import sys
import time
from time import sleep
import icons
import rec_main

count = [1,2,3,4,5]

def Splash(self):
    app = QtWidgets.QApplication(sys.argv)
    QProcess.startDetached(app.processEvents())
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap(":ico/23.png"))

    font = QFont()
    font.setPixelSize(72)
    font.setWeight(QFont.Bold)
    font.setFixedPitch(True)
    splash.setFont(font)

    #splash.setFont(font)
    #splash.showMessage(str(count[0]), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white )
    splash.show()
    for i in range(0, 6):
        time.sleep(1.5)
        splash = QtWidgets.QSplashScreen(QtGui.QPixmap(":ico/23.png"))

        if i <= 4.0:
            splash.showMessage(str(count[i]), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter | QtCore.Qt.AlignHCenter| QtCore.Qt.WindowStaysOnTopHint, QtCore.Qt.darkRed)
            font = splash.font()
            font.setPixelSize(640)
            font.setWeight(QFont.Bold)
            splash.setFont(font)
            splash.show()
        else:
            QProcess.startDetached(app.processEvents())
        splash.show()
    while splash.finish:
        break
    print "ok"
    rec_main.Ui_MainWindow.show()



if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Splash(([0]))
    app.exec_()
    Form = QtWidgets.QWidget()


