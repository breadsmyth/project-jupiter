import subprocess


current_hash = subprocess.run(
    ['git', 'rev-parse', '--short', 'HEAD'],
    capture_output=True,
    text=True).stdout[:-1]


FPS = 30
RESOLUTION = (800, 800)
TITLE = f'Project Juptier ({current_hash})'
