import gzip
import json
import os

import game.item
import gamestate


SAVE_FILE = 'save.dat'

def load():
    if not os.path.exists(SAVE_FILE): return

    with gzip.open(SAVE_FILE, 'rb') as file:
        data = file.read()
    obj = json.loads(data.decode())

    for item in obj['items']:
        game.item.Item(item[0], item[1])


def save():
    obj = { 'items': [] }

    for item in gamestate.items:
        if item.slot_id.startswith('source'): continue
        obj['items'].append([item.item_id, item.slot_id])

    data = json.dumps(obj, separators=(',', ':')).encode()
    with gzip.open(SAVE_FILE, 'wb') as file:
        file.write(data)
