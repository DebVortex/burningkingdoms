import pygame
from pygame import locals as key

from burningkingdoms.game.scenes.core import Scene
from burningkingdoms.game.scenes.maps.test import TestScene
from burningkingdoms.game.sprites.icons import MenuCursor


class StartScreen(Scene):

    def __init__(self, fill, game, screen):
        self.key_events = {
            key.K_UP: self._handle_key_up,
            key.K_DOWN: self._handle_key_down,
            key.K_RETURN: self._handle_key_return
        }
        super(StartScreen, self).__init__(fill, game, screen)
        title_font = pygame.font.SysFont("Arial", 108)
        menu_font = pygame.font.SysFont("Arial", 36)

        self.title_text = title_font.render("Burning Kingdoms", 1, (255, 255, 255))
        self.single_player_text = menu_font.render("Single Player", 1, (255, 255, 255))
        self.multi_player_text = menu_font.render("Multi Player", 1, (255, 255, 255))
        self.exit_text = menu_font.render("Exit", 1, (255, 255, 255))

        self.surface_center_x = self.screen.get_rect().centerx
        self.surface_center_y = self.screen.get_rect().centery

        self.title_rect = self.title_text.get_rect()
        self.title_rect.centerx = self.surface_center_x
        self.title_rect.centery = self.surface_center_y * 0.5

        self.single_player_rect = self.single_player_text.get_rect()
        self.single_player_rect.centerx = self.surface_center_x
        self.single_player_rect.centery = self.surface_center_y * 1.5 - self.single_player_rect.height

        self.multi_player_rect = self.multi_player_text.get_rect()
        self.multi_player_rect.centerx = self.surface_center_x
        self.multi_player_rect.centery = self.surface_center_y * 1.5

        self.exit_rect = self.exit_text.get_rect()
        self.exit_rect.centerx = self.surface_center_x
        self.exit_rect.centery = self.surface_center_y * 1.5 + self.exit_rect.height

        self.menu_rects = [self.single_player_rect, self.multi_player_rect, self.exit_rect]
        self.active_menu_rect = 0
        self.cursor = MenuCursor(self, scale=3)
        self.sprites.add(self.cursor)

    def render(self):
        surface = pygame.Surface(self.screen.get_size())
        surface.fill(self.fill)

        surface.blit(self.title_text, self.title_rect)
        surface.blit(self.single_player_text, self.single_player_rect)
        surface.blit(self.multi_player_text, self.multi_player_rect)
        surface.blit(self.exit_text, self.exit_rect)

        self.sprites.draw(surface)
        return surface

    def update(self):
        self.sprites.update()

    def handle_event(self, event):
        if event.key in self.key_events:
            self.key_events[event.key]()
        if self != self.game.active_scene:
            del self

    def _handle_key_up(self):
        self.active_menu_rect -= 1
        if self.active_menu_rect < 0:
            self.active_menu_rect = 0
        else:
            # TODO: Play sound...
            pass

    def _handle_key_down(self):
        self.active_menu_rect += 1
        if self.active_menu_rect > 2:
            self.active_menu_rect = 2
        else:
            # TODO: Play sound...
            pass

    def _handle_key_return(self):
        if self.active_menu_rect == 0:
            self.game.active_scene = TestScene((0, 0, 0), self.game, self.screen)
        elif self.active_menu_rect == 1:
            pass
        elif self.active_menu_rect == 2:
            self.game.running = False
