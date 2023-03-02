from Trabalho_num_TCM_lib import *

class Temperatura:

    def __init__(self):
        self.L = 1
        self.difus = 1
        self.N = 3
        self.k_final = 1
        self.Ti = 0
        self.funct = const
        self.fluxoi = 0
        self.Xi = 0
        self.functi = const
        self.fluxof = 0
        self.Xf = 0
        self.functf = const
        self.cor = 1
        self.dx = self.L/self.N
        self.dt = 0.1*self.dx*self.dx
        self.Temperatura = np.zeros((self.N+1, self.N+1), dtype=float)

    def Tamanho(self, tamanho, divisoes):
        self.L = tamanho
        self.N = divisoes
        self.dx = self.L/self.N
        self.dt = 0.1*self.dx*self.dx

    def Tempo(self, Tempo):
        # self.k_final = int(Tempo/self.dt)
        self.k_final = self.N*Tempo

    def difusividade(self, difusividade):
        self.difus = difusividade

    def Cond_iniciais(self, Temperatura, funcao):
        self.Ti = Temperatura
        self.funct = funcao

    def Cond_contorno(self, Tempi, Functi, Fluxoi, Tempf, Functf, Fluxof):
        self.Xi = Tempi
        self.Xf = Tempf
        self.fluxoi = Fluxoi
        self.fluxof = Fluxof
        self.functi = Functi
        self.functf = Functf

    def Mudar_cor(self, Cor):
        self.cor = Cor

    def Base(self):
        self.Temperatura = np.zeros((self.N+1, self.N+1), dtype=float)
        self.Temperatura = cond_inic(self.Temperatura, self.Ti, self.L, self.funct)
        self.Temperatura = cond_cont(self.Temperatura, self.Xi, self.functi, self.Xf, self.functf, self.k_final*self.dt)

    def Evolucao(self):
        self.Temperatura = evolucao(self.Temperatura, self.N, self.k_final, self.dx, self.dt, self.difus, self.fluxoi, self.fluxof)

    def Plotar(self):
        plotTemp3d(self.Temperatura, self.L, self.N, self.k_final, self.dt, viridis=self.cor)

    def Plotar2d(self):
        plotTemp2d(self.Temperatura[self.N], self.L, self.k_final*self.dt)