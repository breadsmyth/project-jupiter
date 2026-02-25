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


class ItemStack:
    def __init__(self, item_id, slot_id):
        self.item_id = item_id
        self.slot_id = slot_id

        self.name = get_name(item_id)
        self.sprite = get_img(item_id)

        gamestate.itemstacks.append(self)
    
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

