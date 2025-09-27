from config import load as load_config
import context


def init():
    global config
    config = load_config()

    global current_context
    current_context = context.title_context

    global running
    running = True

    global ui_buttons
    ui_buttons = []
