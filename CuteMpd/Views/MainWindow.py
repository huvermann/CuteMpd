import sys
from PyQt4 import QtGui, QtCore
import UI.MainWindowUI
from Utils.ServiceLocator import ServiceLocator, ServiceNames
from Viewmodels.MpdViewModel import MpdViewModel
from Views.SelectPlaylistDialog import SelectPlaylistDialog
from Views.SettingsDialog import SettingsDialog
import Utils.Client

class MainWindow(QtGui.QMainWindow, UI.MainWindowUI.Ui_MainWindow):
    """The main window class."""
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.currentSong = None
        self.currentPlaylist = None
        self._volume = 0

        self.config = ServiceLocator.getGlobalServiceInstance(ServiceNames.Configuration)
        self.mpdViewModel = MpdViewModel(self)
        ServiceLocator.registerGlobalService(ServiceNames.MpdViewModel, self.mpdViewModel)
        self.mpdViewModel.connectPlayListChanged(self, self.songListChanged)
        self.mpdViewModel.connectSongChanged(self, self.songChanged)
        self.mpdViewModel.connectMixerChanged(self, self.mixerHasChanged)
        self.mpdViewModel.connectObserver()
        self.connectUI()

    def connectUI(self):
        """Connects the UI elements."""
        self.btnAlben.clicked.connect(self.onBtnAlbenClicked)
        self.btnRadio.clicked.connect(self.onBtnRadioClicked)
        self.btnSettings.clicked.connect(self.onBtnSettingsClicked)
        self.btnSwitchOff.clicked.connect(self.onBtnSwitchoffClicked)
        self.btnPrev.clicked.connect(self.onBtnPrevClicked)
        self.btnPlay.clicked.connect(self.onBtnPlayClicked)
        self.btnStop.clicked.connect(self.onBtnStopClicked)
        self.btnNext.clicked.connect(self.onBtnNextClicked)
        self.btnVolPlus.clicked.connect(self.onBtnVolPlusClicked)
        self.btnVolMinus.clicked.connect(self.onBtnVolMinusClicked)

    def connectClient(self):
        result = Utils.Client.connectClient(self.config)
        return result


    def songListChanged(self, songs):
        """Songlist has changed."""
        self.mpdViewModel.updateSongs(songs)
        print("Songliste geändert")
        pass
    def songChanged(self, current):
        """Current song has changed."""
        print("Song wurde geändert.")
        self.currentSong = current
        self.textBrowser.setText(self.songDataToHtml(current))
        pass

    def mixerHasChanged(self, mixer):
        if 'volume' in mixer:
            self._volume = int(mixer['volume'])
            self.lcdNumber.display(self._volume)
        pass


    def onBtnAlbenClicked(self):
        """Button clicked handler."""
        dlg = SelectPlaylistDialog(self)
        if sys.platform == 'win32':
            dlg.show()
        else:
            dlg.showFullScreen()
        if dlg.exec_():
            dlg.changePlaylist(dlg.selectedList)
        pass

    def onBtnRadioClicked(self):
        """Button clicked handler."""
        print("Button clicked.")
        pass

    def onBtnSettingsClicked(self):
        """Button clicked handler."""
        dlg = SettingsDialog(self)
        if sys.platform == 'win32':
            dlg.show()
        else:
            dlg.showFullScreen()
        if dlg.exec_():
            dlg.saveChanges()
        pass

    def onBtnSwitchoffClicked(self):
        """Button clicked handler."""
        print("Button clicked.")
        pass

    def onBtnPrevClicked(self):
        """Button clicked handler."""
        client = self.connectClient()
        client.previous()
        client.close()
        pass
    def onBtnPlayClicked(self):
        """Button clicked handler."""
        client = self.connectClient()
        client.play()
        client.close()
        pass
    def onBtnStopClicked(self):
        """Button clicked handler."""
        client = self.connectClient()
        client.stop()
        client.close()
        pass

    def onBtnNextClicked(self):
        """Button clicked handler."""
        client = self.connectClient()
        client.next()
        client.close()
        pass

    def onBtnVolPlusClicked(self):
        if self.volume < 100:
            self.volume += 5
        pass
    def onBtnVolMinusClicked(self):
        """Button clicked handler."""
        if self.volume > 0:
            self.volume -= 5
        pass

    #Utilities
    def songDataToHtml(self, songData):
        filter = ["title", "artist", "album", "name"]
        result = ""
        for data in songData:
            if data in filter:
                result += "<p>{0}:</p>".format(data)
                result += "<h2>{0}</h2>".format(songData[data])
        return result

    #Properties
    @property
    def pos(self):
        result = 0
        if self.currentSong:
            if 'pos' in self.currentSong:
                result = int(self.currentSong['pos'])
        return result

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        if self._volume != value:
            self._volume = value
            client = self.connectClient()
            client.setvol(self._volume)
            client.close()

















