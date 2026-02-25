from config import load as load_config
import constants


def init():
    global config
    config = load_config()

    global current_context
    current_context = constants.Context.SPLASH

    global itemstacks
    itemstacks = []

    global mouse_item
    mouse_item = None

    global running
    running = True

    global slots
    slots = {}

    global time_elapsed
    time_elapsed = 0  # in milliseconds

    global ui_buttons
    ui_buttons = {}
