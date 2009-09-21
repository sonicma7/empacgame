import pygame
import config

class Window():
    def __init__(self,position,health):
        self.window = pygame.image.load("art/window.png")
        self.windowRect = self.window.get_rect()
        self.brokenWindow = pygame.image.load("art/brokenwindow.png")
        self.windowHit = pygame.image.load("art/attack.png").convert_alpha()
        self.attack = False
        self.hitCounter = 0
        self.altwindow  = pygame.image.load("art/player.png")
        self.brokenWindowRect = self.brokenWindow.get_rect()
        self.health = health
        self.position = position

    def attackWindow(self):
        self.health -= 1
        self.attack = True
        self.hitCounter = 0
        if self.health == 0:
            config.score += config.glassValue

    def HandleEvent(self, event):
        pass

    def Update(self):        
        if self.health > 0:
            self.drawWindow = self.window
        elif self.health == -1:
            self.drawWindow = self.window
        else:
            self.drawWindow = self.brokenWindow

    def Render(self, screen):   
        screen.blit(self.drawWindow,self.position)
        if self.attack == True:
            screen.blit(self.windowHit,(self.position[0]+45,self.position[1]+20))
            self.hitCounter += 1
            if self.hitCounter == 4:
                self.attack = False