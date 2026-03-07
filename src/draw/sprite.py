import os
import pygame

import constants
import gamestate


IMG_PATH = os.path.join('assets', 'img')


def draw(screen, image, pos):
    pos = (
        pos[0] * constants.WINDOW_SCALE,
        pos[1] * constants.WINDOW_SCALE)
    
    screen.blit(image, pos)


def load(filename):
    image = load_without_scaling(filename)

    if gamestate.config['hidpi']:
        image = pygame.transform.scale_by(image, constants.WINDOW_SCALE)

    return image

def load_without_scaling(filename):
    filepath = os.path.join(IMG_PATH, filename)
    image = pygame.image.load(filepath)
    image.convert_alpha()

    return image
