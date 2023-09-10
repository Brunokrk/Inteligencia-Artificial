import random
from ant import Ant
import pygame
import numpy as np
import sys
import math

class Board():
    def __init__(self, dimension, ants, corpses, screen, width, height):
        self.dimension = dimension
        self.ants = self.instantiateAnts(ants)
        self.corpses = corpses
        self.cellSize = 10
        self.screen = screen #pygame
        self.window_width = width
        self.window_heigth = height
        self.board = self.randomCorpses()

    def randomCorpses(self):
        '''Espalha Corpos pelo Board de Forma Aleatória'''
        if self.corpses > (self.dimension**2):
            raise ValueError("Impossível alocar esta quantidade de corpos")

        board = [["_" for _ in range(self.dimension)] for _ in range(self.dimension)]
        corpsePositions = [(i,j) for i in range(self.dimension) for j in range(self.dimension)]
        random.shuffle(corpsePositions)

        for i in range(self.corpses):
            row,col = corpsePositions[i]
            board[row][col] = "1" # type: ignore

        return board
    
    def instantiateAnts(self, ants):
        antsPop = [Ant(random.randint(0, (self.dimension-1)), random.randint(0, (self.dimension-1))) for _ in range(ants)]
        return antsPop

    def clustering(self, totalMovements):
        GRASS = (80, 200, 120)
        RED = (255, 0, 0)
        running = True
        movement_count = 0
        ants_done = False

        body_positions = [[False for _ in range(self.dimension)] for _ in range(self.dimension)]

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:  # Verifique se a tecla "P" está pressionada
                ants_done = not ants_done

            if not ants_done:
                # superfície temporária
                temp_surface = pygame.Surface((self.window_width, self.window_heigth))
                temp_surface.fill(GRASS)  

                #corpos 
                for row in range(self.dimension):
                    for col in range(self.dimension):
                        if self.board[row][col] == "1":
                            body_positions[row][col] = True
                            pygame.draw.rect(temp_surface, (82, 48, 41), (col * self.cellSize, row * self.cellSize, self.cellSize, self.cellSize))

                for ant in self.ants:
                    ant.move(self.dimension)
                    row = ant.row
                    col = ant.column
                    if body_positions[row][col] == True and ant.payload != "1":
                        # chance de pegar
                        randPegar = np.random.rand()
                        chancePegar = self.calculaChancePegar(ant, "p")
                        if(randPegar < chancePegar ):
                            print("Pegou")
                            ant.payload = self.board[row][col]
                            self.board[row][col] = "_"
                            body_positions[row][col] = False
                    elif body_positions[row][col] == False and ant.payload == "1":
                        #chance de largar
                        txLargar = np.random.rand()
                        chanceLargar = self.calculaChancePegar(ant, "l")
                        print(str(chanceLargar) +":"+str(txLargar))
                        if(txLargar < chanceLargar):
                            print("Largou")
                            self.board[row][col] = ant.payload
                            ant.payload = "_"
                            body_positions[row][col] = True
                    # formigas
                    pygame.draw.rect(temp_surface, RED, (col * self.cellSize, row * self.cellSize, self.cellSize, self.cellSize))

                #atualizaçaõ
                self.screen.fill(GRASS) 
                self.screen.blit(temp_surface, (0, 0))
                pygame.time.delay(30)
                pygame.display.flip()
                #movement_count += 1  
                #if movement_count >= totalMovements:
                #    ants_done = True  
  
        pygame.quit()
        sys.exit()

    def calculaChancePegar(self, ant, paramRet):
        qtdItens = 0
        
        for i in range(-ant.vision, ant.vision+1):
            for j in range(-ant.vision, ant.vision+1):
                if i == 0 and j == 0:
                    continue
                row = ant.row + i
                col = ant.column + j   

                row %= self.dimension
                col %= self.dimension  
                

                if self.board[row][col] == "1":
                    qtdItens+= 1   
        

        if paramRet == "p":
            
            return (1 - (qtdItens**2 / ((2 * ant.vision + 1) ** 2 - 1)))
            #return self.sigmoid(1 - (qtdItens / ((2 * ant.vision + 1) ** 2 - 1)))
        else:
            return (qtdItens**2 / ((2 * ant.vision + 1) ** 2 - 1))
            #return self.sigmoid(((qtdItens / ((2 * ant.vision + 1) ** 2 - 1))))


    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])