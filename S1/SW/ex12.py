"""
 Folosind o singură linie de cod :
citește un string de la tastatură (ex: 'alabala portocala');
salvează fiecare cuvânt într-o variabilă;
printează ambele variabile pentru verificare

"""

"""
test_text = str(input("Introdu text:\n"))           #declaram string-ul de la tastatura
words = test_text.split()                           #impartim string-ul cu functia split
print(words)                                        #afisam lista de cuvinte
a, b = test_text.split(maxsplit=1)                  #declaram variabilele
print (f"valoarea lui a este: {a}")                                           #printam valoarea variabilelor
print (f"valoarea lui b este: {b}")
"""

"""
o rezolvare simpla si corecta:

var1, var2 = input("Introduceti un sir de caractere: ").split()
print(var1)
print(var2)

"""

#sau rezolvare mai complexa:

string_12 = input("Introduceti un string gen alabala portocala:\n")
string_separat = string_12.split()
print(string_separat)
for i in string_separat:
    print(i)


