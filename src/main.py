import pygame

import audio
import constants
import event
import game_context
import gamestate
import text


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
text.init()

game_context.init()


# Test code

# main window loop
while gamestate.running:
    screen.fill(constants.Color.BG)

    event.handle(pygame.event.get())

    gamestate.current_context(screen)

    event.draw_cursor(screen)

    pygame.display.flip()
    clock.tick(constants.FPS)
