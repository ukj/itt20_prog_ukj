__author__ = 'Uku-Kaarel Jõesaar, ITT20'
# 15.01.2021
# Ülesanne 04
import datetime
# from calendar import isleap
import random

def input_taisarv(msg, lenght=0):
    input_loop = 0
    while input_loop == 0:
        arv = input(msg)
        if lenght == 0 and arv.isdigit():
            input_loop = 1
        elif len(arv)==lenght and arv.isdigit():
            input_loop = 1
    return int(arv)

def input_nimi(msg):
    input_loop = 0
    while input_loop == 0:
        nimi = input(msg)
        if nimi.replace(' ','').isalpha():
        	# nimi = nimi.camelcase()
            nimi = nimi.title()
            input_loop = 1
    return nimi

def input_lubatudSona(msg, lubatudSonadS):
    '''
    msg kuvatakse ekraanil
    lubatudSonad on loend lubatud sõnadest.
    '''
    lubatudSonad = []
    for lsona in lubatudSonadS:
        lubatudSonad.append(lsona.lower())
    print ( lubatudSonad )
    input_loop = 0
    while input_loop == 0:
        sona = input(msg)
        sona = sona.strip().lower()
        if sona in lubatudSonad:
            input_loop = 1
    return sona





'''
Ruudu küljed
'''
ruudu_kyljed = []
for i in range(4):
    ruudu_kylg_loop = 0
    while ruudu_kylg_loop == 0:
        ruudu_kylg  = input(f'Sisesta ruudu {i}. külje pikkus: ')
        if ruudu_kylg.replace('.', '', 1).isdigit():
            ruudu_kylg = float(ruudu_kylg)
            ruudu_kyljed.append(float(ruudu_kylg))
            ruudu_kylg_loop = 1


if (ruudu_kyljed[0] == ruudu_kyljed[1] == ruudu_kyljed[2] == ruudu_kyljed[3]):
    print('Vastus: kõik küljed on sama pikkusega, saab tegu olla ruuduga.')
else:
    print('Kõik küljed pole sama pikkusega, see pole ruut.')
print (ruudu_kyljed)



'''

Mis tehe
'''
arvud = []
for i in range(2):
    arvu_sisestamine_loop = 0
    while arvu_sisestamine_loop == 0:
        arv  = input(f'Sisesta {i}. arv: ')
        if arv.replace('.', '', 1).isdigit():
            arv = float(arv)
            arvud.append(float(arv))
            arvu_sisestamine_loop = 1

tehted = ['+','-','*','/','%','==','>','<','<=','>=']
tehted_msg = 'Mis tehe '+' '.join(tehted)+ ' ?'
tehte_sisestamine_loop = 0
while tehte_sisestamine_loop == 0:
    tehe = input(tehted_msg)
    if tehe in tehted:
        tehte_sisestamine_loop = 1

tehe_tehe= f"{arvud[0]} {tehe} {arvud[1]}"
print(tehe_tehe," = ", eval(tehe_tehe) )





'''
Kas on juubel

https://stackoverflow.com/questions/4436957/pythonic-difference-between-two-dates-in-years
'''
sunnipaev_loop = 0
while sunnipaev_loop == 0:
    sunnipaev  = input('Sisesta oma sünnikuupäev kujul pp.kk.aaaa : ')
    sunnipaev.replace('.', '').isdigit()
    sunnipaev_loop = 1

date_format = "%d.%m.%Y"
synnipaev_d  = datetime.datetime.strptime(sunnipaev, date_format)
tana_d  = datetime.datetime.now()
diff_years = tana_d.year - synnipaev_d.year
if diff_years%10==0 :
    print('On juubel')
else:
    print('Ei ole juubel')
# diff.years
# 31557600sek

'''
Kui palju soodukat

https://www.geeksforgeeks.org/python-check-for-float-string/
'''
tootehinna_sisestamine_loop = 0
while tootehinna_sisestamine_loop == 0:
    hind = input('Toote hind eurodes: ')
    if hind.replace('.', '', 1).isdigit():
        hind = float(hind)
        tootehinna_sisestamine_loop = 1

soodukas = 0
if hind > 0 and hind <= 10:
    soodukas = '10%'
    hind_L   = hind-(0.1*hind)
elif hind > 10:
    soodukas = '20%'
    hind_L   = hind-(0.2*hind)
print(f'Saad {soodukas} soodukat, hinnaks kujuneb {hind_L}')



'''
https://www.w3schools.com/python/python_datetime.asp
https://www.pythoncoders.org/2020/09/convert-a-list-of-strings-to-upper-case-or-lower-case-using-python/
'''
nyyd = datetime.datetime.now()
sugu = input_lubatudSona('Sisestage sugu (m/mees/n/naine):', ['m','mees','n','naine'])
if sugu[0]=='m':
    vanus = input_taisarv('Sisestage kandideerija vanus:')
    xkond = 'meeskonda'
else:
    vanus = input_taisarv('Sisestage kandideerija sünniaasta:', 4)
    vanus = nyyd.year - vanus
    xkond = 'naiskonda'
if vanus in [16,17,18] :
    sobiv = 'olete'
else:
    sobiv = 'ei ole'
print(f"Te {sobiv} sobiv meie {xkond}.")





# ruut
for iy in range(5):
    for ix in range(5):
        print('* ', end=" ")
    print()
print()
for iy in range(5):
    for ix in range(0,iy+1):
        print('*', end=" ")
    print()
print()
for iy in [5,4,3,2,1]:
    for ix in range(iy):
        print('*', end=" ")
    print()
print()





'''
https://www.w3schools.com/python/ref_random_randint.asp
'''
for i in range(5):
    print( random.randint(0,9), end='' )
print("\n\n")





'''
https://www.programiz.com/python-programming/examples/odd-even
'''
#theend=', '
soned = []
for i in range(1,101):
    #if i==100:
    #    theend = ''
    if (i % 2) == 0:
        soned.append("{0} paaris".format(i))
        # print("{0} paaris".format(i), end=theend)
    else:
        soned.append("{0} paaritu".format(i))
        # print("{0} paaritu".format(i), end=theend)
print(', '.join(soned))
print("")



'''
12345
'''
for ik in [1,2,3,4,5,6,7,8,9,10]:
    print("5 x {0} = {1}".format(ik, 5*ik))
print()



'''
/5
'''
soned = []
for i in range(1,101):
    if (i % 5) == 0:
        soned.append(f"{i}")
print(', '.join(soned))
print("")






print('=== Arvamismäng ===')
arvamised_loop = 0
while arvamised_loop == 0:
    arva = random.randint(1,5)
    for i in range(3):
        arvati  = input_taisarv('=== Number vahemikus 1-5: ', 0)
        if arvati == arva:
            print(f'Õige!')
            break
        else:
            print(f'See pole see!')
    kasveel = input_lubatudSona('Kas soovid veel arvata (j/jah/e/ei):', ['j','jah','e','ei'])
    if kasveel[0]=='j':
        continue
    else:
        arvamised_loop = 1
        continue




print("=== Raha kasvatamine ===\n Intress on 5%")
summa  = input_taisarv('=== Kui palju panka pannakse: ', 0)
summaa = summa
intress_pr = 5
aastad  = input_taisarv('=== Kui kauaks(min 1): ', 0)
if aastad<1:
    aastad = 1
else:
    aastad += 1
print('Aasta  |  Algsumma  | Interss | Aasta lõpuks') # rea pikkus 44
for i in range(1,aastad):
    intress   = (summaa/100)*intress_pr
    summal    = summaa+intress
    i_s       = f"{i}"
    summaa_s  = f"{summaa:.2f}"
    summaa    = summal
    summal_s  = f"{summal:.2f}"
    intress_s = f"{intress:.2f}"
    print(f"{i_s.ljust(7)}|{summaa_s.rjust(12)}|{intress_s.center(9)}|{summal_s.rjust(13)}")
summa_kokku = f"Summa kokku: {summal_s.rjust(13)}"
summa_kasum = f"      Kasum: {summal_s.rjust(13)}"
print(f"{summa_kokku.rjust(44)}")
print(f"{summa_kasum.rjust(44)}")
print()



# https://www.programiz.com/python-programming/methods/string/format
print('Arv  |  Ruut  | Kuup') # rea pikkus 20
for i in range(1,11):
    print("{:<5d}|{:^8d}|{:>5d}".format(i, i*i, i*i*i))