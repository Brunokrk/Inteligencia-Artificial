import pygame
class DataType():
    def __init__(self, x, y,rot, isData):
        self.x = x
        self.y = y 
        self.rot = rot
        self.isData = isData
        self.color = self.setRot()  

    def setRot(self):
        if self.rot == 1 :
            return pygame.Color(0,0,255) #AZUL
        elif self.rot == 2:
            return pygame.Color(0, 128, 129) # ROSA
        elif self.rot == 3:
            return pygame.Color(255,255,0) #Amarelo
        elif self.rot == 4:
            return pygame.Color(255, 128, 0) #Laranja
        return pygame.Color(255, 255, 255, 128)

    def __str__(self):
        return str(self.rot)