import layermanager
import pygame
import window
import player
import enemy
import config
import random


class Background(layermanager.Layer):
    def __init__(self,screen):
        layermanager.Layer.__init__(self)
        self.background = pygame.image.load("art/background.png")
        self.backgroundRect = self.background.get_rect()
        self.sky = pygame.image.load("art/sky.png")
        self.skyRect = self.sky.get_rect()
        self.grass = pygame.image.load("art/grass.png")
        self.grassRect = self.grass.get_rect()
        self.font = pygame.font.Font(pygame.font.match_font("Verdana"), 40)
        self.sublist = []
        self.windowHealth = [[1,1,1,1,0,0,0,0], #Can move onto 1's can't move to 0's
                            [1,1,1,1,1,0,0,0], #Rotated so x,y coordinates are correct
                            [1,1,1,1,1,0,0,0],
                            [1,1,1,1,1,1,0,0],
                            [1,1,1,1,1,1,0,0],
                            [1,1,1,1,1,1,1,0],
                            [1,1,1,1,1,1,1,0],
                            [1,1,1,1,1,1,1,1]]
        self.windowGrid = []
        self.enemies = []
        self.balloons = []
        self.setupWindows()
        self.player = player.Player(self,[random.randrange(7),random.randrange(4)])
        self.sublist.append(self.player)
        self.setupEnemies() 
        self.gameRunning = True

    def setupWindows(self):    
        for i in range(8):
            temp = []
            for j in range(8):                
                if (i == 0 and j == 4) or (i == 2 and j == 5) or (i == 4 and j == 6) or (i == 6 and j == 7):
                    self.sublist.append(window.Window((3+(i*127),60+(j*79)),-1))                
                else:
                    self.sublist.append(window.Window((3+(i*127),60+(j*79)),self.windowHealth[i][j]))
                temp.append(self.sublist[-1])
            self.windowGrid.append(temp)
    
    def setupEnemies(self):
        #Test enemy, most enemies wont be added until later in the level
        self.enemies.append(enemy.Enemy(self, 0))
        self.enemies.append(enemy.Enemy(self, 1))

    def HandleEvent(self, event):
        if self.gameRunning == False:
            return True
        for i in self.sublist:
            i.HandleEvent(event)
        for i in self.enemies:
            i.HandleEvent(event)

    def Update(self):
        if self.gameRunning == False:
            return True
        for i in self.sublist:
            if i.Update() == False:
                self.gameRunning = False
        for i in self.enemies:
            i.Update()
        for i in self.balloons:
            j = i.Update()
            if j == True:
                self.balloons.remove(i)
         
        for i in self.balloons:
            if pygame.sprite.collide_rect(self.player, i):
                self.balloons.remove(i)
                self.player.life -= 1.0
                if self.player.life == 0.0:
                    self.gameRunning = False
        

    def Render(self, screen):          
        screen.blit(self.background,self.backgroundRect)
        screen.blit(self.sky,self.skyRect)
        for i in self.sublist:
            i.Render(screen)
        screen.blit(self.grass,self.grassRect) 
        if self.gameRunning == False:
            return True
        for i in self.enemies:
            i.Render(screen)
        for i in self.balloons:
            i.Render(screen)
        scoreText = self.font.render(str(config.score), 1, (0, 0, 0))
        rect = scoreText.get_rect()
        rect.center = (100,700)
        screen.blit(scoreText, rect)