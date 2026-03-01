import pygame

import constants
import draw.text
import game.item


tooltip_text = {}

def init():
    for item_id in game.item.item_dict.keys():
        tooltip_text[item_id] = draw.text.Text(
            text=game.item.get_name(item_id),
            size=40)


def draw_tooltip(screen, item_id):
    text = tooltip_text[item_id]

    surf = pygame.Surface(size=(
        text.width + 2 * constants.UI_GAP,
        text.height + 2 * constants.UI_GAP))

    surf.fill(constants.Color.BG)

    text.draw(surf, (constants.UI_GAP // 2, constants.UI_GAP // 2))
    
    pos = pygame.mouse.get_pos()
    offset_x = constants.UI_GAP
    if pos[0] > constants.RESOLUTION[0] // 2:
        offset_x = -(surf.get_width() + constants.UI_GAP)

    pos = (
        pos[0] + offset_x,
        pos[1] - surf.get_height() // 2
    )

    screen.blit(surf, pos)
