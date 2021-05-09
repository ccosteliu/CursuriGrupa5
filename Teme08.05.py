# Tema 1 OK
nume = input("Numele: ")
text_introdus = input("Va rugam sa introduceti textul: ")
if text_introdus.isdigit():
    raspuns = f"Sirul de numere a fost gasit de {nume}."
else:
    raspuns = f"Sirul de caractere a fost gasit de {nume}."
print(raspuns)


# Tema 2

numar_introdus = int(input("Introduceti un nr: "))

if numar_introdus % 2 == 1:
    text = f"Numarul introdus este impar"
elif numar_introdus % 2 == 0:
    text = f"Numarul introdus este par"
else:
    text = f'Introduceti doar cifre'
print(text)

# Tema 3

# anul = int(input("Anul: "))
#
# if anul % 4 == 1:
#     text = f"Acest an nu este bisect."
# elif anul % 4 == 0:
#     text = f"Acest an este bisect."
# print(text)

# Tema 4

# numar = eval(input("Introduceti un nr: "))
# if numar in range(1,10):
#     print("Numarul este pozitiv si mai mic decat 10")
# elif numar == 0:
#     print("Numarul este 0.")
# elif numar < 0:
#     print(f'Numarul pozitiv este: {abs(numar)}.')

#Tema 5
# meniu = ""
#
# while meniu.lower() != "quit":
#     meniu = input("> ")
#     if meniu == "help":
#         print("""
# 1 – Afisare lista de cumparaturi
# 2 – Adaugare element
# 3 – Stergere element
# 4 – Stergere lista de cumparaturi
# 5 - Cautare in lista de cumparaturi""")
#     elif meniu == "1":
#         print("Afisare lista de cumparaturi")
#     elif meniu == "2":
#         print("Adaugare element")
#     elif meniu == "3":
#         print("Stergere element")
#     elif meniu == "4":
#         print("Stergere lista cumparaturi")
#     elif meniu == "5":
#         print("Cautare in lista de cumparaturi")
#     else:print("Alegerea nu exista.Reincercati")
