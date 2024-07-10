import random 
import matplotlib.pyplot as plt


# Tento kód vytvorí náhodnú maticu o rozmere n s prvkami 1 alebo -1.

def pociatocny_stav(k):
    mriezka=[] 
    for i in range(k):
        riadok = []
        for j in range(k):    
            riadok.append(random.choice([1, -1]))  # Náhodné číslo z množiny {-1,1}
        mriezka.append(riadok)
    return mriezka


# Výpočet energie pre stav daný maticou mriežky.  

def energia(matica):
    S=matica
    n=len(matica)
    H=0
    for i in range (0,n-2):
        for j in range (0,n-2):
            Energia-=S[i][j]*(S[i-1][j]+S[i][j+1]) #príspevky zo stredu
    for i in range (0,n-2):
        Energia-=S[i][n-1]*S[i+1][n-1] #pravý roh
    for i in range (0,n-2):
        Energia-=S[n-1][i]*S[n-1][i+1] #príspevky zo spodného okraja mriežky
    return H 

#funkcia na výpočet zmeny energie po zámene spinu na pozícii (i, j) v mriežke. 

def delta_energia(matica, i, j):
    n = len(matica)
    spin = matica[i][j]
    delta_E = 0

    # Získanie susedov
    susedia = []
    if i > 0:
        susedia.append(matica[i-1][j])  # hore
    if i < n - 1:
        susedia.append(matica[i+1][j])  # dole
    if j > 0:
        susedia.append(matica[i][j-1])  # vľavo
    if j < n - 1:
        susedia.append(matica[i][j+1])  # vpravo

    # Výpočet zmeny energie
    for sused in susedia:
        delta_E -= 2 * spin * sused

    return delta_E

def magnetizacia (matica):
    S=matica
    n=len(matica)
    M=0




    

