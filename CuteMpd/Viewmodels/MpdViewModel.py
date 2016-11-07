from mpd import MPDClient
from PyQt4.QtCore import SIGNAL, Qt, QVariant, pyqtSlot
from Utils.Observer import Observer, ObserverSignals
from PyQt4.QtCore import QAbstractTableModel, Qt
from PyQt4 import QtCore
from PyQt4.QtGui import QStandardItemModel


class SongListModel(QAbstractTableModel):
    def __init__(self, data, parent = None):
        QAbstractTableModel.__init__(self, parent)
        self.columns = ['title', 'artist']
        self._data = data
        pass

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return 2

    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self._data[row][self.getColumnName(column, self._data[row])]
            return value

    def getColumnName(self, column, rowData):
        result = 'id'
        if column == 0:
            if "title" in rowData:
                result = 'title'
            elif "name" in rowData:
                result = 'name'
        elif column == 1:
            if 'artist' in rowData:
                result = 'artist'
            elif 'file' in rowData:
                result = 'file'
        return result

    def updateSongs(self, newData):
        self._data = newData
        self.reset()



class PlayListModel(QStandardItemModel):
    def __init__(self, parent = None):
        super().__init__(parent)


class MpdViewModel(object):
    """description of class"""
    def __init__(self, parent):
        #self._client = MPDClient()
        self._observer = Observer()
        self._songListModel = SongListModel([])
        self._playlistModel = PlayListModel()
        pass

    def connectPlayListChanged(self, form, callback):
        form.connect(self._observer, SIGNAL(ObserverSignals.PlaylistChanged), callback)
        pass

    def connectSongChanged(self, form, callback):
        form.connect(self._observer, SIGNAL(ObserverSignals.PlayerChanged), callback)

    def connectMixerChanged(self, form, callback):
        form.connect(self._observer, SIGNAL(ObserverSignals.MixerChanged), callback)
        pass

    def connectConnectionError(self, form, callback):
        form.connect(self._observer, SIGNAL(ObserverSignals.ConnectionError), callback)
        pass


    def connectObserver(self):
        self._observer.start()

    def updateSongs(self, songs):
        self._songListModel.updateSongs(songs)
        pass

    @property
    def songList(self):
        return self._songListModel

    @property
    def playLists(self):
        return self._playlistModel


