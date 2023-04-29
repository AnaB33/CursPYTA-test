"""
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
"""

x = input("Introduceti o valoare pentru x: ")
x = int(x) # daca se introduce un float il transformam direct in int
if x >=1: # sau x > 0
    print("Numarul este pozitiv")
elif x <= 1 and x!= 0: # sau x <0
    print("Numarul este negativ")
else:
    print("Numarul este neutru")