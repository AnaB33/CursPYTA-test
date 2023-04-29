"""
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.

"""
#APARE EROARE CAND SE INTRODUCE UN FLOAT, ASTFEL CA TRB SA AVERTIZAM UTILIZATORUL-DECI trb editate variantele de mai jos
#Introducem x si y
# print("Introdu x:")
# x = int(input())
# print("Introdu y:")
# y = int(input())
# #Verificam daca x si y sunt egale sau nu
# if x == y:
#     print("x si y sunt egale")
# elif x != y:
#     print("x si y nu sunt egale")
#     # Verificam care dintre x si y este mai mare si afisam cel mai mare
#     if x > y:
#         print(f"Numarul mai mare dintre x si y este : x = {x}")
#     else:
#         print(f"Numarul mai mare dintre x si y este : y = {y}")

#alta varianta mai jos:
# x = int(input("x = "))
# y = int(input("y = "))
# if x == y:
#     print("Sunt egale")
# elif x > y:
#     print(f'{x} este mai mare decat {y}')
# else:
#     print(f'{y} este mai mare decat {x}')

#varianta 3
x = int(input("x = "))
y = int(input("y = "))
if x == y:
    print("Sunt egale")
else:
    print(f'Numarul mai mare este {max(x,y)}')