import pygame

import audio
import constants
import draw.button
import gamestate


def on_left_click(slot_name):
    slot = gamestate.slots[slot_name]
    item = slot.get_item()

    if item is None:
        # clkicked on an empty slot
        if gamestate.mouse_item is not None:
            # putting down an item
            gamestate.mouse_item.slot_id = slot_name
            gamestate.mouse_item = None
    
    else:
        if gamestate.mouse_item is None:
            # picking up an item
            gamestate.mouse_item = item
            item.slot_id = 'mouse'
            audio.play('pickup.ogg')

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
        
        gamestate.slots[name] = self
        
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
    
    def get_item(self):
        for item in gamestate.itemstacks:
            if item.slot_id == self.name:
                return item
        else:
            return None
