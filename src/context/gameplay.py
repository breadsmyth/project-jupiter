import pygame

import constants
import game.item
import gamestate
import draw.slot


def init():
    SQUARE_LEFT = (
        constants.RESOLUTION[0] - (
            5*constants.UI_SLOT_HEIGHT + 4*constants.UI_GAP
        )
    ) // 2

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
            x = SQUARE_LEFT + col * (constants.UI_SLOT_HEIGHT + constants.UI_GAP)
            y = INV_TOP + constants.UI_GAP + row * (constants.UI_SLOT_HEIGHT + constants.UI_GAP)
            id = col + 5*row

            draw.slot.Slot(f'inv_{id}', (x, y))
    
    # Test code
    global TEST_ITEMS
    TEST_ITEMS = []
    TEST_ITEMS.append(game.item.ItemStack('goo', 'mouse', quantity=10))
    TEST_ITEMS.append(game.item.ItemStack('goo', 'inv_3', quantity=2))


def do(screen):
    # Draw inventory panel
    screen.blit(inv_panel, (INV_LEFT, INV_TOP))

    # Draw all inventory slots
    for slot in gamestate.ui_buttons[constants.Context.MAIN]:
        slot.draw(screen)
    
    # Test: draw the items
    for item in TEST_ITEMS:
        item.draw(screen)