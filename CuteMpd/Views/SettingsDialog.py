from PyQt4 import QtGui, QtCore
import UI.SettingsUI
from Utils.ServiceLocator import ServiceLocator, ServiceNames

class SettingsDialog(QtGui.QDialog, UI.SettingsUI.Ui_Dialog):
    """The settings view implementation."""
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.configuration = ServiceLocator.getGlobalServiceInstance(ServiceNames.Configuration)
        self.connectButtons()
        self.editHostname.setText(self.configuration.mpdserver)
        self.EditPassword.setText(self.configuration.mpdpassword)
        self.editPort.setText(self.configuration.mpdport)

        pass

    def saveChanges(self):
        self.configuration.mpdserver = self.editHostname.text()

        self.configuration.saveConfiguration()
        pass

    def connectButtons(self):

        pass


    def closeEvent(self, event):
        """save the configuration"""
        pass

    #def accepted(*args, **kwargs):
    #    print(args)
    #    return super().accepted(**kwargs)



