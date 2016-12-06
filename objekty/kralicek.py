from tridy import Kralicek, Stenatko

kralicek1=Kralicek("Karel Marx")


kralicek1.zanufej()
kralicek1.snez("seno")
kralicek1.prejmenuj("pani Karla Marxova")
stenatko1=Stenatko("Amalka")
stenatko1.zastekej()
stenatko1.snez("parek")
print(stenatko1.vaha)
stenatko1.vaha=30
print(stenatko1.vaha)
print(kralicek1.vaha)

#polymorfismus
zviratka=[Kralicek("Chlupacek"), Kralicek("Usacek"),Stenatko("Kukatko")]

for z in zviratka:
    z.snez("granulka")

print("\n")

def nakrm_zver(seznam_zvere):
    for z in zviratka:
        z.snez("granulka")

nakrm_zver(zviratka)