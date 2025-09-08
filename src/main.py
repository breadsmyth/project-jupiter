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

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

# initialize everything else
gamestate.init()
event.init()


# main window loop
while gamestate.running:
    screen.fill((20, 20, 40))

    event.handle(pygame.event.get())

    event.draw_cursor(screen)

    pygame.display.flip()
    clock.tick(constants.FPS)
