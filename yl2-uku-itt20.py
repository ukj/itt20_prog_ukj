'''
Kodutöö 1
2021-01-29
'''
__author__ = 'Uku-Kaarel Jõesaar'

import os, sys, time, math, functools, random

if os.name == 'nt':
    import winsound





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
Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. Eeldame, et reisijaid
on vähemalt üks. Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi
kohtade arvu (just sellises järjekorras) ning väljastab ekraanile, mitu bussi on vaja ja mitu
inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).

// täisarvuline jagamine, 36 // 10 → 3
% jäägi leidmine 36 % 10 → 6

https://www.journaldev.com/37089/how-to-compare-two-lists-in-python
https://www.golinuxcloud.com/python-if-else-one-line/
'''
def bussid(inimeste_arv=-1, bussis_kohti=-1,printout=True):
    print("""
###===              Kui palju busse on vaja                ===###
    """)
    if(inimeste_arv == -1):
        inimeste_arv = input_taisarv('Inimeste arv:')
    elif printout==True:
        print('Inimeste arv:', inimeste_arv)
    if(bussis_kohti == -1):
        bussis_kohti = input_taisarv('Kohti bussis:')
    elif printout==True:
        print('Kohti bussis:', bussis_kohti)

    busse_vaja = int(math.ceil(inimeste_arv / bussis_kohti))
    #tjup = inimeste_arv // bussis_kohti + (inimeste_arv % bussis_kohti > 0)
    #tj = inimeste_arv // bussis_kohti
    
    viimases_busssis = inimeste_arv % bussis_kohti
    if viimases_busssis==0:
        viimases_busssis=bussis_kohti

    if printout==True:
        print('---------------------')
        print('     Busse vaja:', busse_vaja)
        print('Viimases bussis:',viimases_busssis)
        print()
    return [inimeste_arv, bussis_kohti, busse_vaja, viimases_busssis]
'''
printout=True
#Busse 2, Viimases 20
t=bussid(inimeste_arv=60, bussis_kohti=40 ,printout=printout)
print(end='') if t[2]==2 and t[3]==20 else print('viga',t)
#Busse 2, Viimases 40
t=bussid(inimeste_arv=80, bussis_kohti=40 ,printout=printout)
print(end='') if t[2]==2 and t[3]==40 else print('viga',t)
#Busse 1, Viimases 20
t=bussid(inimeste_arv=20, bussis_kohti=40 ,printout=printout)
print(end='') if t[2]==1 and t[3]==20 else print('viga',t)
#Busse 1, Viimases 40
t=bussid(inimeste_arv=40, bussis_kohti=40 ,printout=printout)
print(end='') if t[2]==1 and t[3]==40 else print('viga',t)
#Busse 1, Viimases 10
t=bussid(inimeste_arv=10, bussis_kohti=22 ,printout=printout) 
print(end='') if t[2]==1 and t[3]==10 else print('viga',t)
#Busse 3, Viimases 3
t=bussid(inimeste_arv=103, bussis_kohti=50 ,printout=printout)
print(end='') if t[2]==3 and t[3]==3 else print('viga',t)
#Busse 3, Viimases 23
t=bussid(inimeste_arv=103, bussis_kohti=40 ,printout=printout)
print(end='') if t[2]==3 and t[3]==23 else print('viga',t)
'''
#bussid()






'''
Manivaldil on hommikuti raske tõusta ja tal on äratuskell, mis äratab teda teatud arv kordi koos
tervitustekstiga. Koostada programm, mis

küsib kasutajalt, mitu korda äratus heliseb ning
väljastab sama arv kordi ekraanile Tõuse ja sära!.
'''

def manivaldi_hommik(aratuste_arv=-1):
    if(aratuste_arv == -1):
        aratuste_arv = input_taisarv("""
    ###===                Manivaldi Äratuskell           ===####
Mitu korda Manivaldi äratada? """)
    aratamine_loop = 0
    while aratamine_loop < aratuste_arv:
        print('Tõuse ja sära!')

        if os.name == 'nt':
            winsound.Beep(2500, 300) #Hz, ms
        else:
            sys.stdout.write('\a')
            sys.stdout.flush()
        time.sleep(1)
        aratamine_loop += 1

#manivaldi_hommik(3)
#manivaldi_hommik()




'''
Jänesevanemad on mures, et lapsed ei liigu piisavalt. Laste motiveerimiseks mõtlesid nad välja
süsteemi, kus 2. metsaringi läbimisel saab jänesepoeg 2 porgandit, 4. metsaringi läbimisel 4
porgandit juurde, 6. metsaringi läbimisel 6 porgandit juurde jne. Paarituarvulistel ringidel
porgandeid juurde ei saa.

küsib kasutajalt ringide arvu (mittenegatiivne täisarv);
arvutab while-tsükli abil saadavate porgandite koguarvu;
väljastab saadavate porgandite koguarvu ekraanile.

Näiteks, kui kasutaja sisestas 6, siis summa on 12, sest 2 + 4 + 6 = 12. Kui kasutaja sisestas 7,
siis on summa samuti 12, sest 2 + 4 + 6 = 12.
'''
def janeste_systeem(ringide_arv=-1):
    print("""
    ###===              Jänkude porgandijagaja             ===###

""")
    if(ringide_arv == -1):
        ringide_arv = input_taisarv("Mitu ringi jänkupoeg tegi:  ")

    saab_porgandit = 0
    paaris_ringid  = 0
    while paaris_ringid <= ringide_arv:
        if (paaris_ringid % 2)==0:
            saab_porgandit += paaris_ringid
        # saab_porgandit += paaris_ringid if (paaris_ringid % 2)==0 else saab_porgandit
        paaris_ringid +=2
    print("Jänkupoeg tegi",ringide_arv,"ja saab", saab_porgandit,"porgandit.")
'''
janeste_systeem(1) #0
janeste_systeem(3) #2
janeste_systeem(5) #6  2+4
janeste_systeem(6) #12 2+4+6
janeste_systeem(7) #12 2+4+6
janeste_systeem(8) #20 2+4+6+8
janeste_systeem(9) #20 2+4+6+8
janeste_systeem(12) #42 2+4+6+8+10+12
'''
#janeste_systeem()






'''
Erinevate täringumängude jaoks on vajalik erinev arv täringuid. Näiteks Yahtzee (Yatzy) jaoks on
vaja 5 täringut, Crapsi jaoks aga 2 täringut. Koostada programm, mis

küsib kasutajalt vajalike täringute arvu;

viskab vastava arvu täringuid (genereerib vastava arvu suvalisi arve, mis jäävad 1 ja 6
vahele);

väljastab iga arvu eraldi reale.

Vihje: Kui kasutada tsüklit, mis teeb kasutaja sisestatud arvu samme, siis igal sammul tuleb
genereerida üks juhuslik arv ja see väljastada.
Näited programmi tööst:
'''

def taringud():
    input_loop = 0
    msg="""
    
    ###===                       TÄRINGUMASIN              ===###
            Jätkamiseks sisestage täringute arv, 
            katkestamiseks Q või mingi teine täht.
    Mitu täringut visata? """
    
    while input_loop == 0:
        arv = input(msg)
        if arv.isdigit():
            for t in range(1,int(arv)+1):
                t_vise = random.randint(1,6)
                print("    Täring {0}:  {1}".format(t,t_vise))
        else:
            input_loop = 1


#taringud()

'''
Lumivalgekesel oli 14 õuna ja ta tahtis neid pöialpoistega jagada. Ta sai aru, et kui kõik seitse
pöialpoissi tahavad õunu ja ta annaks kõigile kaks õuna, jääks ta ise üldse ilma. Nüüd otsustas ta
õunu jagada nii, et küsib, mitu pöialpoissi tahab õunu, ja seejärel loosib iga soovija korral, kas
anda talle üks või kaks õuna. Koostada programm, mis

küsib kasutajalt, mitu pöialpoissi tahab õunu (võib eeldada, et sisestatakse täisarv lõigust
[0; 7]);

leiab ja väljastab eraldi ridadele, mitu õuna saab iga pöialpoiss (programm genereerib iga
kord juhuslikult arvu 1 või 2);

leiab ja väljastab eraldi reale, mitu õuna jääb Lumivalgekesele.
'''

def poialpoiste_ounad():
    input_loop = 0
    poialpoiste_arv = 7
    msg="""
    
    ###===                                  ÕUNTE JAGAMINE                         ===###
            Jätkamiseks sisestage õunu soovivate pöialpoiste arv(0-7), 
            katkestamiseks Q või mingi teine täht.
    Mitu neist õuna tahavad? """
    while input_loop == 0:
        Lv_ounad = 14
        Pp_ounad = []
        #arv = input_taisarv(msg, 1, [0,1,2,3,4,5,6,7])
        arv = input(msg)
        if arv.isdigit():
            arv = int(arv)
            if arv < 0:
                continue
            elif arv > poialpoiste_arv:
                continue
            for pp in range(1,int(arv)+1):
                t_vise = random.randint(1,2)
                Pp_ounad.append(t_vise)
                print("    Õuna sooviv pöialpoiss {0} saab {1} õuna.".format(pp,t_vise))
                t_vise = 0
        else:
            input_loop = 1
            return 0
        Lv_ounad = Lv_ounad-sum(Pp_ounad)
        print("    Lumivalgekesele jääb {0} õuna".format(Lv_ounad))
        




'''
https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
'''
yl_def_list =  ['bussid', 'manivaldi_hommik', 'janeste_systeem', 'taringud', 'poialpoiste_ounad']

print('\n\nÜlesanded', yl_def_list, '\n')
for yl_def in yl_def_list:
    locals()[yl_def]()
    yl_kasJatkata = input('Jätkamiseks vajuta Enter, Katkestamiseks Q ja Enter \n')
    if yl_kasJatkata=='':
        continue
    else:
        if yl_kasJatkata == 'Q' or  yl_kasJatkata == 'q':
            print("\n\n\nProgramm lõpetab\n\n\n")
            break
        else:
            print("\n\n\nViga #None\nSisestasite tundmatu sümboli, programm jooksis kokku!\n\n\n")
        break
