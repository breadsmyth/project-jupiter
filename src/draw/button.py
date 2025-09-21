import pygame

import constants


class Text_Button:
    def __init__(self, text_surf, pos, size):
        'Construct a textbutton where the button has'
        'position `pos` and size `size`'
        
        # First, verify the text will fit in the size
        if text_surf.width > size[0]:
            print(f'WARNING: Text {text_surf.text} too wide to fit in width {size[0]}!')
            size = (text_surf.width, size[1])

        if text_surf.height > size[1]:
            print(f'WARNING: Text {text_surf.text} too tall to fit in height {size[1]}!')
            size = (size[0], text_surf.height)
        
        # Construct the surface
        self.surf = pygame.Surface(size)
        self.surf.fill(constants.Color.WHITE)

        self.pos = pos
    
    def draw(self, surf):
        'Blit this button to surf'
        surf.blit(self.surf, self.pos)
