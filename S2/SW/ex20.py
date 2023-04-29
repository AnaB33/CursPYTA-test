"""
20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat

"""

x = input('String\n')
assert x[0].lower() == x[-1].lower(), 'Primul si ultimul caracter nu sunt la fel'
print('Primul si ultimul caracter sunt la fel')