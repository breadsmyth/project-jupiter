from config import load as load_config


def init():
    global config
    config = load_config()

    global running
    running = True
