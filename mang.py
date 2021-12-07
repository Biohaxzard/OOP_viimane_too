import random
while True:
    class Karakter:
        def __init__(self, nimi, elud, tugevus):
            self.nimi = nimi
            self.elud = elud
            self.tugevus = tugevus
        def kaotaelusi(self):
            self.kaotaelusi = random.randint(0,20) 
            self.elud -= self.kaotaelusi * self.tugevus
            if self.elud < 0:
                print("sa kaotasid kõik oma elud ggwp")
            else:
                print("kaotasid veic elusi")
        def lisaelusi(self):
            if self.elud < 0:
                print("oled juba dead")
            else:
                self.lisaelusi = 20
                self.lisaelusi = self.elud
                self.elud += self.lisaelusi
    class Vaenlane:
        def __init__(self, elud, tugevus):
            self.elud = elud
            self.tugevus = tugevus
        def kaotaelusi(self):
            self.kaotaelusi = random.randint(0,20) 
            self.elud -= self.kaotaelusi * self.tugevus
            if self.elud < 0:
                print("vaenlane kaotas kõik oma crypto varanduse ")
            else:
                print("vaenlane sai põske veic")
    break
karakter = Karakter("peeter", 100, 10)
vaenlane = Vaenlane(100, 10)
karakter.kaotaelusi()
karakter.lisaelusi()
vaenlane.kaotaelusi()
print(karakter.elud, vaenlane.elud)