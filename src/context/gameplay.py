import pygame

import constants
import draw.sprite


def init():
    # Create inventory panel
    global inv_panel
    inv_panel = pygame.Surface((
        constants.RESOLUTION[0],
        constants.RESOLUTION[1] // 3
    ))

    inv_panel.fill(constants.Color.FG)


def do(screen):
    # Draw inventory panel
    screen.blit(inv_panel, (0, constants.RESOLUTION[1] // 3 * 2))