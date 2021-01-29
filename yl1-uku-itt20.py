'''
Kodutöö 1
2021-01-17
'''
__author__ = 'Uku-Kaarel Jõesaar'

print ('Tere, maailm!')
print ('')

aasta        = 2020
liblikas     = 'teelehe-mosaiikliblikas'
liblikas_url = 'https://et.m.wikipedia.org/wiki/Teelehe-mosaiikliblikas'
lause_keskosa= '. aasta liblikas on '
lause        = f"{aasta}{lause_keskosa}{liblikas}."
print (lause)
print ('')

def input_taisarv(msg):
    input_loop = 0
    while input_loop == 0:
        arv = input(msg)
        if arv.isdigit():
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
    
alus      = input_taisarv('Sisestage astme alus(täisarv):')
astendaja = input_taisarv('Sisestage astendaja(täisarv):')
astendus  = pow(alus, astendaja)
print (f"{alus}^{astendaja}={astendus}")
print ('')

htrahv_piir    = 190
htrahv_kordaja = 3
nimi           = input_nimi('Sisestage nimi:')
kiirus_lubatud = input_taisarv('Sisestage lubatud kiirus (km/h):')
kiirus_tegelik = input_taisarv('Sisestage tegelik kiirus (km/h):')
kiirus_erinevus= kiirus_tegelik-kiirus_lubatud
if kiirus_erinevus <= 0:
    print(f"{nimi}, Te ei ületanud kiirust ja teid ei trahvita.")
else:
    htrahv = kiirus_erinevus * htrahv_kordaja
    htrahv = min(htrahv, htrahv_piir)
#    if htrahv > htrahv_piir:
#        htrahv = htrahv_piir
    print(f"{nimi}, kiiruse ületamise eest on teie trahv {htrahv} eurot.")