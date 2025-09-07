import pygame

import config
import constants
import event
import gamestate


# load config
config_dict = config.load()

resolution = constants.RESOLUTION
if config_dict['hidpi']:
    resolution = tuple(value * 2 for value in resolution)

display_flags = 0
if config_dict['fullscreen']:
    display_flags |= pygame.FULLSCREEN

# initialize pygame
pygame.init()
screen = pygame.display.set_mode(resolution, display_flags)
pygame.display.set_caption(constants.TITLE)

clock = pygame.time.Clock()

# initialize everything else
gamestate.init()


# main window loop
while gamestate.running:
    event.handle(pygame.event.get())

    pygame.display.flip()
    clock.tick(constants.FPS)
