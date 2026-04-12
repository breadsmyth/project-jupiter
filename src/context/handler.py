import constants
from context import credits, gameplay, recipes, splash, title
import gamestate


def change_context(new_context):
    gamestate.current_context = new_context


def handle(screen):
    match gamestate.current_context:
        case constants.Context.CREDITS:
            credits.do(screen)
        case constants.Context.MAIN:
            gameplay.do(screen)
        case constants.Context.RECIPES:
            recipes.do(screen)
        case constants.Context.SPLASH:
            splash.do(screen)
        case constants.Context.TITLE:
            title.do(screen)


def init():
    for context in constants.Context:
        gamestate.ui_buttons[context] = []

    credits.init()
    gameplay.init()
    recipes.init()
    splash.init()
    title.init()
