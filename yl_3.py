__author__ = 'Uku-Kaarel Jõesaar, ITT20'
# 15.01.2021
# Ülesanne 03

import base64
import re
from datetime import datetime

'''
UKU-KaaREL     JÕesaar
Uku-kaarel Jõesaar
'''
nimi = input('Sisesta Nimi: ')
nimi = nimi.strip()
nimi = nimi.replace('-',' ')
nimi = nimi.lower()
nimed = nimi.split(' ')
arv=0
while arv<=len(nimed)-1:
    if(nimed[arv] == ''):
        continue
        # sõnade vahelised ülearused tühikud
    else:
        print(nimed[arv].capitalize(),end=' ')
    arv += 1

'''
Kurisõnade eemaldaja

https://www.base64encoder.io/python/
https://www.base64decoder.io/python/
https://www.foxinfotech.in/2020/05/python-replace-string-case-insensitive-example.html

# sõnade varjamine
data = 'sõna sõna sõna'
encodedBytes = base64.b64encode(data.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(encodedStr)
'''
sisestatud_tekst = input('Palun sisesta tekst: ')
kurisoand_base64encoded = 'a3VyYXQga3VyYWRpIGt1cmFkaXQgcHV0cyBwdXRzaSB0w7xyYSB2aXR0IHZpdHR1IG11bm4gbXVubmk='
kurisoand_decodedBytes = base64.b64decode(kurisoand_base64encoded)
kurisoand_decodedStr = str(kurisoand_decodedBytes, "utf-8")
kurisonad = kurisoand_decodedStr.split(' ')
arv=0
while arv<=len(kurisonad)-1:
    kurisona_pikkus = len(kurisonad[arv])
    sisestatud_tekst = re.sub(kurisonad[arv], kurisona_pikkus*'*', sisestatud_tekst, flags=re.IGNORECASE)
    arv += 1
print(sisestatud_tekst)

'''

'''
email = input('Sisesta e-posti aadress: ')
print('@' in email)

'''

https://www.tutorialsmade.com/calculate-hours-minutes-two-times-python/
https://www.programiz.com/python-programming/methods/string/format
'''
tunnid_algavad_loop = 1
while tunnid_algavad_loop == 1:
    tunnid_algavad  = input('Sisesta tundide algus kujul hh:mm : ')
    if ':' in tunnid_algavad:
        tunnid_algavad_loop = 0
        
tunnid_loppevad_loop = 1
while tunnid_loppevad_loop == 1:
    tunnid_loppevad = input('tundide lõpp: ')
    if ':' in tunnid_loppevad:
        tunnid_loppevad_loop = 0
date_format = "%H:%M"
tunnid_a  = datetime.strptime(tunnid_algavad, date_format)
tunnid_l  = datetime.strptime(tunnid_loppevad, date_format)
#tunnid_a = tunnid_algavad.split(':')
#tunnid_l = tunnid_loppevad.split(':')
#tunnid_aa = datetime(0, 0, 0, tunnid_a[0], tunnid_a[1])
#tunnid_ll = datetime(0, 0, 0, tunnid_l[0], tunnid_l[1])

diff = tunnid_l - tunnid_a
#diff sekundites
hours = int((diff.seconds) / 3600)
minutes = int(((diff.seconds)/60) -(hours*60))

print("Tunnid algavad kl {} ja lõpevad kl {}, see teeb päeva pikkuseks {} tundi ja {} minutit.".format(tunnid_algavad, tunnid_loppevad, hours, minutes))
#print ("Tunnid algavad kl %s ja lõpevad kl %s, see teeb päeva pikkuseks %s tundi ja %s minutit." %(tunnid_algavad, tunnid_loppevad, hours, minutes))



'''
https://et.wikipedia.org/wiki/Palindroom
TENET
UKU
'''
palindroom = input('Kas on palindroom? Sisesta kontrolliks tekst: ')
palindroom_L = len(palindroom)-1
arv=0
pal=0
while arv<=palindroom_L:
    print(palindroom[arv] , palindroom[palindroom_L-arv])
    if palindroom[arv] != palindroom[palindroom_L-arv]:     
        pal += 1
        break
    arv += 1
if pal > 0:
    print('Ei ole')
else:
    print('Jah, on.')
