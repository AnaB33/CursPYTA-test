"""

21. Având stringul '0123456789'
Afișează doar numerele pare
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)

"""

#solutia 1:
# s = "0123456789"
# p = s[0:10:2]
# i = s[1:10:2]
# print(p)
# print(i)

#solutia 2:
# s = "0123456789"
# pare = list()
# impare = list()
#
# for n in list(s):
#     if int(n) % 2 == 0:
#         pare.append(n)
#     else:
#         impare.append(n)
#
# print(pare)
# print(impare)

#solutia 3:
str = "0123456789"
print(str[::2])
print(str[1::2])