class Scene(object):
    def __init__(self, fill, game, screen):
        self.fill = fill
        self.game = game
        self.screen = screen

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_event(self, event):
        raise NotImplementedError
