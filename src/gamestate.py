from config import load as load_config
import context


def init():
    global config
    config = load_config()

    global current_context
    current_context = context.splash_context

    global running
    running = True

    global time_elapsed
    time_elapsed = 0  # in milliseconds

    global ui_buttons
    ui_buttons = []
