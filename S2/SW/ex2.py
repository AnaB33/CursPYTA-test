"""
2. Verifică și afișează dacă x este număr natural sau nu.
(un numar natural inseamna sa fie numar intreg pozitiv)
"""


x = int(input("Introduceti un numar:\n"))
if x >= 0:
    print(f"{x} este numar natural")
else:
    print(f"{x} nu este numar natural")