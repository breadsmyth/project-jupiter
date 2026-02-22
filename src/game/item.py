import json

import pygame

import constants
import draw.sprite


with open('assets/data/items.json') as file:
    item_dict = json.loads(file.read())


def get_name(id):
    return item_dict[id]['name']

def get_img(id):
    filename = item_dict[id]['img']
    sprite = draw.sprite.load(filename)
    sprite = pygame.transform.scale(sprite, (
        constants.UI_SLOT_HEIGHT, constants.UI_SLOT_HEIGHT))
    
    return sprite


class ItemStack:
    def __init__(self, id, quantity=1):
        self.id = id
        self.quantity = quantity

        self.name = get_name(id)
        self.sprite = get_img(id)
    
    def draw(self, screen):
        screen.blit(self.sprite, (100, 100))

