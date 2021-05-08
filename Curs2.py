# print("Ana are mere")
# print("Ana \"are\" mere")
# nr1 = 2
# culoare = "rosii"

# variabila = "Ana are {1} mere {0}.".format(nr1,culoare)
#variabila = f"\tAna are \n{nr1} mere\n{culoare}. "
#variabila = "Ana are " + str(nr1) + " mere " + culoare + "."
# print(variabila)
#c = 0

# c -= a
# c = c -a
#c = a + b
#c = b * a
# c += a
#c = a / b
# c = a // b #cat
#c = a % b #modulo => rest

#print(f"Rezultatul este: {c}")
# a = 3.2
# b = int("2")

# a,b = 3.2, int("2")
#
# #print(type(b))
# a_boolean = True# => 1
# b_boolean = False# => 0
#
# #text = "Variabilele sunt egale"
# #text = None
# if a_boolean is True:
#     text = f"Variabila a {a} este mai mare"
# elif a < b:
#     text = f"Variabila b {b} este mai mare."
# elif a < 0:
#     text = f'Variabila a {a} este mai mica decat 0'
# print(text)

# while conditie:
#     sintaxa 1
#     sintaxa 2
#     ........

#convertire in string => str(variabila)
#convertire in integer => int(variabila)
#convertire in zecimale => float(variabila)
#convertire in boolean => bool(variabila)
# a = False
# while True:
#     print('bucla infinita')
#     a = False
#     #a += 1
#     #break
#     #continue
#
#nume_utilizator = input("Care este numele tau: ")
# # print(nume_utilizator)
# while nume_utilizator:
#     print(f"Numele utilizatortului este: {nume_utilizator}")
#     nume_utilizator = None
#     #break
# print(nume_utilizator)
# x = 10
# while x > 1:
#     print(f"x este {x}")
#     x -= 1
#     continue

# item = "Ana are mere"
# # for variabila temporara in item:
# # #     bloc expresii
# for variabila_temporara in reversed(item):
#      print(variabila_temporara)
#
# # for i in range(10, 1, -1):
# #     print(i)
# a = ["a", "b"]
# for index, value in enumerate (a):
#     print(index, value)

# a = "Anv are mere"
# # print(a[2])
# # a = a.replace("a", "d")
# # print(a)
# # print('ad' in a)
# # print(a.split(" "))
# # print(a.replace(' ', "_"))
# #print("_".join(a.split(" ")))
# for item in a:
#     if a.index(item) == 0 and item != " ":
#         a = a.replace(' ', '_')
# print(a)

list = ['a', 2, True,['a', "b", 3]]
# print()
# for item , x in enumerate(list):
#     print(item, x)
list.append(44)
list.insert(0, 'Ana')
list.pop(2)
print(list)
for index, value in enumerate(list):
    print(index, value)
print(list.pop(2))