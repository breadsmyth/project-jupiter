import pygame

import audio
import constants
import event
import gamestate


# load gamestate
gamestate.init()

resolution = constants.RESOLUTION
if gamestate.config['hidpi']:
    resolution = tuple(value * 2 for value in resolution)

display_flags = 0
if gamestate.config['fullscreen']:
    display_flags |= pygame.FULLSCREEN

# initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(resolution, display_flags)
pygame.display.set_caption(constants.TITLE)

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

# initialize everything else
audio.init()
event.init()


# main window loop
while gamestate.running:
    screen.fill((20, 20, 40))

    event.handle(pygame.event.get())

    event.draw_cursor(screen)

    pygame.display.flip()
    clock.tick(constants.FPS)
