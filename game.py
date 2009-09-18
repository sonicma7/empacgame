import pygame
import config
import splashscreen
import layermanager
import sys
import background

from pygame.locals import *

pygame.font.init()
pygame.init()

screen = pygame.display.set_mode(config.screensize)#, pygame.FULLSCREEN)
pygame.display.set_caption(config.title)
masterclock = pygame.time.Clock()

mainmenu = splashscreen.SplashScreen(screen)
manager = layermanager.LayerManager()
manager.layerStack.append(mainmenu)
manager.layerStack.append(background.Background(screen))

while True:
    masterclock.tick(60)
    pygame.event.pump()
    keys = pygame.key.get_pressed()  #Check if keys have been pressed
    if keys[K_ESCAPE]:
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
        manager.HandleEvent(event)

    manager.Update()
    manager.Render(screen)
    pygame.display.flip()