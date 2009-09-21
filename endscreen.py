import layermanager

class endScreen(layermanager.Layer):
    def __init__(self,screen):
        layermanager.Layer.__init__(self)

    def HandleEvent(self, event):
        pass

    def Update(self):
        pass

    def Render(self, screen):   
        screen.fill((0,0,0))