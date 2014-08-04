# -*- coding: utf-8 -*-

import pygame

# Classes that build game objects
class HouseObj:

    def __init__(self, x,y,width,height,screen,colour,lineThickness, is_player):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.colour = colour
        self.lineThickness = lineThickness
        self.is_player = is_player

    def make(self):
        # start with an empty list
        self.points = []
        self.points.append((self.x,self.y- ((2/3.0) * self.height))) # top of 1st story, upper left
        self.points.append((self.x,self.y))  # lower left corner
        self.points.append((self.x+self.width,self.y)) # lower right corner
        self.points.append((self.x+self.width,self.y-(2/3.0) * self.height)) # top of 1st story upper right
        self.points.append((self.x,self.y- ((2/3.0) * self.height))) # top of first story, upper left
        self.points.append((self.x + self.width/2.0,self.y-self.height)) # top of roof
        self.points.append((self.x+self.width,self.y-(2/3.0)*self.height)) # top of 1st story, upper right
        return self.points

    def move(self):
        if self.is_player is False:
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

    def draw(self):
        pygame.draw.lines(self.screen, self.colour,
                        False, self.make(), self.lineThickness)


class SquareObj:

    def __init__(self, x,y,width,height,screen,colour,lineThickness, is_player):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.colour = colour
        self.lineThickness = lineThickness
        self.is_player = is_player

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
        if not self.is_player:
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

    def draw(self):
        pygame.draw.lines(self.screen, self.colour,
                            False, self.make(), self.lineThickness)

class TriangleObj:

    def __init__(self, x,y,width,height,screen, screenwh, colour,lineThickness, is_player):
        self.x = x
        self.y = y
        self.screenwh = screenwh
        self.width = width
        self.height = height
        self.screen = screen
        self.colour = colour
        self.lineThickness = lineThickness
        self.is_player = is_player
        self.myfont = pygame.font.SysFont("monospace", 12)
        self.firetxt = 'PewPew!'
        self.fire = False

    def make(self):
        self.points = [] # start with an empty list
        self.points.append((self.x,self.y- ((2/3.0) * self.height))) # top of 1st story, upper left
        self.points.append((self.x+self.width,self.y-(2/3.0) * self.height)) # top of 1st story upper right
        self.points.append((self.x,self.y- ((2/3.0) * self.height))) # top of first story, upper left
        self.points.append((self.x + self.width/2.0,self.y-self.height)) # top of roof
        self.points.append((self.x+self.width,self.y-(2/3.0)*self.height)) # top of 1st story, upper right
        return self.points

    def move(self):
        if not self.is_player:
            pass
        else:
            """ Handles Keys """
            key = pygame.key.get_pressed()
            dist = 10 # distance moved in 1 frame, try changing it to 5
            #if key[pygame.K_DOWN]: # down key
                #self.y += dist # move down
            if key[pygame.K_UP]: # up key
                self.fire = True
                self.firetxthud = self.myfont.render(self.firetxt, 2, self.colour)

            if key[pygame.K_RIGHT]: # right key
                if self.x >= self.screenwh[0]-64:
                    pass
                else:
                    self.x += dist # move right
            elif key[pygame.K_LEFT]: # left key
                if self.x <= 0+12:
                    pass
                else:
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
        #below is a placeholder for shooting stuff
        if self.fire is True:
            self.screen.blit(self.firetxthud, (self.x, self.y-72))
            self.fire = False


class EnemyWave:

    def __init__(self, screen, enemyColour, screenwh, count):
        self.count = count
        self.screen = screen
        self.enemyColour = enemyColour
        self.screenwh = screenwh
        self.x = 42
        self.y = 90
        self.width = 20
        self.height = 20
        self.enemies = []
        self.wave = self.make()


    def make(self):
        n = 0
        if self.enemies:
            pass
        else:
            for x in xrange(1, 5, 1):
                #print "creating row", n + 1
                n += 1
                for y in xrange(1, 13, 1):
                    self.enemyObj = SquareObj(self.x,self.y,self.width,self.height,self.screen,self.enemyColour,3, False)
                    self.enemies.append(self.enemyObj)
                    self.x += 30
                self.x = 42
                self.y += 30

            return self.enemies

    #def move(self):

    def draw(self):
        #print self.enemies
        for self.enemyObj in self.enemies:
            self.enemyObj.draw()