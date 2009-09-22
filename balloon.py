import pygame
import sys 
import math
import layermanager
import player

from pygame.locals import *

class Balloon(pygame.sprite.Sprite):
    def __init__(self, enemy):
        self.enemy = enemy
        if self.enemy.type == 0:
            self.image = pygame.image.load('art/balloon.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.enemy.rect.center
        if self.enemy.type == 1:
            self.image = pygame.image.load('art/balloon2.png').convert_alpha()
            self.rect = self.image.get_rect()
        
        self.endpos = self.enemy.background.player.positionOffset[1]+(79*self.enemy.background.player.window[1])
        self.ground = 0
        for i in self.enemy.background.windowHealth[self.enemy.rooftop[0]]:
            if i == 1:
                self.ground += 1
        self.ground = self.enemy.background.player.positionOffset[1]+(79*self.ground)
        self.positionOffset = [53]
        self.speed = 5.0
        self.height = 10
        self.rooftop = self.enemy.rooftop[0]
        self.timer = pygame.time.get_ticks()
        self.dead = False
        
    def HandleEvent(self, event):
        pass
        
    def Update(self):
        if self.enemy.type == 0:
            self.rect.centery -= self.speed
            if self.rect.centery < self.endpos:
                self.dead = True
            
        elif self.enemy.type == 1:
            self.height += self.speed
            if self.height > self.ground:
                self.dead = True
                
        return self.dead
            
        
    def Render(self, screen):
        if self.enemy.type == 0:
            screen.blit(self.image, self.rect)
        elif self.enemy.type == 1:
            self.rect = screen.blit(self.image, (self.positionOffset[0]+(127*self.rooftop),self.height)) 