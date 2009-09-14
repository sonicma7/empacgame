import pygame
import sys
import random


class LayerManager:
    def __init__(self):
        self.layerStack = []

    def HandleEvent(self, event):
        for layer in self.layerStack:
            if layer.HandleEvent(event):
                return

    def Update(self):
        for layer in self.layerStack:
            if not layer.Update():
                return

    def Render(self, screen):
        for layer in self.layerStack:
            if not layer.Render(screen):
                return

class Layer:
    def __init__(self):
        #self.config = config
        pass
        return

    #returns true if we handled the event, false otherwise
    def HandleEvent(self, event):
        return False

    #returns true if we should continue to update the layers below.
    #for a pause screen, you would return False
    def Update(self):
        return True

    #called to render this layer
    def Render(self, screen):
        return True

class DemoLayer(Layer):
    def __init__(self):
        Layer.__init__(self)
        self.pixels = []

    def HandleEvent(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.pixels.append(pygame.mouse.get_pos())
            return True

    def Render(self, screen):
        screen.set_at(pygame.mouse.get_pos(), (255,255,255))
        return True

class QuitLayer(Layer):
    def __init__(self):
        Layer.__init__(self)

    def HandleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_q, pygame.K_ESCAPE):
                raise SystemExit
        elif event.type == pygame.QUIT:
            raise SystemExit

class PauseLayer(Layer):
    def __init__(self):
        Layer.__init__(self)
        self.paused = False

    def HandleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            self.paused = not self.paused
            print "Paused: ", self.paused
            return True

        return False

    def Update(self):
        return not self.paused
