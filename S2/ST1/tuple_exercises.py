"""
Tuple (tupla) = structura de date asemenatoare cu o lista, cu diferenta ca este IMUTABILA, adica odata declarata nu o
mai putem schimba in niciun fel
Sintaxa este cu paranteze rotunde()
"""

t = (1, 2, 3)
print(type(t))
print(t[0])
print(t[1])
print(f'Lungimea tuplei este de {len(t)} elemente')

# t[0] = 7 # va da eroare, nu putem schimba valorile existene
# del t[0] # va da eroare, nu putem sterge valori

tupla_complexa= (1, 2, True, 1, 2, "string", [100, 101, 102])
print(tupla_complexa)
tupla_complexa[6].append(103) # se poate modifica lista din cadrul tuplei, am adaugat 103 la lista din tupla, indexul 6 a fost modificat
print(tupla_complexa)

tupla_goala = ()
print(type(tupla_goala))