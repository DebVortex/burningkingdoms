from burningkingdoms.game.scenes.core import Scene

import pygame
from pygame import locals as key

from burningkingdoms.game.sprites.char import CharacterSprite


class TestScene(Scene):

    def __init__(self, fill, game, screen):
        self.key_events = {
            key.K_ESCAPE: self._handle_key_escape,
            key.K_1: self._handle_key_1,
            key.K_2: self._handle_key_2,
            key.K_3: self._handle_key_3,
            key.K_4: self._handle_key_4,
            key.K_5: self._handle_key_5,
            key.K_6: self._handle_key_6,
            key.K_7: self._handle_key_7,
            key.K_8: self._handle_key_8,
            key.K_9: self._handle_key_9,
            key.K_0: self._handle_key_0,
            key.K_q: self._handle_key_q,
            key.K_w: self._handle_key_w,
            key.K_e: self._handle_key_e,
            key.K_r: self._handle_key_r,
            key.K_t: self._handle_key_t,
        }
        super(TestScene, self).__init__(fill, game, screen)
        self.char_sprite = CharacterSprite(self)
        self.sprites.add(self.char_sprite)

    def render(self):
        surface = pygame.Surface(self.screen.get_size())
        surface.fill(self.fill)
        self.sprites.draw(surface)
        return surface

    def update(self):
        pass

    def handle_event(self, event):
        if event.key in self.key_events:
            self.key_events[event.key]()
            if self == self.game.active_scene:
                self.char_sprite.update_base_sprites()
                self.char_sprite.build_sprite()
                self.char_sprite.image = self.char_sprite.sprite_image
            else:
                del self

    def _handle_key_escape(self):
        self.game.running = False

    def _handle_key_1(self):
        self.char_sprite.sex += 1
        self.char_sprite.hair_color = 0
        self.char_sprite.hair_type = 0
        if self.char_sprite.sex > 1:
            self.char_sprite.sex = 0

    def _handle_key_2(self):
        self.char_sprite.body += 1
        if self.char_sprite.body > 9:
            self.char_sprite.body = 0

    def _handle_key_3(self):
        self.char_sprite.ears += 1
        if self.char_sprite.ears > 2:
            self.char_sprite.ears = 0

    def _handle_key_4(self):
        self.char_sprite.eyes += 1
        if self.char_sprite.eyes > 8:
            self.char_sprite.eyes = 0

    def _handle_key_5(self):
        self.char_sprite.nose += 1
        if self.char_sprite.nose > 3:
            self.char_sprite.nose = 0

    def _handle_key_6(self):
        self.char_sprite.hair_color += 1
        if self.char_sprite.sex == 0:
            if self.char_sprite.hair_color > 7:
                self.char_sprite.hair_color = 0
        if self.char_sprite.sex == 1:
            if self.char_sprite.hair_color > 23:
                self.char_sprite.hair_color = 0

    def _handle_key_7(self):
        self.char_sprite.hair_type += 1
        if self.char_sprite.sex == 0:
            if self.char_sprite.hair_type > 11:
                self.char_sprite.hair_type = 0
        if self.char_sprite.sex == 1:
            if self.char_sprite.hair_type > 13:
                self.char_sprite.hair_type = 0

    def _handle_key_8(self):
        self.char_sprite.belt += 1
        if self.char_sprite.belt > 2:
            self.char_sprite.belt = 0

    def _handle_key_9(self):
        self.char_sprite.feets += 1
        if self.char_sprite.feets > 5:
            self.char_sprite.feets = 0

    def _handle_key_0(self):
        self.char_sprite.hands += 1
        if self.char_sprite.hands > 3:
            self.char_sprite.hands = 0

    def _handle_key_q(self):
        self.char_sprite.legs += 1
        if self.char_sprite.legs > 6:
            self.char_sprite.legs = 0

    def _handle_key_w(self):
        self.char_sprite.arms += 1
        if self.char_sprite.arms > 3:
            self.char_sprite.arms = 0

    def _handle_key_e(self):
        self.char_sprite.torso += 1
        if self.char_sprite.torso > 7:
            self.char_sprite.torso = 0

    def _handle_key_r(self):
        self.char_sprite.weapon1 += 1
        if self.char_sprite.weapon1 > 11:
            self.char_sprite.weapon1 = 0

    def _handle_key_t(self):
        self.char_sprite.weapon2 += 2
        if self.char_sprite.weapon2 > 11:
            self.char_sprite.weapon2 = 0
