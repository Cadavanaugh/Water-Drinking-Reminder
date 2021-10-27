from pygame import mixer
from random import randint, seed
from time import sleep
from os import system, name
from datetime import datetime
from time import time

def som(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

system('cls' if name == 'nt' else 'clear')
print("="*10,"WATER DRINKING REMINDER","="*10)

x = 0 
while True:
    seed(time()) # Create true randomness
    interval = randint(1,1800) # A random interval from 1s to 30min
    sleep(interval)
    clock = datetime.now().strftime("%H:%M:%S")
    
    x+=1
    print(f"Water drank at {clock} [{x}]")
    som('Water sound effect.mp3')
    sleep(6) # Sound effect takes 6s to finish