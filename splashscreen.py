import layermanager
import pygame

from pygame.locals import *

pygame.font.init()
pygame.init()

class SplashScreen(layermanager.Layer):   
    def __init__(self,screen):
        layermanager.Layer.__init__(self)
        self.gameRunning = False
        self.currentscreen = 0 #0 for main screen, 1 for instruction screen
        self.selected = 0

        self.font = pygame.font.Font(pygame.font.match_font("Verdana"), 40)


        self.startPosition = (60,170)
        self.instructionPosition = (60,270)

        self.startText = self.font.render("Start", 1, (0, 161, 236))
        self.startTextAlt = self.font.render("Start", 1, (255, 255, 255))
        self.instructionText = self.font.render("Instructions", 1, (0, 161, 236))
        self.instructionTextAlt = self.font.render("Instructions", 1, (255, 255, 255))

        self.startRect = pygame.Rect(self.startText.get_rect())
        self.startRect.topleft = self.startPosition

        self.backRect = pygame.Rect(60,485,180,95)
        
        self.instructionRect = pygame.Rect(self.instructionText.get_rect())
        self.instructionRect.topleft = self.instructionPosition

    def HandleEvent(self, event):
        #dont handle if not on splashscreen
        if self.gameRunning:
            return False
        
        if self.currentscreen == 0:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % 2
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % 2
                
            #begin Game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if self.selected == 0:
                    self.selected = 1
                    self.currentscreen = 1 #Go to instructions screen...etc
                else:
                    self.gameRunning = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.startRect.collidepoint(pos):
                    self.gameRunning = True
                if self.instructionRect.collidepoint(pos):
                    self.selected = 1
                    self.currentscreen = 1

        if self.currentscreen == 1:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  
                self.currentscreen = 0    
                self.selected = 0 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.backRect.collidepoint(pos):
                    self.currentscreen = 0
                    self.selected = 0  
            

    def Update(self):    
        #not on main screen so proceed to next layer
        if self.gameRunning:
            return True

        pos = pygame.mouse.get_pos()
        
        if self.currentscreen == 0:
            if self.startRect.collidepoint(pos):
                self.selected = 0
            elif self.instructionRect.collidepoint(pos):
                self.selected = 1
        elif self.currentscreen == 1:
            pass
        return False

    def Render(self, screen):    
        #not on main screen so proceed to next layer
        if self.gameRunning:
            return True

        screen.fill((0,0,0))
        #screen.blit(self.image, self.rect)
        if self.currentscreen == 0:
            if self.selected == 0:
                startText = self.font.render("Start", 1, (0, 161, 236))
            else:
                startText = self.font.render("Start", 1, (255, 255, 255))
            
            if self.selected == 1:
                instructionText = self.font.render("Instructions", 1, (0, 161, 236))
            else:
                instructionText = self.font.render("Instructions", 1, (255, 255, 255))
 
            screen.blit(startText, (60,170))
            screen.blit(instructionText, (60,270))

        if self.currentscreen == 1:
            backText = self.font.render("Back", 1, (0, 161, 236))
            screen.blit(backText,self.backRect)

 
            

def main():
    screen = pygame.display.set_mode((1024, 768))#, pygame.FULLSCREEN)
    manager = layermanager.LayerManager()
    manager.layerStack.append(SplashScreen(screen))
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




