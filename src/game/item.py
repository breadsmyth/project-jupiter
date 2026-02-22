import json

import pygame

import constants
import draw.slot
import draw.sprite
import draw.text
import gamestate


with open('assets/data/items.json') as file:
    item_dict = json.loads(file.read())


ITEM_FONT_SIZE = 50

def get_name(item_id):
    return item_dict[item_id]['name']

def get_img(item_id):
    filename = item_dict[item_id]['img']
    sprite = draw.sprite.load(filename)
    sprite = pygame.transform.scale(sprite, (
        constants.UI_ITEM_HEIGHT, constants.UI_ITEM_HEIGHT))
    
    return sprite

def make_quantity_text(quantity):
    if quantity == 1: return None

    return draw.text.Text(
        text=str(quantity),
        size=ITEM_FONT_SIZE,
        color=constants.Color.BLACK)


class ItemStack:
    def __init__(self, item_id, slot_id, quantity=1):
        self.item_id = item_id
        self.slot_id = slot_id
        self.quantity = quantity

        self.name = get_name(item_id)
        self.sprite = get_img(item_id)

        self.quantity_text = make_quantity_text(self.quantity)
    
    def draw(self, screen):
        pos = (0, 0)

        if self.slot_id == 'mouse':
            pos = pygame.mouse.get_pos()
        else:
            my_slot = None
            for slot in gamestate.ui_buttons[gamestate.current_context]:
                if (
                        isinstance(slot, draw.slot.Slot)
                        and slot.name == self.slot_id):
                    my_slot = slot
                    break
            else:
                raise Exception(f"Slot {self.slot_id} does not exist!")
            
            pos = my_slot.pos

        pos = tuple(dim // constants.WINDOW_SCALE for dim in pos)

        draw.sprite.draw(
            screen,
            self.sprite,
            tuple(dim + constants.UI_GAP for dim in pos))

        if self.quantity_text is not None:
            self.quantity_text.draw(screen, (
                pos[0] + (constants.UI_ITEM_HEIGHT - len(str(self.quantity))*ITEM_FONT_SIZE//2) // constants.WINDOW_SCALE,
                pos[1] + (constants.UI_ITEM_HEIGHT - ITEM_FONT_SIZE//2) // constants.WINDOW_SCALE))

