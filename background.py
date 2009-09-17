import layermanager
import pygame
import window

class Background(layermanager.Layer):
    def __init__(self,screen):
        layermanager.Layer.__init__(self)
        self.background = pygame.image.load("art/background.png")
        self.backgroundRect = self.background.get_rect()
        self.sky = pygame.image.load("art/sky.png")
        self.skyRect = self.sky.get_rect()
        self.grass = pygame.image.load("art/grass.png")
        self.grassRect = self.grass.get_rect()
        self.sublist = []
        self.setupWindows()
        self.windowGrid = [[1,1,1,1,1,1,1,1] #Can move onto 1's can't move to 0's
                           [1,1,1,1,1,1,1,1]
                           [1,1,1,1,1,1,1,1]
                           [1,1,1,1,1,1,1,1]
                           [0,1,1,1,1,1,1,1]
                           [0,0,0,1,1,1,1,1]
                           [0,0,0,0,0,1,1,1]
                           [0,0,0,0,0,0,0,1]
 

    def setupWindows(self):
        for i in range(8):
            for j in range(8):
                self.sublist.append(window.Window((3+(i*127),60+(j*79))))

    def HandleEvent(self, event):
        for i in self.sublist:
            i.HandleEvent(event)

    def Update(self):
        for i in self.sublist:
            i.Update()

    def Render(self, screen):   
        screen.blit(self.background,self.backgroundRect)
        screen.blit(self.sky,self.skyRect)
        for i in self.sublist:
            i.Render(screen)
        screen.blit(self.grass,self.grassRect)
