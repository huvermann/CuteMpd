# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectPlayListDialog.ui'
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
        self.PlayListsView = QtGui.QListView(Dialog)
        self.PlayListsView.setGeometry(QtCore.QRect(0, 54, 461, 261))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PlayListsView.setFont(font)
        self.PlayListsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PlayListsView.setObjectName(_fromUtf8("PlayListsView"))
        self.btnBack = QtGui.QPushButton(Dialog)
        self.btnBack.setGeometry(QtCore.QRect(4, 4, 200, 42))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnBack.setFont(font)
        self.btnBack.setStyleSheet(_fromUtf8("QPushButton {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #FF0000);\n"
"min-width: 80px;\n"
"}\n"
"\n"
" QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Back-button")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon)
        self.btnBack.setIconSize(QtCore.QSize(48, 48))
        self.btnBack.setObjectName(_fromUtf8("btnBack"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btnBack, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.btnBack.setText(_translate("Dialog", "Zurück", None))

import resources_rc
