"""
Functia input ne permite sa obtinem date de la utilizatorul programului nostru
"""
# print("Incepe programul...")
# input()   # programul asteapta aici infrmatii de la utilizator, si contina doar la enter
# print ('Gata')

# cu \n fortam cursorul sa treaca pe linia urmatoare
name = input("Care este numele tau?\n")
print (f"Salut, {name}!")

age = input("Ce varsta ai?\n")
age = int(age) #by default, input imi da mereu un string, e datoria mea sa il convertesc
print(f"Acum ai {age} ani, la anul vei avea {age +1} ani")