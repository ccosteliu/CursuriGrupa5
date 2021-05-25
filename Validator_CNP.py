import datetime
valoare_cnp = input("Introdu CNP:> ")
# print(valoare_cnp[0])
if len(valoare_cnp) == 13:
    an = int(valoare_cnp[1:3])
    luna = int(valoare_cnp[3:5])
    zi = int(valoare_cnp[5:7])
    sex = int(valoare_cnp[0])
    cnp_jj = valoare_cnp[7:9]
    if sex == 9:
        print('Persoana straina')
    else:
        try:
            data_de_comparat = datetime.datetime(int(f"19{an}"), luna, zi)
            data_18 = datetime.datetime(int(f"18{an}"), luna, zi)
            data_20 = datetime.datetime(int(f"20{an}"), luna, zi)
            if sex == 1 and datetime.datetime(1900, 1, 1) < data_de_comparat < datetime.datetime(1999, 12, 31):
                print(f'Sex masculin nascut intre anii 1900 - 1999, luna: {luna}, ziua: {zi}')
            elif sex == 2 and datetime.datetime(1900, 1, 1) < data_de_comparat < datetime.datetime(1999, 12, 31):
                print(f'Sex feminim nascut intre anii 1900 - 1999, luna: {luna}, ziua: {zi}')
            elif sex == 3 and datetime.datetime(1800, 1, 1) < data_18 < datetime.datetime(1899, 12, 31):
                print(f'Sex masculin nascut intre anii 1800 - 1899, luna: {luna}, ziua: {zi}')
            elif sex == 4 and datetime.datetime(1800, 1, 1) < data_18 < datetime.datetime(1899, 12, 31):
                print(f'Sex feminim nascut intre anii 1800 - 1899, luna: {luna}, ziua: {zi}')
            elif sex == 5 and datetime.datetime(2000, 1, 1) < data_20 < datetime.datetime(2099, 12, 31):
                print(f"Sex masculin nascut intre anii 2000 - 2099, luna: {luna}, ziua: {zi}'")
            elif sex == 6 and datetime.datetime(2000, 1, 1) < data_20 < datetime.datetime(2099, 12, 31):
                print(f'Sex feminin nascut intre anii 2000 - 2099, luna: {luna}, ziua: {zi}')
            elif sex == 7:
                print("Sex masculin, rezident in Romania")
            elif sex == 8:
                print("Sex feminin, rezident in Romania")

            else:
                print('Sex nevalidat')
        except ValueError:
            print('Data nu este valida')




        dictionar_judete = {'01': 'Alba', '02': 'Arad', '03': 'Arges', '04': 'Bacau', '05': 'Bihor', '06': 'Bistrita Nasaud', '07': 'Botosani', '08': 'Brasov', '09': 'Braila', '10': 'Buzau', '11': 'Caras Severin', '12': 'Cluj', '13': 'Constanta', '14': 'Covasna', '15': 'Dambovita', '16': 'Dolj', '17': 'Galati', '18': 'Gorj', '19': 'Hargita', '20': 'Hunedoara', '21': 'Ialomnia', '22': 'Iasi', '23': 'Ilfov', '24': 'Maramures', '25': 'Mehedinti', '26': 'Mures', '27': 'Neamt', '28': 'Olt', '29': 'Prahova', '30': 'Satu Mare', '31': 'Salaj', '32': 'Sibiu', '33': 'Suceava', '34': 'Teleorman', '35': 'Timis', '36': 'Tulcea', '37': 'Vaslui', '38': 'Valcea', '39': 'Vrancea', '40': 'Bucuresti', '41': 'Bucuresti - Sector 1', '42': 'Bucuresti - Sector 2', '43': 'Bucuresti - Sector 3', '44': 'Bucuresti - Sector 4', '45': 'Bucuresti - Sector 5', '46': 'Bucuresti - Sector 6', '51': 'Calarasi', '52': 'Giurgiu', }

# JJ
        if cnp_jj in dictionar_judete.keys():
            print(f'Persoana nascuta in judetul :{dictionar_judete.get(cnp_jj)}.')
        else:
            print('Judet invalid')

        # NNN
        NNN = valoare_cnp[9:12]
        if int(NNN) == 000:
            print("NNN invalid")

# C
        cnp_control = list('279146358279')
        c = []
        for i in range(0, 12):
            c.append(float(int(valoare_cnp[i])*int(cnp_control[i])))
        # print(c)
        total = 0
        for i in range(0, len(c)):
           total += c[i]
        # print(f'Total C {total}')
        rest = total % 11
        # print(rest)
        if rest == int(valoare_cnp[-1]):
            print("'C' valid")
        elif rest == 10:
            var = valoare_cnp[-1] == 1
        else:print("'C' invalid")



else:
        print("CNP incomplet")

6110115169101