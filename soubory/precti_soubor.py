with open("soubor.txt") as soubor:
    obsah=soubor.read()
    print(obsah)

with open("soubor.txt") as soubor:
    for radek in soubor.readlines():
        if len(radek)>25:
            print(radek.upper())
        else:
            print(radek)

#zapis
with open("zapis.txt", "w") as soubor:
    soubor.write("Tohle je nas zapis do souboru\n")
    soubor.write("A tohle je zas dalsi")
