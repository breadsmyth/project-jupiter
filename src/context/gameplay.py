import pygame

import constants
import gamestate
import draw.slot


def init():
    GAP_WIDTH = 5 * constants.WINDOW_SCALE
    SQUARE_HEIGHT = (constants.RESOLUTION[1] // 3 - 4*GAP_WIDTH) // 3
    SQUARE_LEFT = (constants.RESOLUTION[0] - (5*SQUARE_HEIGHT + 4*GAP_WIDTH)) // 2

    # Create inventory panel
    global inv_panel
    INV_WIDTH = constants.RESOLUTION[0]
    INV_HEIGHT = constants.RESOLUTION[1] // 3

    global INV_LEFT
    INV_LEFT = 0

    global INV_TOP
    INV_TOP = INV_HEIGHT * 2

    inv_panel = pygame.Surface((INV_WIDTH, INV_HEIGHT))

    inv_panel.fill(constants.Color.FG)

    # Create inventory squares
    # 3 rows of 5 squares
    for row in range(3):
        for col in range(5):
            x = SQUARE_LEFT + col * (SQUARE_HEIGHT + GAP_WIDTH)
            y = INV_TOP + GAP_WIDTH + row * (SQUARE_HEIGHT + GAP_WIDTH)
            # inv_panel.blit(square_rect, (x, y))
            draw.slot.Slot(
                f'{x} {y}',
                (x, y))


def do(screen):
    # Draw inventory panel
    screen.blit(inv_panel, (INV_LEFT, INV_TOP))

    # Draw all inventory slots
    for slot in gamestate.ui_buttons[constants.Context.MAIN]:
        slot.draw(screen)