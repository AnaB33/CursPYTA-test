"""

Același string. Coral is either the stupidest animal or the smartest rock'

Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest'


"""
phrase = "Coral is either the stupidest animal or the smartest rock"
idx = phrase.find("rock")
print(phrase[:idx])