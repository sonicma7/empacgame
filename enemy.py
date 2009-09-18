import pygame
import sys 
import math
import layermanager
import player

from pygame.locals import *

class Enemy():
    def __init__(self, background):
        self.gameRunning = False
        self.image = pygame.image.load('art/testenemy.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (500,625)
        self.speed = 3.0
        self.background = background
        
        
    def HandleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if self.speed > 1:
                self.speed -= 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.speed += 1
    
    def Update(self):
        pos = self.background.player.positionOffset[0]+(127*self.background.player.window[0])
        
        if self.rect.centerx < pos:
            if pos - self.rect.centerx < self.speed:
                self.rect.centery += (pos - self.rect.centerx)/3.0
                self.rect.centerx += pos - self.rect.centerx
            else:
                self.rect.centerx += self.speed
                self.rect.centery += self.speed/3.0
        elif self.rect.centerx > pos:
            if self.rect.centerx - pos < self.speed:
                self.rect.centery -= (self.rect.centerx - pos)/3.0
                self.rect.centerx -= self.rect.centerx - pos
            else:
                self.rect.centerx -= self.speed
                self.rect.centery -= self.speed/3.0
        else:
            print 'pew pew'
            
    def Render(self, screen):
        screen.blit(self.image, self.rect)