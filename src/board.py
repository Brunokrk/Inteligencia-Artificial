import random
from ant import Ant

class Board():
    def __init__(self, dimension, ants, corpses):
        self.dimension = dimension
        self.ants = self.instantiateAnts(ants)
        self.corpses = corpses
        self.board = self.randomCorpses()

    def randomCorpses(self):
        '''Espalha Corpos pelo Board de Forma Aleatória'''
        if self.corpses > (self.dimension**2):
            raise ValueError("Impossível alocar esta quantidade de corpos")

        board = [[0 for _ in range(self.dimension)] for _ in range(self.dimension)]
        corpsePositions = [(i,j) for i in range(self.dimension) for j in range(self.dimension)]
        random.shuffle(corpsePositions)

        for i in range(self.corpses):
            row,col = corpsePositions[i]
            board[row][col] = '1'
        
        return board
    
    def instantiateAnts(self, ants):
        antsPop = [Ant(random.randint(0, self.dimension), random.randint(0, self.dimension)) for _ in range(ants)]
        return antsPop

    def runCLustering(self):
        return
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])