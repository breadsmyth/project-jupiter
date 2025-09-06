import pygame

import constants
import event
import gamestate

# initialize pygame
pygame.init()
screen = pygame.display.set_mode(constants.RESOLUTION)
pygame.display.set_caption(constants.TITLE)

clock = pygame.time.Clock()

# initialize everything else
gamestate.init()


# main window loop
while gamestate.running:
    event.handle(pygame.event.get())

    pygame.display.flip()
    clock.tick(constants.FPS)
