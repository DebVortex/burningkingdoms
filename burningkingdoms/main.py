import os

from game.core import Game
from game.config import Config


def main():
    config_file = os.path.join(os.path.dirname(__file__), 'burningkingdoms.cfg')
    config = Config(config_file)
    game = Game(config)
    game.main_loop()


if __name__ == '__main__':
    main()
