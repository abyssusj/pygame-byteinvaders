# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Project: Byte Invaders
Concept: Retro space invader game with a twist

Author: abyssus dot <nospamkkty> j at gmail dot com

Status: incomplete
Todo: just about everything
'''
# installed python libaries
import pygame
import os
import sys
import time
import random

# local custom libaries
from data import cosmetics
from data import interface
from data import objects


# Main game loop
if __name__ == "__main__":
    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

    pygame.init()

    clock = pygame.time.Clock()

    pygame.display.set_caption('Python Byte Invaders')
    pygame.mixer.music.load(os.path.join('data','sounds', 'nuttypc2.wav'))#load music

    screenwh = [432, 423]
    screen = pygame.display.set_mode((screenwh[0], screenwh[1]))

    # play music non-stop
    pygame.mixer.music.play(-1)

    paint = cosmetics.PaintBrush()
    swatch = paint.swatch()

    bgColour = swatch['black']
    gridColour = swatch['vdarkBlue']
    playerColour = swatch['green']
    enemyColour = swatch['red']
    textColour = swatch['yellow']

    enemyWave = objects.EnemyWave(screen, enemyColour, screenwh, 2)

    playerObj = objects.TriangleObj(190,440,50,50,screen,screenwh,playerColour,3, True)

    playerscore = 0
    wavenum = 1
    playerlives = 3

    playerHUD = interface.UserHUDObj(screen,textColour, playerscore, wavenum, playerlives)
    gridBg = interface.GridBgOBJ(screen, gridColour)
    gridBg.make()

    game_on = True

    while game_on is True:

       # check for quit events
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                  pygame.quit(); sys.exit();

        # game speed
        msElapsed = clock.tick(15)


        # erase the screen
        screen.fill(bgColour)

        # draw something
        gridBg.draw()
        playerHUD.make()
        playerHUD.draw()

        playerObj.draw()
        playerObj.move()

        enemyWave.draw()

        # update the screen
        pygame.display.update()
