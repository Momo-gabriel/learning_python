 #Lists

 #1


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#lista2 = range(1, 11)


# a&b

user_input = input("Enter a number between 1 and 999: ")

# transforma input in int (pozitive negative integers) 
# o alta varianta care stocheaza orice se introduce: lista.append(user_input)
lista.append(int(user_input))
# lista.append(user_input)
print(lista)