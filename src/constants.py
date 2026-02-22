from enum import Enum, auto
import subprocess


current_hash = subprocess.run(
    ['git', 'rev-parse', '--short', 'HEAD'],
    capture_output=True,
    text=True).stdout[:-1]


class Color:
    BG = (30, 30, 46)
    BG_ACTIVE = (64, 50, 77)
    FG = (205, 214, 244)
    FG_ACTIVE = (234, 238, 250)

    BLACK = (24, 24, 37)
    BLUE = (116, 199, 236)
    PURPLE = (203, 166, 247)
    WHITE = (255, 255, 255)


class Context(Enum):
    MAIN = auto()
    SPLASH = auto()
    TITLE = auto()


FPS = 30
RESOLUTION = (800, 800)
TITLE = 'Project Jupiter'
WINDOW_SCALE = 1
WINDOW_TITLE = f'{TITLE} ({current_hash})'

def ui_init():
    global UI_GAP
    UI_GAP = 5 * WINDOW_SCALE

    global UI_SLOT_HEIGHT
    UI_SLOT_HEIGHT = (RESOLUTION[1] // 3 - 4*UI_GAP) // 3

    global UI_ITEM_HEIGHT
    UI_ITEM_HEIGHT = UI_SLOT_HEIGHT - 4 * UI_GAP
