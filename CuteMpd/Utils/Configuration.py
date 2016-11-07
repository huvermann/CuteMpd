import configparser

class Configuration(object):
    """Loads the configuration file."""
    def __init__(self):
        self.configFileName = 'cutempdconfig.ini'
        self._configParser = configparser.ConfigParser()
        self._loadConfiguration()
        pass

    def _loadConfiguration(self):
        """Loads the configuration from file."""
        self._configParser.read(self.configFileName)
        pass

    def saveConfiguration(self):
        """Saves the configuration to file."""
        with open(self.configFileName, 'w') as configfile:
            self._configParser.write(configfile)

        pass

    def _isConfigurationAttribute(self, name, value):
        result = False
        if self._configParser != None:
            section = self._configParser['Main']
            if section != None:
                section[name] = value
                result = True
        return result

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        else:
            if '_configParser' in self.__dict__:
                conf = self.__dict__['_configParser']
                if name in conf['Main']:
                    return conf['Main'][name]

    def __setattr__(self, name, value):
        if not self._isConfigurationAttribute(name, value):
            super(Configuration, self).__setattr__(name, value)

        






