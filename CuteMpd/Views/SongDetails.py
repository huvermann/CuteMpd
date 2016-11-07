from PyQt4 import QtGui, QtCore
import UI.SongDetailsUI
from Utils.ServiceLocator import ServiceLocator, ServiceNames
from mpd import MPDClient

class SongDetails(QtGui.QDialog, UI.SongDetailsUI.Ui_Dialog):
    """Displays song details."""
    def __init__(self, row, changeSong=True, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self._volume = 0
        self.btnBack.clicked.connect(self.onBtnBackClicked)
        self.btnPlay.clicked.connect(self.onBtnPlayClicked)
        self.btnStop.clicked.connect(self.onBtnStopClicked)
        self.btnNext.clicked.connect(self.onBtnNextClicked)
        self.btnPrev.clicked.connect(self.onBtnPrevClicked)
        self.mpdViewModel = ServiceLocator.getGlobalServiceInstance(ServiceNames.MpdViewModel)
        self.config = ServiceLocator.getGlobalServiceInstance(ServiceNames.Configuration)
        self.mpdViewModel.connectSongChanged(self, self.songHasChanged)
        self.mpdViewModel.connectMixerChanged(self, self.mixerHasChanged)
        #self.VolumeSlider.sliderReleased.connect(self.onVolumeSliderReleased)
        self.btnVolPlus.clicked.connect(self.onBtnVolPlusClicked)
        self.btnVolMinus.clicked.connect(self.onBtnVolMinusClicked)


        self.position = row
        if changeSong:
            self.playSong(self.position)
        else:
            self.requestUpdate()
        pass

    def onBtnVolPlusClicked(self):
        if self.volume < 95:
            self.volume += 5
        pass
    def onBtnVolMinusClicked(self):
        if self.volume > 5:
            self.volume -= 5
        pass

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



    def playSong(self, row):
        client = self.connectClient()
        client.play(row)
        client.close()

        pass

    def requestUpdate(self):
        client = self.connectClient()
        current = client.currentsong()
        self.songHasChanged(current)
        mixer = client.status()
        self.mixerHasChanged(mixer)
        client.close()


    def connectClient(self):
        client = MPDClient()
        
        client.timeout = 10
        client.idletimeout = None
        try:
            client.connect(self.config.mpdserver, self.config.mpdport)
            if len(self.config.mpdpassword) > 0:
                self.client.password(self._config.mpdpassword)
        except Exception as e:
            print(e)

        return client

       

    def songHasChanged(self, currentSong):
        if "pos" in currentSong:
            self.position = int(currentSong["pos"])

        if "title" in currentSong:
            self.lblSong.setText( currentSong["title"])
        elif "name" in currentSong:
            self.lblSong.setText(currentSong["name"])
        if 'artist' in currentSong:
            self.lblInterpret.setText(currentSong["artist"])
        if 'album' in currentSong:
            self.lblAlbum.setText(currentSong["album"])
        else:
            self.lblAlbum.setText("")

        pass

    def mixerHasChanged(self, mixer):
        if 'volume' in mixer:
            vol = int(mixer['volume'])
            #self.VolumeSlider.setValue(vol)
            self.lcdNumber.display(vol)
            self._volume = vol

    #def onVolumeSliderReleased(self):
    #    vol = self.VolumeSlider.value()
    #    self.volume = vol


    def onBtnBackClicked(self):
        self.accept()

    def onBtnPlayClicked(self):
        if not self.position == None:
            client = self.connectClient()
            client.play()
            client.close()

    def onBtnStopClicked(self):
        client = self.connectClient()
        client.stop()
        client.close()
        pass

    def onBtnNextClicked(self):
        client = self.connectClient()
        client.next()
        client.close()

    def onBtnPrevClicked(self):
        client = self.connectClient()
        client.previous()
        client.close()






