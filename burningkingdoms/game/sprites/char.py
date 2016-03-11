import os

import pygame

from .constants import *  # noqa


class CharacterSprite(pygame.sprite.Sprite):

    def __init__(self, scene, scale=1, sex=SEX_MALE, body=BODY_LIGHT, ears=EAR_NORMAL, eyes=EYE_BLUE,
            nose=NOSE_NORMAL, hair_color=0, hair_type=0, belt=BELT_DEFAULT, feets=FEETS_DEFAULT,
            hand=HANDS_DEFAULT, legs=LEGS_CLOTH_WHITE, hands=HANDS_DEFAULT, arms=ARMS_DEFAULT,
            torso=TORSO_CLOTH_WHITE, weapon1=WEAPON_DEFAULT, weapon2=WEAPON_DEFAULT):
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
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.update_base_sprites()
        self.build_sprite()
        self.image = self.sprite_image
        self.rect = self.image.get_rect()

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
            self.feets_image, self.weapon1_image, self.weapon2_image]

    def build_sprite(self):
        sprite_rect = self.body_image.get_rect()
        sprite = pygame.Surface((sprite_rect.width, sprite_rect.height))
        for layer in self.layer_order:
            if layer:
                sprite.blit(layer, (0, 0))
        self.sprite_image = sprite
