import random

import pygame

import audio
import constants
import game.craft
import game.item
import draw.button
import draw.sprite
import gamestate


def item_pickup(slot):
    item = slot.get_item()

    gamestate.mouse_item = item
    item.slot_id = 'mouse'
    audio.play('pickup.ogg')


def item_put(slot):
    if gamestate.mouse_item is None: return

    # special logic, delete all items from trash
    if slot.name == 'trash':
        gamestate.mouse_item.delete()
        audio.play('trash.ogg')
        return
    
    # special logic, only put Well into WellSlot
    if isinstance(slot, WellSlot):
        if not game.item.is_well(gamestate.mouse_item.item_id): return

    gamestate.mouse_item.slot_id = slot.name
    gamestate.mouse_item = None
    audio.play('put.ogg')


def item_swap(slot):
    if gamestate.mouse_item is None:
        raise Exception('Tried to swap without holding an item')

    item = slot.get_item()

    # special logic, only put Well into WellSlot
    if isinstance(slot, WellSlot):
        if not game.item.is_well(gamestate.mouse_item.item_id): return

    temp = gamestate.mouse_item
    gamestate.mouse_item = item
    item.slot_id = 'mouse'
    temp.slot_id = slot.name
    audio.play('pickup.ogg')


def new_item(item_id, slot_id):
    if game.item.is_tool(item_id):
        num_uses = game.item.get_num_tool_uses(item_id)
        return game.item.Tool(item_id, slot_id, num_uses)

    return game.item.Item(item_id, slot_id)


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
    if isinstance(slot, Source):
        print('game.slot.on_left_click(): Should not be possible')
        return

    # check for craft
    result = game.craft.check(
        item.item_id,
        gamestate.mouse_item.item_id)
    
    if result is not None:
        # do the craft
        if game.item.is_tool(gamestate.mouse_item.item_id):
            item.delete()
            new_item(result, slot.name)

            gamestate.mouse_item.use_once()
            audio.play('use_tool.ogg')
        
        elif game.item.is_tool(item.item_id):
            gamestate.mouse_item.delete()
            gamestate.mouse_item = new_item(result, 'mouse')

            item.use_once()
            audio.play('use_tool.ogg')

        else:
            item.delete()
            gamestate.mouse_item.delete()
            new_item(result, slot.name)
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
        
        plus = draw.sprite.load('plus.png')
        self.plus = pygame.transform.scale(
            plus,
            (constants.UI_ITEM_HEIGHT, constants.UI_ITEM_HEIGHT))
        
        self.surf.blit(decoration, (0, 0))

        def on_left_click():
            self.spawn()
        
        self.event = on_left_click

    def draw(self, surf):
        bg_color = constants.Color.BG
        if self.is_moused():
            bg_color = constants.Color.BG_ACTIVE
        
        self.inner_surf.fill(bg_color)
        self.inner_surf.blit(
            self.plus,
            (constants.UI_GAP, constants.UI_GAP))

        surf.blit(self.surf, self.pos)
        surf.blit(self.inner_surf,
                  tuple(dim + constants.UI_GAP for dim in self.pos))
    
    def spawn(self):
        if gamestate.mouse_item is not None:
            return

        gamestate.mouse_item = new_item(self.item_id, 'mouse')
        audio.play('pickup.ogg')


class WellSource(Source):
    def __init__(self, name, pos):
        super().__init__(name, pos, None)
        self.well_slot = name[7:]  # evil
    
    def draw(self, surf):
        if self.get_well_slot().get_item() is None: return
        super().draw(surf)
    
    def get_well_slot(self):
        return gamestate.slots[self.well_slot]

    def spawn(self):
        well_item = self.get_well_slot().get_item()
        if well_item is None: return

        result = game.item.get_well_result(well_item.item_id)
        self.item_id = random.choice(result)
        super().spawn()


class TrashSlot(Slot):
    def __init__(self, name, pos):
        super().__init__(name, pos)
        self.surf = draw.sprite.load('trash.png')
        self.surf = pygame.transform.scale(
            self.surf,
            (constants.UI_SLOT_HEIGHT, constants.UI_SLOT_HEIGHT))

    def draw(self, surf):
        surf.blit(self.surf, self.pos)


class WellSlot(Slot):
    def __init__(self, name, pos):
        super().__init__(name, pos)
    
    def draw(self, surf):
        outline_color = constants.Color.FG

        # If well in mouse, draw with green outline
        if (gamestate.mouse_item is not None
                and game.item.is_well(gamestate.mouse_item.item_id)):
            outline_color = constants.Color.GREEN

        elif self.get_item() is None:
            return

        # Draw
        bg_color = constants.Color.BG
        if self.is_moused():
            bg_color = constants.Color.BG_ACTIVE

        self.surf.fill(outline_color)
        self.inner_surf.fill(bg_color)

        surf.blit(self.surf, self.pos)
        surf.blit(self.inner_surf,
                  tuple(dim + constants.UI_GAP for dim in self.pos))
