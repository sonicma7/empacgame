import layermanager
import pygame
import config

class endScreen(layermanager.Layer):
    def __init__(self,screen):
        layermanager.Layer.__init__(self)
        self.font = pygame.font.Font(pygame.font.match_font("Verdana"), 40)
        

    def HandleEvent(self, event):
        pass

    def Update(self):
        pass

    def Render(self, screen):   
        #screen.fill((0,0,0))
        scoreText = self.font.render("Game Over", 1, (0, 0, 0))
        rect = scoreText.get_rect()
        rect.center = (400,300)
        screen.blit(scoreText, rect)
        scoreText = self.font.render("Final Score: " + str(config.score), 1, (0, 0, 0))
        rect = scoreText.get_rect()
        rect.center = (400,400)
        screen.blit(scoreText, rect)
