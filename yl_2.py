__author__ = 'Uku-Kaarel Jõesaar, ITT20'
# 15.01.2021
# Ülesanne 02

# import math

'''
Kõik vastused täislausega ja vajadusel ümardatud
Arvutame kolmnurga ümbermõõdu
Loo kolm täisarvulist muutujat a, b, c
Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
'''
k1_a = input('Sisesta kolmnurga külg a: ')
k1_b = input('külg b: ')
k1_c = input('külg c: ')
k1_a = int(k1_a);
k1_b = int(k1_b);
k1_c = int(k1_c);
k1_P = k1_a+k1_b+k1_c;
print('Kolmnurga ümbermõõt: ', k1_P)

'''
Toote hind 36,75€
Soodushind hetkel 40%
Soovin kolme toote summat
'''
toote_hind = float(35.75)
soodus_pr  = 40
kogus      = float(3)
summa      = round(toote_hind * float(soodus_pr/100) * kogus, 2)
print(f"Toote hind on {toote_hind}€ TÄNA AINULT {soodus_pr}% ja ostes {kogus}, tuleb maksta kõigest {summa}€!")

'''
Võtsite 3 sõbraga suure pitsa hinnaga 12,90€
Jätate teenindajale 10% jootraha
Koosta programm, mis leiab kui palju peab igaüks maksma
'''
suure_pitsa_hind = float(12.90)
jootraha_pr      = 10
jootraha         = suure_pitsa_hind*float(jootraha_pr/100)
soprade_arv      = 3
igauhel_maksta   = (jootraha+suure_pitsa_hind)/float(soprade_arv)
print(f"Igaühel tuleb maksta {igauhel_maksta}€, kui {soprade_arv} sõpra ostavad {suure_pitsa_hind}€ maksva pita ja annvad {jootraha_pr}% jootraha")

'''
Rulluisutajad
Rulluisutaja keskmine kiirus on 29,9km/h
Kui kaugele jõuab 24minutiga
'''
kiirus_kmh  = 29.9
kiirus_kmmin= kiirus_kmh/60
aega_min    = float(24)
vahemaa     = round(aega_min*kiirus_kmmin, 2)
print(aega_min,'minutiga läbib rulluisutaja',vahemaa,'km, kui tema keskmine kiirus on ',kiirus_kmh)
      
'''
Leia kolmnurga hüpotenuus
Kolmnurga külgede pikkused on a=16 ja b=9
Kasuta Pythagorase teoreemi (a2 + b2 = c2) ja leia kolmnurga hüpotenuus
'''
kl2_a  = float(16)
kl2_b  = float(9)
#kl2_c2 = (kl2_a*kl2_a) + (kl2_b*kl2_b)
kl2_c2 = pow(kl2_a, 2) + (kl2_b ** 2)
print('Kui kolmnurga külgede pikkused on a=16 ja b=9, siis hüpotenuusi pikkus on',kl2_c2)

'''
Ajateisendus
Kasutaja sisestab aja minutites
Sinu valem leiab ja väljastab tunnid ja minutid
Näiteks: sisestus 72, vastus 1:12
'''
aeg_min = float(input('Sisesta aeg minutites: '))
tunde_i   = int(aeg_min / 60)
min_jaak  = int(aeg_min - (tunde_i * 60))
print(f"Tunnid ja minutid: {tunde_i}:{min_jaak}")

'''
Arvusüsteemid
Kasutaja sisestab täisarvu kümnendsüsteemis
Sinu programm teisendab selle 2nd ja 16nd süsteemi
'''
arv10 = int(input('Sisesta kümnendarv: '))
arv2  = bin(arv10)
arv16 = hex(arv10)
print(f"Arv {arv10} 16nd kujul on {arv16} ja 2nd kujul on {arv2}")

'''
Kütusekulu arvutamine
Kasutaja sisestab tangitud kütuse liitrid
Kasutaja sisestab läbitud kilomeetrid
Programm leiab kütusekulu 100km kohta keskmiselt
'''
tangiti_ltr = float(input('Sisesta mitu liitreit tankisid: '))
labiti_km = float(input('mitu kilomeetrid läbisid: '))
kutuse_kulu100km = round((tangiti_ltr/labiti_km)*100, 1)
print('Kütusekulu 100km kohta:',kutuse_kulu100km)
