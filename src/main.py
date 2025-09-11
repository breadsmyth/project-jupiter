import pygame

import audio
import constants
import event
import gamestate
import text


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
text.init()


# Test code
title_surf = text.write('Project Juptier', 200)

# main window loop
while gamestate.running:
    screen.fill(constants.Color.BG)

    event.handle(pygame.event.get())

    screen.blit(title_surf, (100, 100))
    event.draw_cursor(screen)

    pygame.display.flip()
    clock.tick(constants.FPS)
