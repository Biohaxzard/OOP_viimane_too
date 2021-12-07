class Karakter:
    def __init__(self, nimi, elud=100, tugevus=10):
        self.nimi = nimi
        self.elud = elud
        self.tegevus = tugevus
    def kaotaelusi(self, elud):
        self.elud = (elud -10)
    def lisaelusi(self, elud):
        self.elud = (elud+10)
class Vaenlane:
    def __init__(self, elud=100, tugevus=10):
        self.elud = elud
        self.tegevus = tugevus
    def kaotaelusi1(self, elud):
        self.elud = elud
        
        
