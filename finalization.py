import matplotlib.pyplot as plt
import numpy as np
from initialstate import pociatocny_stav, energia, magnetizacia
from metropolis import relaxacia, zmena_stavu

#funkcia na výpočet strednej hodnoty energie 


def stredovani (m,T,r,n): #m je počet stredovaných energií, T je teplota, r je počet časových krokov pre relaxáciu systému, n je rozmer mriežky. 
    mrizka = pociatocny_stav(n)	
    relaxovana_mrizka = relaxacia(mrizka,r,T)

    nova_mrizka = relaxovana_mrizka
    H = 0
    M = 0
    for i in range (m):
        nova_mrizka = zmena_stavu(nova_mrizka, T)
        H += energia(nova_mrizka)
        M += magnetizacia(nova_mrizka)

    return H / m, M / m


def stredovani_v_rozsahu (teploty,m,r,n):
    energie=[]
    magnetizace=[]
    for T in teploty:
        E, M = stredovani(m,T,r,n)
        energie.append(E)
        magnetizace.append(M)
    return energie,magnetizace


m = 200
r = 200
n = 50
Teploty = np.linspace(0, 4, 100) # Interval teplôt

Energie, Magnetizacie = stredovani_v_rozsahu(Teploty, m, r, n)
# Magnetizacie = magnetizacie_v_rozsahu(T1, T2, k, r, n)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Graf energie
ax1.scatter(Teploty, Energie, color='b')
ax1.set_xlabel('$T$')
ax1.set_ylabel('$H(T)$')
ax1.set_title('Závislosť energie od teploty')


# Graf magnetizácie 
ax2.scatter(Teploty, Magnetizacie, color='r')
ax2.set_xlabel('$T$')
ax2.set_ylabel('$M(T)$')
ax2.set_title('Závislosť magnetizácie od teploty')


plt.tight_layout()
plt.show()


