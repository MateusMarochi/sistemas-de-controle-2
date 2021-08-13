"""
Data: 14/07/2021
Autor: Mateus Marochi Olenik

Título: Questionário sobre Projeto de Controlador PD pelo Método do Lugar das Raízes
Questão: 2
"""

from IPython import get_ipython                  # As próximas linhas são para selecionar entre plot inline ou em nova janela
get_ipython().run_line_magic('matplotlib', 'qt') # get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np                               # Biblioteca para cálculo numérico
import math                                      #Funções matemáticas
import control as ct                             # Biblioteca para controle
import matplotlib.pyplot as plt                  # Funções de plot similares as do MATLAB


print("Planta em malha fechada:")
num=[1]
den=[1,0,-2]
G=ct.tf(num,den) 
print(G)

print("\nPlanta sem compensação em malha fechada:")
Gmf=ct.feedback(G,1)
print(Gmf)

print("\nPolos de Malha Fechado sem compensação:")
print(ct.pole(Gmf))  

print("\nFrequência natural:")
wn=math.sqrt(num[0])
print(wn)
print("\nCoeficiente de Amortecimento:")
print(den[1]/(2*wn))

print("\nLugar das raízes de G(s):")      
ct.rlocus(G)

wn_desejado = 2
zeta_desejado = 0.707
S = [-(zeta_desejado*wn_desejado), wn_desejado*math.sqrt(1-zeta_desejado**2)]
s = complex(S[0],S[1])
print(s)

print("\nVerificação da condição de ângulo (graus):")
angle=round(np.angle(1/(s**2-2), deg=True),3)
print(angle)

print("\nA contribuição angular que o compensador de avanço deve inserir no lugar das raízes é:")
angle_cont = round(180-angle,3)
print(180-angle)

Kp=round(1/abs((Td*(s+zero_PD)*num[0])/(s**2*den[0]+s*den[1]+den[2])),3)
print("\nKp = ",Kp)
