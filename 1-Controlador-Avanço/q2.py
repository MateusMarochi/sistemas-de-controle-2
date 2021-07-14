"""
Data: 04/07/2021
Autor: Mateus Marochi Olenik

Título: Questionário sobre Projeto de Controlador de Avanço por Lugar das Raízes
Questão: 2
"""

from IPython import get_ipython                  # As próximas linhas são para selecionar entre plot inline ou em nova janela
get_ipython().run_line_magic('matplotlib', 'qt') # get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np                               # Biblioteca para cálculo numérico
import control as ct                             # Biblioteca para controle

print("Planta em malha fechada:")
num=[1]
den=[1,1,0]
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
s=complex(-1,1)
angle=np.angle(1/(s*(s+1)), deg=True)
print(angle)