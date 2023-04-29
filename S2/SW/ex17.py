"""

17. Același string 'Coral is either the stupidest animal or the smartest rock'.
Declară un string nou care să fie format din primele 5 caractere + ultimele 5.

"""
string1 = "Coral is either the stupidest animal or the smartest rock" # stringul initial
string2 = string1[:5]+ string1[-5:] # se declara noul string
print(f"Noul string este {string2}") # se printeaza pentru verificare