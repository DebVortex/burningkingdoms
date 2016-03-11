# Constants for sex
SEX_MALE = 0
SEX_FEMALE = 1
SEX_CHOICES = (
    (SEX_MALE, 'Male'),
    (SEX_FEMALE, 'Female'),
)

# Constants for Body
BODY_LIGHT = 0
BODY_TANNED = 1
BODY_TANNED2 = 2
BODY_DARK = 3
BODY_DARK2 = 4
BODY_DARKELF = 5
BODY_DARKELF2 = 6
BODY_ORC = 7
BODY_REDORC = 8
BODY_SKELETON = 9
BODY_CHOICES = (
    (BODY_LIGHT, '0'),
    (BODY_TANNED, '1'),
    (BODY_TANNED2, '2'),
    (BODY_DARK, '3'),
    (BODY_DARK2, '4'),
    (BODY_DARKELF, '5'),
    (BODY_DARKELF2, '6'),
    (BODY_ORC, '7'),
    (BODY_REDORC, '8'),
    (BODY_SKELETON, '9'),
)
PLAYER_BODY_CHOICES = (
    (BODY_LIGHT, '0'),
    (BODY_TANNED, '1'),
    (BODY_TANNED2, '2'),
    (BODY_DARK, '3'),
    (BODY_DARK2, '4'),
    (BODY_DARKELF, '5'),
    (BODY_DARKELF2, '6'),
)

# Returns the body imagepath according to the choosen sex and body
BODY_IMAGE_DICT = {
    SEX_MALE: {
        BODY_LIGHT: 'data/src/body/male/light.png',
        BODY_TANNED: 'data/src/body/male/tanned.png',
        BODY_TANNED2: 'data/src/body/male/tanned2.png',
        BODY_DARK: 'data/src/body/male/dark.png',
        BODY_DARK2: 'data/src/body/male/dark2.png',
        BODY_DARKELF: 'data/src/body/male/darkelf.png',
        BODY_DARKELF2: 'data/src/body/male/darkelf2.png',
        BODY_ORC: 'data/src/body/male/orc.png',
        BODY_REDORC: 'data/src/body/male/red_orc.png',
        BODY_SKELETON: 'data/src/body/male/skeleton.png',
    },
    SEX_FEMALE: {
        BODY_LIGHT: 'data/src/body/female/light.png',
        BODY_TANNED: 'data/src/body/female/tanned.png',
        BODY_TANNED2: 'data/src/body/female/tanned2.png',
        BODY_DARK: 'data/src/body/female/dark.png',
        BODY_DARK2: 'data/src/body/female/dark2.png',
        BODY_DARKELF: 'data/src/body/female/darkelf.png',
        BODY_DARKELF2: 'data/src/body/female/darkelf2.png',
        BODY_ORC: 'data/src/body/female/orc.png',
        BODY_REDORC: 'data/src/body/female/red_orc.png',
        BODY_SKELETON: 'data/src/body/male/skeleton.png',
    },
}

# Constants for Ears
EAR_NORMAL = 0
EAR_BIG = 1
EAR_ELVE = 2
EAR_CHOICES = (
    (EAR_NORMAL, 'Normal'),
    (EAR_BIG, 'Big'),
    (EAR_ELVE, 'Elven'),
)

# Return the ear imagepath according to the choosen sex, body and ears
EARS_IMAGE_DICT = {
    SEX_MALE: {
        BODY_LIGHT: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/male/ears/bigears_light.png',
            EAR_ELVE: 'data/src/body/male/ears/elvenears_light.png',
        },
        BODY_TANNED: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/male/ears/bigears_tanned.png',
            EAR_ELVE: 'data/src/body/male/ears/elvenears_tanned.png',
        },
        BODY_TANNED2: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/male/ears/bigears_tanned2.png',
            EAR_ELVE: 'data/src/body/male/ears/elvenears_tanned2.png',
        },
        BODY_DARK: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/male/ears/bigears_dark.png',
            EAR_ELVE: 'data/src/body/male/ears/elvenears_dark.png',
        },
        BODY_DARK2: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/male/ears/bigears_dark2.png',
            EAR_ELVE: 'data/src/body/male/ears/elvenears_dark2.png',
        },
        BODY_DARKELF: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/male/ears/bigears_darkelf.png',
            EAR_ELVE: 'data/src/body/male/ears/elvenears_darkelf.png',
        },
        BODY_DARKELF2: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/male/ears/bigears_darkelf2.png',
            EAR_ELVE: 'data/src/body/male/ears/elvenears_darkelf2.png',
        },
        BODY_ORC: {
            EAR_NORMAL: None,
            EAR_BIG: None,
            EAR_ELVE: None,
        },
        BODY_REDORC: {
            EAR_NORMAL: None,
            EAR_BIG: None,
            EAR_ELVE: None,
        },
        BODY_SKELETON: {
            EAR_NORMAL: None,
            EAR_BIG: None,
            EAR_ELVE: None,
        },
    },
    SEX_FEMALE: {
        BODY_LIGHT: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/female/ears/bigears_light.png',
            EAR_ELVE: 'data/src/body/female/ears/elvenears_light.png',
        },
        BODY_TANNED: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/female/ears/bigears_tanned.png',
            EAR_ELVE: 'data/src/body/female/ears/elvenears_tanned.png',
        },
        BODY_TANNED2: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/female/ears/bigears_tanned2.png',
            EAR_ELVE: 'data/src/body/female/ears/elvenears_tanned2.png',
        },
        BODY_DARK: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/female/ears/bigears_dark.png',
            EAR_ELVE: 'data/src/body/female/ears/elvenears_dark.png',
        },
        BODY_DARK2: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/female/ears/bigears_dark2.png',
            EAR_ELVE: 'data/src/body/female/ears/elvenears_dark2.png',
        },
        BODY_DARKELF: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/female/ears/bigears_darkelf.png',
            EAR_ELVE: 'data/src/body/female/ears/elvenears_darkelf.png',
        },
        BODY_DARKELF2: {
            EAR_NORMAL: None,
            EAR_BIG: 'data/src/body/female/ears/bigears_darkelf2.png',
            EAR_ELVE: 'data/src/body/female/ears/elvenears_darkelf2.png',
        },
        BODY_ORC: {
            EAR_NORMAL: None,
            EAR_BIG: None,
            EAR_ELVE: None,
        },
        BODY_REDORC: {
            EAR_NORMAL: None,
            EAR_BIG: None,
            EAR_ELVE: None,
        },
        BODY_SKELETON: {
            EAR_NORMAL: None,
            EAR_BIG: None,
            EAR_ELVE: None,
        },
    },
}

# Constants for Eyes
EYE_BLUE = 0
EYE_BROWN = 1
EYE_GRAY = 2
EYE_GREEN = 3
EYE_ORANGE = 4
EYE_PURPLE = 5
EYE_RED = 6
EYE_YELLOW = 7
EYE_SKELETON = 8
EYE_CHOICES = (
    (EYE_BLUE, 'Blue'),
    (EYE_BROWN, 'Brown'),
    (EYE_GRAY, 'Grey'),
    (EYE_GREEN, 'Green'),
    (EYE_ORANGE, 'Orange'),
    (EYE_PURPLE, 'Purple'),
    (EYE_RED, 'Red'),
    (EYE_YELLOW, 'Yellow'),
    (EYE_SKELETON, 'Skeleton-Yellow'),
)
PLAYER_EYE_CHOICES = (
    (EYE_BLUE, 'Blue'),
    (EYE_BROWN, 'Brown'),
    (EYE_GRAY, 'Gray'),
    (EYE_GREEN, 'Green'),
    (EYE_ORANGE, 'Orange'),
    (EYE_PURPLE, 'Purple'),
    (EYE_RED, 'Red'),
    (EYE_YELLOW, 'Yellow'),
)

# Return the eye imagepath according to the choosen sex, body and eyes
EYE_IMAGE_DICT = {
    SEX_MALE: {
        EYE_BLUE: 'data/src/body/male/eyes/blue.png',
        EYE_BROWN: 'data/src/body/male/eyes/brown.png',
        EYE_GRAY: 'data/src/body/male/eyes/gray.png',
        EYE_GREEN: 'data/src/body/male/eyes/green.png',
        EYE_ORANGE: 'data/src/body/male/eyes/orange.png',
        EYE_PURPLE: 'data/src/body/male/eyes/purple.png',
        EYE_RED: 'data/src/body/male/eyes/red.png',
        EYE_YELLOW: 'data/src/body/male/eyes/yellow.png',
        EYE_SKELETON: 'data/src/body/male/eyes/casting_eyeglow_skeleton.png',
    },
    SEX_FEMALE: {
        EYE_BLUE: 'data/src/body/female/eyes/blue.png',
        EYE_BROWN: 'data/src/body/female/eyes/brown.png',
        EYE_GRAY: 'data/src/body/female/eyes/gray.png',
        EYE_GREEN: 'data/src/body/female/eyes/green.png',
        EYE_ORANGE: 'data/src/body/female/eyes/orange.png',
        EYE_PURPLE: 'data/src/body/female/eyes/purple.png',
        EYE_RED: 'data/src/body/female/eyes/red.png',
        EYE_YELLOW: 'data/src/body/female/eyes/yellow.png',
        EYE_SKELETON: 'data/src/body/male/eyes/casting_eyeglow_skeleton.png',
    },
}

# Constants for Nose
NOSE_NORMAL = 0
NOSE_BIG = 1
NOSE_BUTTON = 2
NOSE_STRAIGHT = 3
NOSE_CHOICES = (
    (NOSE_NORMAL, 'normal Nose'),
    (NOSE_BIG, 'big Nose'),
    (NOSE_BUTTON, 'button Nose'),
    (NOSE_STRAIGHT, 'straight Nose'),
)

# Return the nose imagepath according to the choosen sex, body and nose
NOSE_IMAGE_DICT = {
    SEX_MALE: {
        BODY_LIGHT: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/male/nose/bignose_light.png',
            NOSE_BUTTON: 'data/src/body/male/nose/buttonnose_light.png',
            NOSE_STRAIGHT: 'data/src/body/male/nose/straightnose_light.png',
        },
        BODY_TANNED: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/male/nose/bignose_tanned.png',
            NOSE_BUTTON: 'data/src/body/male/nose/buttonnose_tanned.png',
            NOSE_STRAIGHT: 'data/src/body/male/nose/straightnose_tanned.png',
        },
        BODY_TANNED2: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/male/nose/bignose_tanned2.png',
            NOSE_BUTTON: 'data/src/body/male/nose/buttonnose_tanned2.png',
            NOSE_STRAIGHT: 'data/src/body/male/nose/straightnose_tanned2.png',
        },
        BODY_DARK: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/male/nose/bignose_dark.png',
            NOSE_BUTTON: 'data/src/body/male/nose/buttonnose_dark.png',
            NOSE_STRAIGHT: 'data/src/body/male/nose/straightnose_dark.png',
        },
        BODY_DARK2: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/male/nose/bignose_dark2.png',
            NOSE_BUTTON: 'data/src/body/male/nose/buttonnose_dark2.png',
            NOSE_STRAIGHT: 'data/src/body/male/nose/straightnose_dark2.png',
        },
        BODY_DARKELF: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/male/nose/bignose_darkelf.png',
            NOSE_BUTTON: 'data/src/body/male/nose/buttonnose_darkelf.png',
            NOSE_STRAIGHT: 'data/src/body/male/nose/straightnose_darkelf.png',
        },
        BODY_DARKELF2: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/male/nose/bignose_darkelf2.png',
            NOSE_BUTTON: 'data/src/body/male/nose/buttonnose_darkelf2.png',
            NOSE_STRAIGHT: 'data/src/body/male/nose/straightnose_darkelf2.png',
        },
        BODY_ORC: {
            NOSE_NORMAL: None,
            NOSE_BIG: None,
            NOSE_BUTTON: None,
            NOSE_STRAIGHT: None,
        },
        BODY_REDORC: {
            NOSE_NORMAL: None,
            NOSE_BIG: None,
            NOSE_BUTTON: None,
            NOSE_STRAIGHT: None,
        },
        BODY_SKELETON: {
            NOSE_NORMAL: None,
            NOSE_BIG: None,
            NOSE_BUTTON: None,
            NOSE_STRAIGHT: None,
        },
    },
    SEX_FEMALE: {
        BODY_LIGHT: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/female/nose/bignose_light.png',
            NOSE_BUTTON: 'data/src/body/female/nose/buttonnose_light.png',
            NOSE_STRAIGHT: 'data/src/body/female/nose/straightnose_light.png',
        },
        BODY_TANNED: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/female/nose/bignose_tanned.png',
            NOSE_BUTTON: 'data/src/body/female/nose/buttonnose_tanned.png',
            NOSE_STRAIGHT: 'data/src/body/female/nose/straightnose_tanned.png',
        },
        BODY_TANNED2: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/female/nose/bignose_tanned2.png',
            NOSE_BUTTON: 'data/src/body/female/nose/buttonnose_tanned2.png',
            NOSE_STRAIGHT: 'data/src/body/female/nose/straightnose_tanned2.png',
        },
        BODY_DARK: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/female/nose/bignose_dark.png',
            NOSE_BUTTON: 'data/src/body/female/nose/buttonnose_dark.png',
            NOSE_STRAIGHT: 'data/src/body/female/nose/straightnose_dark.png',
        },
        BODY_DARK2: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/female/nose/bignose_dark2.png',
            NOSE_BUTTON: 'data/src/body/female/nose/buttonnose_dark2.png',
            NOSE_STRAIGHT: 'data/src/body/female/nose/straightnose_dark2.png',
        },
        BODY_DARKELF: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/female/nose/bignose_darkelf.png',
            NOSE_BUTTON: 'data/src/body/female/nose/buttonnose_darkelf.png',
            NOSE_STRAIGHT: 'data/src/body/female/nose/straightnose_darkelf.png',
        },
        BODY_DARKELF2: {
            NOSE_NORMAL: None,
            NOSE_BIG: 'data/src/body/female/nose/bignose_darkelf2.png',
            NOSE_BUTTON: 'data/src/body/female/nose/buttonnose_darkelf2.png',
            NOSE_STRAIGHT: 'data/src/body/female/nose/straightnose_darkelf2.png',
        },
        BODY_ORC: {
            NOSE_NORMAL: None,
            NOSE_BIG: None,
            NOSE_BUTTON: None,
            NOSE_STRAIGHT: None,
        },
        BODY_REDORC: {
            NOSE_NORMAL: None,
            NOSE_BIG: None,
            NOSE_BUTTON: None,
            NOSE_STRAIGHT: None,
        },
        BODY_SKELETON: {
            NOSE_NORMAL: None,
            NOSE_BIG: None,
            NOSE_BUTTON: None,
            NOSE_STRAIGHT: None,
        },
    }
}


# Constants for Hair Male Color
HAIR_COLOR_MALE_BLONDE = 0
HAIR_COLOR_MALE_BLUE = 1
HAIR_COLOR_MALE_BRUNETTE = 2
HAIR_COLOR_MALE_GREEN = 3
HAIR_COLOR_MALE_PINK = 4
HAIR_COLOR_MALE_RAVEN = 5
HAIR_COLOR_MALE_REDHEAD = 6
HAIR_COLOR_MALE_WHITEBLOND = 7
HAIR_COLOR_MALE_CHOICES = (
    (HAIR_COLOR_MALE_BLONDE, 'Blonde'),
    (HAIR_COLOR_MALE_BLUE, 'Blue'),
    (HAIR_COLOR_MALE_BRUNETTE, 'Brunette'),
    (HAIR_COLOR_MALE_GREEN, 'Green'),
    (HAIR_COLOR_MALE_PINK, 'Pink'),
    (HAIR_COLOR_MALE_RAVEN, 'Raven'),
    (HAIR_COLOR_MALE_REDHEAD, 'Redhead'),
    (HAIR_COLOR_MALE_WHITEBLOND, 'Whiteblonde'),
)

# Constants for Hair Male Type
HAIR_TYPE_MALE_BALD = 0
HAIR_TYPE_MALE_BANGS = 1
HAIR_TYPE_MALE_BEDHEAD = 2
HAIR_TYPE_MALE_LONG = 3
HAIR_TYPE_MALE_LONGHAWK = 4
HAIR_TYPE_MALE_MESSY1 = 5
HAIR_TYPE_MALE_MESSY2 = 6
HAIR_TYPE_MALE_MOHAWK = 7
HAIR_TYPE_MALE_PAGE = 8
HAIR_TYPE_MALE_PARTED = 9
HAIR_TYPE_MALE_PLAIN = 10
HAIR_TYPE_MALE_SHORTHAWK = 11
HAIR_TYPE_MALE_CHOICES = (
    (HAIR_TYPE_MALE_BALD, 'Bald'),
    (HAIR_TYPE_MALE_BANGS, 'Bangs'),
    (HAIR_TYPE_MALE_BEDHEAD, 'Bedhead'),
    (HAIR_TYPE_MALE_LONG, 'Long'),
    (HAIR_TYPE_MALE_LONGHAWK, 'Longhawk'),
    (HAIR_TYPE_MALE_MESSY1, 'Messy1'),
    (HAIR_TYPE_MALE_MESSY2, 'Messy2'),
    (HAIR_TYPE_MALE_MOHAWK, 'Mohawk'),
    (HAIR_TYPE_MALE_PAGE, 'Page'),
    (HAIR_TYPE_MALE_PARTED, 'Parted'),
    (HAIR_TYPE_MALE_PLAIN, 'Plain'),
    (HAIR_TYPE_MALE_SHORTHAWK, 'Shorthawk'),
)

# Constants for Hair Female Color
HAIR_COLOR_FEMALE_BLACK = 0
HAIR_COLOR_FEMALE_BLONDE = 1
HAIR_COLOR_FEMALE_BLONDE2 = 2
HAIR_COLOR_FEMALE_BLUE = 3
HAIR_COLOR_FEMALE_BLUE2 = 4
HAIR_COLOR_FEMALE_BROWN = 5
HAIR_COLOR_FEMALE_BRUNETTE = 6
HAIR_COLOR_FEMALE_BRUNETTE2 = 7
HAIR_COLOR_FEMALE_DARKBLONDE = 8
HAIR_COLOR_FEMALE_GRAY = 9
HAIR_COLOR_FEMALE_GREEN = 10
HAIR_COLOR_FEMALE_GREEN2 = 11
HAIR_COLOR_FEMALE_LIGHTBLONDE = 12
HAIR_COLOR_FEMALE_LIGHTBLONDE2 = 13
HAIR_COLOR_FEMALE_PINK = 14
HAIR_COLOR_FEMALE_PINK2 = 15
HAIR_COLOR_FEMALE_RAVEN = 16
HAIR_COLOR_FEMALE_RAVEN2 = 17
HAIR_COLOR_FEMALE_REDHEAD = 18
HAIR_COLOR_FEMALE_RUBYRED = 19
HAIR_COLOR_FEMALE_WHITEBLONDE = 20
HAIR_COLOR_FEMALE_WHITEBLONDE2 = 21
HAIR_COLOR_FEMALE_WHITECYAN = 22
HAIR_COLOR_FEMALE_WHITE = 23
HAIR_COLOR_FEMALE_CHOICES = (
    (HAIR_COLOR_FEMALE_BLACK, 'Black'),
    (HAIR_COLOR_FEMALE_BLONDE, 'Blonde'),
    (HAIR_COLOR_FEMALE_BLONDE2, 'Blonde2'),
    (HAIR_COLOR_FEMALE_BLUE, 'Blue'),
    (HAIR_COLOR_FEMALE_BLUE2, 'Blue2'),
    (HAIR_COLOR_FEMALE_BROWN, 'Brown'),
    (HAIR_COLOR_FEMALE_BRUNETTE, 'Brunette'),
    (HAIR_COLOR_FEMALE_BRUNETTE2, 'Brunette2'),
    (HAIR_COLOR_FEMALE_DARKBLONDE, 'Darkblonde'),
    (HAIR_COLOR_FEMALE_GRAY, 'Grey'),
    (HAIR_COLOR_FEMALE_GREEN, 'Green'),
    (HAIR_COLOR_FEMALE_GREEN2, 'Green2'),
    (HAIR_COLOR_FEMALE_LIGHTBLONDE, 'Lightblonde'),
    (HAIR_COLOR_FEMALE_LIGHTBLONDE2, 'Lightblonde2'),
    (HAIR_COLOR_FEMALE_PINK, 'Pink'),
    (HAIR_COLOR_FEMALE_PINK2, 'Pink2'),
    (HAIR_COLOR_FEMALE_RAVEN, 'Raven'),
    (HAIR_COLOR_FEMALE_RAVEN2, 'Raven2'),
    (HAIR_COLOR_FEMALE_REDHEAD, 'Redhead'),
    (HAIR_COLOR_FEMALE_RUBYRED, 'Rubyred'),
    (HAIR_COLOR_FEMALE_WHITEBLONDE, 'Whiteblonde'),
    (HAIR_COLOR_FEMALE_WHITEBLONDE2, 'Whiteblonde2'),
    (HAIR_COLOR_FEMALE_WHITECYAN, 'Whitecyan'),
    (HAIR_COLOR_FEMALE_WHITE, 'White'),
)

# male helperdicts for get_hair_path function
HAIR_TYPE_MALE_DICT = {
    HAIR_TYPE_MALE_BANGS: 'male/bangs',
    HAIR_TYPE_MALE_BEDHEAD: 'male/bedhead',
    HAIR_TYPE_MALE_LONG: 'male/long',
    HAIR_TYPE_MALE_LONGHAWK: 'male/longhawk',
    HAIR_TYPE_MALE_MESSY1: 'male/messy1',
    HAIR_TYPE_MALE_MESSY2: 'male/messy2',
    HAIR_TYPE_MALE_MOHAWK: 'male/mohawk',
    HAIR_TYPE_MALE_PAGE: 'male/page',
    HAIR_TYPE_MALE_PARTED: 'male/parted',
    HAIR_TYPE_MALE_PLAIN: 'male/plain',
    HAIR_TYPE_MALE_SHORTHAWK: 'male/shorthawk',
}
HAIR_COLOR_MALE_DICT = {
    HAIR_COLOR_MALE_BLONDE: 'blonde.png',
    HAIR_COLOR_MALE_BLUE: 'blue.png',
    HAIR_COLOR_MALE_BRUNETTE: 'brunette.png',
    HAIR_COLOR_MALE_GREEN: 'green.png',
    HAIR_COLOR_MALE_PINK: 'pink.png',
    HAIR_COLOR_MALE_RAVEN: 'raven.png',
    HAIR_COLOR_MALE_REDHEAD: 'redhead.png',
    HAIR_COLOR_MALE_WHITEBLOND: 'white-blonde.png',
}

# Constants for Hair Female Type
HAIR_TYPE_FEMALE_BALD = 0
HAIR_TYPE_FEMALE_BANGSLONG = 1
HAIR_TYPE_FEMALE_BANGSLONG2 = 2
HAIR_TYPE_FEMALE_BANGSSHORT = 3
HAIR_TYPE_FEMALE_BUNCHES = 4
HAIR_TYPE_FEMALE_LOOSE = 5
HAIR_TYPE_FEMALE_PIXIE = 6
HAIR_TYPE_FEMALE_PONYTAIL = 7
HAIR_TYPE_FEMALE_PONYTAIL2 = 8
HAIR_TYPE_FEMALE_PRINCESS = 9
HAIR_TYPE_FEMALE_SHOULDERL = 10
HAIR_TYPE_FEMALE_SHOULDERR = 11
HAIR_TYPE_FEMALE_SWOOP = 12
HAIR_TYPE_FEMALE_UNKEMPT = 13
HAIR_TYPE_FEMALE_CHOICES = (
    (HAIR_TYPE_FEMALE_BALD, 'Bald'),
    (HAIR_TYPE_FEMALE_BANGSLONG, 'Bangslong'),
    (HAIR_TYPE_FEMALE_BANGSLONG2, 'Bangslong2'),
    (HAIR_TYPE_FEMALE_BANGSSHORT, 'Bangsshort'),
    (HAIR_TYPE_FEMALE_BUNCHES, 'Bunches'),
    (HAIR_TYPE_FEMALE_LOOSE, 'Loose'),
    (HAIR_TYPE_FEMALE_PIXIE, 'Pixie'),
    (HAIR_TYPE_FEMALE_PONYTAIL, 'Ponytail'),
    (HAIR_TYPE_FEMALE_PONYTAIL2, 'Ponytail2'),
    (HAIR_TYPE_FEMALE_PRINCESS, 'Princess'),
    (HAIR_TYPE_FEMALE_SHOULDERL, 'Shoulder'),
    (HAIR_TYPE_FEMALE_SHOULDERR, 'Shoulder2'),
    (HAIR_TYPE_FEMALE_SWOOP, 'Swoop'),
    (HAIR_TYPE_FEMALE_UNKEMPT, 'Unkempt'),
)

# female helperdicts for get_hair_path function
HAIR_TYPE_FEMALE_DICT = {
    HAIR_TYPE_FEMALE_BANGSLONG: 'female/bangslong',
    HAIR_TYPE_FEMALE_BANGSLONG2: 'female/bangslong2',
    HAIR_TYPE_FEMALE_BANGSSHORT: 'female/bangsshort',
    HAIR_TYPE_FEMALE_BUNCHES: 'female/bunches',
    HAIR_TYPE_FEMALE_LOOSE: 'female/loose',
    HAIR_TYPE_FEMALE_PIXIE: 'female/pixie',
    HAIR_TYPE_FEMALE_PONYTAIL: 'female/ponytail',
    HAIR_TYPE_FEMALE_PONYTAIL2: 'female/ponytail2',
    HAIR_TYPE_FEMALE_PRINCESS: 'female/princess',
    HAIR_TYPE_FEMALE_SHOULDERL: 'female/shoulderl',
    HAIR_TYPE_FEMALE_SHOULDERR: 'female/shoulderr',
    HAIR_TYPE_FEMALE_SWOOP: 'female/swoop',
    HAIR_TYPE_FEMALE_UNKEMPT: 'female/unkempt',
}
HAIR_COLOR_FEMALE_DICT = {
    HAIR_COLOR_FEMALE_BLACK: 'black.png',
    HAIR_COLOR_FEMALE_BLONDE: 'blonde.png',
    HAIR_COLOR_FEMALE_BLONDE2: 'blonde2.png',
    HAIR_COLOR_FEMALE_BLUE: 'blue.png',
    HAIR_COLOR_FEMALE_BLUE2: 'blue2.png',
    HAIR_COLOR_FEMALE_BROWN: 'brown.png',
    HAIR_COLOR_FEMALE_BRUNETTE: 'brunette.png',
    HAIR_COLOR_FEMALE_BRUNETTE2: 'brunette2.png',
    HAIR_COLOR_FEMALE_DARKBLONDE: 'dark-blonde.png',
    HAIR_COLOR_FEMALE_GRAY: 'gray.png',
    HAIR_COLOR_FEMALE_GREEN: 'green.png',
    HAIR_COLOR_FEMALE_GREEN2: 'green2.png',
    HAIR_COLOR_FEMALE_LIGHTBLONDE: 'light-blonde.png',
    HAIR_COLOR_FEMALE_LIGHTBLONDE2: 'light-blonde2.png',
    HAIR_COLOR_FEMALE_PINK: 'pink.png',
    HAIR_COLOR_FEMALE_PINK2: 'pink2.png',
    HAIR_COLOR_FEMALE_RAVEN: 'raven.png',
    HAIR_COLOR_FEMALE_RAVEN2: 'raven2.png',
    HAIR_COLOR_FEMALE_REDHEAD: 'redhead.png',
    HAIR_COLOR_FEMALE_RUBYRED: 'ruby-red.png',
    HAIR_COLOR_FEMALE_WHITEBLONDE: 'white-blonde.png',
    HAIR_COLOR_FEMALE_WHITEBLONDE2: 'white-blonde2.png',
    HAIR_COLOR_FEMALE_WHITECYAN: 'white-cyan.png',
    HAIR_COLOR_FEMALE_WHITE: 'white.png',
}


def get_hair_path(sex, hair_type, hair_color):
    if sex == SEX_MALE:
        hair_type_txt = HAIR_TYPE_MALE_DICT.get(hair_type)
        hair_color_txt = HAIR_COLOR_MALE_DICT.get(hair_color)
    else:
        hair_type_txt = HAIR_TYPE_FEMALE_DICT.get(hair_type)
        hair_color_txt = HAIR_COLOR_FEMALE_DICT.get(hair_color)
    if hair_color_txt and hair_type_txt:
        return 'data/src/hair/%s/%s' % (hair_type_txt, hair_color_txt)


# Constants for Belts
BELT_DEFAULT = 0
BELT_CLOTH = 1
BELT_LEATHER = 2

# Return the belt imagepath according to the choosen sex, and type
BELT_DICT = {
    SEX_MALE: {
        BELT_DEFAULT: None,
        BELT_CLOTH: 'data/src/belt/cloth/male/white_cloth_male.png',
        BELT_LEATHER: 'data/src/belt/cloth/female/white_cloth_female.png'
    },
    SEX_FEMALE: {
        BELT_DEFAULT: None,
        BELT_CLOTH: 'data/src/belt/leather/male/leather_male.png',
        BELT_LEATHER: 'data/src/belt/leather/female/leather_female.png'
    }
}

# Constant for quiver. Allways used with bows.
QUIVER_PATH = 'data/src/equipment/quiver.png'

# Constants for feets
FEETS_DEFAULT = 0
FEETS_BLACK = 1
FEETS_BROWN = 2
FEETS_MAROON = 3
FEETS_METAL = 4
FEETS_GOLD = 5

# Return the feets Imagepath according to the choosen sex and type
FEETS_DICT = {
    SEX_MALE: {
        FEETS_DEFAULT: None,
        FEETS_BLACK: 'data/src/feet/shoes/male/black_shoes_male.png',
        FEETS_BROWN: 'data/src/feet/shoes/male/brown_shoes_male.png',
        FEETS_MAROON: 'data/src/feet/shoes/male/maroon_shoes_male.png',
        FEETS_METAL: 'data/src/feet/armor/male/metal_boots_male.png',
        FEETS_GOLD: 'data/src/feet/armor/male/golden_boots_male.png',
    },
    SEX_FEMALE: {
        FEETS_DEFAULT: None,
        FEETS_BLACK: 'data/src/feet/shoes/female/black_shoes_female.png',
        FEETS_BROWN: 'data/src/feet/shoes/female/brown_shoes_female.png',
        FEETS_MAROON: 'data/src/feet/shoes/female/maroon_shoes_female.png',
        FEETS_METAL: 'data/src/feet/armor/female/metal_boots_female.png',
        FEETS_GOLD: 'data/src/feet/armor/female/golden_boots_female.png',
    }
}

# Constants for hands
HANDS_DEFAULT = 0
HANDS_LEATHER = 1
HANDS_METAL = 2
HANDS_GOLD = 3

# Return the hands Imagepath according to the choosen sex and type
HANDS_DICT = {
    SEX_MALE: {
        HANDS_DEFAULT: None,
        HANDS_LEATHER: 'data/src/hands/bracers/male/leather_bracers_male.png',
        HANDS_METAL: 'data/src/hands/gloves/male/metal_gloves_male.png',
        HANDS_GOLD: 'data/src/hands/gloves/male/golden_gloves_male.png',
    },
    SEX_FEMALE: {
        HANDS_DEFAULT: None,
        HANDS_LEATHER: 'data/src/hands/bracers/female/leather_bracers_female.png',
        HANDS_METAL: 'data/src/hands/gloves/female/metal_gloves_female.png',
        HANDS_GOLD: 'data/src/hands/gloves/female/golden_gloves_female.png',
    }
}

# Constants for Legs
LEGS_CLOTH_WHITE = 0
LEGS_CLOTH_TEAL = 1
LEGS_CLOTH_RED = 2
LEGS_CLOTH_MAGENTA = 3
LEGS_ARMOR_METAL = 4
LEGS_ARMOR_GOLD = 5
LEGS_SKIRT = 6

# Return the legs Imagepath according to the choosen sex and type
LEGS_DICT = {
    SEX_MALE: {
        LEGS_CLOTH_WHITE: 'data/src/legs/pants/male/white_pants_male.png',
        LEGS_CLOTH_TEAL: 'data/src/legs/pants/male/teal_pants_male.png',
        LEGS_CLOTH_RED: 'data/src/legs/pants/male/red_pants_male.png',
        LEGS_CLOTH_MAGENTA: 'data/src/legs/pants/male/magenta_pants_male.png',
        LEGS_ARMOR_METAL: 'data/src/legs/armor/male/metal_pants_male.png',
        LEGS_ARMOR_GOLD: 'data/src/legs/armor/male/golden_greaves_male.png',
        LEGS_SKIRT: 'data/src/legs/skirt/male/robe_skirt_male.png',
    },
    SEX_FEMALE: {
        LEGS_CLOTH_WHITE: 'data/src/legs/pants/female/white_pants_female.png',
        LEGS_CLOTH_TEAL: 'data/src/legs/pants/female/teal_pants_female.png',
        LEGS_CLOTH_RED: 'data/src/legs/pants/female/red_pants_female.png',
        LEGS_CLOTH_MAGENTA: 'data/src/legs/pants/female/magenta_pants_female.png',
        LEGS_ARMOR_METAL: 'data/src/legs/armor/female/metal_pants_female.png',
        LEGS_ARMOR_GOLD: 'data/src/legs/armor/female/golden_greaves_female.png',
        LEGS_SKIRT: 'data/src/legs/skirt/female/robe_skirt_female.png',
    }
}

# Constants for Shoulder
ARMS_DEFAULT = 0
ARMS_LEATHER = 1
ARMS_PLATE = 2
ARMS_GOLD = 3

# Return the shoulder Imagepath according to the choosen sex and type
ARMS_DICT = {
    SEX_MALE: {
        ARMS_DEFAULT: None,
        ARMS_LEATHER: 'data/src/torso/leather/male/shoulders_male.png',
        ARMS_PLATE: 'data/src/torso/plate/male/arms_male.png',
        ARMS_GOLD: 'data/src/torso/gold/male/arms_male.png',
    },
    SEX_FEMALE: {
        ARMS_DEFAULT: None,
        ARMS_LEATHER: 'data/src/torso/leather/female/shoulders_female.png',
        ARMS_PLATE: 'data/src/torso/plate/female/arms_female.png',
        ARMS_GOLD: 'data/src/torso/gold/female/arms_female.png',
    },
}

# Constants for Torso
TORSO_CLOTH_WHITE = 0
TORSO_CLOTH_TEAL = 1
TORSO_CLOTH_MAROON = 2
TORSO_CLOTH_BROWN = 3
TORSO_LEATHER = 4
TORSO_CHAIN = 5
TORSO_PLATE = 6
TORSO_GOLD = 7

# Return the shoulder Imagepath according to the choosen sex and type
TORSO_DICT = {
    SEX_MALE: {
        TORSO_CLOTH_WHITE: 'data/src/torso/shirts/male/white_longsleeve.png',
        TORSO_CLOTH_TEAL: 'data/src/torso/shirts/male/teal_longsleeve.png',
        TORSO_CLOTH_MAROON: 'data/src/torso/shirts/male/maroon_longsleeve.png',
        TORSO_CLOTH_BROWN: 'data/src/torso/shirts/male/brown_longsleeve.png',
        TORSO_LEATHER: 'data/src/torso/leather/male/chest_male.png',
        TORSO_CHAIN: 'data/src/torso/chain/male/mail_male.png',
        TORSO_PLATE: 'data/src/torso/plate/male/chest_male.png',
        TORSO_GOLD: 'data/src/torso/gold/male/chest_male.png',
    },
    SEX_FEMALE: {
        TORSO_CLOTH_WHITE: 'data/src/torso/shirts/female/white_sleeveless.png',
        TORSO_CLOTH_TEAL: 'data/src/torso/shirts/female/teal_sleeveless.png',
        TORSO_CLOTH_MAROON: 'data/src/torso/shirts/female/maroon_sleeveless.png',
        TORSO_CLOTH_BROWN: 'data/src/torso/shirts/female/brown_sleeveless.png',
        TORSO_LEATHER: 'data/src/torso/leather/female/chest_female.png',
        TORSO_CHAIN: 'data/src/torso/chain/female/mail_female.png',
        TORSO_PLATE: 'data/src/torso/plate/female/chest_female.png',
        TORSO_GOLD: 'data/src/torso/gold/female/chest_female.png',
    },
}

# Constants for weapons
WEAPON_DEFAULT = 0
WEAPON_BOTH_HANDS_SPEAR = 1
WEAPON_LEFT_HAND_ARROW = 2
WEAPON_LEFT_HAND_SKELETON_ARROW = 3
WEAPON_LEFT_HAND_SHIELD_1 = 4
WEAPON_LEFT_HAND_SHIELD_2 = 5
WEAPON_RIGHT_HAND_BOW = 6
WEAPON_RIGHT_HAND_SKELETON_BOW = 7
WEAPON_RIGHT_HAND_DAGGER = 8
WEAPON_RIGHT_HAND_GREATBOW = 9
WEAPON_RIGHT_HAND_RECURVEBOW = 10
WEAPON_RIGHT_HAND_WOODWAND = 11

WEAPON_DICT = {
    SEX_MALE: {
        WEAPON_DEFAULT: None,
        WEAPON_BOTH_HANDS_SPEAR: 'data/src/weapons/right_hand/male/spear_male.png',
        WEAPON_LEFT_HAND_ARROW: 'data/src/weapons/left_hand/arrow.png',
        WEAPON_LEFT_HAND_SKELETON_ARROW: 'data/src/weapons/left_hand/arrow_skeleton.png',
        WEAPON_LEFT_HAND_SHIELD_1: 'data/src/weapons/left_hand/shield_male_cutoutforbody.png',
        WEAPON_LEFT_HAND_SHIELD_2: 'data/src/weapons/left_hand/shield_male_cutoutforhat.png',
        WEAPON_RIGHT_HAND_BOW: 'data/src/weapons/right hand/male/bow.png',
        WEAPON_RIGHT_HAND_SKELETON_BOW: 'data/src/weapons/right_hand/male/bow_skeleton.png',
        WEAPON_RIGHT_HAND_DAGGER: 'data/src/weapons/right_hand/male/dagger_male.png',
        WEAPON_RIGHT_HAND_GREATBOW: 'data/src/weapons/right_hand/male/greatbow.png',
        WEAPON_RIGHT_HAND_RECURVEBOW: 'data/src/weapons/right_hand/male/recurvebow.png',
        WEAPON_RIGHT_HAND_WOODWAND: 'data/src/weapons/right_hand/male/woodwand_male.png',
    },
    SEX_FEMALE: {
        WEAPON_DEFAULT: None,
        WEAPON_BOTH_HANDS_SPEAR: 'data/src/weapons/right_hand/female/spear_female.png',
        WEAPON_LEFT_HAND_ARROW: 'data/src/weapons/left_hand/arrow.png',
        WEAPON_LEFT_HAND_SKELETON_ARROW: 'data/src/weapons/left_hand/arrow_skeleton.png',
        WEAPON_LEFT_HAND_SHIELD_1: 'data/src/weapons/left_hand/shield_male_cutoutforbody.png',
        WEAPON_LEFT_HAND_SHIELD_2: 'data/src/weapons/left_hand/shield_male_cutoutforhat.png',
        WEAPON_RIGHT_HAND_BOW: 'data/src/weapons/right_hand/female/bow.png',
        WEAPON_RIGHT_HAND_SKELETON_BOW: 'data/src/weapons/right_hand/female/bow_skeleton.png',
        WEAPON_RIGHT_HAND_DAGGER: 'data/src/weapons/right_hand/female/dagger_female.png',
        WEAPON_RIGHT_HAND_GREATBOW: 'data/src/weapons/right_hand/female/greatbow.png',
        WEAPON_RIGHT_HAND_RECURVEBOW: 'data/src/weapons/right_hand/female/recurvebow.png',
        WEAPON_RIGHT_HAND_WOODWAND: 'data/src/weapons/right_hand/female/woodwand_female.png',
    }
}
