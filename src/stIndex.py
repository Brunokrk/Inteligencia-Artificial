import streamlit as st
from corpseAnts.board import *
from dataAnts.scrappyBoard import *
import pygame

if __name__ == "__main__":
    
    pygame.init()
    
    st.header("Ant Clustering Algorithm - IAR0002", divider=True)
    algorithm =st.selectbox("Qual Algoritmo quer rodar?", ("Clusterização Homogênea", "Clusterização Heterogênea (DataFrame)"))
    board_dimension = st.slider("Selecione a Dimensão do Espaço de Busca:", min_value=5)
    corpses = st.slider("Selecione a Quantidade de Corpos que serão espalhados:", max_value=1000)
    ants = st.slider("Selecione Quantas Formigas irão Compor a Colônia:", min_value=2, max_value=50)
    
    executeClustering = st.button("Go!", use_container_width=True)
    if executeClustering:
        #Pygame screen configs
        if(algorithm == "Clusterização Homogênea"): 
            pygame.init()
            cell_size = 10
            window_width = board_dimension * cell_size
            window_height = board_dimension * cell_size
            # Create Window
            screen = pygame.display.set_mode((window_width, window_height))
            pygame.display.set_caption('Ant Clustering Algorithm')

            #Executa Clusterização Homogênea
            clusteringBoard = Board(board_dimension, ants, corpses, screen, window_width, window_height)
            clusteringBoard.clustering()
        else:
            #Clusterização Heterogênea
            pygame.init()
            cell_size = 10
            window_width = board_dimension * cell_size
            window_height = board_dimension * cell_size
            # Create Window
            screen = pygame.display.set_mode((window_width, window_height))
            pygame.display.set_caption('Ant Clustering Algorithm')

            #Executa Clusterização Homogênea
            clusteringBoard = ScrappyBoard(board_dimension, ants, screen, window_width, window_height)
            #print(clusteringBoard)
            clusteringBoard.clustering()
            pass
            

        
