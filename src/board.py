import random
from ant import Ant
import threading

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
        antsPop = [Ant(random.randint(0, (self.dimension-1)), random.randint(0, (self.dimension-1))) for _ in range(ants)]
        return antsPop

    def clustering(self, totalMovements):
        for ant in self.ants:
            for _ in range(totalMovements):
                ant.move(self.dimension)
                row = ant.row
                col = ant.column
                self.board[row][col] = 'A'
            print("\n----")
            print(self)
    
    def thClustering(self, totalMovements):
        threads = []

        for ant in self.ants:
            thread = threading.Thread(target=self.move_ant, args=(ant, totalMovements))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        #print("\n----")
        #print(self)

    def move_ant(self, ant, totalMovements):
        for _ in range(totalMovements):
            ant.move(self.dimension)
            row = ant.row
            col = ant.column
            self.board[row][col] = 'A'
            print(self)
            print("\n----")

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])