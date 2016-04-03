from burningkingdoms.game.scenes.core import Scene

import pygame
from pygame import locals as key

from burningkingdoms.game.sprites.char import CharacterSprite
from burningkingdoms.game.sprites.constants import MAIN_HAND_WEAPONS, OFF_HAND_WEAPONS


class SpriteTestScene(Scene):

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
            key.K_z: self._handle_key_z,
            key.K_u: self._handle_key_u,
            key.K_i: self._handle_key_i,
            key.K_o: self._handle_key_o,
            key.K_p: self._handle_key_p,
            key.K_y: self._handle_key_y,
            key.K_x: self._handle_key_x,
            key.K_c: self._handle_key_c,
            key.K_v: self._handle_key_v,
            key.K_b: self._handle_key_b,
            key.K_n: self._handle_key_n,
            key.K_m: self._handle_key_m,
            key.K_UP: self._handle_key_up,
            key.K_DOWN: self._handle_key_down,
            key.K_LEFT: self._handle_key_left,
            key.K_RIGHT: self._handle_key_right,
        }
        super(SpriteTestScene, self).__init__(fill, game, screen)
        self.font = pygame.font.SysFont("Mono", 18)
        self.char_sprite = CharacterSprite(self)
        self.sprites.add(self.char_sprite)

    def build_help_texts(self):
        self.help_text_texts = []
        self.divider = self.font.render("-----------------------------------------", 1, (255, 0, 0))
        self.help_text_texts.append(self.font.render(
            "1: sex [{}]".format(self.char_sprite.sex), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "2: body [{}]".format(self.char_sprite.body), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "3: ears [{}]".format(self.char_sprite.ears), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "4: eyes [{}]".format(self.char_sprite.eyes), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "5: nose [{}]".format(self.char_sprite.nose), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "6: hair_type [{}]".format(self.char_sprite.hair_type), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "7: hair_color [{}]".format(self.char_sprite.hair_color), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "8: belt [{}]".format(self.char_sprite.belt), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "9: feets [{}]".format(self.char_sprite.feets), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "0: hands [{}]".format(self.char_sprite.hands), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "q: legs [{}]".format(self.char_sprite.legs), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "w: arms [{}]".format(self.char_sprite.arms), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "e: torso [{}]".format(self.char_sprite.torso), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "r: head [{}]".format(self.char_sprite.head), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "t: main hand [{}]".format(self.char_sprite.main_hand), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.font.render(
            "z: off hand [{}]".format(self.char_sprite.off_hand), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.divider)
        self.help_text_texts.append(self.font.render(
            "o/p: increase/reduce scaling [{}]".format(self.char_sprite.scale), 1, (255, 0, 0))
        )
        self.help_text_texts.append(self.divider)
        self.help_text_texts.append(self.font.render("u: animation once / cont", 1, (255, 0, 0)))
        self.help_text_texts.append(self.font.render("y: animation casting", 1, (255, 0, 0)))
        self.help_text_texts.append(self.font.render("x: animation spear", 1, (255, 0, 0)))
        self.help_text_texts.append(self.font.render("c: animation walk", 1, (255, 0, 0)))
        self.help_text_texts.append(self.font.render("v: animation slash", 1, (255, 0, 0)))
        self.help_text_texts.append(self.font.render("b: animation bow", 1, (255, 0, 0)))
        self.help_text_texts.append(self.font.render("n: animation die", 1, (255, 0, 0)))
        self.help_text_texts.append(self.font.render("m: animation stand", 1, (255, 0, 0)))
        self.help_text_texts.append(self.divider)
        self.help_text_texts.append(self.font.render("up: look up", 1, (255, 0, 0)))
        self.help_text_texts.append(self.font.render("down: look down", 1, (255, 0, 0)))
        self.help_text_texts.append(self.font.render("left: look left", 1, (255, 0, 0)))
        self.help_text_texts.append(self.font.render("right: look right", 1, (255, 0, 0)))
        self.help_text_texts.append(self.divider)
        self.help_text_texts.append(self.font.render(
            "CharID: {}".format(self.char_sprite.char_id), 1, (255, 0, 0))
        )

    def render(self):
        surface = pygame.Surface(self.screen.get_size())
        surface.fill(self.fill)
        self.sprites.draw(surface)
        top = 0
        self.build_help_texts()
        for help_text in self.help_text_texts:
            rect = help_text.get_rect()
            rect.left = surface.get_rect().right - self.divider.get_rect().width
            rect.top = top
            surface.blit(help_text, rect)
            top += rect.height
            surface.blit(help_text, rect)
        return surface

    def update(self):
        self.char_sprite.draw_image()

    def handle_event(self, event):
        if event.key in self.key_events:
            self.key_events[event.key]()
            if self == self.game.active_scene:
                self.char_sprite.update_base_sprites()
                self.char_sprite.build_sprite()
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
        self.char_sprite.hair_type += 1
        if self.char_sprite.sex == 0:
            if self.char_sprite.hair_type > 11:
                self.char_sprite.hair_type = 0
        if self.char_sprite.sex == 1:
            if self.char_sprite.hair_type > 13:
                self.char_sprite.hair_type = 0

    def _handle_key_7(self):
        self.char_sprite.hair_color += 1
        if self.char_sprite.sex == 0:
            if self.char_sprite.hair_color > 7:
                self.char_sprite.hair_color = 0
        if self.char_sprite.sex == 1:
            if self.char_sprite.hair_color > 23:
                self.char_sprite.hair_color = 0

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
        self.char_sprite.head += 1
        if self.char_sprite.head > 7:
            self.char_sprite.head = 0
        if self.char_sprite.head != 0:
            self.char_sprite.hair_type = 0

    def _handle_key_t(self):
        self.char_sprite.main_hand += 1
        if self.char_sprite.main_hand > (len(MAIN_HAND_WEAPONS) - 1):
            self.char_sprite.main_hand = 0
            self.char_sprite.active_frame = 0
            self.char_sprite.time_passed = 0

    def _handle_key_z(self):
        self.char_sprite.off_hand += 1
        if self.char_sprite.off_hand > (len(OFF_HAND_WEAPONS) - 1):
            self.char_sprite.off_hand = 0

    def _handle_key_u(self):
        self.char_sprite.animate_once = not self.char_sprite.animate_once
        self.char_sprite.time_passed = 0

    def _handle_key_i(self):
        quiver = 1
        if self.char_sprite.quiver:
            quiver = 0
        self.char_sprite.quiver = quiver

    def _handle_key_o(self):
        self.char_sprite.scale += 0.2

    def _handle_key_p(self):
        self.char_sprite.scale -= 0.2

    def _handle_key_up(self):
        self.char_sprite.direction = 'north'

    def _handle_key_down(self):
        self.char_sprite.direction = 'south'

    def _handle_key_left(self):
        self.char_sprite.direction = 'west'

    def _handle_key_right(self):
        self.char_sprite.direction = 'east'

    def _handle_key_y(self):
        self.char_sprite.animation = self.char_sprite.CASTING
        self.char_sprite.active_frame = 0
        self.char_sprite.time_passed = 0

    def _handle_key_x(self):
        self.char_sprite.animation = self.char_sprite.SPEAR
        self.char_sprite.active_frame = 0
        self.char_sprite.time_passed = 0

    def _handle_key_c(self):
        self.char_sprite.animation = self.char_sprite.WALK
        self.char_sprite.active_frame = 0
        self.char_sprite.time_passed = 0

    def _handle_key_v(self):
        self.char_sprite.animation = self.char_sprite.SLASH
        self.char_sprite.active_frame = 0
        self.char_sprite.time_passed = 0

    def _handle_key_b(self):
        self.char_sprite.animation = self.char_sprite.BOW
        self.char_sprite.active_frame = 0
        self.char_sprite.time_passed = 0

    def _handle_key_n(self):
        self.char_sprite.animation = self.char_sprite.DIE
        self.char_sprite.active_frame = 0
        self.char_sprite.time_passed = 0

    def _handle_key_m(self):
        self.char_sprite.animation = self.char_sprite.STAND
        self.char_sprite.active_frame = 0
        self.char_sprite.time_passed = 0
