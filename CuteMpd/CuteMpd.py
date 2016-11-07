#!/usr/bin/python3
import sys
from PyQt4 import QtGui, QtCore
import resources_rc
from Views.CuteMpdMainWindow import CuteMpdMainWindow
from Utils.ServiceLocator import ServiceLocator, ServiceNames
from Utils.Configuration import Configuration
from Views.MainWindow import MainWindow


if __name__ == "__main__":
    ServiceLocator.registerGlobalService(ServiceNames.Configuration, Configuration())
    app = QtGui.QApplication(sys.argv)

    file = QtCore.QFile(':/styles/stylesheet')
    if file.open(QtCore.QFile.ReadOnly):
        styleSheet = str(file.readAll(), 'utf-8')
        app.setStyleSheet(styleSheet)
        file.close()
    
    gui = MainWindow()
    #gui = CuteMpdMainWindow()
    if sys.platform == 'win32':
        gui.show()
    else:
        gui.showFullScreen()
    sys.exit(app.exec_())
