import random
class Ant():
    def __init__ (self, row, column):
        self.vision = 1
        self.row = row
        self.column = column
        self.payload = None
    
    def move(self, boardDimension):
        '''Responsável pela movimentação da formiguinha'''
        possibilites = [(0,1), (0,-1), (1,0), (-1,0)]
        direction = random.choice(possibilites)

        next_row = self.row + direction[0]
        next_col = self.column + direction[1]

        #Checar se movimento é possível
        if 0<= next_row < boardDimension and 0 <= next_col < boardDimension:
            self.row = next_row
            self.column = next_col