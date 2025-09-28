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
    filepath = os.path.join(IMG_PATH, filename)
    image = pygame.image.load(filepath)
    image.convert_alpha()

    if gamestate.config['hidpi']:
        image = pygame.transform.scale_by(image, 2)

    return image
