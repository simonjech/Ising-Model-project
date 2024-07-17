import matplotlib.pyplot as plt
import numpy as np
from initialstate import pociatocny_stav, energia, magnetizacia
from metropolis import relaxacia, zmena_stavu
import matplotlib.animation as animation

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

# def stredna_magnetizacia (k,T,r,n):
#     M=0
#     for i in range (k):
#         M+=magnetizacia(relaxacia(pociatocny_stav(n),r,T)[i])/k
#     return M

#vytvorí súbor energií v rozsahu teplôt T1 až T2.

def stredovani_v_rozsahu (teploty,m,r,n):
    energie=[]
    magnetizace=[]
    for T in teploty:
        E, M = stredovani(m,T,r,n)
        energie.append(E)
        magnetizace.append(M)
    return energie,magnetizace

#vytvorí súbor magnetizácií v rozsahu teplôt T1 až T2.

# def magnetizacie_v_rozsahu (T1,T2,k,r,n):
#     magnetizacie=[]
#     teploty=[]
#     for T in range (T1,T2):
#         magnetizacie.append(stredna_magnetizacia(k,T,r,n))
#         teploty.append(T)
#     return [teploty,magnetizacie]

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
ax1.set_ylabel('$H$')
ax1.set_title('Závislosť energie od teploty')


# Graf magnetizácie 
ax2.scatter(Teploty, Magnetizacie, color='r')
ax2.set_xlabel('$T$')
ax2.set_ylabel('$M$')
ax2.set_title('Závislosť magnetizácie od teploty')


plt.tight_layout()
plt.show()
#zobrazenie vývinu stavu 

n=20 #rozmer mriežky 
T=1 # teplota
r=10 # počet relaxovaných stavov
A=relaxacia(pociatocny_stav(n),r,T)

# Vytvorenie animácie
fig, ax = plt.subplots()

# Inicializácia mriežky
im = ax.imshow(A[0], cmap='gray')
ax.set_title(f'Vývoj stavu - Teplota $T={T}$, Počet stavov $r={r}$.')

def update(frame):
    im.set_array(A[frame])
    return [im]

ani = animation.FuncAnimation(fig, update, frames=len(A), interval=400, blit=True)

plt.show()

