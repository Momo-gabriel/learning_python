###p1###
a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))

sum = a + b + c
diff = a - b - c
prod = a * b * c

print(sum)
print(diff)
print(prod)
####

inp = input("Da a,b,c separate de ,: ")
rez = inp.split(",")

# rez = list(map(int, rez))
# print(rez)
a, b, c = rez
a=int(a)
b=int(b)
c=int(c)
sum = a + b + c
diff = a - b - c
prod = a * b * c

print(sum)
print(diff)
print(prod)



###p2###

age = int(input("Age="))
months = int(input("Months="))

print(age * 12 + months)

###p3###

# nr = int(input("Nr="))
# if nr % 2 == 0:
#     print("True")
# else:
#     print("False")

nr = int(input("Nr="))
print(nr % 2 == 0)


###p4###

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

sum = a + b + c
print(sum)

#scap de ce e dupa virgula si sa verific daca e egal cu numarul intregit
#7.0 == 7 == True
#7.1 == 7 == False

print(sum == int(sum))



###p5###

year = int(input("Year="))

is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap_year)

