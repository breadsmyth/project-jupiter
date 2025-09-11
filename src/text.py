import os
from pygame import freetype

import constants


FONT_PATH = os.path.join('assets', 'Red_Alert.ttf')

def init():
    global font
    freetype.init()
    
    font = freetype.Font(FONT_PATH)


def write(text, size):
    surf, _ = font.render(text, constants.Color.FG, size=size)

    # surf.convert_alpha()
    return surf
