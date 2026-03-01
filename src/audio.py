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
    for filename in os.listdir(AUDIO_PATH):
        cached_sounds[filename] = Sound(filename, maxtime=100)


def play(filename):
    if filename not in cached_sounds.keys():
        raise KeyError(f"'{filename}' not found in {AUDIO_PATH}!")

    cached_sounds[filename].play()
