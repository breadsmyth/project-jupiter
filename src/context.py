from enum import Enum, auto

import pygame

import draw.button
import constants
import gamestate
import draw.sprite
import draw.text
    

class Context(Enum):
    MAIN = auto()
    SPLASH = auto()
    TITLE = auto()


def change_context(new_context):
    gamestate.current_context = new_context


def handle(screen):
    match gamestate.current_context:
        case Context.MAIN:
            main_context(screen)
        case Context.SPLASH:
            splash_context(screen)
        case Context.TITLE:
            title_context(screen)


def init():
    for context in Context:
        gamestate.ui_buttons[context] = []

    init_main()
    init_splash()
    init_title()


def init_main():
    global PLAYER_IMG
    PLAYER_IMG = draw.sprite.load('peep.png')


def init_splash():
    global SPLASH_IMG
    SPLASH_IMG = draw.sprite.load('pygame_powered.png')

    global SPLASH_POS
    SPLASH_POS = (
        (
            constants.RESOLUTION[0] - SPLASH_IMG.get_width()
        ) // (2*constants.WINDOW_SCALE),
        (
            constants.RESOLUTION[1] - SPLASH_IMG.get_height()
        ) // (2*constants.WINDOW_SCALE),
    )

    global SPLASH_OVERLAY
    SPLASH_OVERLAY = pygame.Surface(
        size=tuple(
            dim*constants.WINDOW_SCALE for dim in constants.RESOLUTION),
        flags=pygame.SRCALPHA,
    )
    SPLASH_OVERLAY.fill((0, 0, 0, 0))


def init_title():
    global TITLE_TEXT
    TITLE_TEXT = draw.text.Text(constants.TITLE, 100)

    global TITLE_POS
    x = (constants.RESOLUTION[0] - TITLE_TEXT.width) // 2
    TITLE_POS = (x // constants.WINDOW_SCALE, 100)

    def start_event():
        change_context(Context.MAIN)

    global START_BTN
    START_TEXT = draw.text.Text('Start', 50)
    START_BTN = draw.button.Text_Button(
        text_surf=START_TEXT,
        pos=(TITLE_POS[0], 400),
        size=(TITLE_TEXT.width // constants.WINDOW_SCALE, 50),
        event=start_event,
        context=Context.TITLE,
    )
    
    def quit_event():
        gamestate.running = False

    global QUIT_BTN
    QUIT_TEXT = draw.text.Text('Quit', 50)
    QUIT_BTN = draw.button.Text_Button(
        text_surf=QUIT_TEXT,
        pos=(TITLE_POS[0], 500),
        size=(TITLE_TEXT.width // constants.WINDOW_SCALE, 50),
        event=quit_event,
        context=Context.TITLE,
    )


def main_context(screen):
    draw.sprite.draw(screen, PLAYER_IMG, (100, 100))


def splash_context(screen):
    screen.fill((0, 0, 0))
    draw.sprite.draw(screen, SPLASH_IMG, SPLASH_POS)
    
    # make the splash fade out
    if gamestate.time_elapsed >= 1000:
        alpha = min(255, int(
            (gamestate.time_elapsed - 1000)  # start fade-out at 1000ms
             / 1000  # fade-out lasta 1000ms
             * 255  # alpha goes from 0 to 255
        ))
        SPLASH_OVERLAY.fill((0, 0, 0, alpha))

    screen.blit(SPLASH_OVERLAY, (0, 0))

    if gamestate.time_elapsed > 2000:
        change_context(Context.TITLE)


def title_context(screen):
    # draw the title screen
    TITLE_TEXT.draw(screen, TITLE_POS)
    # screen.blit(TITLE_TEXT, TITLE_POS)

    START_BTN.draw(screen)
    QUIT_BTN.draw(screen)
