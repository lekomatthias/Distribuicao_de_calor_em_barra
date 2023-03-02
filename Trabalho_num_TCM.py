# Programa feito para observar o desenvolvimento da temperatura
# em uma barra no decorrer do tempo, sendo preciso indicar as 
# condicoes de contorno e iniciais do problema, o tamanho da
# barra, quantidade de divisoes desejadas no comprimento e 
# quantidade de tempo decorrido.

from Temperatura_classe import *

# tamanho da barra
L = 2*np.pi
# L = 1
# numero de pontos
N = 50
# quantidades de amostras no tempo (k_final)
t = 100
# condicoes iniciais
Ti = 0
# mais comportamento
funct = const
# condicoes de contorno 
# fluxo = 1: as condicoes indicam o fluxo nas bordas
# fluxo = 0: as condicoes indicam uma temperatura fixa nas bordas
fluxoi = 1
Xi = 0
funci = np.sin
fluxof = 0
Xf = 0
funcf = np.sin
# difusividade do material
difusividade = 1

cor = 0

# --------------------------------------------------------------------------------

T = Temperatura()
T.Tamanho(L, N)
T.Tempo(t)
T.Cond_iniciais(Ti, funct)
T.Cond_contorno(Xi, funci, fluxoi, Xf, funcf, fluxof)
T.difusividade(difusividade)
T.Base()
T.Evolucao()
T.Mudar_cor(cor)
T.Plotar()
