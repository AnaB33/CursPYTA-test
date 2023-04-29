"""
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
Verifică tipul acesteia.

"""
steps = 16.900
steps = round(steps)

print('Dupa type casting:', type(steps))
print(steps)



valoare = 5
valoare = round(valoare)
print(f"Valoarea rotunjita a numarului {valoare} cu tip {type(valoare)}este {valoare}")


"""
exemplu 2

var_4 = float(input("Introdu o valoarea cu zecimale:\n"))
valoare = var_4
var_4 = round(var_4)
print(f"Valoarea rotunjita a numarului {valoare} cu tip {type(valoare)} este {var_4}")
"""