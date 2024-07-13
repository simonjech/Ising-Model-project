import matplotlib.pyplot as plt
from initialstate import pociatocny_stav, energia, magnetizacia
from metropolis import relaxacia
import matplotlib.animation as animation

#funkcia na výpočet strednej hodnoty energie 


def stredna_energia (k,T,r,n): #l je počet stredovaných energií, T je teplota, r je počet časových krokov pre relaxáciu systému, n je rozmer mriežky. 
    H=0
    for i in range (k):
        H+=energia(relaxacia(pociatocny_stav(n),r,T)[i])/k
    return H

def stredna_magnetizacia (k,T,r,n):
    M=0
    for i in range (k):
        M+=magnetizacia(relaxacia(pociatocny_stav(n),r,T)[i])/k
    return M

#vytvorí súbor energií v rozsahu teplôt T1 až T2.

def energie_v_rozsahu (T1,T2,k,r,n):
    energie=[]
    teploty=[]
    for T in range (T1,T2):
        energie.append(stredna_energia(k,T*1.5,r,n))
        teploty.append(T*1.5)
    return [teploty,energie]

#vytvorí súbor magnetizácií v rozsahu teplôt T1 až T2.

def magnetizacie_v_rozsahu (T1,T2,k,r,n):
    magnetizacie=[]
    teploty=[]
    for T in range (T1,T2):
        magnetizacie.append(stredna_magnetizacia(k,T,r,n))
        teploty.append(T)
    return [teploty,magnetizacie]

k = 3
r = 6
n = 50
T1, T2 = 1, 200  # Rozsah teplôt

Energie = energie_v_rozsahu(T1, T2, k, r, n)
Magnetizacie = magnetizacie_v_rozsahu(T1, T2, k, r, n)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Graf energie
ax1.scatter(Energie[0], Energie[1], color='b')
ax1.set_xlabel('$T$')
ax1.set_ylabel('$H$')
ax1.set_title('Závislosť energie od teploty')


# Graf magnetizácie 
ax2.scatter(Magnetizacie[0], Magnetizacie[1], color='r')
ax2.set_xlabel('$T$')
ax2.set_ylabel('$M$')
ax2.set_title('Závislosť magnetizácie od teploty')


plt.tight_layout()
plt.show()
#zobrazenie vývinu stavu 

n=200 #rozmer mriežky 
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

