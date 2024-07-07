import numpy as np
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
    '''
    Kedže molekuly v rôznych častiach mriežky interagujú s rôznym počtom susedov, tak som celkovú energiu rozdelil na tri členy E=E_kraj+E_roh+E_stred.  
    '''
    E_kraj=0 #Príspevok energie krajných molekúl bez rohov.
    E_hore=0
    E_dole=0
    E_vpravo=0
    E_vlavo=0
    E_stred=0 #Príspevok energie vnúorných molekúl.  
    # E_R je príspevok energie od krajných atómov v rohoch mriežky. 
    E_roh=-(S[0][0] * (S[0][1] + S[1][0]) + S[0][n-1] * (S[0][n-2]+S[1][n-1]) + S[n-1][0] * (S[n-2][0] + S[n-1][1]) + S[n-1][n-1] * (S[n-2][n-1] + S[n-1][n-2]))

    for i in range (1,n-1):
        E_hore -= S[0][i] * (S[0][i+1] + S[0][i-1] + S[1][i])
        E_dole -= S[n-1][i] * (S[n-1][i+1] + S[n-1][i-1] + S[n-2][i])
        E_vpravo -= S[i][n-1] * (S[i+1][n-1] + S[i-1][n-1] + S[i][n-2])
        E_vlavo -= S[i][0] * (S[i+1][0] + S[i-1][0] + S[i][1])
    E_kraj=E_hore+E_dole+E_vpravo+E_vlavo

    for i in range (1,n-1):
        for j in range (1,n-1):
            E_stred -= S[i][j] * (S[i+1][j]+S[i][j+1]+S[i-1][j]+S[i][j-1])

    E=E_kraj+E_roh+E_stred
    return E

def delta_energia(matica, i, j):
    """
    Funkcia počíta zmenu energie po zámene spinu na pozícii (i, j) v mriežke.
    """
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




    

