"""
Data: 04/07/2021
Autor: Mateus Marochi Olenik

Título: Questionário sobre Projeto de Controlador de Avanço-Atraso por Lugar das Raízes
Questão: 2
"""

from IPython import get_ipython                  # As próximas linhas são para selecionar entre plot inline ou em nova janela
get_ipython().run_line_magic('matplotlib', 'qt') # get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np                               # Biblioteca para cálculo numérico
import control as ct                             # Biblioteca para controle
import matplotlib.pyplot as plt                  # Funções de plot similares as do MATLAB
from control.matlab import *      # Funções para controle similares as do MATLAB

print("Planta em malha fechada:")
num=[5,75]
den=[1,16,65,50]
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
s=complex(-2.778,2.061)
angle=np.angle(((5*s+75)/(s**3+16*s**2+65*s+50)), deg=True)
print(angle)

print("\nA contribuição angular que o compensador de avanço deve inserir no lugar das raízes é:")
print(180-angle)

Kv = 1+75/50
erro_perm = 1/Kv

Kv_2 = 1/0.02-1
beta = Kv_2/Kv

T=1/0.05

polo = round(1/(beta*T),3)

print("\nCálculo de Kc")
Kc=round(1/abs(((s+0.05)/(s+polo))*((5*s+75)/(s*s*s+16*s*s+65*s+50))),3)
print(Kc)

print("\nKv = ",Kv," Kv_2 = ",Kv_2,"Erro em regime permanete =",erro_perm," Beta = ",beta,"T =",T,"polo =",polo, "Kc =",Kc)


Gc=ct.tf([Kc, Kc*0.05],[1, polo])
#Planta com compensação em malha fechada
Gmfc=ct.feedback(Gc*G,1)
Gmfc=ct.minreal(Gmfc)
print(Gmfc)
#Zero e Polos de malha fechada com compensação
print(ct.zero(Gmfc))
print(ct.pole(Gmfc))

#Resposta ao degrau
t=np.linspace(0,2000,10000)
y1, t1 = step(Gmf,t)
y2, t2 = step(Gmfc,t)
plt.figure()
plt.plot(t1,y1,t2,y2)
plt.legend(('Sem compensação','Com compensação'))
plt.xlabel('t(s)')
plt.ylabel('Amplitude')
plt.title('Resposta ao Degrau')
plt.grid()



#Resposta a rampa
t=np.linspace(0,1000,1000)
Gi=tf(1,[1, 0])
yi, ti = step(Gi,t)
yr1, tr1 = step(Gi*Gmf,t)
yr2, tr2 = step(Gi*Gmfc,t)

plt.figure()
plt.plot(ti,yi,tr1,yr1,tr2,yr2)
plt.legend(('Referência','Sem compensação','Com compensação'))
plt.xlabel('t(s)')
plt.ylabel('Amplitude')
plt.title('Resposta à Rampa')
plt.grid()


#Erros em regime permanente para entrada rampa
t=np.linspace(0,2000,2000)
Yi, t=step(Gi,t);
Y1, T1=step(Gi*Gmf,t);
Y2, T2=step(Gi*Gmfc,t);
erro_MF=Yi-Y1;
erro_MF_C=Yi-Y2;

plt.figure();
plt.plot(T1,erro_MF,T2,erro_MF_C);
plt.legend(('Erro sem compensador','Erro com compensador'))
plt.xlabel('t(s)')
plt.ylabel('Amplitude')
plt.grid()