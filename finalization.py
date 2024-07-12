import math as m
import matplotlib.pyplot as plt
import random as rd
from initialstate import pociatocny_stav, energia, delta_energia, magnetizacia
from metropolis import zmena_stavu, relaxacia

#funkcia na výpočet strednej hodnoty energie 

def stredna_energia (k,T,r,n): #k je počet stredovaných energií, T je teplota, r je počet časových krokov pre relaxáciu systému, n je rozmer mriežky. 
    H=0
    for i in range (k):
        H+=energia(relaxacia(pociatocny_stav(n),r,T))/k
    return H

def stredna_magnetizacia (k,T,r,n):
    



