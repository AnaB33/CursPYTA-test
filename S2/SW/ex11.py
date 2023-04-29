"""
11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

12.Verifică dacă x are exact 6 cifre.


"""

while True:
    x = input('Introduceti valoarea lui x\n')
    if x.isdigit():
        if int(x[0]) == 0: # daca prima pozitie din valoare este 0 atunci printam x are valori de 0
            print(f'{x} are valori de 0')
            continue
        else:
            break
    elif not x.isdigit():
            print('Ai introdus litere')
    else:
        break
cifre = int(len(x))
if cifre == 4:
    print(f'{x} are 4 cifre!')
elif cifre == 6:
    print(f'{x} are exact 6 cifre!!')
else:
    print(f'{x} nu are 4 cifre si nici exact 6!')
