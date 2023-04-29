"""
8.
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.

"""
x, y, z = input("tasteaza 3 numere intregi despartite de virgula :\n ").split(',')
print(f"x={x}\n y={y}\n z={z}\n")
if x == y and y != z:
    print("Triunghiul este isoscel")
elif x != y and y == z:
    print("Triunghiul este isoscel")
elif x != y and x == z:
    print("Triunghiul este isoscel")
elif x == y and y == z:
    print("Triunghiul este echilateral")
else: #daca nici una din variantele de mai sus nu este indeplinita atunci printam este oarecarere
    print("Triunghiul este oarecare")