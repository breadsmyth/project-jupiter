import os
from pygame import mixer


AUDIO_PATH = os.path.join('assets', 'audio')

class Sound():
    def __init__(self, filename, maxtime):
        self.filename = filename
        self.maxtime = maxtime

        self.sound = mixer.Sound(os.path.join(AUDIO_PATH, filename))

    def play(self):
        self.sound.play(maxtime=self.maxtime)


cached_sounds = {}

def init():
    sounds = [
        Sound('blip.ogg', maxtime=100),
        Sound('pickup.ogg', maxtime=100),
        Sound('put.ogg', maxtime=100),
        Sound('trash.ogg', maxtime=100),
    ]

    for sound_obj in sounds:
        cached_sounds[sound_obj.filename] = sound_obj


def play(filename):
    if filename not in cached_sounds.keys():
        raise KeyError(f'{filename} is not a valid sound!')

    cached_sounds[filename].play()
