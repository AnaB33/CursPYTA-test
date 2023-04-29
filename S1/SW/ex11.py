"""
Exercițiu:
citește de la tastatură un string de dimensiune impară;
afișează caracterul din mijloc.

"""

inp_string = input("Introdu un string impar, minim 3 caractere:\n")
print(len(inp_string)) # cate caractere contine stringul adaugat de noi de la tastarura
print(len(inp_string) // 2) # ne arata pozitia caracterului din mijloc (a e pe pozitia 0, b pozita 1)
print(inp_string[len(inp_string) // 2]) # pe ce pozitie se regaseste fiecare caracter dintr-un string, indexarea in []

""""
exemplu 2

np_string = input("Introdu un string impar, minim 3 caractere:\n")

# mai intai eliminam stringurile neconforme: mai mici de 3 sau pare:

if len(inp_string) < 3:
    print("Ai introdus mai putin de 3 caractere!")
elif (len(inp_string) % 2) == 0:
    print("Numarul caracterelor introduse este par, te rog introdu un string impar!")

# daca totul e ok atunci printam rezultat

else:
    print(f"Caracterul din mijloc este: {inp_string[len(inp_string) // 2]}")    # parantezele patrate se folosesc pentru indexarea caracterelor din string
"""

