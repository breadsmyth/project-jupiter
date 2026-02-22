import pygame

import constants
import draw.button


class Slot(draw.button.Button):
    def __init__(self, name, pos):
        def slot_event():
            return

        self.name = name

        super().__init__(
            pos=pos,
            size=(constants.UI_SLOT_HEIGHT, constants.UI_SLOT_HEIGHT),
            event=slot_event,
            context=constants.Context.MAIN)
        
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
