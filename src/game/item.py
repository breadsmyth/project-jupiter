import json
import os

import pygame

import constants
import game.slot
import draw.sprite
import draw.text
import gamestate


def init():
    global item_dict
    with open(os.path.join('assets', 'data', 'items.json')) as file:
        item_dict = json.loads(file.read())

    global tools
    with open(os.path.join('assets', 'data', 'tools.json')) as file:
        tools = json.loads(file.read())
    
    global tool_sprite
    tool_sprite = draw.sprite.load_without_scaling('tool.png')
    tool_sprite = pygame.transform.scale(
        tool_sprite,
        (constants.UI_TOOL_SCALE, constants.UI_TOOL_SCALE))
    
    global wells
    with open(os.path.join('assets', 'data', 'wells.json')) as file:
        wells = json.loads(file.read())


def get_name(item_id):
    return item_dict[item_id]['name']

def get_img(item_id):
    filename = item_dict[item_id]['img']
    sprite = draw.sprite.load(filename)
    sprite = pygame.transform.scale(sprite, (
        constants.UI_ITEM_HEIGHT, constants.UI_ITEM_HEIGHT))
    
    if is_tool(item_id):
        sprite.blit(tool_sprite, (
            constants.UI_ITEM_HEIGHT - constants.UI_TOOL_SCALE,
            constants.UI_ITEM_HEIGHT - constants.UI_TOOL_SCALE))
    
    return sprite

def is_tool(item_id):
    return item_id in [elt[0] for elt in tools]

def get_num_tool_uses(item_id):
    for elt in tools:
        if elt[0] == item_id:
            return elt[1]
    
    raise KeyError(f'{item_id} is not a tool!')

def is_well(item_id):
    return item_id in [elt[0] for elt in wells]

def get_well_result(item_id):
    for elt in wells:
        if elt[0] == item_id:
            return elt[1:]

    raise KeyError(f'{item_id} is not a well!')

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
        pos = self.get_pos()
        draw.sprite.draw(
            screen,
            self.sprite,
            tuple(dim + constants.UI_GAP * 2 for dim in pos))
    
    def get_pos(self):
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

        return tuple(dim // constants.WINDOW_SCALE for dim in pos)


class Tool(Item):
    def __init__(self, item_id, slot_id, num_uses):
        super().__init__(item_id, slot_id)
        self.num_uses = num_uses
        self.update_text()

    
    def draw(self, screen):
        super().draw(screen)
        
        text_pos = self.get_pos()
        text_pos = (
            text_pos[0] + (2*constants.UI_GAP) // constants.WINDOW_SCALE,
            text_pos[1] + (
                constants.UI_ITEM_HEIGHT - constants.UI_GAP
            ) // constants.WINDOW_SCALE)

        if self.num_uses != -1:
            self.number_surf.draw(screen, text_pos)
    
    def update_text(self):
        self.number_surf = draw.text.Text(
            text=str(self.num_uses),
            size=24,
            color=constants.Color.WHITE,
            shadow_color=constants.Color.BLACK,
            shadow_distance=1)

    def use_once(self):
        if self.num_uses == -1: return

        self.num_uses -= 1
        if self.num_uses == 0:
            self.delete()
            return
        
        self.update_text()
