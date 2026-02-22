import pygame

import constants
import draw.button


def on_left_click(slot_name):
    print(f'Left clicked slot {slot_name}')

def on_right_click(slot_name):
    print(f'Right clicked slot {slot_name}')


class Slot(draw.button.Button):
    def __init__(self, name, pos):
        def left_click_event():
            on_left_click(self.name)

        def right_click_event():
            on_right_click(self.name)

        self.name = name

        super().__init__(
            pos=pos,
            size=(constants.UI_SLOT_HEIGHT, constants.UI_SLOT_HEIGHT),
            event=left_click_event,
            context=constants.Context.MAIN,
            audio=None,
            right_click_event=right_click_event)
        
        # draw the edges of the border in contrast
        self.surf.fill(constants.Color.WHITE)
        self.surf.fill(
            constants.Color.BLACK,
            pygame.Rect(
                0,
                0,
                constants.UI_SLOT_HEIGHT - constants.UI_GAP,
                constants.UI_SLOT_HEIGHT - constants.UI_GAP))

    def draw(self, surf):
        bg_color = constants.Color.FG
        if self.is_moused():
            bg_color = constants.Color.FG_ACTIVE
        
        self.inner_surf.fill(bg_color)

        surf.blit(self.surf, self.pos)
        surf.blit(self.inner_surf,
                  tuple(dim + constants.UI_GAP for dim in self.pos))
