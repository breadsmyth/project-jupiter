import constants
import context
import draw.button
import game.craft


def init():
    # Create back button
    def back_event():
        context.handler.change_context(constants.Context.MAIN)
    
    back_pos = (constants.UI_GAP, constants.UI_GAP)
    back_size = (constants.UI_SLOT_HEIGHT, constants.UI_SLOT_HEIGHT)

    global back_button
    back_button = draw.button.ImageButton(
        image_filename='back.png',
        pos=back_pos,
        size=back_size,
        event=back_event,
        context=constants.Context.RECIPES)
    

def do(screen):
    back_button.draw(screen)
