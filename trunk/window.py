import pygame

class Window():
    def __init__(self,position):
        self.window = pygame.image.load("art/window.png")
        self.windowRect = self.window.get_rect()
        self.brokenWindow = pygame.image.load("art/brokenwindow.png")
        self.brokenWindowRect = self.brokenWindow.get_rect()
        self.health = 3
        self.position = position

    def HandleEvent(self, event):
        pass

    def Update(self):
        if self.health > 0:
            self.drawWindow = self.window
        else:
            self.drawWindow = self.brokenWindow

    def Render(self, screen):   
        screen.blit(self.drawWindow,self.position)