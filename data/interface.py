
import pygame




class UserHUDObj:

    def __init__(self, screen, textColour, playerscore, wavenum, playerlives):
        self.colour = textColour
        self.myfont = pygame.font.SysFont("monospace", 12)
        self.x = 10
        self.y = 46
        self.points = []
        self.screen = screen
        self.score = playerscore
        self.scoretxt = "Score"

        self.wavenum = wavenum
        self.wavetxt = "Wave"

        self.livesnum = playerlives
        self.livestxt = "Lives"

        self.textColour = textColour

    def make(self):
        self.scoretxthud = self.myfont.render(self.scoretxt, 1, self.textColour)
        self.scorenumhud = self.myfont.render(str(self.score), 1, self.textColour)

        self.wavetxthud = self.myfont.render(self.wavetxt, 1, self.textColour)
        self.wavenumhud = self.myfont.render(str(self.wavenum), 1, self.textColour)

        self.livestxthud = self.myfont.render(self.livestxt, 1, self.textColour)
        self.livesnumhud = self.myfont.render(str(self.livesnum), 1, self.textColour)

        self.points.append((self.x,self.y- ((2/3.0) * 20))) # top of 1st story, upper left
        self.points.append((self.x+414,self.y-(2/3.0) * 20)) # top of 1st story upper right
        return self.points

    def draw(self):
        pygame.draw.lines(self.screen, self.colour, False, self.points, 1)

        self.screen.blit(self.livestxthud, (334, 8))
        self.screen.blit(self.livesnumhud, (390, 8))

        self.screen.blit(self.scoretxthud, (184, 8))
        self.screen.blit(self.scorenumhud, (230, 8))

        self.screen.blit(self.wavetxthud, (34, 8))
        self.screen.blit(self.wavenumhud, (90, 8))




class GridBgOBJ:

    def __init__(self, screen, gridColour):
        self.screen = screen
        self.colour = gridColour
        self.grid = []
        self.linesh = []
        self.linesv = []

        self.hx = 12
        self.hstart = 0
        self.hy = 432
        self.hstop = 432

        self.vx1 = 0
        self.vy1 = 12
        self.vx2 = 432
        self.vy2 = 432


    def make(self):

        for i in xrange(36):
            self.points = []
            self.points.append((self.vx1,self.vy1))
            self.points.append((self.vx2,self.vy1))

            self.linesv.append(self.points)
            self.vy1 += 12

        for i in xrange(36):
            self.points = []
            self.points.append((self.hx,self.hstart))
            self.points.append((self.hx,self.hstop))

            self.linesh.append(self.points)
            self.hx += 12

        self.grid = self.linesh + self.linesv

        return self.grid


    def draw(self):
        for i in self.grid:
            pygame.draw.lines(self.screen, self.colour, False, i, 1)

