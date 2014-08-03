# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Project: Byte Invaders
Concept: Retro space invader game with a twist

Author: abyssus.j@gmail.com

Status: incomplete
Todo: just about everything
'''

import pygame
import os
import sys
import time
import random


# Classes that define colours and stuff
class PaintBrush:

    def __init__(self):
        return

    def swatch(self):
        colours = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255),
                'darkBlue': (0,0,128), 'white': (255,255,255), 'black': (0,0,0),
                'pink': (255,51,102), 'yellow': (255,255,0)}
        return colours


# Classes that build game objects
class HouseObj:

    def __init__(self, x,y,width,height,screen,colour,lineThickness, isplayer):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.colour = colour
        self.lineThickness = lineThickness
        self.isplayer = isplayer
        return

    def make(self):
        self.points = [] # start with an empty list
        self.points.append((self.x,self.y- ((2/3.0) * self.height))) # top of 1st story, upper left
        self.points.append((self.x,self.y))  # lower left corner
        self.points.append((self.x+self.width,self.y)) # lower right corner
        self.points.append((self.x+self.width,self.y-(2/3.0) * self.height)) # top of 1st story upper right
        self.points.append((self.x,self.y- ((2/3.0) * self.height))) # top of first story, upper left
        self.points.append((self.x + self.width/2.0,self.y-self.height)) # top of roof
        self.points.append((self.x+self.width,self.y-(2/3.0)*self.height)) # top of 1st story, upper right
        return self.points

    def move(self):
        if self.isplayer is False:
            pass
        else:
            """ Handles Keys """
            key = pygame.key.get_pressed()
            dist = 0.5 # distance moved in 1 frame, try changing it to 5
            if key[pygame.K_DOWN]: # down key
                self.y += dist # move down
            elif key[pygame.K_UP]: # up key
                self.y -= dist # move up
            if key[pygame.K_RIGHT]: # right key
                self.x += dist # move right
            elif key[pygame.K_LEFT]: # left key
                self.x -= dist # move left
        return

    def draw(self):
        pygame.draw.lines(self.screen, self.colour,
                            False, self.make(), self.lineThickness)


class SquareObj:

    def __init__(self, x,y,width,height,screen,colour,lineThickness, isplayer):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.colour = colour
        self.lineThickness = lineThickness
        self.isplayer = isplayer
        return

    def make(self):
        self.points = [] # start with an empty list
        self.points.append((self.x,self.y- ((2/2) * self.height))) # top of 1st story, upper left
        self.points.append((self.x,self.y))  # lower left corner
        self.points.append((self.x+self.width,self.y)) # lower right corner
        self.points.append((self.x+self.width,self.y-(2/2) * self.height)) # top of 1st story upper right
        self.points.append((self.x,self.y- ((2/2) * self.height))) # top of first story, upper left
        self.points.append((self.x+self.width,self.y-(2/2)*self.height)) # top of 1st story, upper right
        return self.points

    def move(self):
        if self.isplayer is False:
            pass
        else:
            """ Handles Keys """
            key = pygame.key.get_pressed()
            dist = 0.5 # distance moved in 1 frame, try changing it to 5
            if key[pygame.K_DOWN]: # down key
                self.y += dist # move down
            elif key[pygame.K_UP]: # up key
                self.y -= dist # move up
            if key[pygame.K_RIGHT]: # right key
                self.x += dist # move right
            elif key[pygame.K_LEFT]: # left key
                self.x -= dist # move left
        return

    def draw(self):
        pygame.draw.lines(self.screen, self.colour,
                            False, self.make(), self.lineThickness)

class TriangleObj:

    def __init__(self, x,y,width,height,screen,colour,lineThickness, isplayer):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.colour = colour
        self.lineThickness = lineThickness
        self.isplayer = isplayer
        return

    def make(self):
        self.points = [] # start with an empty list
        self.points.append((self.x,self.y- ((2/3.0) * self.height))) # top of 1st story, upper left
        self.points.append((self.x+self.width,self.y-(2/3.0) * self.height)) # top of 1st story upper right
        self.points.append((self.x,self.y- ((2/3.0) * self.height))) # top of first story, upper left
        self.points.append((self.x + self.width/2.0,self.y-self.height)) # top of roof
        self.points.append((self.x+self.width,self.y-(2/3.0)*self.height)) # top of 1st story, upper right
        return self.points

    def move(self):
        if self.isplayer is False:
            pass
        else:
            """ Handles Keys """
            key = pygame.key.get_pressed()
            dist = 0.5 # distance moved in 1 frame, try changing it to 5
            #if key[pygame.K_DOWN]: # down key
                #self.y += dist # move down
            #elif key[pygame.K_UP]: # up key
                #elf.y -= dist # move up
            if key[pygame.K_RIGHT]: # right key
                self.x += dist # move right
            elif key[pygame.K_LEFT]: # left key
                self.x -= dist # move left
            '''if pressed[pygame.K_SPACE]:
                if reloaded:
                    shots.append(player.copy())
                    reloaded = False
                    # when shooting, create a timeout of RELOAD_SPEED
                    pygame.time.set_timer(reloaded_event, RELOAD_SPEED) '''
        return

    def draw(self):
        pygame.draw.lines(self.screen, self.colour,
                            False, self.make(), self.lineThickness)

class EnemyWave:

    def __init__(self, count):
        self.count = count
        self.x = 50
        self.y = 50
        self.width = 20
        self.height = 20
        self.enemies = []
        self.wave = self.make()
        return

    def make(self):
        n = 0
        if self.enemies is False:
            pass
        else:
            for x in xrange(1, 5, 1):
                print "creating row", n + 1
                n += 1
                for y in xrange(1, 12, 1):
                    self.enemyObj = SquareObj(self.x,self.y,self.width,self.height,screen,enemyColour,3, False)
                    self.enemies.append(self.enemyObj)
                    self.x += 30
                self.x = 50
                self.y += 30

            return self.enemies

    def move(self):
        return

    def draw(self):
        print self.enemies
        for self.enemyObj in self.enemies:
            self.enemyObj.draw()
        return

# Main game loop
if __name__ == "__main__":
    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

    pygame.init()

    clock = pygame.time.Clock()

    pygame.display.set_caption('Pewpew')
    pygame.mixer.music.load(os.path.join('sounds', 'nuttypc2.wav'))#load music

    screen = pygame.display.set_mode((424, 320))

    # play music non-stop
    pygame.mixer.music.play(-1)

    paint = PaintBrush()
    swatch = paint.swatch()

    bgColour = swatch['black']
    playerColour = swatch['green']
    enemyColour = swatch['red']
    textColour = swatch['yellow']

    enemyWave = EnemyWave(2)
    playerObj = TriangleObj(190,340,50,50,screen,playerColour,3, True)


    game_on = True

    while game_on is True:

       # check for quit events
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                  pygame.quit(); sys.exit();

        # game speed
        msElapsed = clock.tick(300)


        # erase the screen
        screen.fill(bgColour)


        # draw something
        playerObj.draw()
        playerObj.move()

        enemyWave.draw()

        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Welcome to byte invaders!", 1, textColour)
        screen.blit(label, (100, 5))


        # update the screen
        pygame.display.update()
