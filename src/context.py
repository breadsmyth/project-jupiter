import constants
import text
    

def init():
    global TITLE_SURF
    TITLE_SURF = text.write(constants.TITLE, 100 * constants.WINDOW_SCALE)

    global TITLE_POS
    x = (constants.RESOLUTION[0] - TITLE_SURF.get_width()) // 2
    TITLE_POS = (x, 100 * constants.WINDOW_SCALE)


def title_screen(screen):
    # draw the title screen
    screen.blit(TITLE_SURF, TITLE_POS)
