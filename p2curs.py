# inp = input("Da a,b,c separate de ,: ")
# rez = inp.split(",")

# # rez = list(map(int, rez))
# # print(rez)
# a, b, c = rez
# a = int(a)
# b = int(b)
# c = int(c)

# sum = a + b + c
# diff = a - b - c
# prod = a * b * c

# print(sum)
# print(diff)
# print(prod)



# p2

# age = int(input("Age= "))
# months = int(input("Months= "))

# print(age * 12 + months)

# p3

# nr = int(input("Nr= "))
# if nr % 2 == 0:
#     print(True)
# else:
#     print(False)

# nr = int(input("Nr= "))
# print(nr % 2 == 0)

# p4

# a = float(input("a= "))
# b = float(input("b= "))
# c = float(input("c= "))

# sum = a + b + c
# print(sum)

# # scap de ce e dupa virgula si va verific daca e egal cu numaru intregit
# # 7.0 == 7  == True
# # 7.1 == 7 == False

# print(sum == int(sum))

# 7.1 -> 0.1 == 0

# p5

# year = int(input("Year="))

# is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# print(is_leap_year)
# The year must be evenly divisible by 4

# If it can be evenly divisible by 100, it is not a leap year
# If it is evenly divisible by 400, it is a leap year

# lista = [1,2,3,3,3,3]


# a = lista.pop(4)
# lista.remove(3)

# print(a)
# print(lista)


lista = [1,7,2,4,7,2,3,1]
# lista.reverse()

# print(lista)

# lista.sort(reverse=True)
# print(lista)


# print(max(lista))
# print(len(lista))

# print(all(lista))

a = sorted(lista)
print(lista)
print(a)