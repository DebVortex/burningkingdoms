try:
    import configparser
except ImportError:
    import ConfigParser as configparser


class Config(object):
    """Handles loading of the configuration file for the primary game."""
    def __init__(self, file):
        self.config = configparser.ConfigParser()
        self.config.read(file)

        self.resolution_x = self.config.get("display", "resolution_x")
        self.resolution_y = self.config.get("display", "resolution_y")
        self.resolution = (int(self.resolution_x), int(self.resolution_y))

        self.fps = int(self.config.get("display", "fps"))

        self.debug_logging = self.config.get("logging", "debug_logging")
        self.debug_level = str(self.config.get("logging", "debug_level")).lower()
        self.loggers = self.config.get("logging", "loggers")
        self.loggers = self.loggers.replace(" ", "").split(",")
