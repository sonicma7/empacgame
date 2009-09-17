import pygame
import sys
import math
import layermanager

from pygame.locals import *

class EnemyScreen(layermanager.Layer):
    def __init__(self, screen):
        layermanager.Layer.__init__(self)
        self.gameRunning = False
        self.image = pygame.image.load('testenemy.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (500,650)
        self.speed = 3
        
        
    def HandleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if self.speed > 1:
                self.speed -= 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.speed += 1
    
    def Update(self):
        pos = pygame.mouse.get_pos()
        
        if self.rect.x < pos[0]:
            self.rect.x += self.speed
            #self.rect.y += self.speed/3
        elif self.rect.x > pos[0]:
            self.rect.x -= self.speed
            #self.rect.y -= self.speed/3
        else:
            print 'pew pew'
            
    def Render(self, screen):
        screen.blit(self.image, self.rect)
        

def main():
    screen = pygame.display.set_mode((1024, 768))#, pygame.FULLSCREEN)
    manager = layermanager.LayerManager()
    manager.layerStack.append(EnemyScreen(screen))
    masterclock = pygame.time.Clock()
        
    while True:
        masterclock.tick(60)
        pygame.event.pump()
        keys = pygame.key.get_pressed()  #Check if keys have been pressed
        if keys[K_ESCAPE]:
            sys.exit()

        for event in pygame.event.get():
            manager.HandleEvent(event)
    
        screen.fill((0,0,0))
        manager.Update()
        manager.Render(screen)      
            
        pygame.display.flip()




if __name__ == '__main__': main()