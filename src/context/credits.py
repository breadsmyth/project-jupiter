import pygame

import constants
import context.handler
import draw.button
import draw.sprite
import draw.text


TEXT_OFFSET = 230
TEXT_SIZE = 50

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
    back_text = draw.text.Text('Back', TEXT_SIZE)
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

    text = draw.text.Text('Engine: pygame', TEXT_SIZE)
    text.draw(surf, ((
        (CREDIT_WIDTH - text.width) // 2) // constants.WINDOW_SCALE,
        TEXT_OFFSET))

    return surf

def make_surf_font():
    surf = pygame.Surface(
        (CREDIT_WIDTH, CREDIT_HEIGHT),
        flags=pygame.SRCALPHA)
    
    IMG_GAP_X = 80 * constants.WINDOW_SCALE
    IMG_GAP_Y = 30 * constants.WINDOW_SCALE

    IMG_WIDTH = CREDIT_WIDTH - 2 * IMG_GAP_X
    IMG_HEIGHT = TEXT_OFFSET * constants.WINDOW_SCALE - 2 * IMG_GAP_Y

    surf.fill(
        color=constants.Color.FG,
        rect=pygame.Rect(
            IMG_GAP_X,
            IMG_GAP_Y,
            IMG_WIDTH // 2,
            IMG_HEIGHT))

    letter_A = draw.text.Text(
        'A',
        IMG_WIDTH // constants.WINDOW_SCALE,
        constants.Color.BG)
    letter_A_pos = (
        CREDIT_WIDTH // 2 - letter_A.width - constants.UI_GAP,
        IMG_HEIGHT + IMG_GAP_Y - letter_A.height - constants.UI_GAP)

    letter_a = draw.text.Text(
        'a',
        IMG_WIDTH // constants.WINDOW_SCALE)
    letter_a_pos = (
        CREDIT_WIDTH // 2 + constants.UI_GAP,
        IMG_HEIGHT + IMG_GAP_Y - letter_a.height - constants.UI_GAP)
    
    letter_A.draw(
        surf,
        tuple(dim // constants.WINDOW_SCALE for dim in letter_A_pos))
    letter_a.draw(
        surf,
        tuple(dim // constants.WINDOW_SCALE for dim in letter_a_pos))

    text = draw.text.Text('Font: C&C Red Alert', TEXT_SIZE)
    text.draw(surf, ((
        (CREDIT_WIDTH - text.width) // 2) // constants.WINDOW_SCALE,
        TEXT_OFFSET))

    return surf

def make_surf_catppuccin():
    surf = pygame.Surface(
        (CREDIT_WIDTH, CREDIT_HEIGHT),
        flags=pygame.SRCALPHA)

    img_width = CREDIT_WIDTH // 3
    img_top = (TEXT_OFFSET * constants.WINDOW_SCALE - img_width) // 2

    img = draw.sprite.load('catppuccin.png')
    img = pygame.transform.scale(img, (img_width, img_width))

    surf.blit(img, (img_width, img_top))

    text = draw.text.Text('Colors: Catppuccin', TEXT_SIZE)
    text.draw(surf, ((
        (CREDIT_WIDTH - text.width) // 2) // constants.WINDOW_SCALE,
        TEXT_OFFSET))

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
