import pygame

from pygame import locals as key

from burningkingdoms.game.scenes.menu.start_screen import StartScreen


class Game(object):
    def __init__(self, config):
        self.config = config
        pygame.init()
        self.screen = pygame.display.set_mode(config.resolution)
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
        self.running = False
        self.clock = pygame.time.Clock()  # to track FPS
        self.fps = config.fps
        self.scenes = []
        self.active_scene = None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == key.QUIT:
                self.running = False
            if event.type == key.KEYUP:
                self.active_scene.handle_event(event)

    #enter the main loop, possibly setting max FPS
    def main_loop(self):
        self.running = True
        fill = (0, 0, 0)
        self.active_scene = StartScreen(fill, self, self.screen)
        while self.running:
            pygame.display.set_caption("FPS: {fps}".format(fps=self.clock.get_fps()))
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)

    def update(self):
        self.active_scene.update()

    def render(self):
        self.screen.blit(self.active_scene.render(), (0, 0))
        pygame.display.flip()
