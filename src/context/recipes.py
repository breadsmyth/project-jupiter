import pygame

import constants
import context
import draw.button
import draw.sprite
import draw.text
import game.craft
import game.item


def init():
    global plus
    global equals

    plus = draw.sprite.load('plus.png')
    equals = draw.sprite.load('equals.png')

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

    global cached_text
    cached_text = ''

    global text_obj
    text_obj = draw.text.Text('', constants.UI_SLOT_HEIGHT)

    global cached_results
    cached_results = []


def do(screen):
    global cached_text
    global text_obj
    global cached_results

    back_button.draw(screen)
    screen.blit(search_box, search_pos)

    if cached_text != search_text:
        # Update caches
        text_obj = draw.text.Text(search_text, constants.UI_SLOT_HEIGHT)
        cached_text = search_text

        cached_results = find_results(search_text)

    # Draw search text
    text_obj.draw(screen, (
        search_pos[0] + constants.UI_GAP*2,
        search_pos[1] + constants.UI_GAP*2))
    
    # Draw search results
    for i, row in enumerate(cached_results[:6]):
        render_row(
            screen=screen,
            row=row,
            y_pos=i * (constants.UI_SLOT_HEIGHT + constants.UI_GAP*2) + 2*constants.UI_SLOT_HEIGHT)


def do_keypress(key):
    global search_text

    char = get_char(key)
    if char is None: return

    if char == '\b':
        search_text = search_text[:-1]
    else:
        search_text += char


def find_results(text):
    if len(text) < 1: return []

    results = []

    for result, ingredients in game.craft.crafting_dict.items():
        ing_name_a = game.item.item_dict[ingredients[0]]['name']
        ing_name_b = game.item.item_dict[ingredients[1]]['name']
        result_name = game.item.item_dict[result]['name']

        if text in result_name.upper() or text in ing_name_a.upper() or text in ing_name_b.upper():
            results.append((
                game.item.get_img(ingredients[0]),
                game.item.get_img(ingredients[1]),
                game.item.get_img(result)))
    
    return results


def get_char(key):
    if key == pygame.K_SPACE:
        return ' '
    
    elif key == pygame.K_BACKSPACE:
        return '\b'
    
    elif pygame.K_a <= key <= pygame.K_z:
        return chr(key - pygame.K_a + ord('A'))

    else:
        return None


def render_row(screen, row, y_pos):
    global plus
    global equals

    ing_a, ing_b, result = row

    screen.blit(ing_a, (constants.UI_SLOT_HEIGHT, y_pos))
    screen.blit(plus, (constants.RESOLUTION[0] // 4 + constants.UI_SLOT_HEIGHT // 2, y_pos))
    screen.blit(ing_b, ((constants.RESOLUTION[0] - constants.UI_SLOT_HEIGHT) // 2, y_pos))
    screen.blit(equals, (3*constants.RESOLUTION[0] // 4 - constants.UI_SLOT_HEIGHT, y_pos))
    screen.blit(result, (constants.RESOLUTION[0] - constants.UI_SLOT_HEIGHT*2, y_pos))
