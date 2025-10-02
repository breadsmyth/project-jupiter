import draw


def init():
    global PLAYER_IMG
    PLAYER_IMG = draw.sprite.load('peep.png')


def do(screen):
    draw.sprite.draw(screen, PLAYER_IMG, (100, 100))
