"""
In general, folosim FOR pentru a itera peste colectii sau in situatii in care stim exact numarul de repetitii

While in schimb, este folosit atunci cand nu stim exact nr de iteratii, DAR
stim cand vrem sa ne oprim (adica avem o conditie de oprire)


"""
"exercitiu mai jos: avem o lista numbers:"
numbers = [4, 54, 6, 90, 12, -5, 0]
for number in numbers:
    print(number) # imi printeaza toate elementele pe rand

print("Parcurgere cu while")
idx = 0 # pornim de la primul element, cel cu index 0
while idx < len(numbers): # cat timp indexul este mai mic decat lungimea listei
    print(numbers[idx]) # daca ne oprim aici ne va da doar 4 intr-o bucla infinita asa ca mai adaugam o linie
    idx += 1 # trebuie sa incrementam NOI indexul, altfel intrram intr- o bucla infinita

"""
    ATENTIE MARE:
    in while, putem intra in bucla infinita, DACA conditia noastra nu devine niciodata False
"""

"""
Exercitiu: avem un numar, vrem sa afisam toate numerele divizibile cu 5,
intre acest numar si 100 inclusiv (folosind while)
"""

print("_" * 80)
nr = 12
while nr <= 100: # sa fie mai mic sau egal cu 100
    if nr % 5 == 0: # daca e divizibil cu 5
        print(nr)
        nr += 1
    else:
        nr += 1
        continue # skip catre urmatoarea iteratie
