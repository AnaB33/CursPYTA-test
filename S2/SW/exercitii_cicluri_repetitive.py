"""
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
8. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).

"""

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
i = 0
suma = 0
for numere[i] in numere:
    suma = suma + numere[i]
    i += 1
print(f'suma este: {suma}')

"""
varianta 2:
"""

suma = 0
for i in range(len(numere)):
    suma = suma + numere[i]
print(f"Suma numerelor din lista este: {suma}")
