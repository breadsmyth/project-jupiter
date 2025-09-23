import os
from pygame import freetype

import constants


FONT_PATH = os.path.join('assets', 'Red_Alert.ttf')

def init():
    global font
    freetype.init()
    
    font = freetype.Font(FONT_PATH)


class Text:
    def __init__(self, text, size, color=constants.Color.FG):
        # account for hidpi
        size *= constants.WINDOW_SCALE

        self.surf, _ = font.render(
            text,
            color,
            size=size)
        
        self.width, self.height = self.surf.get_size()
        self.text = text
    
    def draw(self, surf, pos):
        # account for hidpi
        pos = (
            pos[0] * constants.WINDOW_SCALE,
            pos[1] * constants.WINDOW_SCALE)

        surf.blit(self.surf, pos)
