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
        config_toml = toml.dumps(DEFAULT_CONFIG)

        with open(CONFIG_PATH, 'w') as file:
            file.write(config_toml)
    
    # load config
    config_dict = toml.load(CONFIG_PATH)
    return config_dict
