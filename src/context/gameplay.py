import pygame

import constants
import draw.sprite


def init():
    GAP_WIDTH = 10
    SQUARE_HEIGHT = (constants.RESOLUTION[1] // 3 - 4*GAP_WIDTH) // 3
    SQUARE_LEFT = (constants.RESOLUTION[0] - (5*SQUARE_HEIGHT + 4*GAP_WIDTH)) // 2

    # Create inventory panel
    global inv_panel
    inv_panel = pygame.Surface((
        constants.RESOLUTION[0],
        constants.RESOLUTION[1] // 3
    ))

    inv_panel.fill(constants.Color.FG)

    # Create inventory squares
    square_rect = pygame.Surface((SQUARE_HEIGHT, SQUARE_HEIGHT))
    square_rect.fill(constants.Color.BLACK)
    square_rect.fill(constants.Color.WHITE, pygame.Rect(
        GAP_WIDTH,
        GAP_WIDTH,
        SQUARE_HEIGHT - GAP_WIDTH,
        SQUARE_HEIGHT - GAP_WIDTH))
    square_rect.fill(constants.Color.FG, pygame.Rect(
        GAP_WIDTH,
        GAP_WIDTH,
        SQUARE_HEIGHT - 2*GAP_WIDTH,
        SQUARE_HEIGHT - 2*GAP_WIDTH))

    # 3 rows of 5 squares
    for row in range(3):
        for col in range(5):
            x = SQUARE_LEFT + col * (SQUARE_HEIGHT + GAP_WIDTH)
            y = GAP_WIDTH + row * (SQUARE_HEIGHT + GAP_WIDTH)
            inv_panel.blit(square_rect, (x, y))


def do(screen):
    # Draw inventory panel
    screen.blit(inv_panel, (0, constants.RESOLUTION[1] // 3 * 2))