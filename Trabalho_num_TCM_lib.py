import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# coloca a condicao inicial da barra
def cond_inic(vetor2d, valor, L, funct):
    div = len(vetor2d[0])
    for j in range(0, 2):
        for i in range(0, div):
             vetor2d[j, i] = valor + funct(i*(L/div))
    return vetor2d

# coloca as condicoes de contorno na barra pelo tempo
def cond_cont(vetor2d, valori, functi, valorf, functf, t):
    final = len(vetor2d)-1
    variacao = t/(final+1)
    for i in range(0, final+1):
        vetor2d[i, 0] = valori + functi(i*variacao)
    for i in range(0, final+1):
        vetor2d[i, final] = valorf + functf(i*variacao)
    return vetor2d

def const(x, opc=0):
    return 0

def reta(x, t=1):
    return x*t

# Desenvolve a evolucao da temperatura na barra no tempo, 
# podendo variar as bordas como um fluxo ou uma temperatura
# fixada
def evolucao(matriz_temp, X, T, dx, dt, difus, fluxoi, fluxof):
    aux = matriz_temp[0].copy()
    final = len(aux)-1
    for k in range (1, T+1):

        if fluxoi == 1:
            # derivada primeira usando os termos a direita
            aux[0] = -2*(matriz_temp[round(k/(T/X)), 0]*dx + aux[2]/2 - 2*aux[1])/3
        if fluxof == 1:
            # derivada primeira usando os termos a esquerda
            aux[final] = -2*(matriz_temp[round(k/(T/X)), final]*dx + aux[final-2]/2 - 2*aux[final-1])/3
        
        for i in range (1 ,X) :
            # derivada segunda pela equacao do calor
            aux[i] = aux[i] + difus*(dt/(dx*dx))*(aux[i+1] - 2*aux[i] + aux[i-1])
        # verifica qual a numeracao da amostra no menor intervalo possivel
        if k%(T/X) == 0:
            matriz_temp[int(k/(T/X))] = aux
        
        aux[0] = matriz_temp[round(k/(T/X)), 0]
        aux[final] = matriz_temp[round(k/(T/X)), final]

    return matriz_temp

# usa o metodo de diferencas finitas, fixando a temperatura 
# nas bordas.
def evolucao_dirichlet(matriz_temp, X, T, dx, dt, difus, borda=0):
    aux = matriz_temp[0].copy()
    for k in range (1, T+1+borda):
        for i in range (1+borda ,X) :
            # derivada segunda pela equacao do calor
            aux[i] = aux[i] + difus*(dt/(dx*dx))*(aux[i+1] - 2*aux[i] + aux[i-1])
            # verifica qual a numeracao da amostra no menor intervalo possivel
            if k%(T/X) == 0:
                matriz_temp[int(k/(T/X))+borda] = aux
    return matriz_temp

# plota o gráfico da temperatura e usa os outros dados para
# colocar legendas adequadas nele
def plotTemp3d(Temperatura, L,  N, t_final, dt, borda=0, viridis=1):
    # variacao de tempo total
    t = (t_final-borda) * dt
    # criacao do espaco 3d
    X, Y = np.mgrid[0-(t_final/N)*borda:t:(len(Temperatura[0]))*1j, 0-borda:L:(len(Temperatura))*1j]
    # fig = plt.figure()
    ax = plt.axes(projection = '3d')
    if viridis == 0:
        ax.plot_surface(X, Y, Temperatura, cmap = cm.coolwarm)
    else:
        ax.plot_surface(X, Y, Temperatura, cmap = 'viridis')
    ax.set_title('comprimento x: %.3fm '%L
                +'\ntempo t: %.3fs '%t)
                # +'\ndifusividade: %.2f'%difusividade)
    ax.set_ylabel('$x$')
    ax.set_xlabel('$t$')
    ax.set_zlabel('$T[°C]$')

    plt.show()

def plotTemp2d(Temperatura, L, t):
    abscissas = np.linspace(0, L, len(Temperatura))
    fig = plt.figure()
    ax = fig.add_subplot()
    plt.title("Temperatura x Posicao \n Tempo = %.3f"%t)
    ax.set_xlabel('$posicao$', fontsize=12)
    ax.set_ylabel('$Temperatura$', fontsize=12)

    # plt.ylim(0, 1.5)
    plt.plot(abscissas, Temperatura, color='red', linewidth=3)
    plt.show()
