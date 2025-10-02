import pygame

import constants
from context import handler
import draw
import gamestate


def init():
    global SPLASH_IMG
    SPLASH_IMG = draw.sprite.load('pygame_powered.png')

    global SPLASH_POS
    SPLASH_POS = (
        (
            constants.RESOLUTION[0] - SPLASH_IMG.get_width()
        ) // (2*constants.WINDOW_SCALE),
        (
            constants.RESOLUTION[1] - SPLASH_IMG.get_height()
        ) // (2*constants.WINDOW_SCALE),
    )

    global SPLASH_OVERLAY
    SPLASH_OVERLAY = pygame.Surface(
        size=tuple(
            dim*constants.WINDOW_SCALE for dim in constants.RESOLUTION),
        flags=pygame.SRCALPHA,
    )
    SPLASH_OVERLAY.fill((0, 0, 0, 0))

def do(screen):
    screen.fill((0, 0, 0))
    draw.sprite.draw(screen, SPLASH_IMG, SPLASH_POS)
    
    # make the splash fade out
    if gamestate.time_elapsed >= 1000:
        alpha = min(255, int(
            (gamestate.time_elapsed - 1000)  # start fade-out at 1000ms
             / 1000  # fade-out lasta 1000ms
             * 255  # alpha goes from 0 to 255
        ))
        SPLASH_OVERLAY.fill((0, 0, 0, alpha))

    screen.blit(SPLASH_OVERLAY, (0, 0))

    if gamestate.time_elapsed > 2000:
        handler.change_context(constants.Context.TITLE)
