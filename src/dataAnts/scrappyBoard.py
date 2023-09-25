import random
from dataAnts.scrappyAnt import ScrappyAnt
from dataAnts.dataType import *
import pygame
import numpy as np
import sys
import math

class ScrappyBoard():
    def __init__(self, dimension, ants, screen, width, height):
        self.dimension = dimension
        self.ants = self.instantiateAnts(ants)
        self.corpses = None #dataset
        self.cellSize = 10 #pygame
        self.screen = screen #pygame
        self.window_width = width
        self.window_heigth = height
        self.board = self.randomCorpses()
        self.k1 = 0.1
        self.k2 = 0.3
        self.alpha = 0.3

    def lerDataset(self):
        linhas = []
        with open("dataAnts/data_A.csv", 'r') as file:
            for linha in file:
                linhas.append(linha.strip())
        return linhas

    def randomCorpses(self):
        '''Espalha Corpos pelo Board de Forma Aleatória'''
        noneDataType = DataType(None, None, None, False)
        board = [[noneDataType for _ in range(self.dimension)] for _ in range(self.dimension)]

        linhas = self.lerDataset()
        for linha in linhas:
            #print(linha)
            partes = linha.split(',')
            x, y, rot = float(partes[0].replace(".", "")), float(partes[1].replace(".", "")), int(partes[2].replace(".",""))
            data_type = DataType(x, y, rot, True)
            x_random, y_random = random.randint(0, self.dimension - 1), random.randint(0, self.dimension - 1)
            board[x_random][y_random] = data_type

        return board
    
    def instantiateAnts(self, ants):
        antsPop = [ScrappyAnt(random.randint(0, (self.dimension-1)), random.randint(0, (self.dimension-1))) for _ in range(ants)]
        return antsPop

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])

    def clustering(self):
        GRASS = (255, 255, 255) #floor
        RED = (255, 0, 0) #ants
        running = True
        #movement_count = 0
        ants_done = False
        noneDataType = DataType(None, None, None, False)
        body_positions = [[False for _ in range(self.dimension)] for _ in range(self.dimension)]

        while running:
            #print("entrou aqui")
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
                        if self.board[row][col].isData == True:
                            body_positions[row][col] = True
                            pygame.draw.rect(temp_surface, self.board[row][col].color, (col * self.cellSize, row * self.cellSize, self.cellSize, self.cellSize))
                
                
                for ant in self.ants:
                    ant.move(self.dimension)
                    row = ant.row
                    col = ant.column
                    if body_positions[row][col] == True and ant.payload == None:
                        # chance de pegar

                        #calcular f(xi)
                        #pegar com prob Pp(xi)

                        randPegar = np.random.rand()
                        chancePegar = self.calculatingPickAndDrop(ant, "p")
                        if(randPegar < chancePegar ):
                            print("Pegou")
                            ant.setPayload(self.board[row][col])
                            self.board[row][col] = noneDataType
                            body_positions[row][col] = False
                    elif body_positions[row][col] == False and ant.payload != None:
                        #chance de largar

                        #calcule f(xi)
                        #pegue com prob Pd(xi)
                        txLargar = np.random.rand()
                        chanceLargar = self.calculatingPickAndDrop(ant, "l")
                        print(str(chanceLargar) +":"+str(txLargar))
                        if(txLargar < chanceLargar):
                            print("Largou")
                            self.board[row][col] = ant.payload
                            ant.payload = None
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

    def calculatingPickAndDrop(self, ant, paramRet):
        qtdItens = 0 
        distances =[]
        #contando dados na vizinhança
        for i in range(-ant.vision, ant.vision+1):
            for j in range(-ant.vision, ant.vision+1):
                if i == 0 and j == 0:
                    continue
                row = ant.row + i
                col = ant.column + j   

                row %= self.dimension
                col %= self.dimension  
                if self.board[row][col].isData == True:
                    qtdItens+= 1   
                    distance = self.euclideanDistance(ant, self.board[row][col], action)
                    distances.append(distance)


        if paramRet == "p":
            #pegar
            similarity = self.calculateSimilarity(distances)
            pick_probability = self.calculatePickProbability(similarity)
            return pick_probability
        else:
            #largar
            similarity = self.calculateSimilarity(distances)
            drop_probability = self.calculateDropProbability(similarity)
            return drop_probability

    def euclideanDistance(self, ant, item, action,):
        """Calcula a distância entre a formiga e o item"""
        if action == "p":
            dx = self.board[ant.row][ant.col].x - item.x
            dy = self.board[ant.row][ant.col].y - item.y
            return np.sqrt(dx**2 + dy**2)
        else:
            dx = ant.payload.x - item.x
            dy = ant.payload.y - item.y
            return np.sqrt(dx**2 + dy**2)
        

    def calculateSimilarity(self, distances):
        pass

    def calculateDropProbability(self,similarity):
        pass

    def calculatePickProbability(self, similarity):
        pass