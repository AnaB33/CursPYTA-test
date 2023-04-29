"""
Functia print ne ajuta sa afisam intormatii in terminal
print(ceva, altceva, etc) <= putem afisa oricate chestii, cu virgula intre ele
"""
print("Adela","Neacsu", "hello", 1234, True)
#print(Ce mai faci?) # va da eroare, nu este un tip de data valid

nume = "Adela Neacsu"
print("Numele meu este" + nume)

#functia print trece pe o line noua la fiecare apelare
print("numele meu este")
print(nume)

varsta = 30
#print("Varsta mea este" + varsta) = va da eroare
# f-string => un mod may phytonic de a afisa variabile in mesajele noastre
# punem un f'' si numele de variabile le punem intre {}

print(f"Numele meu este {nume} si am {varsta} ani")