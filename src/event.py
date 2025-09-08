import pygame

import audio
import gamestate
import sprite



keys_pressed = {}

def draw_cursor(screen):
    offset_amt = 6  # cursor image is 11x11 px
    if gamestate.config['hidpi']:
        offset_amt *= 2

    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = tuple(pos - offset_amt for pos in mouse_pos)
    screen.blit(cursor_img, mouse_pos)


def handle(events):
    for event in events:
        if event.type == pygame.QUIT:
            gamestate.running = False
        
        elif event.type == pygame.KEYDOWN:
            keys_pressed[event.key] = True

            # Handle specific keypress
            if event.key == pygame.K_ESCAPE:
                gamestate.running = False

        elif event.type == pygame.KEYUP:
            keys_pressed[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # temp code
            if event.button == 1:
                audio.play('blip.ogg')
        
        elif event.type == pygame.MOUSEWHEEL:
            scroll_direction = event.y  # 1 or -1


def init():
    global cursor_img
    cursor_img = sprite.load('cursor.png')


def is_pressed(key):
    global keys_pressed
    if key in keys_pressed.keys():
        return keys_pressed[key]
    
    return False
