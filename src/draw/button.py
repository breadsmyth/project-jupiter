import pygame

import constants
import gamestate


class Button:
    "Base class for buttons"
    def __init__(self, pos, size, event, context):
        """Construct a button element.

        pos:        the position where this button will be drawn.
        size:       size of the element, will be expanded to cover
                    surf if needed.
        event:      function to be called when the button is clicked.
        context:    context.Context enum during which this button
                    is clickable.
        """

        # Construct the surface
        self.surf = pygame.Surface(size)
        self.surf.fill(constants.Color.FG)

        # add an inner box
        inner_size = tuple(dim - (constants.UI_GAP * 2) for dim in self.surf.get_size())
        self.inner_surf = pygame.Surface(inner_size)

        self.pos = pos
        self.event = event

        # calculate bounding rect
        self.rect = self.surf.get_rect().move(*pos)

        # add to buttons list for the current context
        gamestate.ui_buttons[context].append(self)
    
    def draw(self, surf):
        'Blit this button to surf'
        
        bg_color = constants.Color.BG
        if self.is_moused():
            bg_color = constants.Color.BG_ACTIVE

        self.inner_surf.fill(bg_color)

        surf.blit(self.surf, self.pos)
        surf.blit(self.inner_surf,
                  tuple(dim + constants.UI_GAP for dim in self.pos))
    
    def is_moused(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)


class Text_Button(Button):
    def __init__(self, text_surf, pos, size, event, context):
        """Construct a textbutton element.

        text_sutf:  surface containing the text to display.
        pos:        the position where this button will be drawn.
        size:       size of the element, will be expanded to cover
                    text_surf if needed.
        event:      function to be called when the button is clicked.
        context:    context.Context enum during which this button
                    is clickable.
        """

        # verify the text will fit in the size
        if text_surf.width > size[0]:
            print(f'WARNING: Text {text_surf.text} too wide to fit in width {size[0]}!')
            size = (text_surf.width, size[1])

        if text_surf.height > size[1]:
            print(f'WARNING: Text {text_surf.text} too tall to fit in height {size[1]}!')
            size = (size[0], text_surf.height)
        
        self.text_surf = text_surf

        # calculate text position
        self.text_pos = (
            pos[0] + (size[0] - text_surf.width) // 2,
            pos[1] + (size[1] - text_surf.height) // 2)
        
        super().__init__(pos, size, event, context)

    
    def draw(self, surf):
        'Blit this button to surf'
        super().draw(surf)
        surf.blit(self.text_surf.surf, self.text_pos)
