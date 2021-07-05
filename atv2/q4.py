# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 20:30:37 2021

@author: mateu
"""

"""
Data: 04/07/2021
Autor: Mateus Marochi Olenik

Título: Questionário sobre Projeto de Controlador de Atraso por Lugar das Raízes
Questão: 4
"""

from IPython import get_ipython                  # As próximas linhas são para selecionar entre plot inline ou em nova janela
get_ipython().run_line_magic('matplotlib', 'qt') # get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np                               # Biblioteca para cálculo numérico
import control as ct                             # Biblioteca para controle

print("Planta em malha fechada:")
num=[20]
den=[1,5,4]
G=ct.tf(num,den) 
print(G)

print("\nPlanta sem compensação em malha fechada:")
Gmf=ct.feedback(G,1)
print(Gmf)

print("\nPolos de Malha Fechado sem compensação:")
print(ct.pole(Gmf))  


numc=[1,  0.05]
denc=[1, 0.005]
Gcp=ct.tf(numc,denc)
print("\nLugar das raízes de G(s):")      
ct.rlocus(G)
print("\nLugar das raízes de Gc(s)G(s):") 
ct.rlocus(Gcp*G)

print("\nCálculo analítico de Kc:")
s=complex(-0.31,0.55)
Kc=1/abs(((s+0.05)*20)/((s+0.005)*((s+1)*(s+4))))
print(Kc)

