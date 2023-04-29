"""
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)

"""

# dict1 = {
#     'Ana' : 8,
#     'Gigel' : 10,
#     'Dorel' : 5
# }
# print(dict1.keys())

"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
"""

# dict1 = {
#     'Ana' : 8,
#     'Gigel' : 10,
#     'Dorel' : 5
# }
# for keys, values in dict1.items():
#     print(f"Ana a luat nota: {dict1.get('Ana')}")
#     print(f"Gigel a luat nota: {dict1.get('Gigel')}")
#     print(f"Dorel a luat nota: {dict1.get('Dorel')}")
#     break


#alta varianta

dict1 = {
    'Ana' : 8,
    'Gigel' : 10,
    'Dorel' : 5
}
tuple_dict = tuple(dict1.keys())
print(tuple_dict)
for i in tuple_dict:
    print(f"{i} a luat nota {dict1.get(i)}")

for nume, nota in dict1.items(): # alta varianta, doar dictionarul si liniile astea 2
    print(f'{nume} a luat nota {nota}')
"""
5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
Lista este goală.
Lista nu este goală.

3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
  Găsește 2 variante să le unești într-o singură listă. 
"""

# list1 = [3,1,0,2]
# list2 = [6,5,4]
# gen_list = list(set().union(list1, list2)) # generam lista noua, o unim intr-o singura lista
# print(gen_list) # printam pentru verificare lista unita
# if not gen_list: # ex 5 sa folosim if pentru a genera daca lista este goala
#     print('Empty list')
# else:
#     print('List is not empty:\n', gen_list)

"""

6. Folosește o funcție care să șteargă lista de la exercițiul 3.

"""
# gen_list.clear()
# print(gen_list)

"""
10. Dorel a făcut contestație și a primit 6
Modifică nota lui Dorel în 6
Printează nota după modificare

"""

# dict1 = {
#     'Ana' : 8,
#     'Gigel' : 10,
#     'Dorel' : 5
# } # luam dictionarul cu notele de la primele exercitii
# dict1['Dorel'] = 6 # cu aceasta se modifica nota lui Dorel; se modifica prin keys valoarea
# print(f"Dorel are acum nota {dict1['Dorel']}, el a facut contestatie")

