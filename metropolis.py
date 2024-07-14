import math as m
import matplotlib.pyplot as plt
import random as rd
from initialstate import pociatocny_stav, energia, delta_energia, magnetizacia
import copy
import matplotlib.animation as animation

k=1 #Boltzmanova konštanta

#funkcia, ktorá zmení stav podľa Metropolisovho algoritmu.

def zmena_stavu (matica,T):
    S=matica #matica počiatočného stavu
    M = copy.deepcopy(S) #matica výsledného stavu
    for i in range(len(matica)):
        for j in range(len(matica)):
            E_diff = delta_energia(S, i, j) #zmena energie dE
            if E_diff <= 0:
                M[i][j] = -S[i][j]
            elif E_diff > 0 and rd.random() < m.exp(-E_diff / (k * T)):
                M[i][j] = -S[i][j]
    return M

#funkcia, ktorá nechá systém r časových krokov relaxovať pri teplote T. 

def relaxacia (matica,r,T): #r je počet časových krokov
    M = [None] * r
    stavy = []
    M[0] = matica
    stavy.append(M[0])
    for i in range(1, r):
        M[i] = zmena_stavu(M[i-1], T)
        stavy.append(M[i])
    return stavy

