import pygame
import math
import time
import numpy as np
from random import randint, choice
import os

if __name__ == '__main__':
    title='RL_fun'
    egzit = False
    pygame.init()
    pygame.key.set_repeat(50,50)
    pygame.font.init()
    window_size = (1200,900)
    interface = pygame.display.set_mode(window_size)
    pygame.display.set_caption('RL_fun')
    stage = 'editor'

    clock = pygame.time.Clock()

    while not egzit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                egzit = True

        pygame.display.update()
        clock.tick(24)
    pygame.quit()
    quit()
