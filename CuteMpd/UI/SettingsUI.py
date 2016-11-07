# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(480, 320)
        Dialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 280, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 461, 251))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.ServerConfigTab = QtGui.QWidget()
        self.ServerConfigTab.setObjectName(_fromUtf8("ServerConfigTab"))
        self.layoutWidget = QtGui.QWidget(self.ServerConfigTab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 191))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.editHostname = QtGui.QLineEdit(self.layoutWidget)
        self.editHostname.setEchoMode(QtGui.QLineEdit.Normal)
        self.editHostname.setObjectName(_fromUtf8("editHostname"))
        self.verticalLayout.addWidget(self.editHostname)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.EditPassword = QtGui.QLineEdit(self.layoutWidget)
        self.EditPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.EditPassword.setObjectName(_fromUtf8("EditPassword"))
        self.verticalLayout.addWidget(self.EditPassword)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.editPort = QtGui.QLineEdit(self.layoutWidget)
        self.editPort.setObjectName(_fromUtf8("editPort"))
        self.verticalLayout.addWidget(self.editPort)
        self.tabWidget.addTab(self.ServerConfigTab, _fromUtf8(""))
        self.toolsTab = QtGui.QWidget()
        self.toolsTab.setObjectName(_fromUtf8("toolsTab"))
        self.btnRefreshPlaylist = QtGui.QPushButton(self.toolsTab)
        self.btnRefreshPlaylist.setGeometry(QtCore.QRect(10, 10, 251, 34))
        self.btnRefreshPlaylist.setObjectName(_fromUtf8("btnRefreshPlaylist"))
        self.tabWidget.addTab(self.toolsTab, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Mpd Hostname:", None))
        self.label_2.setText(_translate("Dialog", "Password:", None))
        self.label_3.setText(_translate("Dialog", "Port", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ServerConfigTab), _translate("Dialog", "MPD Server", None))
        self.btnRefreshPlaylist.setText(_translate("Dialog", "Refresh Playlists", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.toolsTab), _translate("Dialog", "Tools", None))

