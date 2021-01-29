__author__='Uku-Kaarel Jõesaar, ITT20'
# 23.01.2021
# Ülesanne 09'
from datetime import datetime
from datetime import timedelta
import locale
kuup = datetime.now()


#16. June 2016
locale.setlocale(locale.LC_TIME, "en")
print(kuup.strftime("%d. %B %Y"))
locale.setlocale(locale.LC_TIME, "et_EE.UTF-8")
print(kuup.strftime("%d. %B %Y"))
print()

isikukood='38301254710'
#          01234567890
isikukood_dtObj = datetime.strptime(isikukood[1:7], '%y%m%d').date()
vanus = kuup.year - isikukood_dtObj.year
print('Isikukood:',isikukood,'Sünnikuupäev:', isikukood_dtObj.strftime("%d. %B %Y"), 'Vanus:', vanus)