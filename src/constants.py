import subprocess


current_hash = subprocess.run(
    ['git', 'rev-parse', '--short', 'HEAD'],
    capture_output=True,
    text=True).stdout[:-1]


class Color:
    BG = (30, 30, 46)
    FG = (205, 214, 244)
    BLUE = (116, 199, 236)
    BLACK = (24, 24, 37)

FPS = 30
RESOLUTION = (800, 800)
TITLE = 'Project Jupiter'
WINDOW_SCALE = 1
WINDOW_TITLE = f'{TITLE} ({current_hash})'
