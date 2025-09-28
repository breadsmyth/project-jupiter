import pygame

import audio
import constants
import draw.button
import draw.text
import event
import context
import gamestate


# load gamestate
gamestate.init()

if gamestate.config['hidpi']:
    constants.RESOLUTION = tuple(value * 2 for value in constants.RESOLUTION)
    constants.WINDOW_SCALE *= 2

resolution = constants.RESOLUTION

display_flags = 0
if gamestate.config['fullscreen']:
    display_flags |= pygame.FULLSCREEN

# initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(resolution, display_flags)
pygame.display.set_caption(constants.WINDOW_TITLE)

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

# initialize everything else
audio.init()
event.init()
draw.button.init()
draw.text.init()

context.init()


# Test code

# main window loop
while gamestate.running:
    screen.fill(constants.Color.BG)

    event.handle(pygame.event.get())

    context.handle(screen)

    event.draw_cursor(screen)

    pygame.display.flip()
    gamestate.time_elapsed += clock.tick(constants.FPS)
