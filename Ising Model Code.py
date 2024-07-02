import numpy as np
import random 


'''
Tento kód vytvorí náhodnú maticu o rozmere n s prvkami 1 alebo -1.
'''
n=int(input("Zadaj rozmer mriežky "))

mriezka=[] 
for i in range(n):
    row = []
    for j in range(n):    
        row.append(random.choice([1, -1]))  # Náhodné číslo z množiny {-1,1}
    mriezka.append(row)
print(mriezka)





