import pygame

from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self,background,position):
        self.player = pygame.image.load("art/player.png")
        self.playerRect = self.player.get_rect()
        self.rect = self.playerRect
        self.attack = pygame.image.load("art/attack.png").convert_alpha()
        self.attackRect = self.attack.get_rect()
        self.background = background
        self.positionOffset = [53,72]
        self.window = position
        self.pressed = {"d":0,"a":0,"w":0,"s":0,"space":0}
        self.moveRight = True
        self.moveleft = False
        self.moveUp = False
        self.moveDown = True
        self.jumpRight = True
        self.jumpLeft = False
        self.jumpUp = False
        self.jumpDown = True
        self.life = 5.0

    def HandleEvent(self, event):
        if event.type == KEYUP:
            if event.key == K_d:
                self.pressed["d"] = 0
            if event.key == K_a:
                self.pressed["a"] = 0
            if event.key == K_w:
                self.pressed["w"] = 0
            if event.key == K_s:
                self.pressed["s"] = 0
            if event.key == K_SPACE:
                self.pressed["space"] = 0

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                if self.window[0] < 7 and self.background.windowGrid[self.window[0]+1][self.window[1]].health > 0:
                    self.background.windowGrid[self.window[0]+1][self.window[1]].attackWindow()
                    return
            if event.key == K_LEFT:
                if self.window[0] > 0 and self.background.windowGrid[self.window[0]-1][self.window[1]].health > 0:
                    self.background.windowGrid[self.window[0]-1][self.window[1]].attackWindow()
                    return
            if event.key == K_UP:
                if self.window[1] > 0 and self.background.windowGrid[self.window[0]][self.window[1]-1].health > 0:
                    self.background.windowGrid[self.window[0]][self.window[1]-1].attackWindow()
                    return
            if event.key == K_DOWN:
                if self.window[1] < 7 and self.background.windowGrid[self.window[0]][self.window[1]+1].health > 0:
                    self.background.windowGrid[self.window[0]][self.window[1]+1].attackWindow()
                    return

            if event.key == K_d:
                self.pressed["d"] = 1
            if event.key == K_a:
                self.pressed["a"] = 1
            if event.key == K_w:
                self.pressed["w"] = 1
            if event.key == K_s:
                self.pressed["s"] = 1
            if event.key == K_SPACE:
                if self.pressed["d"] == 0 and self.pressed["a"] == 0 and self.pressed["w"] == 0 and self.pressed["s"] == 0:
                    self.pressed["space"] = 1
                else:
                    return

            if self.pressed["space"]:
                if self.pressed["d"] and self.pressed["space"]:
                    if self.window[0] < 6 and self.background.windowGrid[self.window[0]+2][self.window[1]].health > 0:
                        self.window[0]+=2
                if self.pressed["a"] and self.pressed["space"]:
                    if self.window[0] > 1 and self.background.windowGrid[self.window[0]-2][self.window[1]].health > 0:
                        self.window[0]-=2
                if self.pressed["w"] and self.pressed["space"]:
                    if self.window[1] > 1 and self.background.windowGrid[self.window[0]][self.window[1]-2].health > 0:
                        self.window[1]-=2
                if self.pressed["s"] and self.pressed["space"]:
                    if self.window[1] < 6 and self.background.windowGrid[self.window[0]][self.window[1]+2].health > 0:
                        self.window[1]+=2
            else:
                if self.pressed["d"]:
                    if self.window[0] < 7 and self.background.windowGrid[self.window[0]+1][self.window[1]].health > 0:
                        self.window[0]+=1
                if self.pressed["a"]:
                    if self.window[0] > 0 and self.background.windowGrid[self.window[0]-1][self.window[1]].health > 0:
                        self.window[0]-=1
                if self.pressed["w"]:
                    if self.window[1] > 0 and self.background.windowGrid[self.window[0]][self.window[1]-1].health > 0:
                        self.window[1]-=1
                if self.pressed["s"]:
                    if self.window[1] < 7 and self.background.windowGrid[self.window[0]][self.window[1]+1].health > 0:
                        self.window[1]+=1
            



    def Update(self):
        if (self.window[0] < 6 and self.background.windowGrid[self.window[0]+2][self.window[1]].health > 0):
            self.jumpRight = True
        else:
            self.jumpRight = False
        if (self.window[0] > 1 and self.background.windowGrid[self.window[0]-2][self.window[1]].health > 0):
            self.jumpLeft = True
        else:
            self.jumpLeft = False
        if (self.window[1] > 1 and self.background.windowGrid[self.window[0]][self.window[1]-2].health > 0):
            self.jumpUp = True
        else:
            self.jumpUp = False
        if (self.window[1] < 6 and self.background.windowGrid[self.window[0]][self.window[1]+2].health > 0):
            self.jumpDown = True
        else:
            self.jumpDown = False
        if (self.window[0] < 7 and self.background.windowGrid[self.window[0]+1][self.window[1]].health > 0):
            self.moveRight = True
        else:
            self.moveRight = False
        if (self.window[0] > 0 and self.background.windowGrid[self.window[0]-1][self.window[1]].health > 0):
            self.moveLeft = True
        else:
            self.moveLeft = False
        if (self.window[1] > 0 and self.background.windowGrid[self.window[0]][self.window[1]-1].health > 0):
            self.moveUp = True
        else:
            self.moveUp = False
        if (self.window[1] < 7 and self.background.windowGrid[self.window[0]][self.window[1]+1].health > 0):
            self.moveDown = True
        else:
            self.moveDown = False
        if (self.moveRight == False and self.moveLeft == False and self.moveUp == False and self.moveDown == False 
        and self.jumpRight == False and self.jumpLeft == False and self.jumpUp == False and self.jumpDown == False):
            return False
            
    
    def Render(self, screen):   
        self.playerRect = screen.blit(self.player,(self.positionOffset[0]+(127*self.window[0]),self.positionOffset[1]+(79*self.window[1])))
        self.rect = self.playerRect
        

