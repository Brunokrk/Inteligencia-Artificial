class DataType():
    def __init__(self, x, y,rot):
        self.x = x
        self.y = y 
        self.rot = rot  
        self.color = None  

    def __str__(self):
        return str(self.rot)