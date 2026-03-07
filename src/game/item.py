import json
import os

import pygame

import constants
import game.slot
import draw.sprite
import gamestate


with open(os.path.join('assets', 'data', 'items.json')) as file:
    item_dict = json.loads(file.read())

with open(os.path.join('assets', 'data', 'tools.json')) as file:
    tools = json.loads(file.read())

TOOL_SCALE = 24


def get_name(item_id):
    return item_dict[item_id]['name']

def get_img(item_id):
    filename = item_dict[item_id]['img']
    sprite = draw.sprite.load(filename)
    sprite = pygame.transform.scale(sprite, (
        constants.UI_ITEM_HEIGHT, constants.UI_ITEM_HEIGHT))
    
    if is_tool(item_id):
        tool_sprite = draw.sprite.load_without_scaling('tool.png')
        tool_sprite = pygame.transform.scale(
            tool_sprite,
            (TOOL_SCALE, TOOL_SCALE))

        sprite.blit(tool_sprite, (
            constants.UI_ITEM_HEIGHT - TOOL_SCALE,
            constants.UI_ITEM_HEIGHT - TOOL_SCALE))
    
    return sprite

def is_tool(item_id):
    return item_id in tools

MOUSE_OFFSET = 20

class Item:
    def __init__(self, item_id, slot_id):
        self.item_id = item_id
        self.slot_id = slot_id

        self.name = get_name(item_id)
        self.sprite = get_img(item_id)

        gamestate.items.append(self)
    
    def delete(self):
        if gamestate.mouse_item == self:
            gamestate.mouse_item = None

        self.slot_id = None
        gamestate.items.remove(self)
    
    def draw(self, screen):
        pos = (0, 0)

        if self.slot_id == 'mouse':
            pos = tuple(dim - MOUSE_OFFSET * constants.WINDOW_SCALE
                        for dim in pygame.mouse.get_pos())
        else:
            my_slot = None
            for slot in gamestate.ui_buttons[gamestate.current_context]:
                if (
                        isinstance(slot, game.slot.Slot)
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

