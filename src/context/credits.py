import pygame

import constants
import context.handler
import draw.button
import draw.sprite
import draw.text


def init():
    global CREDIT_WIDTH
    CREDIT_WIDTH = constants.RESOLUTION[0] // 2

    global CREDIT_HEIGHT
    CREDIT_HEIGHT = constants.RESOLUTION[1] * 3 // 7

    global surf_pygame
    surf_pygame = make_surf_pygame()

    global surf_font
    surf_font = make_surf_font()

    global surf_catppuccin
    surf_catppuccin = make_surf_catppuccin()

    global surf_me
    surf_me = make_surf_me()

    # Make back button
    btn_height = 50 * constants.WINDOW_SCALE
    height_offset = (constants.RESOLUTION[1] // 7 - btn_height) // 2

    def title_event():
        context.handler.change_context(constants.Context.TITLE)

    global btn_back
    back_text = draw.text.Text('Back', 50)
    btn_back = draw.button.Text_Button(
        text_surf=back_text,
        pos=(
            constants.RESOLUTION[0] // 4,
            CREDIT_HEIGHT * 2 + height_offset),
        size=(constants.RESOLUTION[0] // 2, btn_height),
        event=title_event,
        context=constants.Context.CREDITS)


def make_surf_pygame():
    surf = pygame.Surface(
        (CREDIT_WIDTH, CREDIT_HEIGHT),
        flags=pygame.SRCALPHA)

    img_width = CREDIT_WIDTH - 2 * constants.UI_GAP
    img = draw.sprite.load('pygame_powered.png')
    img_height = img_width * img.get_height() // img.get_width()

    img = pygame.transform.scale(img, (img_width, img_height))
    
    surf.blit(img, (constants.UI_GAP, 50 * constants.WINDOW_SCALE))

    text = draw.text.Text('Engine: pygame', 50)
    text.draw(surf, ((
        (CREDIT_WIDTH - text.width) // 2) // constants.WINDOW_SCALE,
        230))

    return surf

def make_surf_font():
    surf = pygame.Surface(
        (CREDIT_WIDTH, CREDIT_HEIGHT),
        flags=pygame.SRCALPHA)
    surf.fill(constants.Color.FG)

    return surf

def make_surf_catppuccin():
    surf = pygame.Surface(
        (CREDIT_WIDTH, CREDIT_HEIGHT),
        flags=pygame.SRCALPHA)
    surf.fill(constants.Color.PURPLE)

    return surf

def make_surf_me():
    surf = pygame.Surface(
        (CREDIT_WIDTH, CREDIT_HEIGHT),
        flags=pygame.SRCALPHA)
    surf.fill(constants.Color.WHITE)

    return surf


def do(screen):
    # screen.fill((0, 0, 0))

    screen.blit(surf_pygame, (0, 0))
    screen.blit(surf_font, (CREDIT_WIDTH, 0))
    screen.blit(surf_catppuccin, (0, CREDIT_HEIGHT))
    screen.blit(surf_me, (CREDIT_WIDTH, CREDIT_HEIGHT))

    btn_back.draw(screen)
