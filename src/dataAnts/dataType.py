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
            return pygame.Color(255, 0, 0)
        elif self.rot == 2:
            return pygame.Color(0, 255, 0) 
        elif self.rot == 3:
            return pygame.Color(0, 0, 255)
        elif self.rot == 4:
            return pygame.Color(255, 255, 0) 
        elif self.rot == 5:
            return pygame.Color(255, 0, 255)
        elif self.rot == 6:
            return pygame.Color(0, 255, 255)
        elif self.rot == 7:
            return pygame.Color(255, 165, 0)
        elif self.rot == 8:
            return pygame.Color(255, 105, 180) 
        elif self.rot == 9:
            return pygame.Color(50, 205, 50)
        elif self.rot == 10:
            return pygame.Color(128, 0, 128)
        elif self.rot == 11:
            return pygame.Color(139, 69, 19)
        elif self.rot == 12:
            return pygame.Color(64, 224, 208)
        elif self.rot == 13:
            return pygame.Color(255, 215, 0)
        elif self.rot == 14:
            return pygame.Color(128, 128, 0)
        elif self.rot == 15:
            return pygame.Color(0, 0, 128)
        return pygame.Color(255, 255, 255, 128)

    def __str__(self):
        return str(self.rot)