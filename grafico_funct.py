import numpy as np
import matplotlib.pyplot as plt

# devolve a temperatura da barra na posicao x no tempo t
def funct(x, t, quest):
    result = 0
    if quest == 1:
        for n in range(1, 100):
            # problema 1  
            result = result + (4/((2*n-1)*np.pi))*np.sin((2*n-1)*np.pi*x)*np.exp(-((2*n-1)*(2*n-1))*(np.pi*np.pi)*t)
        return result
    elif quest == 2:
        for n in range(1, 100):
            # problema 2
            result = result + (2/(n*np.pi))*np.sin(n*np.pi*x)*np.exp(-n*n*np.pi*np.pi*t)
        return 1-x-result
    else:
        for n in range(1, 100):
            # problema 3
            result = np.sin((np.pi/2)*x)*np.exp((-np.pi*np.pi*t)/4)
        return result

# desenha o grafico da funcao no tempo t para uma barra de tamanho L
# e devolve uma matriz com as característica da imagem
def plotar_graf(t, L, questao, nome, formato):
    x = np.linspace(0, L, 200)
    y = funct(x, t, questao)

    fig = plt.figure()
    ax = fig.add_subplot()
    fig.suptitle('t=%.3f'%t, fontsize=18, fontweight='bold')
    ax.set_xlabel('$x$', fontsize=18)
    ax.set_ylabel('$T$', fontsize=18)
    # plt.axis("off")
    plt.ylim(0, 1.3)
    plt.xlim(0-0.01, L+0.01)
    plt.plot(x, y, color='red')
    plt.savefig(nome , format=formato , dpi=200, bbox_inches='tight')
    plt.cla()
    plt.close(fig)

if __name__ == '__main__':
    t = 0.133
    L = 1
    x = np.linspace(0, L, 200)
    y = funct(x, t, 1)

    fig = plt.figure()
    ax = fig.add_subplot()
    fig.suptitle('t=%.3f'%t, fontsize=18, fontweight='bold')
    ax.set_xlabel('$x$', fontsize=18)
    ax.set_ylabel('$T$', fontsize=18)
    # plt.axis("off")
    plt.ylim(-0, 1.3)
    # plt.xlim(0-0.1, L+0.1)
    plt.plot(x, y, color='red')
    plt.savefig('figura.png' , format='png' , dpi=1000, bbox_inches='tight')

    plt.show()

    plt.cla()
    plt.close(fig)
