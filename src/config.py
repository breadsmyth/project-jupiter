import toml
import os


CONFIG_PATH = 'config.toml'

DEFAULT_CONFIG = {
    'fullscreen': False,
    'hidpi': False
}


def load():
    if not os.path.exists(CONFIG_PATH):
        # create the default config
        with open(CONFIG_PATH, 'w') as file:
            toml.dump(DEFAULT_CONFIG, file)
    
    # load config
    config_dict = toml.load(CONFIG_PATH)
    return config_dict
