"""
 Exercițiu:
citește un string de la tastatură (ex: alabala portocala);
salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
alt shift . =zoom mai mare
"""

tastatura = input("introduceti caracterul:\n")
print(tastatura)
x = tastatura[0] #salvez caracterul de pe prima pozitie
y = tastatura.replace(x, x.upper()) #am inlocuit stringul din pozitia 0, sa il faca cu litera mare indiferent de pozitia din cuvant
print(y) # ne va printa pe urmatorul rand toate literele din pozitia 0 si celelalte pozitii identice cu ea cu litera mare
print(y[0].replace(y[0],y[0].lower())+y[1:-1]+y[-1].replace(y[-1],y[-1].lower())) # -1 inseamna de la coada



"""
o varianta mai simpla:

x = input('String random')
y = x[0].lower()
k = x[-1].lower()
z = x.replace(y, y.upper())
print(f'{y +z[1:-1] + k}')
"""