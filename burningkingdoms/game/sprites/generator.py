from PIL import Image
import os

from .constants import *  # noqa


class SpriteGenerator(object):
    """Generates or returnes cache stored sprites."""
    spritegen_dir = os.path.dirname(__file__)

    def __init__(self, sex=SEX_MALE, body=BODY_LIGHT, ears=EAR_NORMAL, eyes=EYE_BLUE,
            nose=NOSE_NORMAL, hair_color=0, hair_type=0, belt=BELT_DEFAULT, feets=FEETS_DEFAULT,
            hand=HANDS_DEFAULT, legs=LEGS_CLOTH_WHITE, hands=HANDS_DEFAULT, arms=ARMS_DEFAULT,
            torso=TORSO_CLOTH_WHITE, cache_on_fs=True):
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
        self.cache_on_fs = cache_on_fs

    @property
    def image_id(self):
        char_dict = {
            'sex': self.sex,
            'body': self.body,
            'ears': self.ears,
            'eyes': self.eyes,
            'nose': self.nose,
            'hair_color': self.hair_color,
            'hair_type': self.hair_type,
            'belt': self.belt,
            'feets': self.feets,
            'hands': self.hands,
            'legs': self.legs,
            'arms': self.arms,
            'torso': self.torso,
        }
        return "%(sex)s%(body)s%(ears)s%(eyes)s%(nose)s%(hair_color)s%(hair_type)s%(belt)s%(feets)s%(hands)s%(legs)s%(arms)s%(torso)s" % char_dict  # noqa

    def generate_sprite(self):
        body_path = BODY_IMAGE_DICT[self.sex][self.body]
        ears_path = EARS_IMAGE_DICT[self.sex][self.body][self.ears]
        eyes_path = EYE_IMAGE_DICT[self.sex][self.eyes]
        nose_path = NOSE_IMAGE_DICT[self.sex][self.body][self.nose]
        hair_path = get_hair_path(self.sex, self.hair_type, self.hair_color)
        belt_path = BELT_DICT[self.sex][self.belt]
        feets_path = FEETS_DICT[self.sex][self.feets]
        hands_path = HANDS_DICT[self.sex][self.hands]
        legs_path = LEGS_DICT[self.sex][self.legs]
        arms_path = ARMS_DICT[self.sex][self.arms]
        torso_path = TORSO_DICT[self.sex][self.torso]
        layer_paths = [ears_path, eyes_path, nose_path, hair_path, torso_path,
            legs_path, belt_path, arms_path, hands_path, feets_path]

        sprite = Image.open(os.path.join(self.spritegen_dir, *body_path.split('/')))

        for path in layer_paths:
            if path:
                with Image.open(os.path.join(self.spritegen_dir, *path.split('/'))) as layer:
                    sprite.paste(layer, (0, 0), layer)
        return sprite

    def get_sprite(self):
        sprite_path = os.path.join(os.path.dirname(__file__), 'data', 'dest', '%s.png' % self.image_id)
        if self.cache_on_fs and os.path.exists(sprite_path):
            # image allready exists
            sprite_data = Image.open(sprite_path)
        else:
            sprite_data = self.generate_sprite()
        if self.cache_on_fs:
            sprite_data.save(sprite_path)
        return sprite_data
