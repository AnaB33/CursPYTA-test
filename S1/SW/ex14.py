"""
Exercițiu:
citește un user de la tastatură;
citește o parolă;
afișează: 'Parola pt user x este ***** și are x caractere';
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

eg: parola abc => ***
      parola abcd => ****

"""

user = input("Introduceti un user:\n")
parola = input("Introduceti o parola:\n")
lungime_parola = len(parola)
indicator = '*' * lungime_parola
print(f"Parola pentru userul {user} este {indicator} si are {lungime_parola} caractere.")


# sau
user = input("Introduceti un user:\n")
parola = input("Introduceti o parola:\n")
lungime_parola = len(parola)
indicator = '*' * lungime_parola
print(f"Parola pentru userul {user} este {'*' * len(parola)} si are {len(parola)} caractere.") #varianta 2
print(f"Parola pentru userul {user} este {parola.replace(parola, '*' * len(parola))} si are {len(parola)} caractere.") #varianta 3
print(parola)

