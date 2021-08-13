"""
Data: 14/07/2021
Autor: Mateus Marochi Olenik

Título: Questionário sobre Projeto de Controlador PI pelo Método do Lugar das Raízes
Questão: 3
"""

from IPython import get_ipython                  # As próximas linhas são para selecionar entre plot inline ou em nova janela
get_ipython().run_line_magic('matplotlib', 'qt') # get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np                               # Biblioteca para cálculo numérico
import math                                      #Funções matemáticas
import control as ct                             # Biblioteca para controle
import matplotlib.pyplot as plt                  # Funções de plot similares as do MATLAB


print("Planta em malha fechada:")
num=[10]
den=[1,4,0]
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

S= [-1, math.sqrt(3)]
s = complex(S[0],S[1])
print("\nPolos dominantes em: ",s)

K=round(1/abs(((num[0]/(s**2*den[0]+s*den[1]+den[2])))),3)
print("\nK =",K)

print("\nVerificação da condição de ângulo (graus):")
angle=round(np.angle((num[0]/(s**2*den[0]+s*den[1]+den[2])), deg=True),3)
print(angle)

print("\nA contribuição angular que o compensador de avanço deve inserir no lugar das raízes é:")
angle_cont = round(180+angle,3)
print(180-angle)

zero_PI = 0.05

Kp=round(1/abs((1+1/(20*s))*(num[0]/(s**2*den[0]+s*den[1]+den[2]))),3)
print("\nKp = ",Kp)

