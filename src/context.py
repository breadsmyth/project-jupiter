import draw.button
import constants
import gamestate
import draw.text
    

def change_context(new_context):
    gamestate.ui_buttons.clear()
    gamestate.current_context = new_context


def main_context(screen):
    pass


def init():
    # Title screen
    global TITLE_TEXT
    TITLE_TEXT = draw.text.Text(constants.TITLE, 100)

    global TITLE_POS
    x = (constants.RESOLUTION[0] - TITLE_TEXT.width) // 2
    TITLE_POS = (x // constants.WINDOW_SCALE, 100)

    def start_event():
        change_context(main_context)

    global START_BTN
    START_TEXT = draw.text.Text('Start', 50)
    START_BTN = draw.button.Text_Button(
        text_surf=START_TEXT,
        pos=(TITLE_POS[0], 400),
        size=(TITLE_TEXT.width // constants.WINDOW_SCALE, 50),
        event=start_event)
    
    def quit_event():
        gamestate.running = False

    global QUIT_BTN
    QUIT_TEXT = draw.text.Text('Quit', 50)
    QUIT_BTN = draw.button.Text_Button(
        text_surf=QUIT_TEXT,
        pos=(TITLE_POS[0], 500),
        size=(TITLE_TEXT.width // constants.WINDOW_SCALE, 50),
        event=quit_event)


def title_context(screen):
    # draw the title screen
    TITLE_TEXT.draw(screen, TITLE_POS)
    # screen.blit(TITLE_TEXT, TITLE_POS)

    START_BTN.draw(screen)
    QUIT_BTN.draw(screen)
