import pygame

import constants


class Text_Button:
    def __init__(self, text, pos, size):
        'Construct a textbutton where the button has'
        'position `pos` and size `size`'
        self.surf = pygame.Surface(size)
        self.surf.fill(constants.Color.WHITE)

        self.pos = pos
    
    def draw(self, surf):
        'Blit this button to surf'
        surf.blit(self.surf, self.pos)
