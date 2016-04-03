try:
    import configparser
except ImportError:
    import ConfigParser as configparser


class Config(object):
    """Handles loading of the configuration file for the primary game."""
    def __init__(self, file):
        self.config = configparser.ConfigParser()
        self.config.read(file)

        self.resolution_x = self.config.getint("display", "resolution_x")
        self.resolution_y = self.config.getint("display", "resolution_y")
        self.resolution = (self.resolution_x, self.resolution_y)
        self.fullscreen = self.config.getboolean("display", "fullscreen")

        self.fps = self.config.getint("display", "fps")

        self.debug_logging = self.config.getint("logging", "debug_logging")
        self.debug_level = str(self.config.get("logging", "debug_level")).lower()
        self.loggers = self.config.get("logging", "loggers")
        self.loggers = self.loggers.replace(" ", "").split(",")
