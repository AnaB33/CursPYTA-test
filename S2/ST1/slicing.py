"""
Slicing (feliere) = operatia care ne permite sa accesam mai multe elemente dintr-o lista
sau dintr-un string (care este de fapt doar o lista de caractere)
Sintaxa
lista[start:stop:pas] => pas este optional, valoarea lui default este 1
start reprezinta indexul de la care incepem accesarea, acesta este inclus in valoarea finala
stop reprezinta indexul la care ne oprim, dar acesta nu este inclus in valoarea finala
pas (step) reprezinta viteza cu care ne miscam de la start la stop, default 1
"""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nl = l[2:5] # voi obtine elemtenele din lista originala care sunt la indecsii de la 2 la 5
print(nl)

l3 = l[5:2:-1] # voi obtine [6, 5, 4]
print(l3)

l4 = l[0:len(l):2] # voi obtine elementele de la indecsii pari
print(l4)

"""
daca start = inceputul listai sau finalul daca mergem cu pas negativ putem sari peste aceasta valoare
daca stop = sfarsitul listei (sau inceputul daca mergem cu pas negativ) putem sari peste aceasta valoare
"""
l5 = l[::2] #echivalent cu l4
print(l5)

"""
o metoda f simpla de a inversa o lista este sa o parcurgem cu pas de -1
"""
lr = l[::-1]
print(lr)

"""
Deoarece stringurile sunt practic liste de caractere, si la ele se aplica aceleasi reguli de slicing
"""
s = "Ana are m" \
    "ere"
print(s[3:10]) # incepe de la pozitia 3 (adica spatiu) pana la poz 10 -1
print(s[::2]) # va merge de la inceput pana la final, mereu al doilea caracter
print(len(s))
print(s[10:100]) #nu va da eroare, dar vom primi caracterele existente pana la sfarsitul stringului

#nu denumiti variabilele list, pt ca este o functie
list = [100, 200] #DON'T