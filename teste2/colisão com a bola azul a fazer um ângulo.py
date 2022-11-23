import numpy as np      #colisão com a bola azul a fazer um ângulo de 𝜙 = 35°
import matplotlib.pyplot as plt
con=np.pi/180.
phi=35 #ANGULO abaixo de eixo X
theta=90.-phi # angulo acima do eixo do X
phi=phi*con
theta=theta*con
det=-np.cos(theta)*np.sin(phi)-np.sin(theta)*np.cos(phi)
vaz=-np.sin(phi)/det
vam=-np.cos(phi)/det
v2=vaz**2+vam**2
vi=1
print('det, vaz, vam, vaz**2 + vam**2 = ', det,vaz,vam,v2)
a=np.array([[np.cos(theta), np.cos(phi)], [np.sin(theta), -np.sin(phi)]]) 
b=np.array([1,0]) #[velocidade da  bola 1 colisao;velocidade bola 2 colisao]
print("velocidade da bola 1 pos colisao,Velocidade bola 2 pos colisao")
x = np.linalg.solve(a, b)
print(x)
