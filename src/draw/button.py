import pygame

import constants


border_width = 10 * constants.WINDOW_SCALE

class Text_Button:
    def __init__(self, text_surf, pos, size, event):
        'Construct a textbutton where the button has'
        'position `pos` and size `size`'

        # account for hidpi
        size = (
            size[0] * constants.WINDOW_SCALE,
            size[1] * constants.WINDOW_SCALE)
        pos = (
            pos[0] * constants.WINDOW_SCALE,
            pos[1] * constants.WINDOW_SCALE)
        
        # verify the text will fit in the size
        if text_surf.width > size[0]:
            print(f'WARNING: Text {text_surf.text} too wide to fit in width {size[0]}!')
            size = (text_surf.width, size[1])

        if text_surf.height > size[1]:
            print(f'WARNING: Text {text_surf.text} too tall to fit in height {size[1]}!')
            size = (size[0], text_surf.height)
        
        # Construct the surface
        self.surf = pygame.Surface(size)
        self.surf.fill(constants.Color.FG)

        # add an inner box
        inner_size = tuple(dim - (border_width * 2) for dim in self.surf.get_size())
        self.inner_surf = pygame.Surface(inner_size)

        self.text_surf = text_surf
        self.pos = pos
        self.event = event

        # calculate text position
        self.text_pos = (
            pos[0] + (size[0] - text_surf.width) // 2,
            pos[1] + (size[1] - text_surf.height) // 2)

        # calculate bounding rect
        self.rect = self.surf.get_rect().move(*pos)
    
    def draw(self, surf):
        'Blit this button to surf'
        
        bg_color = constants.Color.BG
        if self.is_moused():
            bg_color = constants.Color.ACTIVE

        self.inner_surf.fill(bg_color)

        surf.blit(self.surf, self.pos)
        surf.blit(self.inner_surf,
                  tuple(dim + border_width for dim in self.pos))
        
        surf.blit(self.text_surf.surf, self.text_pos)
    
    def is_moused(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)
