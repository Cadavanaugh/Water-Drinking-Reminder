from pygame import mixer
from random import randint
from time import sleep
from os import system, name
from datetime import datetime

def som(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

interval = randint(1,1800) #A random interval from 1s to 30min

system('cls' if name == 'nt' else 'clear')

while True:
    sleep(interval)
    time = datetime.now().strftime("%H:%M:%S")
    print(f"Water drank at {time}")
    som('Water sound effect.mp3')
    sleep(6) #Sound effect takes 6s to finish