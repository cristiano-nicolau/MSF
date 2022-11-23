# imports
import numpy as np
import matplotlib.pyplot as plt

def main():
    # imput
    dt = 0.0001  # passo temporal
    tf = 4.0  # instante final
    t0 = 0  # instante inicial
    n = np.int((tf - t0) / dt + 0.1)  # numero de passos

    # iniciar os arrays com o tempo, a velocidade e a posição
    t = np.zeros(n + 1)
    vy = np.zeros(n + 1)
    y = np.zeros(n + 1)

    # condições iniciais
    g = 9.8  # aceleração gravítica
    t[0] = 0  # instante inicial
    vy[0] = 0  # velocidade inicial eixo y
    y[0] = 0  # posição inicial eixo y

    # Método de Euler
    for i in range(n):
        t[i + 1] = t[i] + dt  # alterar o instante
        vy[i + 1] = vy[i] + g * dt  # alterar a velocidade
        y[i + 1] = y[i] + vy[i] * dt  # alterar a posição

    # print gráfico da posição em função do tempo
    plt.plot(t, y, color='m')
    plt.ylabel("Posição (m)")
    plt.xlabel("Tempo (s)")
    plt.show()

    # print gráfico da velocidade em função do tempo
    plt.plot(t, vy, color='m')
    plt.ylabel("Velocidade (m/s)")
    plt.xlabel("Tempo (s)")
    plt.show()
    for i in range(n):
        if t[i+1] > 3-2*dt and  t[i+1] < 3+2*dt:
            print('dt, t, vy = ',dt,t[i+1],vy[i+1])
        
    for i in range(n):
        if t[i+1] > 2-2*dt and  t[i+1] < 2+2*dt:
            print('dt, t, y = ',dt,t[i+1],y[i+1])
main()






