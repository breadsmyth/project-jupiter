import pygame

import audio
import constants
import game.craft
import game.item
import draw.button
import draw.sprite
import gamestate


# TODO isinstance is bad, maybe rethink logic


def item_pickup(slot):
    item = slot.get_item()

    gamestate.mouse_item = item
    item.slot_id = 'mouse'
    audio.play('pickup.ogg')

    # special logic, refill the source
    if isinstance(slot, Source):
        slot.spawn()


def item_put(slot):
    if gamestate.mouse_item is None: return

    # special logic, delete all items from trash
    if slot.name == 'trash':
        gamestate.mouse_item.delete()
        audio.play('trash.ogg')
        return

    gamestate.mouse_item.slot_id = slot.name
    gamestate.mouse_item = None
    audio.play('put.ogg')


def item_swap(slot):
    if gamestate.mouse_item is None:
        raise Exception('Tried to swap without holding an item')

    item = slot.get_item()

    temp = gamestate.mouse_item
    gamestate.mouse_item = item
    item.slot_id = 'mouse'
    temp.slot_id = slot.name
    audio.play('pickup.ogg')


def on_left_click(slot_name):
    slot = gamestate.slots[slot_name]
    item = slot.get_item()

    if item is None:
        # clkicked on an empty slot
        item_put(slot)
        return
    
    if gamestate.mouse_item is None:
        # picking up an item
        item_pickup(slot)
        return

    # special logic, can't put items into the source
    if isinstance(slot, Source): return

    # check for craft
    result = game.craft.check(
        item.item_id,
        gamestate.mouse_item.item_id)
    
    if result is not None:
        # do the craft
        gamestate.mouse_item.delete()
        item.delete()

        game.item.Item(result, slot.name)
        audio.play('put.ogg')
    else:
        item_swap(slot)


def on_right_click(slot_name):
    print(f'Right clicked slot {slot_name}')


class Slot(draw.button.Button):
    def __init__(self, name, pos):
        def left_click_event():
            on_left_click(self.name)

        def right_click_event():
            on_right_click(self.name)

        self.name = name

        super().__init__(
            pos=pos,
            size=(constants.UI_SLOT_HEIGHT, constants.UI_SLOT_HEIGHT),
            event=left_click_event,
            context=constants.Context.MAIN,
            audio=None,
            right_click_event=right_click_event)
        
        gamestate.slots[name] = self
        
        # draw the edges of the border in contrast
        self.surf.fill(constants.Color.WHITE)
        self.surf.fill(
            constants.Color.BLACK,
            pygame.Rect(
                0,
                0,
                constants.UI_SLOT_HEIGHT - constants.UI_GAP,
                constants.UI_SLOT_HEIGHT - constants.UI_GAP))

    def draw(self, surf):
        bg_color = constants.Color.FG
        if self.is_moused():
            bg_color = constants.Color.FG_ACTIVE
        
        self.inner_surf.fill(bg_color)

        surf.blit(self.surf, self.pos)
        surf.blit(self.inner_surf,
                  tuple(dim + constants.UI_GAP for dim in self.pos))
    
    def get_item(self):
        for item in gamestate.items:
            if item.slot_id == self.name:
                return item
        else:
            return None


class Source(Slot):
    def __init__(self, name, pos, item_id):
        super().__init__(name, pos)
        self.item_id = item_id

        # Add decoration to slot
        decoration = draw.sprite.load('slot_decoration.png')
        decoration = pygame.transform.scale(
            decoration,
            (constants.UI_SLOT_HEIGHT, constants.UI_SLOT_HEIGHT))
        
        self.surf.blit(decoration, (0, 0))

        # Spawn the item once
        self.spawn()
    
    def spawn(self):
        game.item.Item(self.item_id, self.name)


class TrashSlot(Slot):
    def __init__(self, name, pos):
        super().__init__(name, pos)
        self.surf = draw.sprite.load('trash.png')
        self.surf = pygame.transform.scale(
            self.surf,
            (constants.UI_SLOT_HEIGHT, constants.UI_SLOT_HEIGHT))

    def draw(self, surf):
        surf.blit(self.surf, self.pos)
