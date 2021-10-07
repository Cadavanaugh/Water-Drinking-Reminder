from pygame import mixer
from random import randint
from time import sleep

def som(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

interval = randint(1,1800)

while True:
    som()
    sleep(interval)