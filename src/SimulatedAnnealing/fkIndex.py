import streamlit as st
import simulatedAnnealing as sa
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import pandas as pd

def plottingFnc(randomSearch, simulatedAnnealing):
    # Converter as listas em matrizes NumPy
    lista_Rand = np.array(randomSearch)
    listaSimuAne = np.array(simulatedAnnealing)

    # Calcular a média por iteração (coluna)
    media_Rand = np.mean(lista_Rand, axis=0)
    media_SimuAne = np.mean(listaSimuAne, axis=0)

    # Calcular o desvio padrão por iteração (coluna)
    desvio_padrao_Rand = np.std(lista_Rand, axis=0)
    desvio_padrao_SimuAne = np.std(listaSimuAne, axis=0)

    # Criar gráfico usando Plotly
    fig = go.Figure()
    
    # Adicionar a média de Random Search
    fig.add_trace(go.Scatter(x=np.arange(len(media_Rand)), y=media_Rand, mode='lines', name='Média Random Search'))
    
    # Adicionar o desvio padrão de Random Search
    #fig.add_trace(go.Scatter(x=np.arange(len(desvio_padrao_Rand)), y=media_Rand + desvio_padrao_Rand, mode='lines', line=dict(dash='dash'), name='Desvio Padrão Random Search'))
    #fig.add_trace(go.Scatter(x=np.arange(len(desvio_padrao_Rand)), y=media_Rand - desvio_padrao_Rand, mode='lines', line=dict(dash='dash'), showlegend=False))

    # Adicionar a média de Simulated Annealing
    fig.add_trace(go.Scatter(x=np.arange(len(media_SimuAne)), y=media_SimuAne, mode='lines', name='Média Simulated Annealing'))
    
    # Adicionar o desvio padrão de Simulated Annealing
    #fig.add_trace(go.Scatter(x=np.arange(len(desvio_padrao_SimuAne)), y=media_SimuAne + desvio_padrao_SimuAne, mode='lines', line=dict(dash='dash'), name='Desvio Padrão Simulated Annealing'))
    #fig.add_trace(go.Scatter(x=np.arange(len(desvio_padrao_SimuAne)), y=media_SimuAne - desvio_padrao_SimuAne, mode='lines', line=dict(dash='dash'), showlegend=False))

    fig.update_layout(title='Média e Desvio Padrão dos Valores por Iteração',
                    xaxis_title='Iteração',
                    yaxis_title='Média Função Objetivo')

    # Exibir o gráfico
    return fig


def plotTemperature(temperature):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(len(temperature)), y=temperature, mode='lines', name='Temperatura Simulated Annealing'))
    fig.update_layout(title='Temperatura ao Longo das Iterações',
                    xaxis_title='Iteração',
                    yaxis_title='Temperatura')
    return fig

def boxplot(melhorRand, melhorSim):
    df_melhorRand = pd.DataFrame({'Valor': melhorRand, 'Algoritmo': 'melhorRand'})
    df_melhorSim = pd.DataFrame({'Valor': melhorSim, 'Algoritmo': 'melhorSim'})

    # Combinar os DataFrames
    df_combined = pd.concat([df_melhorRand, df_melhorSim])

    # Criar gráfico de boxplot
    fig = px.box(df_combined, x='Algoritmo', y='Valor', points="suspectedoutliers", boxmode='overlay')
    return fig

if __name__ == "__main__":
    st.header("Simulated Annealing -- IAR0002", divider="rainbow")
    dataset = st.selectbox("Selecione o conjunto de dados", ("data/uf20-01.cnf", "data/uf100-01.cnf", "data/uf250-01.cnf"))
    it = st.slider("Selecione a quantidade de iterações", max_value=250000)
    executions = st.slider("Quantas execuções?", max_value=10)
    #Botão de execução
    executeSA = st.button("Execute Simulated Annealing", use_container_width=True)
    if executeSA:
        n_var, n_clau, lista = sa.read_input(dataset)
        lista_Rand, listaSimuAne, melhorRand, melhorSim, temperature = sa.init_execution(lista, n_var, n_clau, it, executions)
        st.plotly_chart(plottingFnc(lista_Rand, listaSimuAne))
        st.plotly_chart(plotTemperature(temperature))
        st.plotly_chart(boxplot(melhorRand, melhorSim))
        #print(temperature)