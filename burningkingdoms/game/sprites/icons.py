import os
import pygame


class Icon(pygame.sprite.Sprite):
    _icon_width = 16
    _icon_height = 16
    sprite_col = 0
    sprite_row = 0

    def __init__(self, scene, scale=1):
        super(Icon, self).__init__()
        self.scene = scene
        self.scale = scale
        self.image = pygame.Surface((self.scale * self._icon_width,
            self.scale * self._icon_height))
        self.icon_sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), 'icons',
            'rpgicons.png'))
        self.icon_sprite = pygame.transform.scale(self.icon_sprite,
            (self.scale * self.icon_sprite.get_rect().width,
            self.scale * self.icon_sprite.get_rect().height)
        )
        self.image.blit(self.icon_sprite, (0, 0), (
            self.sprite_col * self._icon_width * self.scale,
            self.sprite_row * self._icon_height * self.scale,
            self.scale * self._icon_width,
            self.scale * self._icon_height)
        )
        self.rect = self.image.get_rect()


class HeartIcon(Icon):
    pass


class GoldStackIcon(Icon):
    sprite_col = 1


class PouchIcon(Icon):
    sprite_col = 2


class MagicBookIcon(Icon):
    sprite_col = 3


class MapIcon(Icon):
    sprite_col = 4


class MenuCursor(Icon):
    sprite_col = 5

    def update(self):
        active_menu_rect = self.scene.menu_rects[self.scene.active_menu_rect]
        self.rect.right = active_menu_rect.left
        self.rect.centery = active_menu_rect.centery


class StatBarsIcon(Icon):
    sprite_col = 0
    sprite_row = 1


class LevelUpIcon(Icon):
    sprite_col = 1
    sprite_row = 1


class MagicIcon(Icon):
    sprite_col = 2
    sprite_row = 1


class FeatherIcon(Icon):
    sprite_col = 3
    sprite_row = 1


class DicesIcon(Icon):
    sprite_col = 4
    sprite_row = 1


class SwordAndShieldIcon(Icon):
    sprite_col = 5
    sprite_row = 1


class CharIcon(Icon):
    sprite_row = 2
