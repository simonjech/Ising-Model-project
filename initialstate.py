import numpy as np

J=1

#Funkcia vytvorí náhodnú maticu o rozmere n s prvkami 1 alebo -1. Takáto matica reprezentuje stav feromagnetickej látky. 

def pociatocny_stav(n):
    return np.random.choice([-1, 1], size=(n, n))

# Výpočet energie pre stav daný maticou mriežky.  

def energia(matica):
    # PS není nutné vytvářet novou pomocnou proměnnou
    n=len(matica)
    H=0

    # PS zde lze dát vše do jednoho cyklu
    for i in range (0,n-1):
        for j in range (0,n-1):
            H-=matica[i,j]*(matica[i+1,j]+matica[i,j+1]) #príspevky zo stredu, horného a ľavého okraja. 

        H-=matica[i,n-1]*matica[i+1,n-1] #príspevok z pravého okraja mriežky. 
        H-=matica[n-1,i]*matica[n-1,i+1] #príspevky ze spodného okraja mriežky. 

    H *=J
    return H

#Funkcia na výpočet zmeny energie po zámene spinu na pozícii (i, j) v mriežke. 

def delta_energia(matica, i, j):
    n = len(matica)
    spin = matica[i,j]
    delta_E = 0

    # Získanie susedov
    susedia = []
    if i > 0:
        susedia.append(matica[i-1,j])  # hore
    if i < n - 1:
        susedia.append(matica[i+1,j])  # dole
    if j > 0:
        susedia.append(matica[i,j-1])  # vľavo
    if j < n - 1:
        susedia.append(matica[i,j+1])  # vpravo

    # Výpočet zmeny energie
    for sused in susedia:
        delta_E += 2 *J* spin * sused   # PS tady musí být znaménko +, pokud máte delta_E = E_nová - E_stará

    return delta_E

#magnetizácia na jeden spin

def magnetizacia (matica): 
    n=len(matica)
    M=0
    for i in range (n):
        for j in range (n):
            M += matica[i][j]
    return M/(n*n) 




    

