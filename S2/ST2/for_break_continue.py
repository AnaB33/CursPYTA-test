"""
Putem controla iteratiile noastre folosind doua cuvinte cheie:
- break (rupe) => opreste tot for-ul, si nu se mai trece la vreo alta iteratie
- continue (continua) => opreste iteratia curenta si trece mai departe (practic, sarim peste o iteratie)
"""
print(f"inainte de for")
for nr in range(1, 10): # 1 , 2, 3, 4, 5, 6, 7, 8, 9
    if nr == 5:
        break # vom "opri" for ul atunci cand ajugem la valoarea 5
    print(f" Numarul curent este {nr}")
print("Dupa for")

print("_", 80)
for nr in range(10): # de la 0 la 9 caci nu se mentioneaza startul
    print(f" Testam numarul {nr}. Este par? " )
    if nr % 2 == 1: # testam daca e impar
        continue # daca numarul este impar, sarim peste el
    print(f"\tNumar par: {nr}")
print(f"Am terminat de verificat numerele")

print("_" * 80)
students = ["Adela", "Anastasia", "Diana", "Petru", "Ana Maria", "Roxana", "Ionut", "Alin"]
for name in students:
    if name[0] != "A": # daca prima litera a numelui NU este A
        continue # trecem mai departe
    print(f"Numele persoanei este {name}")

print("_" * 80)
"""
Exercitiu: am o lista de numere si vreau sa gasesc un nr negativ in lista (oricare)

"""
numbers = [1, 4, -5, 10, -12, 100, 0, 1, 23, -27]
for numar in numbers:
    if numar < 0:
        print(f"Am gasit un numar negativ: {numar}")
        break # se opreste la primul nr negativ caci am folosit break
    print(f"Nu am gasit inca un numar negativ, mai cautam..")

"""
DACA nu exista nici un nr negativm vreau sa mi se afiseze asta

Vom folosi sintaxa for-else, care functioneaza asa:
if else va fi apelat doar daca tot FOR ul a rulat normal si nu a ajuns niciodata la ..
"""
print("_" * 80)
numbers = [1, 4, 10, 100, 0, 1, 23]
for numar in numbers:
    if numar < 0:
        print(f"Am gasit un numar negativ: {numar}")
        break  # se opreste la primul nr negativ caci am folosit break
    print(f"Nu am gasit inca un numar negativ, mai cautam..")
else: #nobreak
    # vom ajjunge aici doar daca nu am avut break in for ul anterior (adica nu am avut nr negative ca sa se active break)
    print("Nu am gasit niciun nr negativ")

