"""
Data: 04/07/2021
Autor: Mateus Marochi Olenik

Título: Questionário sobre Projeto de Controlador de Avanço-Atraso por Lugar das Raízes
Questão: 3
"""

from IPython import get_ipython                  # As próximas linhas são para selecionar entre plot inline ou em nova janela
get_ipython().run_line_magic('matplotlib', 'qt') # get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np                               # Biblioteca para cálculo numérico
import control as ct                             # Biblioteca para controle
import matplotlib.pyplot as plt                  # Funções de plot similares as do MATLAB

print("Planta em malha fechada:")
num=[1]
den=[1,4,0]
G=ct.tf(num,den) 
print(G)

print("\nPlanta sem compensação em malha fechada:")
Gmf=ct.feedback(G,1)
print(Gmf)

print("\nPolos de Malha Fechado sem compensação:")
print(ct.pole(Gmf))  

print("\nLugar das raízes de G(s):")      
ct.rlocus(G)

print("\nVerificação da condição de ângulo (graus):")
s=complex(-2,2.098)
angle=np.angle(1/(s*(s+4)), deg=True)
print(angle)

print("\nA contribuição angular que o compensador de avanço deve inserir no lugar das raízes é:")
print(180-angle)

print("\nCálculo de Kc")
Kc=1/abs(((s+1))*(4/(s*(s+1)*(s+2))))
print(Kc)

#Compensador de avanço
Gav=ct.tf([1.415, 1.415],[1, 6.181])
#Planta compensada com avanço
Gmfcav=ct.feedback(Gav*G,1)
Gmfcav=ct.minreal(Gmfcav)
print(Gmfcav)
#Polos de malha fechada com compensação de avanço
print(ct.pole(Gmfcav))
#Resposta ao degrau
t=np.linspace(0,10,1000)
y1, t1 = ct.matlab.step(Gmfcav,t)
plt.figure()
plt.plot(t1,y1)
plt.legend(['Com compensação de avanço'])
plt.xlabel('t(s)')
plt.ylabel('Amplitude')
plt.grid()

#Compensador
numc=np.polymul([6.26,  3.13],[1, 0.2])
denc=np.polymul([1,  5.02],[1, 0.01247])
Gc=ct.tf(numc,denc)
#Planta com compensação em malha fechada
Gmfc=ct.feedback(Gc*G,1)
Gmfc=ct.minreal(Gmfc)
print(Gmfc)
#Zero e Polos de malha fechada com compensação
print(ct.zero(Gmfc))
print(ct.pole(Gmfc))