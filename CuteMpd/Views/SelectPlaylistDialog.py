from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QAbstractTableModel, Qt
import UI.SelectPlayListDialogUI
from mpd import MPDClient
from Utils.ServiceLocator import ServiceLocator, ServiceNames
import Utils.Client


class PlayListModel(QAbstractTableModel):
    def __init__(self, data, parent = None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data
        pass

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return 1

    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = index.row()
            value = self._data[row]['playlist']
            return value



class SelectPlaylistDialog(QtGui.QDialog, UI.SelectPlayListDialogUI.Ui_Dialog):
    """description of class"""
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self._config = ServiceLocator.getGlobalServiceInstance(ServiceNames.Configuration)
        self.PlayListsView.clicked.connect(self.onPlayListViewClicked)
        self.selectedList = None
        self.playListModel = PlayListModel(self.loadPlaylists())
        self.PlayListsView.setModel(self.playListModel)
        pass

    def getClient(self):
        client = Utils.Client.connectClient(self._config)
        return client


    def loadPlaylists(self):
        client = self.getClient()
        result = client.listplaylists()
        client.disconnect()
        return result

    def onPlayListViewClicked(self, item):
        self.selectedList = item.data()
        self.accept()
        pass

    def changePlaylist(self, playListName):
        client = self.getClient()
        client.clear()
        client.load(playListName)
        client.play()
        client.disconnect
        pass





