#Verifică dacă x are exact 6 cifre.

numar = int(input("Introdu numarul 'x' de la tastatura "))
if numar >= 100000 and numar < 1000000:
    print(f"x are exact 6 cifre ")
else:
    print(f"Numarul 'x' nu are exact 6 cifre ")

"""
ALTA VARIANTA:
"""

while True:
    x = input("Introduceti un numar: ")
    if not x.isdigit():
        print (f" {x} nu este numar. Mai incercati!")
    else:
        break
x = int(input("Introdu numarul 'x' de la tastatura "))
if numar >= 100000 and numar < 1000000:
    print(f"x are exact 6 cifre ")
else:
    print(f"Numarul 'x' nu are exact 6 cifre ")