import pygame

import audio
import gamestate
import draw.sprite
import draw.tooltip



keys_pressed = {}

def do_drawables(screen):
    # draw tooltip
    for slot in gamestate.slots.values():
        if slot.is_moused():
            item = slot.get_item()
            if item is not None:
                draw.tooltip.draw_tooltip(screen, item.item_id)

            break

    # draw the cursor
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(cursor_img, mouse_pos)


def handle(events):
    for event in events:
        if event.type == pygame.QUIT:
            gamestate.running = False
        
        elif event.type == pygame.KEYDOWN:
            keys_pressed[event.key] = True

            # Handle specific keypress
            if event.key == pygame.K_ESCAPE:
                # gamestate.running = False
                pass

        elif event.type == pygame.KEYUP:
            keys_pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                # check to see whether the mouse is in a UI button
                for button in gamestate.ui_buttons[gamestate.current_context]:
                    if button.is_moused():
                        button.event()
                        
                        if button.audio is not None:
                            audio.play(button.audio)

            elif event.button == 3:  # right click
                # check to see whether the mouse is in a UI button
                for button in gamestate.ui_buttons[gamestate.current_context]:
                    if (button.is_moused()
                            and button.right_click_event is not None):
                        button.right_click_event()
                        
                        if button.audio is not None:
                            audio.play(button.audio)
        
        elif event.type == pygame.MOUSEWHEEL:
            scroll_direction = event.y  # 1 or -1


def init():
    global cursor_img
    cursor_img = draw.sprite.load('cursor.png')

    draw.tooltip.init()


def is_pressed(key):
    global keys_pressed
    if key in keys_pressed.keys():
        return keys_pressed[key]
    
    return False
