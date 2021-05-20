# LIST TUPLE DICT SET

# lista = []
# my_list = [8, 2, -2, 6]
# my_list_string = ['aaa', 'bbb', 'ccc',['www', 'ddd', 'qqq', ['rrr', 'ttt']]]
# print(my_list_string[3][3][1])
# print(my_list_string.index('bbb'))
# my_list_string.append('yyy')
# print(my_list_string)
# my_list_string.insert(1, 'kkk')
# my_list_string.remove('ccc')
# my_list_string.pop(3)
# my_list_string.pop()
# my_list_string.clear()
# my_list.extend(my_list_string)
# print(my_list_string+my_list)
# print(my_list)

# my_tuple = ()
# my_tuple = (1,)
# my_tuple2 = (3, 4)
# print(type(my_tuple))
# print(my_tuple+my_tuple2)

# my_dict = {'k1': 1, 'k2':2, 3:5, (2,3):7}
# my_dict[4] = "2bis"
# print(my_dict[5]) # daca cheia cautata nu exista eroare
# if 3 in my_dict:         # pt a verifica daca exista o cheie fara a da eroare
#     print(my_dict[3])
# print(my_dict[(2,3)])
# print(my_dict.get((4))) # se verifica daca exista o cheie in dict fara a da eroare in cazul in care nu exista

# my_dict.update({4: 'yiu', 5: 9})  # adaugare elemente in dictionar
# my_dict.clear() goleste  dictionarul
# print(my_dict.keys()) # returneaza toate cheile
# print(my_dict.values()) # returneaza toate valorile
# print(my_dict.items()) # returneaza toate cheile cu valorile
# print(my_dict.pop(3))
# my_dict.pop(3) scoate cheia specificata
# my_dict.popitem() scoate ultima cheie
# for key , value in enumerate(my_dict):
# for key, value in my_dict.items():
#  print(key, value, end=';')
# print(list(my_dict))

my_set = {1,2,3,2} # nu e indexabil
# print(my_set)
# my_set = {1, 2, 3}
my_set2 = {2, 3, 4}
my_set.add(5)
print(my_set)
# print(my_set|my_set2) #union aduna elementele dintre cele 2 seturi intr un set
# print(my_set & my_set2) # intersection - elemente comune intre cele 2 seturi
# print(my_set - my_set2) #difference - ce avem in primul set si nu avem in al2lea
# print(my_set2 ^ my_set) # symmetric difference elementele unice din amblele seturi

# list = list()
# set = set()
# tuple = tuple()