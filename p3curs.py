# # # lista = list(range(10))
# # # print(lista)

# # # print(lista[::-1])  # 1 string/list/tuplu/set
# # # lista.reverse()  # 2 liste/tupluri/set
# # # lista = reversed(lista)  # 3 liste/tupluri/set

# # # inp = input('da un palindrom= ')

# # # print(reversed(inp))


# # # You have the following list: my_list = [1, 2, [1, 2, 3], 3, 4, [4, 5, 6, 7, 8], 4, 5, 6]. Create a program that:
# # # Print the length (explain the result)
# # # Programmatically recreate the list, but with the elements from the nested lists to be in the parent list
# # # Print the number of occurrences of the number ‘4’

# #         #                                                             el
# # my_list = [1, 2, [1, 2, 3], 3, 4, [4, 5, 6, 7, 8], 4, 5, 6]
# # flattend_list = []
# # # print(len(my_list))

# # for el in my_list:
# #     if type(el) is int:  # if isinstance(el, int):
# #         flattend_list.append(el)
# #     elif type(el) is list:
# #         flattend_list.extend(el)
# #     elif type(el) is str or type(el) is float:
# #         flattend_list.append(int(el))


# # print(my_list)
# # print(flattend_list)
# # print(my_list.count(4))
# # # print(flattend_list.count(4))


# # tuplu = tuple([1,2,3])
# # tuplu = (1, 2, 3)

# # print(type(tuplu))

# # tuple unpacking
# # COORD_BAZA = (1, 2, 10)
# # print(COORD_BAZA.index(2))


# # x, y, z = COORD_BAZA

# # print(x)
# # print(y)
# # print(z)

# setu = {1, 2, 2, 3, 4, 5, 5,8,1,6,2,3,0,6,3,5,12,76,52,86,24,74,23,85,23,13}

# # # setu1 = set()
# # # print(type(setu1))


# # setu.add(-1)
# # print(setu)

# # print(list(setu))

# # setu.clear()
# # print(setu)

# # setu.discard(3)
# # print(setu)

# # while setu:
# #     el = setu.pop()
# #     print(el)


# # setu = {1, 2, 2, 3, 4, 5, 5,8,1,6,2,3,0,6,3,5,12,76,52,86,24,74,23,85,23,13}
# # setu2 = {1, 2, 2, 3, 4, 5}

# # print(setu.union(setu2))
# # print(setu.intersection(setu2))

# # nume: "Razvan"
# # bani: 2.0
# # age: 20
# # height: 200
# # note: [10, 9, 5, 3]


# # persoana = ["Razvan", 2.0, 1, 2, 3, 4, 20, 200, [10,9,5,3]]

# # persoana[6] += 1


# # note
# # romana: 10
# # mate: 9
# # info: 5
# # spaniola: 3

# # note["spaniola"] = 5

# # from pprint import pprint as pp

# persoana = {
#     "nume": "Ritivoi",
#     "prenume": "Razvan",
#     "varsta": 10,
#     "bani": 2.0,
#     "greutate": 12.6,
#     "note": [10, 9, 8, 2],
#     1: "unu",
#     2: "doi",
#     404: "Cod eroare nu am gasit informatia"
# }

# # Luam valori

# # nume = persoana["nume"]
# # print(persoana["nume"])

# # Modidicam valori existente

# persoana["varsta"] += 1
# persoana["prenume"] = "Razvan-Nicolae"
# persoana["varsta"] = "24"

# # Adaugam perechi cheie valoare

# persoana["e_major"] = False
# persoana["note_amanuntite"] = {
#     "matematica": 10,
#     "info": 5,
#     "engleza": 2
# }
# print(persoana)
# if persoana["e_major"]:
#     persoana["poate_sa_bea"] = True

# # Stergem intrare

# persoana.pop("greutate")

# print(persoana.get("poate_sa_bea", False))  # Daca nu suntem siguri ca poate exista, mai bine folosim .get
# # print(persoana["poate_sa_bea"])  # Daca stim sigur ca exista cheia, putem folosi varianta asta


# # print(persoana.items())

# # for key, value in persoana.items():
# #     print(f"Key={key}, Val={value}")

# # print(persoana.keys())

# # Stergem selectiv anumite chei, sau facem checks
# # lista = list(persoana.keys())
# # for key in lista:
# #     if type(key) is int:
# #         persoana.pop(key)

# # pp(persoana)

# # note_2 = [("ani_de_scoala", 5), ("zile_de_condus", 6)]
# # persoana.update(note_2)

# # pp(persoana)

# pp(persoana.items())  # lista de tupluri cheie valoare
# pp(persoana.keys())  # lista chei
# pp(persoana.values())  # lista valori

my_dict = {
    "student_1": {
        "math": [4, 4, 5, 5],
        "physics": [4, 5, 5, 6],
        "english": [8, 9, 9, 10],
    },
    "student_2": {
        "math": [8, 10, 10, 7],
        "physics": [8, 10, 10, 10],
        "english": [7, 5, 1, 8]
    }, "student_3": {
        "math": [9, 9, 9, 10],
        "physics": [8, 8, 7, 10],
        "english": [10, 10, 9, 10]
    }
}

print(my_dict["student_1"]["purtare"]["sem2"])

my_dict = {
    'emp1': {
        'name': 'Jhon',
        'salary': 7500
    },
    'emp2': {
        'name': 'Emma',
        'salary': 8000
    },
    'emp3': {
        'name': 'Brad',
        'salary': 6500}
}


my_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

