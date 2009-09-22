import pygame
import sys 
import math
import layermanager
import player
import balloon

from pygame.locals import *

class Enemy():
    def __init__(self, background, type):
        self.type = type
        if type == 0:
            self.image = pygame.image.load('art/testenemy.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = (500,625)
        if type == 1:
            self.image = pygame.image.load('art/testenemy2.png').convert_alpha()
            self.rect = self.image.get_rect()
        
        self.rooftop = [0]
        self.groundHeight = 625.0
        self.positionOffset = [53]
        self.speed = 3.0
        self.roofspeed = 3.0
        self.background = background
        self.height = 10
        self.timer = pygame.time.get_ticks()
        self.attacktimer = pygame.time.get_ticks()
        self.attackspeed = 20.0
        
        
    def HandleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_MINUS:
            if self.speed > 1.0:
                self.speed -= 1.0
            self.attackspeed += 10.0
            self.roofspeed += 1.0
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_EQUALS:
            self.speed += 1.0
            if self.attackspeed > 10.0:
                self.attackspeed -= 10.0
            if self.roofspeed > 1.0:
                self.roofspeed -= 1.0

    
    def Update(self):
        if self.type == 0:
            pos = self.background.player.positionOffset[0]+(127*self.background.player.window[0])
            
            if self.rect.centerx < pos:
                if pos - self.rect.centerx < self.speed:
                    self.groundHeight += (pos - self.rect.centerx)/3.0
                    self.rect.centery = self.groundHeight
                    self.rect.centerx += pos - self.rect.centerx
                else:
                    self.rect.centerx += self.speed
                    self.groundHeight += self.speed/3.0
                    self.rect.centery = self.groundHeight
            elif self.rect.centerx > pos:
                if self.rect.centerx - pos < self.speed:
                    self.groundHeight -= (self.rect.centerx - pos)/3.0
                    self.rect.centery = self.groundHeight
                    self.rect.centerx -= self.rect.centerx - pos
                else:
                    self.rect.centerx -= self.speed
                    self.groundHeight -= self.speed/3.0
                    self.rect.centery = self.groundHeight
            else:
                if pygame.time.get_ticks() - self.timer > self.attackspeed * 100.0:
                    self.timer = pygame.time.get_ticks()
                    self.background.balloons.append(balloon.Balloon(self))
                
        
        elif self.type == 1:
            if pygame.time.get_ticks() - self.timer > self.roofspeed * 100.0:
                self.timer = pygame.time.get_ticks()
                if self.rooftop[0] < self.background.player.window[0]:
                    self.rooftop[0] += 1
                elif self.rooftop[0] > self.background.player.window[0]:
                    self.rooftop[0] -= 1
                else:
                    if pygame.time.get_ticks() - self.attacktimer > self.attackspeed * 100.0:
                        self.attacktimer = pygame.time.get_ticks()
                        self.background.balloons.append(balloon.Balloon(self))
            
            
    def Render(self, screen):
        if self.type == 0:
            screen.blit(self.image, self.rect)
        elif self.type == 1:
            screen.blit(self.image,(self.positionOffset[0]+(127*self.rooftop[0]),self.height)) 