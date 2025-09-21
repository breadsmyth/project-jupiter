import draw.button
import constants
import draw.text
    

def init():
    global START_BTN
    START_BTN = draw.button.Text_Button('Start', (100, 400), (500, 50))

    global TITLE_TEXT
    TITLE_TEXT = draw.text.Text(constants.TITLE, 100 * constants.WINDOW_SCALE)

    global TITLE_POS
    x = (constants.RESOLUTION[0] - TITLE_TEXT.width) // 2
    TITLE_POS = (x, 100 * constants.WINDOW_SCALE)


def title_screen(screen):
    # draw the title screen
    TITLE_TEXT.draw(screen, TITLE_POS)
    # screen.blit(TITLE_TEXT, TITLE_POS)

    START_BTN.draw(screen)
