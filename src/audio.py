import os
from pygame import mixer


AUDIO_PATH = os.path.join('assets', 'audio')

class Sound():
    def __init__(self, filename, maxtime):
        self.filename = filename
        self.maxtime = maxtime


sounds = {
    Sound('blip.ogg', maxtime=100)
}

cached_sounds = {}


def init():
    for sound_obj in sounds:
        sound = mixer.Sound(os.path.join(AUDIO_PATH, sound_obj.filename))

        def play_func():
            sound.play(maxtime=sound_obj.maxtime)

        cached_sounds[sound_obj.filename] = play_func


def play(filename):
    if filename not in cached_sounds.keys():
        raise KeyError(f'{filename} is not a valid sound!')

    cached_sounds[filename]()
