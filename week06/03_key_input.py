import RPi.GPIO as GPIO
from time import sleep #time 라이브러리의 sleep함수 사용
import numpy as np
import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((100, 100))
    
def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput [myKey]:
        ans = True
    pygame.display.update()

    return ans

def main():
    if getKey('LEFT'):
        print('Key Left was pressed')
    if getKey('RIGHT'):
        print('Key Right was pressed')
    if getKey('UP'):
        print('Key Up was pressed')
    if getKey('Down'):
        print('Key Up was pressed')


init()

while True:
    if getKey('LEFT'):
        print('Key Left was pressed')
    if getKey('RIGHT'):
        print('Key Right was pressed')
    if getKey('UP'):
        print('Key Up was pressed')
    if getKey('Down'):
        print('Key Up was pressed')
