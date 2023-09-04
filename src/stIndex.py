import streamlit as st
from board import *

if __name__ == "__main__":
    st.header("Ant Clustering Algorithm - IAR0002", divider=True)
    board_dimension = st.slider("Selecione a Dimensão do Espaço de Busca:")
    corpses = st.slider("Selecione a Quantidade de Corpos que serão espalhados:", max_value=10000)
    ants = st.slider("Selecione Quantas Formigas irão Compor a Colônia:", min_value=2, max_value=7)
    
    clusteringBoard = Board(board_dimension, ants, corpses)
    
    executeClustering = st.button("Go!", use_container_width=True)
    if executeClustering:
        st.text(clusteringBoard)
        st.divider()
        #clusteringBoard.clustering(10)
        clusteringBoard.thClustering(5)
        st.text(clusteringBoard)



