"""
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
"""
while True: #pentru a forta utilizatorul sa introduca ce trb la tastatura
    x = input("Introdu valoarea lui x: ")
    y = input("Introdu valoarea lui y: ")
    try: #incearca codul asta,  vezi daca iti da vreo eroare. Daca nu da, treci mai departe. Daca are eroare la blocul de try intra formula except(un fel de else)
        x = float(x)
        y = float(y)
    except:
        print("Mai incearca!")
        continue
    if x - y < 5:
        print(f"Diferenta dintre {x} si {y} este mai mica 5, mai exact {x-y}")
        break
    else:
        print(f"Diferenta dintre {x} si {y} nu este mai mica de 5, este {x-y}")
        break
print("_" * 70)
