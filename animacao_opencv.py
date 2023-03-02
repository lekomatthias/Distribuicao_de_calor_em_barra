from os import system
import cv2
from grafico_funct import *

fps = 10.0
total_frames = 100
unidade_de_passo = 0.001 # segundos
dimensao = (640, 480)
tamanho_barra = 1
questao = 1

video = cv2.VideoWriter('Video_TCM_testes.avi', cv2.VideoWriter_fourcc(*'mp4v'), fps, dimensao)

for t in range(0, total_frames):
    tempo = t*unidade_de_passo
    plotar_graf(tempo, tamanho_barra, questao, 'grafico{}.jpg'.format(''), 'JPG')
    frame = cv2.imread('grafico{}.jpg'.format(''))
    frame = cv2.resize(frame, dsize=dimensao, interpolation=cv2.INTER_CUBIC)
    video.write(frame)
    system("cls")
    print("Fazendo video...")
    print(str(100*t/total_frames) + "%")
print("Video concluido!")

video.release()
cv2.destroyAllWindows()
