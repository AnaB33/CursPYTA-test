"""

set = structura de date care nu permite duplicate
seturile nu sunt ordonate si nici indexate, putem doar adauga sau sterge elemente din ele
Sintaxa:
{elem1, elem2, elem3, ...elemx)
"""

s= {1, 2, 3, 1}
print(s) # va printa{1,2, 3} deoarece setul nu permite duplicate

s.add(7)
s.add(3)
print(s) # va printa {1, 2, 3, 7}

s.remove(2) # vom scoate elementul cu valoarea 2 (nu avem indecsi la set)
print(s)

"""
si setul poate tine orice tipuri de date
toate tipurile de date basic (int, float, bool, string)
liste NU
dictionare NU
ALTE SETURI NU
TUPLE - DA (1, 2) EX MAI JOS
Practic setul poate avea doar valori imutabile , care nu pot fi modificate
"""
set_complex = {1, 2, True, False, 'Ana are mere', (1, 2)}
print(set_complex)

# set_gol = {} # nu putem sa folosim {} pt ca asta e dictionar gol
set_gol = set() # asa facem un set gol
set_gol.add(100)
set_gol.add(12)
set_gol.add(True)
set_gol.add("stringulet")

print(set_gol)
set_gol.clear() # cu clear stergem toate elementele din set

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a.intersection(b)) #intersection = elementele comunte {4, 5}
print(a.difference(b)) # diferenta = elemente care exista in a, dar nu in b {1, 2, 3}
print(b.difference(a)) # elemente care exista doar in b
