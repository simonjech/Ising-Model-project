import math as m
import random as rd
from initialstate import delta_energia
import copy

k=1 #Boltzmanova konštanta

#funkcia, ktorá zmení stav podľa Metropolisovho algoritmu.

def zmena_stavu (matica,T):
    M = copy.deepcopy(matica) #matica výsledného stavu
    if T>0: #pripad T>0
        for i in range(len(matica)):
            for j in range(len(matica)):
                E_diff = delta_energia(M, i, j) #zmena energie dE
                if E_diff <= 0:
                    M[i,j] = -M[i,j]
                elif E_diff > 0 and T > 0 and rd.random() < m.exp(-E_diff / (k * T)): # PS - ošetření případu, kdy T = 0
                    M[i,j] = -M[i,j]
    elif T==0: #pripad T=0 
        for i in range(len(matica)):
            for j in range(len(matica)):
                E_diff = delta_energia(M, i, j)
                if E_diff <= 0:
                    M[i,j] = -M[i,j]
                elif E_diff > 0:
                    M[i,j] = M[i,j]
    return M
    
#funkcia, ktorá nechá systém r časových krokov relaxovať pri teplote T. 

def relaxacia (matica,r,T): #r je počet časových krokov
    for i in range(1, r):
        matica = zmena_stavu(matica, T)
    return matica


def vyvoj_stavu (matica,r,T): #počíta vývoj stavu
    subor_stavov=[matica]
    for i in range (1,r): 
        matica = zmena_stavu(matica, T)
        subor_stavov.append(matica)
    return subor_stavov
        


