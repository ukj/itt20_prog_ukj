__author__='Uku-Kaarel Jõesaar, ITT20'
# 19.01.2021
# Ülesanne 08'

class Auto:
    automark=''
    aasta=0
    hind=0.0
    varv=''
    kiirusm=0.0

    def __init__(self, mark, aasta=0, hind=0, varv=''):
        self.lisaMark(mark)
        self.lisaAasta(aasta)
        self.lisaHind(hind)
        self.lisaVarv(varv)
    
    def lisaMark(self, mark):
        self.automark = mark
    
    def lisaAasta(self, aasta):
        self.aasta = aasta
    
    def lisaHind(self, hind):
        self.hind = hind
    
    def lisaVarv(self, varv):
        self.varv = varv
    
    def lisaKiirusMax(self, kiirus):
        self.kiirusm = kiirus
    
    def kuva(self):
        print('Mark: {} \nAasta: {}\nHind: {}\nVärv: {}\nMax kiirus: {}'.format(self.automark, self.aasta, self.hind, self.varv, self.kiirusm))


uusAuto = Auto('Tesla Model 3', 2019, 35400)
uusAuto.lisaVarv('punane')
uusAuto.lisaKiirusMax(209)
uusAuto.kuva()

uusAuto = Auto('Volvo S90 Momentum T6', varv='valge')
uusAuto.lisaAasta(2020)
uusAuto.lisaHind(51545)
#uusAuto.lisaVarv('valge')
uusAuto.lisaKiirusMax(180)
uusAuto.kuva()