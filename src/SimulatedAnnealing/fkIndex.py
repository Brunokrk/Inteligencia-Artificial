import streamlit as st
import simulatedAnnealing as sa
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import pandas as pd

def plottingFnc(randomSearch, simulatedAnnealing, simulatedAnnelingLinear, clau):
    # Converter as listas em matrizes NumPy
    lista_Rand = np.array(randomSearch)
    listaSimuAne = np.array(simulatedAnnealing)
    listaSimuAneLin = np.array(simulatedAnnelingLinear)

    lista_Rand *= clau
    listaSimuAne *= clau
    listaSimuAneLin *= clau

    # Calcular a média por iteração (coluna)
    media_Rand = np.mean(lista_Rand, axis=0)
    media_SimuAne = np.mean(listaSimuAne, axis=0)
    media_SimuAneLin = np.mean(listaSimuAneLin, axis=0)

    # Criar o primeiro gráfico
    fig1 = go.Figure()
    
    # Adicionar a média de Random Search
    fig1.add_trace(go.Scatter(x=np.arange(len(media_Rand)), y=media_Rand, mode='lines', name='Média Random Search'))
    
    # Adicionar a média de Simulated Annealing
    fig1.add_trace(go.Scatter(x=np.arange(len(media_SimuAne)), y=media_SimuAne, mode='lines', name='Média Simulated Annealing'))
    
    fig1.update_layout(title='Média e Desvio Padrão dos Valores por Iteração',
                    xaxis_title='Iteração',
                    yaxis_title='Média Função Objetivo')

    # Criar o segundo gráfico
    fig2 = go.Figure()
    
    # Adicionar a média de Random Search
    fig2.add_trace(go.Scatter(x=np.arange(len(media_Rand)), y=media_Rand, mode='lines', name='Média Random Search'))
    
    # Adicionar a média de Simulated Annealing Linear
    fig2.add_trace(go.Scatter(x=np.arange(len(media_SimuAneLin)), y=media_SimuAneLin, mode='lines', name='Média Simulated Annealing Linear'))
    
    fig2.update_layout(title='Média e Desvio Padrão dos Valores por Iteração',
                    xaxis_title='Iteração',
                    yaxis_title='Média Função Objetivo')

    # Retornar ambos os gráficos em uma lista
    return [fig1, fig2]

def plotTemperature(temperature):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(len(temperature)), y=temperature, mode='lines', name='Temperatura Simulated Annealing'))
    fig.update_layout(title='Temperatura ao Longo das Iterações',
                    xaxis_title='Iteração',
                    yaxis_title='Temperatura')
    return fig

def boxplot(melhorRand, melhorSim, melhorSimLin, clau):
    #Multiplicar os valores nas listas pelo valor 'clau'
    ##melhorRand = [valor * clau for valor in melhorRand]
    ##melhorSim = [valor * clau for valor in melhorSim]

    # Criar DataFrames com os valores multiplicados
    df_melhorRand = pd.DataFrame({'Valor': melhorRand, 'Algoritmo': 'Random Search'})
    df_melhorSim = pd.DataFrame({'Valor': melhorSim, 'Algoritmo': 'Simulated Annealing Exponencial'})
    df_melhorSimLin = pd.DataFrame({'Valor': melhorSimLin, 'Algoritmo': 'Simulated Annealing Linear'})

    # Combinar os DataFrames
    df_combined = pd.concat([df_melhorRand, df_melhorSim, df_melhorSimLin])

    # Criar gráfico de boxplot
    fig = px.box(df_combined, x='Algoritmo', y='Valor', boxmode='overlay')
    return fig

def calculate_mean_and_std(melhorRand, melhorSim, melhorSimLin, clau):
    # Calcular a média e o desvio padrão de melhorRand
    #melhorRand = [valor * clau for valor in melhorRand]
    #melhorSim = [valor * clau for valor in melhorSim]
    
    mean_melhorRand = np.mean(melhorRand)
    std_melhorRand = np.std(melhorRand)

    # Calcular a média e o desvio padrão de melhorSim
    mean_melhorSim = np.mean(melhorSim)
    std_melhorSim = np.std(melhorSim)

    mean_melhorSimLin = np.mean(melhorSimLin)
    std_melhorSimLin = np.std(melhorSimLin)

    st.write("Média SA Exp: "+ str(mean_melhorSim)+"    Desvio padrão: "+str(std_melhorSim))
    st.write("Média Rand: "+str(mean_melhorRand)+"    Desvio Padrão: "+str(std_melhorRand))
    st.write("Média SA Lin: "+str(mean_melhorSimLin)+ "    Desvio Padrão: "+str(std_melhorSimLin) )
    #return mean_melhorRand, std_melhorRand, mean_melhorSim, std_melhorSim


if __name__ == "__main__":
    st.header("Simulated Annealing -- IAR0002", divider="rainbow")
    dataset = st.selectbox("Selecione o conjunto de dados", ("data/uf20-01.cnf", "data/uf100-01.cnf", "data/uf250-01.cnf"))
    it = st.slider("Selecione a quantidade de iterações", max_value=250000)
    executions = st.slider("Quantas execuções?", max_value=10)
    #Botão de execução
    executeSA = st.button("Execute Simulated Annealing", use_container_width=True)
    
  
    if executeSA:
        n_var, n_clau, lista = sa.read_input(dataset)
        lista_Rand, listaSimuAne, melhorRand, melhorSim, listaSimuAneLin, melhorSimuAneLin, temperatureLin, temperatureExp = sa.init_execution(lista, n_var, n_clau, it, executions)
        graphs = plottingFnc(lista_Rand, listaSimuAne, listaSimuAneLin, n_clau)
        conv1, conv2 = graphs[0], graphs[1]
        
        st.plotly_chart(conv1)
        st.plotly_chart(plotTemperature(temperatureExp))
          
        st.plotly_chart(conv2)
        st.plotly_chart(plotTemperature(temperatureLin))
        
        st.plotly_chart(boxplot(melhorRand, melhorSim, melhorSimuAneLin, n_clau))
        calculate_mean_and_std(melhorRand, melhorSim, melhorSimuAneLin ,n_clau)
        #print(temperature)