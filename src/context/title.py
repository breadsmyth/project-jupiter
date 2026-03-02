import constants
from context import handler
import draw.button
import draw.text
import gamestate


def init():
    global TITLE_TEXT
    TITLE_TEXT = draw.text.Text(constants.TITLE, 100)

    global TITLE_POS
    x = (constants.RESOLUTION[0] - TITLE_TEXT.width) // 2
    TITLE_POS = (x // constants.WINDOW_SCALE, 100)

    def start_event():
        handler.change_context(constants.Context.MAIN)

    BTN_WIDTH = constants.RESOLUTION[0] // 2
    BTN_LEFT = constants.RESOLUTION[0] // 4

    global START_BTN
    START_TEXT = draw.text.Text('Start', 50)
    START_BTN = draw.button.Text_Button(
        text_surf=START_TEXT,
        pos=(BTN_LEFT, 400 * constants.WINDOW_SCALE),
        size=(BTN_WIDTH, 50 * constants.WINDOW_SCALE),
        event=start_event,
        context=constants.Context.TITLE,
    )

    def credits_event():
        handler.change_context(constants.Context.CREDITS)

    global CREDITS_BTN
    CREDITS_TEXT = draw.text.Text('Credits', 50)
    CREDITS_BTN = draw.button.Text_Button(
        text_surf=CREDITS_TEXT,
        pos=(BTN_LEFT, 500 * constants.WINDOW_SCALE),
        size=(BTN_WIDTH, 50 * constants.WINDOW_SCALE),
        event=credits_event,
        context=constants.Context.TITLE,
    )
    
    def quit_event():
        gamestate.running = False

    global QUIT_BTN
    QUIT_TEXT = draw.text.Text('Quit', 50)
    QUIT_BTN = draw.button.Text_Button(
        text_surf=QUIT_TEXT,
        pos=(BTN_LEFT, 600 * constants.WINDOW_SCALE),
        size=(BTN_WIDTH, 50 * constants.WINDOW_SCALE),
        event=quit_event,
        context=constants.Context.TITLE,
    )


def do(screen):
    # draw the title screen
    TITLE_TEXT.draw(screen, TITLE_POS)

    START_BTN.draw(screen)
    CREDITS_BTN.draw(screen)
    QUIT_BTN.draw(screen)
