import gamestate


flags = {
    'injector': 'source_slime',
}

def check_unlock(item):
    if item not in flags.keys(): return
    if get_flag_state(item): return

    gamestate.progress_flags[item] = True
    do_unlock(flags[item])


def do_unlock(source_name):
    print(f'Unlocking {source_name}!')


def get_flag_state(flag):
    if flag not in gamestate.progress_flags.keys():
        return False
    
    return gamestate.progress_flags[flag]
