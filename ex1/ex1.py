# YouTube: https://www.youtube.com/watch?v=EIAqDfid38c
# Git: https://gitlab.com/humbertokramm/tutorial-sistemas-de-controle/
# Autor: Humberto Corrêa Kramm 
# Data: 25/05/2019

import control as clt
import matplotlib.pyplot as plt
from scipy.signal import lti, step


#Parâmetros do controlador
Kp = 10.0
Ki = 0.1
Kd = 10.0

print("Kp= ",Kp)
print("Ki= ",Ki)
print("Kd= ",Kd)

#Pontos de resolução
dots = 5000

	
#sistema
k = 1
wn = [1,5]
a = 1
b = sum(wn)
c = wn[0]*wn[1]

num = [k]
den = [a,b,c]
#Monta a FT
G = clt.TransferFunction(num,den)
print("G(s)= ",G)


#Monta o sistema de controle
controler = Kp*(1+clt.TransferFunction([Ki],[1,0])+clt.TransferFunction([Kd,0],[1]))
print("Ci",clt.TransferFunction([Ki],[1,0]))
print("Cd",clt.TransferFunction([Kd,0],[1]))
print("controler= ",controler)

#Realimenta o sistema com o controlador aplicado
print("controler*G= ",controler*G)
sys = clt.feedback(controler*G)
print("sys= ",sys)

#Aplica o degrau
sys2 = sys.returnScipySignalLTI()[0][0]
t2,y2 = step(sys2,N = dots)

#Faz um degrau só para exibir gráficamente
Tstep = [-0.5,0,1e-15,t2.max()]
Ystep = [0,0,1,1]

#prepara algumas informações da legenda
Pico = max(y2)
print("Pico = ",Pico)
Final = 1
print("Estabiliza em  = ",y2[-1])
SobreSinal_c = 100*(Pico-Final)/Final
print("SobreSinal_c = ",SobreSinal_c,"%")
Erro = (1-y2[-1])*100
print("Erro = ",Erro,"%")


#prepara algumas informações da legenda
Pico2 = max(y2)
Final2 = 1
SobreSinal_c2 = 100*(Pico2-Final2)/Final2
Erro2 = (1-y2[-1])*100


#Monta o Gráfico
plt.title('Step Response - (Kp='+str(Kp)+' Ki='+str(Ki)+' Kd='+str(Kd)+')')
plt.plot(t2,y2,label='scipy lib; MP = '+str(round(SobreSinal_c2,3))+'% with '+str(dots)+' dots')
plt.plot(Tstep,Ystep,label='Step')
plt.ylabel('gain')        # Plota o label y
plt.xlabel('time [s]')            # Plota o label x
plt.grid(which='both', axis='both')     # Gride para frequências intermediárias
plt.grid(True)                          # Mostra o Grid
plt.margins(0, 0.1)                     # Deixa uma margem
plt.legend()


plt.show()
