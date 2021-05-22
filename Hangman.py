cuvant = 'onomatopee'
lista_cuvant = list(cuvant)

# print(lista_cuvant)
# caractere = ' '.join(lista_cuvant)
# print(caractere)
lista_cuvant = []
for i in cuvant:
    if i != cuvant[0] and i != cuvant[-1]:
        lista_cuvant.append('_')
    else:lista_cuvant.append(i)
print(' '.join(lista_cuvant))
nr_incercari = 0
litere_incercate = []
while nr_incercari <= 7:
    litera_utilizator = input('Alege o litera:> ').lower()
               # print(lista_cuvant)
    if litera_utilizator in lista_cuvant:
        print('Litera aleasa este deja afisata...')
    elif litera_utilizator in litere_incercate:
        print(f'Litera {litera_utilizator} deja incercata. Pana acum ai incercat literele:{litere_incercate}')
    elif litera_utilizator in cuvant:
        for iterator, valoare in enumerate(cuvant):
            if valoare == litera_utilizator:
                lista_cuvant[iterator] = litera_utilizator # sau valoare
                # print(f'{iterator}=>{valoare}')
    else:
        litere_incercate.append(litera_utilizator)
        if litera_utilizator not in cuvant or litere_incercate:
            nr_incercari +=1
            print(f'Litera aleasa nu se gaseste in cuvantul secret.Mai aveti {7-int(nr_incercari)} incercari.')

    if 7 - int(nr_incercari)== 0:
        print(f'\nJocul a luat sfarsit.Cuvantul secret era {cuvant}.')
        break
    elif ''.join(lista_cuvant) == cuvant:
        print(f'Felicitari. Ai descoperit cuvantul {cuvant}.')
        break
    else:
        print(' '.join(lista_cuvant))

