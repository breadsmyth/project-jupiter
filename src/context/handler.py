import constants
from context import gameplay, splash, title
import gamestate


def change_context(new_context):
    gamestate.current_context = new_context


def handle(screen):
    match gamestate.current_context:
        case constants.Context.MAIN:
            gameplay.do(screen)
        case constants.Context.SPLASH:
            splash.do(screen)
        case constants.Context.TITLE:
            title.do(screen)


def init():
    for context in constants.Context:
        gamestate.ui_buttons[context] = []

    gameplay.init()
    splash.init()
    title.init()
