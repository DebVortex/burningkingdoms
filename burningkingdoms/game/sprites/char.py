import os

import pygame

from .constants import *  # noqa


class CharacterSprite(pygame.sprite.Sprite):
    SPRITE_SIZE = 64
    ANIMATION_SPEED = 4.0
    CASTING = 0
    SPEAR = 1
    WALK = 2
    SLASH = 3
    BOW = 4
    DIE = 5
    STAND = 6
    ANIMATIONS = {
        CASTING: {
            'north': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)],
            'west': [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)],
            'south': [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6)],
            'east': [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)],
        },
        SPEAR: {
            'north': [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)],
            'west': [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (4, 7)],
            'south': [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (4, 7)],
            'east': [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (4, 7)],
        },
        WALK: {
            'north': [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)],
            'west': [(9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)],
            'south': [(10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8)],
            'east': [(11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8)],
        },
        SLASH: {
            'north': [(12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5)],
            'west': [(13, 0), (13, 1), (13, 2), (13, 3), (13, 4), (13, 5)],
            'south': [(14, 0), (14, 1), (14, 2), (14, 3), (14, 4), (14, 5)],
            'east': [(15, 0), (15, 1), (15, 2), (15, 3), (15, 4), (15, 5)],
        },
        BOW: {
            'north': [(16, 0), (16, 1), (16, 2), (16, 3), (16, 4), (16, 5), (16, 6), (16, 7), (16, 8), (16, 9), (16, 10), (16, 11), (16, 12)],
            'west': [(17, 0), (17, 1), (17, 2), (17, 3), (17, 4), (17, 5), (17, 6), (17, 7), (17, 8), (17, 9), (17, 10), (17, 11), (17, 12)],
            'south': [(18, 0), (18, 1), (18, 2), (18, 3), (18, 4), (18, 5), (18, 6), (18, 7), (18, 8), (18, 9), (18, 10), (18, 11), (18, 12)],
            'east': [(19, 0), (19, 1), (19, 2), (19, 3), (19, 4), (19, 5), (19, 6), (19, 7), (19, 8), (19, 9), (19, 10), (19, 11), (19, 12)],
        },
        DIE: {
            'north': [(20, 0), (20, 1), (20, 2), (20, 3), (20, 4), (20, 5)],
            'west': [(20, 0), (20, 1), (20, 2), (20, 3), (20, 4), (20, 5)],
            'south': [(20, 0), (20, 1), (20, 2), (20, 3), (20, 4), (20, 5)],
            'east': [(20, 0), (20, 1), (20, 2), (20, 3), (20, 4), (20, 5)],
        },
        STAND: {
            'north': [(0, 0)],
            'west': [(1, 0)],
            'south': [(2, 0)],
            'east': [(3, 0)],
        },
    }

    def __init__(self, scene, scale=1.0, sex=SEX_MALE, body=BODY_LIGHT, ears=EAR_NORMAL, eyes=EYE_BLUE,
            nose=NOSE_NORMAL, hair_color=0, hair_type=0, belt=BELT_DEFAULT, feets=FEETS_DEFAULT,
            hand=HANDS_DEFAULT, legs=LEGS_CLOTH_WHITE, hands=HANDS_DEFAULT, arms=ARMS_DEFAULT,
            torso=TORSO_CLOTH_WHITE, head=HEAD_DEFAULT, weapon1=WEAPON_DEFAULT,
            weapon2=WEAPON_DEFAULT):
        super(CharacterSprite, self).__init__()
        self.scene = scene
        self.scale = scale
        self.sex = sex
        self.body = body
        self.ears = ears
        self.eyes = eyes
        self.nose = nose
        self.hair_color = hair_color
        self.hair_type = hair_type
        self.belt = belt
        self.feets = feets
        self.hands = hands
        self.legs = legs
        self.arms = arms
        self.torso = torso
        self.head = head
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.direction = 'south'
        self.animation = self.SLASH
        self.time_passed = 0
        self.active_frame = 0
        self.change_time = self.ANIMATION_SPEED / (self.scene.game.fps/1000.0)
        self.animate_once = True
        self.update_base_sprites()
        self.build_sprite()

    def update_base_sprites(self):
        base_dir = os.path.dirname(__file__)
        if BODY_IMAGE_DICT[self.sex][self.body]:
            body_path = os.path.join(base_dir, BODY_IMAGE_DICT[self.sex][self.body])
            self.body_image = pygame.image.load(body_path)
        else:
            self.body_image = None
        if EARS_IMAGE_DICT[self.sex][self.body][self.ears]:
            ears_path = os.path.join(base_dir, EARS_IMAGE_DICT[self.sex][self.body][self.ears])
            self.ears_image = pygame.image.load(ears_path)
        else:
            self.ears_image = None
        if EYE_IMAGE_DICT[self.sex][self.eyes]:
            eyes_path = os.path.join(base_dir, EYE_IMAGE_DICT[self.sex][self.eyes])
            self.eyes_image = pygame.image.load(eyes_path)
        else:
            self.eyes_image = None
        if NOSE_IMAGE_DICT[self.sex][self.body][self.nose]:
            nose_path = os.path.join(base_dir, NOSE_IMAGE_DICT[self.sex][self.body][self.nose])
            self.nose_image = pygame.image.load(nose_path)
        else:
            self.nose_image = None
        hair_base = get_hair_path(self.sex, self.hair_type,
            self.hair_color)
        if hair_base:
            hair_path = os.path.join(base_dir, hair_base)
            self.hair_image = pygame.image.load(hair_path)
        else:
            self.hair_image = None
        if BELT_DICT[self.sex][self.belt]:
            belt_path = os.path.join(base_dir, BELT_DICT[self.sex][self.belt])
            self.belt_image = pygame.image.load(belt_path)
        else:
            self.belt_image = None
        if FEETS_DICT[self.sex][self.feets]:
            feets_path = os.path.join(base_dir, FEETS_DICT[self.sex][self.feets])
            self.feets_image = pygame.image.load(feets_path)
        else:
            self.feets_image = None
        if HANDS_DICT[self.sex][self.hands]:
            hands_path = os.path.join(base_dir, HANDS_DICT[self.sex][self.hands])
            self.hands_image = pygame.image.load(hands_path)
        else:
            self.hands_image = None
        if LEGS_DICT[self.sex][self.legs]:
            legs_path = os.path.join(base_dir, LEGS_DICT[self.sex][self.legs])
            self.legs_image = pygame.image.load(legs_path)
        else:
            self.legs_image = None
        if ARMS_DICT[self.sex][self.arms]:
            arms_path = os.path.join(base_dir, ARMS_DICT[self.sex][self.arms])
            self.arms_image = pygame.image.load(arms_path)
        else:
            self.arms_image = None
        if TORSO_DICT[self.sex][self.torso]:
            torso_path = os.path.join(base_dir, TORSO_DICT[self.sex][self.torso])
            self.torso_image = pygame.image.load(torso_path)
        else:
            self.torso_image = None
        if HEAD_DICT[self.sex][self.head]:
            head_path = os.path.join(base_dir, HEAD_DICT[self.sex][self.head])
            self.head_image = pygame.image.load(head_path)
        else:
            self.head_image = None
        if WEAPON_DICT[self.sex][self.weapon1]:
            weapon1_path = os.path.join(base_dir, WEAPON_DICT[self.sex][self.weapon1])
            self.weapon1_image = pygame.image.load(weapon1_path)
        else:
            self.weapon1_image = None
        if WEAPON_DICT[self.sex][self.weapon2]:
            weapon2_path = os.path.join(base_dir, WEAPON_DICT[self.sex][self.weapon2])
            self.weapon2_image = pygame.image.load(weapon2_path)
        else:
            self.weapon2_image = None

        self.layer_order = [self.body_image, self.eyes_image, self.nose_image, self.hair_image,
            self.torso_image, self.legs_image, self.belt_image, self.arms_image, self.hands_image,
            self.feets_image, self.head_image, self.weapon1_image, self.weapon2_image]

    def change_animation(animation, animate_once=False):
        self.animation = animation
        self.active_frame = 0
        self.time_passed = 0

    def build_sprite(self):
        sprite_rect = self.body_image.get_rect()
        sprite = pygame.Surface((self.scale * sprite_rect.width, self.scale * sprite_rect.height))
        for layer in self.layer_order:
            if layer:
                scaled_layer = pygame.transform.scale(
                    layer, (
                        int(self.scale * layer.get_rect().width),
                        int(self.scale * layer.get_rect().height),
                    )
                )
                sprite.blit(scaled_layer, (0, 0))
        self.sprite_image = sprite

    def draw_image(self):
        self.image = pygame.Surface((self.scale * self.SPRITE_SIZE, self.scale * self.SPRITE_SIZE))
        self.rect = self.image.get_rect()

        animation_length = len(self.ANIMATIONS[self.animation][self.direction])

        self.time_passed += self.scene.game.dt
        if self.time_passed >= self.change_time:
            self.active_frame = (self.active_frame + 1) % animation_length
            self.time_passed = 0
            if self.animate_once and self.active_frame == 0:
                self.animation = self.STAND

        row, col = self.ANIMATIONS[self.animation][self.direction][self.active_frame]

        self.image.blit(self.sprite_image, (0, 0), (
            col * self.SPRITE_SIZE * self.scale,
            row * self.SPRITE_SIZE * self.scale,
            self.SPRITE_SIZE * self.scale,
            self.SPRITE_SIZE * self.scale,
            )
        )

    @property
    def char_id(self):
        return "{s.sex}{s.body}{s.ears}{s.eyes}{s.nose}{s.hair_color}{s.hair_type}{s.belt}{s.feets}{s.hands}{s.legs}{s.arms}{s.torso}{s.head}{s.weapon1}{s.weapon2}".format(s=self)  # noqa
