import os
import pygame

import gamestate


IMG_PATH = os.path.join('assets', 'img')


def load(filename):
    filepath = os.path.join(IMG_PATH, filename)
    image = pygame.image.load(filepath)
    image.convert_alpha()

    if gamestate.config['hidpi']:
        image = pygame.transform.scale_by(image, 2)

    return image