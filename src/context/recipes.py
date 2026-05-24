import pygame

import constants
import context
import draw.button
import game.craft


def init():
    # Create back button
    def back_event():
        context.handler.change_context(constants.Context.MAIN)
    
    back_pos = (constants.UI_GAP, constants.UI_GAP)
    back_size = (constants.UI_SLOT_HEIGHT, constants.UI_SLOT_HEIGHT)

    global back_button
    back_button = draw.button.ImageButton(
        image_filename='back.png',
        pos=back_pos,
        size=back_size,
        event=back_event,
        context=constants.Context.RECIPES)
    
    # Create search box
    global search_pos
    search_pos = (constants.RESOLUTION[0] // 4, constants.UI_GAP)
    search_size = (constants.RESOLUTION[0] // 2, constants.UI_SLOT_HEIGHT)

    global search_box
    search_box = pygame.Surface(search_size)

    search_box.fill(constants.Color.FG)
    search_box.fill(constants.Color.BLACK, (
        constants.UI_GAP,
        constants.UI_GAP,
        search_size[0] - constants.UI_GAP*2,
        search_size[1] - constants.UI_GAP*2))
    
    global search_text
    search_text = ''


def do(screen):
    back_button.draw(screen)
    screen.blit(search_box, search_pos)


def do_keypress(key):
    global search_text

    char = get_char(key)
    if char is None: return

    if char == '\b':
        search_text = search_text[:-1]
    else:
        search_text += char
    
    print(search_text)


def get_char(key):
    if key == pygame.K_SPACE:
        return ' '
    
    elif key == pygame.K_BACKSPACE:
        return '\b'
    
    elif pygame.K_a <= key <= pygame.K_z:
        return chr(key - pygame.K_a + ord('A'))

    else:
        return None
