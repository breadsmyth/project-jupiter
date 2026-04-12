import pygame

import constants
import context
import draw.button


def init():
    # Create back button
    def back_event():
        context.handler.change_context(constants.Context.MAIN)
    
    global back_pos
    back_pos = (constants.UI_GAP, constants.UI_GAP)
    back_size = (constants.UI_SLOT_HEIGHT, constants.UI_SLOT_HEIGHT)

    draw.button.Button(
        pos=back_pos,
        size=back_size,
        event=back_event,
        context=constants.Context.RECIPES,
        audio='blip.ogg')
    
    global back_arrow
    back_arrow = draw.sprite.load('back.png')
    back_arrow = pygame.transform.scale(back_arrow, back_size)


def do(screen):
    screen.blit(back_arrow, back_pos)
