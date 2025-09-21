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
        self.surf, _ = font.render(
            text,
            color,
            size=size)
        
        self.width, self.height = self.surf.get_size()
    
    def draw(self, surf, pos):
        surf.blit(self.surf, pos)
