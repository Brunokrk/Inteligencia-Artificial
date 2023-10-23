import time
import csv
import random
import math
from copy import deepcopy

def read_input(arq):
    entrada = []
    var = 0
    clau = 0

    with open(arq, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter='\n')
        for row in plots:
            if row:
                linha = row[0]

                if linha[0] != 'c':
                    if linha[0] == 'p':
                        _, tipo, var, clau = linha.split()
                        var, clau = int(var), int(clau)
                    elif linha[0] != '%' and linha[0] != '0':
                        a, b, c, zero = linha.split()
                        a, b, c = int(a), int(b), int(c)
                        clausula = [a, b, c]
                        entrada.append(clausula)

    #print(entrada)
    return var, clau, entrada

def randomize(n):
    return [random.choice([True, False]) for _ in range(n + 1)]

def neg(stt):
    return not stt

def funcAvaliacao(conjuntiveNormalFormula, solution):
    total = 0

    for i in conjuntiveNormalFormula:
        aux = False

        for j in i:
            if j > 0:
                aux = aux or solution[j]
            else:
                aux = aux or neg(solution[-j])

        if not aux:
            total += 1

    return total

def randomSearch(conjuntiveNormalFormula, solution, var, clausule, iterations, num):
    arqNome = 'random{}.txt'.format(num)
    f = open(arqNome, 'w')

    resultado = funcAvaliacao(conjuntiveNormalFormula, solution)
    s = '0 {}\n'.format(resultado / clausule)
    f.write(s)
    lista = [resultado / clausule]

    for i in range(1, iterations):
        sTemp = randomize(var)
        rTemp = funcAvaliacao(conjuntiveNormalFormula, sTemp)
        s = '{} {}\n'.format(i, rTemp / clausule)
        f.write(s)
        lista.append(rTemp / clausule)

        if rTemp < resultado:
            solution = deepcopy(sTemp)
            resultado = rTemp

    f.close()
    return solution, resultado, lista

def tempExp(ti, passo, alpha):
    return ti * pow(alpha, passo)

def tempLinear(t, ti, passos):
    return t - ti / passos

def mutacao(sol, var):
    neighbor = deepcopy(sol)
    flip = random.randint(1, var)
    neighbor[flip] = neg(neighbor[flip])
    return neighbor

def simulatedAnnealing(conjuntiveNormalFormula, solution, var, clau, it, num):
    arqNome = 'simAne{}.txt'.format(num)
    f = open(arqNome, 'w')

    ti = 0.010
    t = ti
    resultado = funcAvaliacao(conjuntiveNormalFormula, solution)/clau
 
    s = '0 {}\n'.format(resultado)
    f.write(s)
    lista = [resultado]

    melhorSol = deepcopy(solution)
    melhorResult = resultado

    for i in range(1, it):
        sTemp = mutacao(solution, var)
        rTemp = funcAvaliacao(conjuntiveNormalFormula, sTemp) / clau
        s = '{} {}\n'.format(i, resultado)
        f.write(s)
        lista.append(resultado)
        deltaE = rTemp - resultado

        if deltaE <= 0:
            solution = deepcopy(sTemp)
            resultado = rTemp
            if rTemp < melhorResult:
                melhorResult = rTemp
                melhorSol = deepcopy(sTemp)
        elif random.uniform(0, 1) <= math.exp(-deltaE / t):
            solution = deepcopy(sTemp)
            resultado = rTemp

        t = tempExp(ti, i, 0.9999)

    f.close()
    return melhorSol, melhorResult, lista

def init_execution(conjuntiveNormalFormula, var, clausule, it, executions):
    melhorRand = []
    melhorSimAne = []
    
    listaRand = []
    listaSimAne = []
    
    for i in range(executions):
        #print(i)
        
        solInicial = randomize(var)
        
        solFinal, rFinal, totalRand = randomSearch(conjuntiveNormalFormula, solInicial, var, clausule, it, i)
        melhorRand.append(rFinal)
        listaRand.append(totalRand)
        #print(listaRand)

        solFinal, rFinal, totalSimAne = simulatedAnnealing(conjuntiveNormalFormula, solInicial, var, clausule, it, i)
        melhorSimAne.append(rFinal)
        listaSimAne.append(totalSimAne)
        #print(listaSimAne)
    
    print(melhorRand)
    print(melhorSimAne)

    
    return listaRand, listaSimAne, melhorRand, melhorSimAne
