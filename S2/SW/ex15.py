"""

X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.

"""

x = float(input("Introduceti unghiul x: "))
y = float(input("Introduceti unghiul y: "))
z = float(input("Introduceti unghiul z: "))

if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print("Triunghiul este valid.")
else:
    print("Triunghiul nu este valid.")
print('' * 80)