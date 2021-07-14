"""
Data: 04/07/2021
Autor: Mateus Marochi Olenik

Título: Questionário sobre Projeto de Controlador de Atraso por Lugar das Raízes
Questão: 3
"""

from IPython import get_ipython                  # As próximas linhas são para selecionar entre plot inline ou em nova janela
get_ipython().run_line_magic('matplotlib', 'qt') # get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np                               # Biblioteca para cálculo numérico
import control as ct                             # Biblioteca para controle


print("\nCálculo analítico de Kc:")
s=complex(-0.99,0.99)
Kc=1/abs(((s+0.01)*2)/((s+0.001)*(s*(s+2))))
print(Kc)
