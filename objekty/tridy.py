
class Zviratko:
    def __init__(self, nejake_jmeno):  # kdyz se vola novy kralicek, tak bude mit vzdycky jmeno
        # vola se pokazde, kdyz se vytvari novy objekt
        self.jmeno = nejake_jmeno
    def snez(self, jidlo):
        print("{}: Mnam, moc mi chutna {}".format(self.jmeno, jidlo))
    vaha=5

class Kralicek(Zviratko): #vsechny tridy, ze kterych chceme dedit vlastnosti jsou v zavorce oddeleny carkama

    def zanufej(self):
        print("Nuf, ja jsem {}".format(self.jmeno))  # umozni nam zavolat hodnoty, o kterych jeste nevime, jake budou

    def prejmenuj(self, nove_jmeno):
        self.jmeno = nove_jmeno
        print("Ted se jmenuji {}".format(self.jmeno))

    def snez(self, jidlo):
        print("Musim to nejdriv roztahat po zemi.")
        super().snez(jidlo) #zavola tridu z predka, takze se provede

class Stenatko(Zviratko):
    vaha=10
    def zastekej(self):
        print("Haf, ja jsem {}".format(self.jmeno))

