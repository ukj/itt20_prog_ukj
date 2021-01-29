__author__='Uku-Kaarel Jõesaar, ITT20'
# 19.01.2021
# Ülesanne 05'
import os

def input_nimi(msg):
    '''
    '''
    input_loop = 0
    while input_loop == 0:
        nimi = input(msg)
        if nimi.replace(' ','').isalpha():
        	# nimi = nimi.camelcase()
            nimi = nimi.title()
            input_loop = 1
    return nimi

def input_taisarv(msg, lenght=0, allowedl=[]):
    '''
    msg string selgitus
    lenght int mitme kohaline arv peab olema
    allowedl list loend lubatud arvudest
    '''
    input_loop = 0
    while input_loop == 0:
        arv = input(msg)
        if arv.isdigit():
            if lenght==0 and allowedl==[]:
                input_loop = 1
            elif lenght==len(arv):
                input_loop = 1
            elif int(arv) in allowedl:
                input_loop = 1
    return int(arv)

def input_lubatudSona(msg, lubatudSonadS):
    '''
    msg string kuvatakse ekraanil
    lubatudSonad list loend lubatud sõnadest.
    '''
    lubatudSonad = []
    for lsona in lubatudSonadS:
        lubatudSonad.append(lsona.lower())
    input_loop = 0
    while input_loop == 0:
        sona = input(msg)
        sona = sona.strip().lower()
        if sona in lubatudSonad:
            input_loop = 1
    return sona

'''
https://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list
'''
print('=== Nimede lisamine loendisse ===')
print('=== Loendisse mahub 5 nime')
nimed = []
for i in range(5):
    nimed_uus = input_nimi('Sisesta nimi: ')
    nimed.append(nimed_uus)
# nimed_viimane = nimed_uus
nimed_viimane = nimed[-1]
nimed.sort()
print(nimed)
print('Viimane lisatud nimi:',nimed_viimane)




'''
https://www.tutorialspoint.com/how-to-clear-screen-in-python
https://www.codespeedy.com/clear-screen-in-python/
https://www.w3schools.com/python/python_howto_remove_duplicates.asp
'''
opilased = ['Juhan','Kati','Maarja','Mario','Mati']
opilased_tmp = opilased 
opilased_fail = 'opilased.txt'
opilased_CMD = 'ÕP> '
opilased_nimekiri_columns = 5
opilased_loop = 0
while opilased_loop == 0:
    #opilased_nimekiri = []
    opilased_nimekiri_columns_i = 0
    opilased_nimi_idxlist = []
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    print('=== Õpilaste nimekirja muutmine ===')
    print(f"Nimekiri:")
    opilased_nimi_idx = 0
    for opilased_nimi in opilased_tmp:
        opilased_nimi_idx = opilased_tmp.index(opilased_nimi, opilased_nimi_idx)
        opilased_nimi_idxlist.append(opilased_nimi_idx)
        opilased_nimi_idx += 1
    opilased_nimi_idx = 0
    for opilased_nimi in opilased_tmp:
        opilased_nimi_idx = opilased_tmp.index(opilased_nimi, opilased_nimi_idx)
        #opilased_nimekiri.append(f"{opilased_nimi_idx}){opilased_nimi}")
        opilased_nimekiri_nimi_print = f"{opilased_nimi_idx}){opilased_nimi}"
        if opilased_nimekiri_columns_i < opilased_nimekiri_columns:
            print(f"\t{opilased_nimekiri_nimi_print.ljust(14)}", end=" ")
            opilased_nimekiri_columns_i += 1
        else:
            print(f"\n\t{opilased_nimekiri_nimi_print.ljust(14)}", end=" ")
            opilased_nimekiri_columns_i = 1
        opilased_nimi_idx += 1
    print()
    print(f"Toimingud:  F)Failist  L)Lisa  M)Muuda  E)Eemalda  D)Duplikaatideta  S)Salvesta  V)Välju")
    opilased_toiming = input_lubatudSona(f"{opilased_CMD}", ['F','L','M','E','D','S','V'])
    if opilased_toiming   == 'l':
        opilased_uus = input_nimi(f"Lisamine, sisesta nimi\n{opilased_CMD}")
        opilased_tmp.append(opilased_uus)
    elif opilased_toiming == 'm':
        opilased_muuda_i = input_taisarv(f"Muutmine, sisesta õpilase number\n{opilased_CMD}", 0, opilased_nimi_idxlist)
        print(opilased_tmp[opilased_muuda_i] )
        opilased_muuda = input_nimi(f"Sisesta parandatud nimi\n{opilased_CMD}")
        opilased_tmp[opilased_muuda_i] = opilased_muuda
    elif opilased_toiming == 'e':
        opilased_kustuta_i = input_taisarv(f"Eemaldamine, sisesta õpilase number\n{opilased_CMD}", 0, opilased_nimi_idxlist)
        opilased_tmp_kustuta = opilased_tmp.pop(opilased_kustuta_i)
        #print(f"Eemaldati:", opilased_tmp_kustuta)
    elif opilased_toiming == 'd':
        opilased_tmp = list(dict.fromkeys(opilased_tmp))
    elif opilased_toiming == 'f':
        if os.path.isfile(opilased_fail):
            opilased_fail_o = open(opilased_fail, 'r')
            opilased_tmp = opilased_fail_o.read().splitlines()
            print(f"Nimekiri loeti failist", opilased_fail)
            opilased_fail_o.close()
        else:
            print(f"! Puudub nimekirja fail", opilased_fail)
            print(f"! Pärast nimekirja salvestamist saab avada failist.")
    elif opilased_toiming == 's':
        opilased = opilased_tmp
        opilased_fail_o = open(opilased_fail, 'w')
        opilased_fail_o.write("\n".join(opilased_tmp))
        print(f"Muutused kirjutati faili", opilased_fail)
        opilased_fail_o.close()
    elif opilased_toiming == 'v':
        print(f"Kas lõpetad?     Kõik salvestamata muutused hüljatakse!")
        opilased_katkesta = input_lubatudSona(f"Kinnita j/jah/e/ei\n{opilased_CMD}", ['j','jah','e','ei'])
        if opilased_katkesta[0]=='j':
            opilased_loop = 1
            break
        elif opilased_katkesta[0]=='e':
            continue