import os
import pygame


IMG_PATH = os.path.join('assets', 'img')


def load(filename):
    filepath = os.path.join(IMG_PATH, filename)
    image = pygame.image.load(filepath)
    image.convert_alpha()

    return image