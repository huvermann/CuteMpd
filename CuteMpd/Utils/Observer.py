from mpd import MPDClient
from PyQt4.QtCore import QThread, SIGNAL
from Utils.ServiceLocator import ServiceLocator, ServiceNames

class ObserverSignals():
    PlaylistChanged = "PlaylistChanged"
    PlayerChanged = "PlayerChanged"
    MixerChanged = "MIXERCHANGED"
    ConnectionError = 'CONNECTIONERROR'


class Observer(QThread):
    """MPD Observer thread."""
    def __init__(self):
        self._config = ServiceLocator.getGlobalServiceInstance(ServiceNames.Configuration)
        self.client = MPDClient()

        return QThread.__init__(self)

    def __del__(self):
        self.wait()

    def mpdConnect(self):
        self.client.timeout = 10
        self.client.idletimeout = None
        self.client.connect(self._config.mpdserver, self._config.mpdport)
        if len(self._config.mpdpassword) > 0:
            self.client.password(self._config.mpdpassword)
        self.client.update()

    def run(self):
        try:
            self.mpdConnect()
    
            while True:
                info = self.client.idle()
                print("info:{0}".format(info))
                if 'update' in info:
                    # Update all
                    self.updatePlaylist()
                    self.updatePlayer()
                    self.updateMixer()

                if 'playlist' in info:
                    self.updatePlaylist()
                if 'player' in info:
                    self.updatePlayer()
                    self.updateMixer()
                if 'mixer' in info:
                    self.updateMixer()
                self.sleep(2)
        except:
             self.emit(SIGNAL(ObserverSignals.ConnectionError))
            

        pass

    def updatePlaylist(self):
        playlist = self.client.playlistinfo()
        self.emit(SIGNAL(ObserverSignals.PlaylistChanged), playlist)
        pass
    def updateMixer(self):
        status = self.client.status()
        self.emit(SIGNAL(ObserverSignals.MixerChanged), status)
        pass

    def updatePlayer(self):
        currentSong = self.client.currentsong()
        self.emit(SIGNAL(ObserverSignals.PlayerChanged), currentSong)
        pass









