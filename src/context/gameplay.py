import pygame

import constants
import context.handler
import draw.button
import draw.sprite
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
    
    # Create infinite random source
    source_pos = (
        GAME_AREA_WIDTH // 2 - constants.UI_SLOT_HEIGHT // 2,
        GAME_AREA_HEIGHT // 2 - constants.UI_SLOT_HEIGHT // 2)
    game.slot.Source(f'source_1', source_pos, [
        ('goo', 3), ('water', 1)])
    
    # Create well slots
    well_pos_0 = (
        GAME_AREA_WIDTH // 4 - constants.UI_SLOT_HEIGHT // 2,
        3*GAME_AREA_HEIGHT // 4 - constants.UI_SLOT_HEIGHT // 2)
    game.slot.WellSlot('well0', well_pos_0)

    well_pos_1 = (
        3*GAME_AREA_WIDTH // 4 - constants.UI_SLOT_HEIGHT // 2,
        3*GAME_AREA_HEIGHT // 4 - constants.UI_SLOT_HEIGHT // 2)
    game.slot.WellSlot('well1', well_pos_1)


    # Create trash slot
    trash_pos = (
        constants.RESOLUTION[0] - constants.UI_SLOT_HEIGHT - constants.UI_GAP,
        constants.RESOLUTION[1] - constants.UI_SLOT_HEIGHT - constants.UI_GAP)
    game.slot.TrashSlot('trash', trash_pos)

    # Create back button
    def back_event():
        context.handler.change_context(constants.Context.TITLE)
    
    global back_pos
    back_pos = (constants.UI_GAP, constants.UI_GAP)
    back_size = (constants.UI_SLOT_HEIGHT, constants.UI_SLOT_HEIGHT)

    back_btn = draw.button.Button(
        pos=back_pos,
        size=back_size,
        event=back_event,
        context=constants.Context.MAIN,
        audio='blip.ogg')
    
    global back_arrow
    back_arrow = draw.sprite.load('back.png')
    back_arrow = pygame.transform.scale(back_arrow, back_size)


def do(screen):
    # Draw back button
    screen.blit(back_arrow, back_pos)

    # Draw inventory panel
    screen.blit(inv_panel, (INV_LEFT, INV_TOP))

    # Draw all inventory slots
    for slot in gamestate.ui_buttons[constants.Context.MAIN]:
        if not isinstance(slot, game.slot.Slot): continue

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
