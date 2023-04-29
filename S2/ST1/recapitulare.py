"""
s = "abracadabra"
print(s[0:11]) # ne returneaza toate pozitiile de la 0 la 11, adica tot cuvantul de 11 litere
print(s[1:11]) # ne returneaza incepand cu pozitia 1 adica litera b pana la ultima pozitie 11, litera a
print(s[7:10]) # ne returneaza cifrele incepand cu pozitia 7 (pozitia incepe cu 0) pana la pozitia 10 inclusiv = abr
"""

l = "abcdefg"    # 6 pozitii de la 0 la 6
nl = l[::2]         # aceg - se ia prima pozitie 0 (adica litera a la noi) si apoi din 2 in 2 =>aceg
print(nl)
nl = l[2:4:2]         #  c - se returneaza literele din 2 in 2 fara pozitia 0 si pana la pozitia 4 (fara a o include)
print(nl)
nl = l[1::2]     # bdf; a returnat din 2 in 2 al doilea caracter
print(nl)
nl = l[:7:2] # de la inceput pana la ultima pozitie (noi avem 6 pozitii, si am pus 7) , nr impar. din 1 in 1
print(nl)
nl = l[:6:2]           # de la inceput pana la ultima pozitie-1 , nr impar. din 1 in 1
print(nl)
nl = l[::-1]     # returneaza invers cuvantul, caracterele de la sfarsit la inceput pe TOATE
print(nl)
nl = l[::-2]        #RETURNEAZA DIN 2 IN 2 DE LA COADA, INCLUSIV ULTIMA POZITIE SI PRIMA
print(nl)
nl = l[::-3]       #RETURNEAZA DIN 3 IN 3 DE LA COADA, INCLUSIV ULTIMA POZITIE SI PRIMA
print(nl)

s = "ABCDEFGHIJKL"
print(s[0:10])         # DE LA PRIMA POZITIE LA POZITIA 10 - 1
print(s[2:10])             # de la pozitia 2 la pozitia 10 -1 =. cdefghij
print(s[3:10])

alta = "a b c d e f g h i j k l m"
print(alta[0:10])      # se numara si casutele si rezulta si casute si numaram de la prima pozitie 0 pana la poz 10-1
print(alta[2:10])
print(alta[3:10])