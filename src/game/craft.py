import json
import os


with open(os.path.join('assets', 'data', 'alias.json')) as file:
    alias_dict = json.loads(file.read())

with open(os.path.join('assets', 'data', 'crafting.json')) as file:
    crafting_dict = json.loads(file.read())


def check(item_id_a, item_id_b):
    if item_id_a in alias_dict.keys():
        item_id_a = alias_dict[item_id_a]
    if item_id_b in alias_dict.keys():
        item_id_b = alias_dict[item_id_b]
    
    if item_id_b < item_id_a:
        item_id_a, item_id_b = item_id_b, item_id_a
    
    for result, ingredients in crafting_dict.items():
        if ingredients[0] == item_id_a and ingredients[1] == item_id_b:
            return result
    
    return None
