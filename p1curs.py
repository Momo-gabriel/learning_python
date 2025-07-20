# a = 5 == 5
# print(a)


# var1 = "Abc"  # 65 98 99
# var2 = "aaz"  # 97 97 122

# print(var1 > var2)


# x = 5

# print(type(x) is int)
# print(isinstance(x, int))


# a = "What's my name?"
# masuratoare_cm = 5.2931

# a = "ana "
# b = "are "
# c = "mere."

# print(a+b+c)

# nume = input("Care e numele tau? ")
# age = input("Care e varsta ta? ")

# # string = "Salutare " + nume + "!"
# # print(string)

# string2 = f"Salutare {nume}, ai {(int(age) % 2 + 1) == 1} ani!"  # Best practice
# string3 = "Salut {} cine esti {}".format("Ana", "Mere")
# print(string3)


# -------------------

# isinstance("as", str)  # functie
# #         0123456789
# string = "Ana are ana mere roanasii siana mov"
#                    # substr, start, stop
# print(string.count("ana", 9, 25))  # metoda

#    0123456789

# print(a.startswith("Ana "))
# print(a.endswith("mere"))

# print(a.find("are1") != -1)
# print(a.count("are1") != 0)
# print("are" in a)

# a = input("What's you age? ")

# if a.isdecimal():
#     a = int(a)
# else:
#     print("Nu ai dat binem incearca iar")
#     a = input("What's you age? ")
#     a = int(a)

# print(type(a))

# a = "Ana are mere"
# a.replace("mere", "pere")

# print(a)

# lista_cumparaturi = ["lapte", "oua", "paine"]

# str_list = ", ".join(lista_cumparaturi)

# print(str_list)

# a = " Ana are mere "
# print(a)
# a = a.strip()
# print(a)

# a = "Ana are mere.Ana are si pere.Dar si alune"

# phrases = a.split(".")
# print(phrases)


# a = "Ana are mere si pere"

# words = a.split()
# print(words)

# a = """Aceasta nu e doar o carte de poezie, ci o hagiografie apocrifă a familiei Popescu, o evanghelie eretică a cotidianului transfigurat.

# Aici, pâinea dospește în vată, fotografiile își schimbă expresia pe furiș, iar tramvaiul 26 alunecă prin oraș ca o corabie funerară, un Styx urban de joasă tensiune. Fiecare gest capătă amploarea unui ritual, fiecare detaliu domestic își revendică locul într-o mitologie personală."""

# lines = a.splitlines()
# print(lines)


# a = "AnA ArE MeRe"

# print(a.capitalize())

# a = -145  # Truthy orice in afara de 0 (de valoarea defaultt, de baza)
# b = 0  # Falsy

# c = "asd" # Truthy, orice in afara de val neutra
# d = ""

# z1 = 1.2  # Truthy
# z2 = 0.0  # Falsy

# z3 = [1]
# z4 = []

# print(bool(b) == False)

# if b:
#     print("Da")



parola = input("parola= ")  # nume = ""  Falsy
is_valid = len(parola) > 10 and len(parola) < 32 and not parola.isalpha()
print(is_valid)