"""
Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
"""
while True: #obliga utilizatorul sa introduca valoarea corecta
    x = input("Introdu valoarea lui x: ")
    try: #verifica daca valoarea introdusa este float
        x = float(x)
    except: # daca try are eroare
        print("Mai incearca")
        continue
    if not (5.0 < x < 27.0): #daca nu are eroare, incepe functia
    #if not (5 < x < 27):        # scriem asa daca vrem ca intervalul sa fie doar cu numere intregi
                                # sau if x not in range(5 < x < 27)
        print(f"{x} nu se afla in intervalul (5,27)")
        break
    else:
        print(f"{x} se afla in intervalul (5,27)")
        break

print("-"*70)

"""
alta metoda

introducem x-ul
print("Introdu un nr. ")
x = int(input())
verificam daca x-ul este sau nu intre 5 si 27 folosind operator logic "not"
if x not in range_(5, 27):
   print("Numarul NU ESTE intre 5 -27")
else:
   print("Numarul ESTE intr 5 -27")
   
   DAR AICI APARE O EROARE DACA SE INTRODUCE FLOAT DE LA TASTURA, ASA CA FOLOSIM DIN VARIANTA 1 PRIMA VERIFICARE
"""