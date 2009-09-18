import pygame

class Window():
    def __init__(self,position,health):
        self.window = pygame.image.load("art/window.png")
        self.windowRect = self.window.get_rect()
        self.brokenWindow = pygame.image.load("art/brokenwindow.png")
        self.altwindow  = pygame.image.load("art/player.png")
        self.brokenWindowRect = self.brokenWindow.get_rect()
        self.health = health
        self.position = position

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