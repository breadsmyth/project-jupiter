import pygame

import constants
import gamestate
import game.item
import game.slot
import draw.tooltip


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

    GAME_AREA_WIDTH = constants.RESOLUTION[0]
    GAME_AREA_HEIGHT = constants.RESOLUTION[1] - INV_HEIGHT

    global INV_LEFT
    INV_LEFT = 0

    global INV_TOP
    INV_TOP = INV_HEIGHT * 2

    # Initialize
    game.item.init()
    draw.tooltip.init()

    inv_panel = pygame.Surface((INV_WIDTH, INV_HEIGHT))

    inv_panel.fill(constants.Color.FG)

    # Create inventory squares
    # 3 rows of 5 squares
    for row in range(3):
        for col in range(5):
            x = SQUARE_LEFT + col * (constants.UI_SLOT_HEIGHT + constants.UI_GAP)
            y = INV_TOP + constants.UI_GAP + row * (constants.UI_SLOT_HEIGHT + constants.UI_GAP)
            id = col + 5*row

            game.slot.Slot(f'inv_{id}', (x, y))
    
    # Create infinite source of Goo
    global source_pos
    source_pos = (
        GAME_AREA_WIDTH // 2 - constants.UI_SLOT_HEIGHT // 2,
        GAME_AREA_HEIGHT // 2 - constants.UI_SLOT_HEIGHT // 2)
    game.slot.Source(f'source_goo', source_pos, 'goo')

    # Create trash slot
    trash_pos = (
        constants.RESOLUTION[0] - constants.UI_SLOT_HEIGHT - constants.UI_GAP,
        constants.RESOLUTION[1] - constants.UI_SLOT_HEIGHT - constants.UI_GAP)
    game.slot.TrashSlot('trash', trash_pos)


def do(screen):
    # Draw inventory panel
    screen.blit(inv_panel, (INV_LEFT, INV_TOP))

    # Draw all inventory slots
    for slot in gamestate.ui_buttons[constants.Context.MAIN]:
        slot.draw(screen)

        item = slot.get_item()
        if item is not None:
            item.draw(screen)
    
    # Draw mouse item
    if gamestate.mouse_item is not None:
        gamestate.mouse_item.draw(screen)
    
    # Draw tooltip
    for slot in gamestate.slots.values():
        if slot.is_moused():
            item = slot.get_item()
            if item is not None:
                draw.tooltip.draw_tooltip(screen, item.item_id)

            break
