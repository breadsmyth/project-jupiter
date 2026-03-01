def check(item_id_a, item_id_b):
    if item_id_b < item_id_a:
        item_id_a, item_id_b = item_id_b, item_id_a
    
    print(f'Checking {item_id_a}, {item_id_b}')
