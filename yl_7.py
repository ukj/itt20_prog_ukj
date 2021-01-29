__author__='Uku-Kaarel Jõesaar, ITT20'
# 23.01.2021
# Ülesanne 07'
import os, math
#import re

def tervita(nimi, keel='de'):
    '''
    https://jaxenter.com/implement-switch-case-statement-python-138315.html
    '''
    nimi = nimi.title()
    tervitused={
        'et':f"Tere {nimi}!",
        'en':f"Hello {nimi}!",
        'fr':f"Bonjour {nimi}!",
        'sp':f"Hola {nimi}!",
        'it':f"Salve {nimi}!",
        'de':f"Guten Tag {nimi}!"
        }
    print(tervitused[keel])

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

def isfloat(value):
    '''
    https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python
    '''
    try:
        float(value)
        return True
    except ValueError:
        return False
        #import re
    #if re.match(r'^-?\d+(?:\.\d+)$', element) is None:
    #   return False
    #else:
    #   return True
    
def input_ujukomaarv(msg):
    '''
    msg string selgitus
    https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python
    '''
    input_loop = 0
    while input_loop == 0:
        arv = input(msg)
        try:
            float(arv)
            input_loop = 1
        except ValueError:
            continue
        #if arv.isfloat():
        #    input_loop = 1
    return float(arv)

def clearScreen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def ruumala():
    '''
    https://www.pythoncentral.io/python-dictionary-operations-and-methods/
    '''
    clearScreen()
    print('********** LEIAME RUUMALA **********')
    kujundid = {1:'Kuup', 2:'Kera', 3:'Koonus',4:'Silinder'}
    #kujundid.keys()
    ruumala_loop = 0
    while ruumala_loop == 0:
        print('Ruumalade arvutamine',kujundid, "\n{0: 'Välju programmist'}")
        kujund = input_taisarv(f"Vali tegevus: ", 0, [0,1,2,3,4])
        
        if kujund==0:
            ruumala_loop = 1
            break

        print(kujundid[kujund])

        if kujund==1:
            a = input_ujukomaarv(f"Külje pikkus: ")
            V = a*a*a
        elif kujund==2:
            r = input_ujukomaarv(f"Raadius: ")
            V = (4/3)*math.pi*r*r*r
        elif kujund==3:
            r = input_ujukomaarv(f"Raadius: ")
            h = input_ujukomaarv(f"Kõrgus: ")
            V = (1/3)*math.pi*r*r*h
        elif kujund==4:
            r = input_ujukomaarv(f"Raadius: ")
            h = input_ujukomaarv(f"Kõrgus: ")
            V = math.pi*r*r*h
        
        if kujund>0:
            print ('Ruumala:',V)





keeled = ['et','en','fr','sp','it','de']
tervita('mario')
for keel in keeled:
    tervita('mario', keel)


ruumala()