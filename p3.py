# ##p1##
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# user_input=input("Introdu un numar: ")
# lista.append(int(user_input))
# print(lista)

# lista.pop(3)
# print(lista)

# idx = lista.index(9)
# lista.append(idx)
# print(lista)

# lista.remove(max(lista))
# print(lista)

# lista.reverse()
# print(lista)

# suma = sum(lista[:5])
# print(suma)

# avrage = sum(lista[-5:])/len(lista[-5:])
# print(avrage)

# diferenta = lista[0] - lista[-1]
# print(diferenta)




# # # ##p2##palindrome
# lista = input("Insert a word: ")
# # # lista1 = lista.split[0, -1]
# lista1 = lista.reverse()
# print(lista)


##de la clasa
# lista = input("Insert a word: ")
# print(lista[::-1])          # 1 string/list/tuplu/set # daca si cum se poate reverse la un string prin alta metoda

# lista.reversed()    # 2 liste/tupluri/set
# lista = reversed(lista)   # 3 liste/tupluri/set

# print(reversed(lista))


# ##p3##
# my_list = [1, 2, [1, 2, 3 ], 3, 4, [4, 5, 6, 7, 8], 4, 5, 6]
# flattend_list = []

# # #print(len(my_list))

# for el in my_list:
#   if type(el) is int:  # if isinstance(el, int):
#     flattend_list.append(el)
#   elif type(el) is list:
#     flattend_list.extend(el)
# print(my_list)
# print(flattend_list)
# print(flattend_list.count(4))



####tuple###

# tuplu = tuple([1, 2, 3])
# tuplu = (1, 2, 3)

# print(tuple(tuplu))  # convert to tuple
# print(tuplu)

##tuple unpacking

# COORD_BAZA = (1, 2 ,10)
# print(COORD_BAZA.count(2))
# print(COORD_BAZA.index(10))

# x, y, z = COORD_BAZA

# print(x)
# print(y)
# print(z)
# print(x, y, z)





setu = {1, 2, 3, 4, 1, 2, 3, 4 }

                   ### set() epty set
                   
# setu1 = {}  #  dictionar
# print(type(setu1))
# setu. add(77)
# # print(setu)
# print(list(setu))  # convert set to list
# # print(setu[0])  # nu merge, setul nu are index
# print(setu.pop())  # elimina un element random din set
# print(setu)
print(setu.remove(2))  # elimina elementul 2 din set
