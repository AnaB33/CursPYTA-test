"""
 Citește de la tastatură:
numele;
prenumele.
    Afișează: 'Numele complet are x caractere'.

"""
nume = input ("Introdu numele:\n")
prenume = input("Introdu prenumele:\n")
nrcaract = len(nume)+len(prenume)
print(f"Numele complet are {nrcaract} caractere") # folosita doar daca declaram variabila nrcaract
print(f"Numele complet are {len(nume+prenume)} caractere") # o putem folosi fara nrcaract=...'putem folosi si len(nume)+len(prenume)

"""
exemplu 2

nume = input('Nmele meu este ')
prenume = input('Prenumele meu este ')
print(f"Numele meu are {len(nume)+ len(prenume)}  caractere.")
"""