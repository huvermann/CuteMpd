# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SongDetails.ui'
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
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 50, 451, 281))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblSong1 = QtGui.QLabel(self.layoutWidget)
        self.lblSong1.setObjectName(_fromUtf8("lblSong1"))
        self.verticalLayout.addWidget(self.lblSong1)
        self.lblSong = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        font.setPointSize(14)
        self.lblSong.setFont(font)
        self.lblSong.setStyleSheet(_fromUtf8(""))
        self.lblSong.setFrameShape(QtGui.QFrame.Box)
        self.lblSong.setFrameShadow(QtGui.QFrame.Raised)
        self.lblSong.setLineWidth(2)
        self.lblSong.setObjectName(_fromUtf8("lblSong"))
        self.verticalLayout.addWidget(self.lblSong)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lblInterpret = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        font.setPointSize(14)
        self.lblInterpret.setFont(font)
        self.lblInterpret.setObjectName(_fromUtf8("lblInterpret"))
        self.verticalLayout.addWidget(self.lblInterpret)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lblAlbum = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        font.setPointSize(14)
        self.lblAlbum.setFont(font)
        self.lblAlbum.setObjectName(_fromUtf8("lblAlbum"))
        self.verticalLayout.addWidget(self.lblAlbum)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnPrev = QtGui.QPushButton(self.layoutWidget)
        self.btnPrev.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnPrev.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Backward")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrev.setIcon(icon)
        self.btnPrev.setIconSize(QtCore.QSize(48, 48))
        self.btnPrev.setObjectName(_fromUtf8("btnPrev"))
        self.horizontalLayout.addWidget(self.btnPrev)
        self.btnPlay = QtGui.QPushButton(self.layoutWidget)
        self.btnPlay.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnPlay.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Go")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlay.setIcon(icon1)
        self.btnPlay.setIconSize(QtCore.QSize(48, 48))
        self.btnPlay.setObjectName(_fromUtf8("btnPlay"))
        self.horizontalLayout.addWidget(self.btnPlay)
        self.btnStop = QtGui.QPushButton(self.layoutWidget)
        self.btnStop.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnStop.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Stop button")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon2)
        self.btnStop.setIconSize(QtCore.QSize(48, 48))
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.horizontalLayout.addWidget(self.btnStop)
        self.btnNext = QtGui.QPushButton(self.layoutWidget)
        self.btnNext.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnNext.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Forward")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNext.setIcon(icon3)
        self.btnNext.setIconSize(QtCore.QSize(48, 48))
        self.btnNext.setObjectName(_fromUtf8("btnNext"))
        self.horizontalLayout.addWidget(self.btnNext)
        self.btnVolPlus = QtGui.QPushButton(self.layoutWidget)
        self.btnVolPlus.setMaximumSize(QtCore.QSize(60, 60))
        self.btnVolPlus.setObjectName(_fromUtf8("btnVolPlus"))
        self.horizontalLayout.addWidget(self.btnVolPlus)
        self.lcdNumber = QtGui.QLCDNumber(self.layoutWidget)
        self.lcdNumber.setMaximumSize(QtCore.QSize(60, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        self.lcdNumber.setPalette(palette)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.btnVolMinus = QtGui.QPushButton(self.layoutWidget)
        self.btnVolMinus.setMaximumSize(QtCore.QSize(60, 60))
        self.btnVolMinus.setObjectName(_fromUtf8("btnVolMinus"))
        self.horizontalLayout.addWidget(self.btnVolMinus)
        self.verticalLayout.addLayout(self.horizontalLayout)
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
"}"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/Back-button")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon4)
        self.btnBack.setIconSize(QtCore.QSize(48, 48))
        self.btnBack.setObjectName(_fromUtf8("btnBack"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblSong1.setText(_translate("Dialog", "Title:", None))
        self.lblSong.setText(_translate("Dialog", "TextLabel", None))
        self.label.setText(_translate("Dialog", "Interpret", None))
        self.lblInterpret.setText(_translate("Dialog", "TextLabel", None))
        self.label_2.setText(_translate("Dialog", "Album", None))
        self.lblAlbum.setText(_translate("Dialog", "TextLabel", None))
        self.btnVolPlus.setText(_translate("Dialog", "VOL+", None))
        self.btnVolMinus.setText(_translate("Dialog", "VOL-", None))
        self.btnBack.setText(_translate("Dialog", "Zurück", None))

import resources_rc
