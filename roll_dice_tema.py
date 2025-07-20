##p1##

numar = int(input("Introduceti un numar: "))
# numar = int(numar)
if numar / 2 == int():   #if numar % 2 == 0  #de ce 0 si de ce procent
    print("even")
else:
    print("odd")
if numar >= 10:
    print("The number is bigger or equal to 10")
if numar % 5 == int():
    print("The number is multiple of 5")
else:
    print("The number is not multiple of 5")
if numar >= 1 and numar <= 7:
    if numar == 1:
        print("Monday")
    elif numar == 2:
        print("Tuesday")
    elif numar == 3:
        print("Wednesday")
    elif numar == 4:
        print("Thursday")
    elif numar == 5:
        print("Friday")
    elif numar == 6:
        print("Saturday")
    elif numar == 7:
        print("Sunday")


##p2##

english_classes = int(input("Number of classes in English: "))
math_classes = int(input("Number of classes in Math: "))
english_attended = int(input("Number of classes attended in English: "))
math_attended = int(input("Number of classes attended in Math: "))
if math_attended >= english_attended:
  print("Math has a greater attendance")
else:
  print("English has a greater attendance")

math_attendeded_percentage = math_attended / math_classes * 100
english_attendeded_percentage = english_attended / english_classes * 100
print("Math attendance percentage: ", math_attendeded_percentage)
print("English attendance percentage: ", english_attendeded_percentage)
if (math_attendeded_percentage + english_attendeded_percentage)/2 >= 75:
  print("The overall attendance percentage is greater than 75%")
print((math_attendeded_percentage + english_attendeded_percentage)/2)


##p3##

# bet = int(input("Bet: $"))
# import random
# Nr = random.randint(1,6)
