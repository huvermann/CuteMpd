import sys
from PyQt4 import QtGui, QtCore
from Viewmodels.MpdViewModel import MpdViewModel
import UI.CuteMpdMainWindowUI
from Utils.ServiceLocator import ServiceLocator, ServiceNames
from Views.SongDetails import SongDetails
from Views.SelectPlaylistDialog import SelectPlaylistDialog
from Views.SettingsDialog import SettingsDialog
from PyQt4 import QtSvg 

class CuteMpdMainWindow(QtGui.QMainWindow, UI.CuteMpdMainWindowUI.Ui_MainWindow):
    """description of class"""
    def __init__(self, parent=None):
        super(CuteMpdMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.mpdViewModel = MpdViewModel(self)
        ServiceLocator.registerGlobalService(ServiceNames.MpdViewModel, self.mpdViewModel)
        self.connectUI()
        self._currentIndex = None
        pass

    def closeEvent(self, event):
        """Disconnect the client."""
        return super().closeEvent(event)

    def connectUI(self):
        """Connect the UI elements."""
        self.btnLoadLists.clicked.connect(self.onBtnLoadListsClicked)
        self.btnExit.clicked.connect(self.onBtnExitClicked)
        self.btnSettings.clicked.connect(self.onBtnSettingsClicked)
        self.mpdViewModel.connectPlayListChanged(self, self.songListChanged)
        self.mpdViewModel.connectSongChanged(self, self.songChanged)
        self.mpdViewModel.connectConnectionError(self, self.connectionError)
        self.tableView.setModel(self.mpdViewModel.songList)
        self.mpdViewModel.connectObserver()
        self.tableView.setColumnWidth(0, 300)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.clicked.connect(self.tableViewClicked)
        pass

    def connectionError(self):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setWindowTitle('Error')
        msg.setInformativeText('Connection Error!')
        msg.setDetailedText('Connection Error!')
        result = msg.exec_()
        pass





    def songListChanged(self, songs):
        self.mpdViewModel.updateSongs(songs)
        pass

    def songChanged(self, current):
        """Current song has changed, update selection."""
        if "pos" in current:
            self._currentIndex = int(current["pos"])
            self.tableView.selectRow(self._currentIndex)
        pass

    def tableViewClicked(self, item):
        row = item.row()
        data = item.data()
        print(row, data)
        changeSong = True
        if row == self._currentIndex:
            changeSong = False
            
        dlg = SongDetails(row, changeSong=changeSong, parent= self)
        if sys.platform == 'win32':
            dlg.show()
        else:
            dlg.showFullScreen()
        dlg.exec_()




    def onBtnLoadListsClicked(self):
        dlg = SelectPlaylistDialog(self)
        if sys.platform == 'win32':
            dlg.show()
        else:
            dlg.showFullScreen()
        if dlg.exec_():
            dlg.changePlaylist(dlg.selectedList)
        pass

    def onBtnExitClicked(self):
        QtCore.QCoreApplication.instance().quit()
        pass

    def onBtnSettingsClicked(self):
        dlg = SettingsDialog(self)
        if sys.platform == 'win32':
            dlg.show()
        else:
            dlg.showFullScreen()
        if dlg.exec_():
            dlg.saveChanges()
        pass





