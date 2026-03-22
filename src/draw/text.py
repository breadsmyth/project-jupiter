import os
import pygame
from pygame import freetype

import constants


FONT_PATH = os.path.join('assets', 'Red_Alert.ttf')

def init():
    global font
    freetype.init()
    
    font = freetype.Font(FONT_PATH)


class Text:
    def __init__(self,
                 text,
                 size,
                 color=constants.Color.FG,
                 shadow_color=None,
                 shadow_distance=10):
        # account for hidpi
        size *= constants.WINDOW_SCALE

        self.shadow_color = shadow_color
        self.shadow_distance = shadow_distance * constants.WINDOW_SCALE

        self.surf, rect = font.render(
            text,
            color,
            size=size)
        
        if self.shadow_color is not None:
            shadow, _ = font.render(text, shadow_color, size=size)
            text_surf = self.surf.copy()

            self.surf = pygame.Surface((
                rect.size[0] + self.shadow_distance,
                rect.size[1] + self.shadow_distance),
                pygame.SRCALPHA)
            self.surf.convert_alpha()
            self.surf.fill((0, 0, 0, 0))

            self.surf.blit(shadow,
                           (self.shadow_distance, self.shadow_distance))
            self.surf.blit(text_surf, (0, 0))
        
        self.width, self.height = self.surf.get_size()
        self.text = text
    
    def draw(self, surf, pos):
        # account for hidpi
        pos = (
            pos[0] * constants.WINDOW_SCALE,
            pos[1] * constants.WINDOW_SCALE)

        surf.blit(self.surf, pos)
