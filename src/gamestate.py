from config import load as load_config
import game_context


def init():
    global config
    config = load_config()

    global current_context
    current_context = game_context.title_screen

    global running
    running = True
