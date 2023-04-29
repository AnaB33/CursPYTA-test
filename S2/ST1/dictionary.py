"""
Dictionary (dictionar) = o structura de date de tipul cheie - valoare,
cu mentiunea ca cheile trebuie sa fie unice!
sintaxa:
{
    cheie1: valoare1,
    cheie2: valoare2,
    cheieX: valoareX
}
"""
d ={
    'dictionary': 'dictionar',
    'car': 'masina',
    'programming': 'programare'
}

train = {
    'white': 'rocks',
    'red': 'iron',
    'blue': 'cereals',
    #'white' - nu pot avea chei duplicate
}

"""
Un dictionar se acceseaza la fel ca si o lista, cu diferenta ca aici nu avem indecsi,
asa ca accesam elementele pe baza cheilor
"""
print(train['white']) # va printa rocks
print(train['red'])

"""
Daca folosim numere intregi incepand cu 0 intr-un dictionar, este la fel ca si o lista
"""

dict_as_list = {
    0: 'Ana',
    1: 'are',
    2: 'mere'
}
my_list = ['Ana', 'are', 'mere']
print(dict_as_list[0], my_list[0])

"""
In valorile dictionarelor putem pune orice tipuri de date,
dar cheile sunt putin mai restrictionate:
putem folosi string, ints, floats, 

"""
"""db = {
    True: "aceasta este true"
    False: "aceasta este false"
    # True: nu putem repeta cheile
}
"""

dict_complex = {
    'id': 1,
    'name': ['Adela', 'Neacsu'],
    'height': 1.80,
    'course': {
        'name': 'Python + Testare automata',
        'start_date': '27 martie 2023'
    }
}
print(dict_complex['name'][0]) # va printa "Adela"
print(dict_complex['name'][1]) # va printa "Neacsu"
print(dict_complex['course']['name']) # va printa 'Python + Testare automata'

print('_' * 80)
print(len(dict_complex))
dict_complex['id'] = 10 #schimbarea valorii se face prin atribuirea unei noi valori
dict_complex['age'] = 31 # adaugarea unui nou element (cheie-valoare)
print(dict_complex)

del dict_complex['course'] # stergerea unui element din dictionar
print(dict_complex)

"""

Cum putem vedea toate cheile unui dictionar? folosind metoda keys()
pPutem verifica d

"""
print(dict_complex.keys()) # partea stanga din dictionar, adica keys
print(dict_complex.values()) # partea dreapta, adica valorile
# print(dict_complex['course']) # va da eroare, pt ca mai sus a fost eliminat
print(dict_complex.get('course')) # va da NONE, o valoare speciala Python , daca cheia nu exista
dict_complex.clear() # va sterge toate elementele din dictionar
print(dict_complex) # va afisa {}, adica dictionarul gol

