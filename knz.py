from random import randrange

cislo=randrange(3)
while True:
    if cislo==0:
        pocitac="kamen"
    elif cislo==1:
        pocitac="nuzky"
    else:
        pocitac="papir"
    human=input("kamen, nuzky, nebo papir? ")
    if human=="kamen":
        if pocitac=="kamen":
            print("Remiza.")
        elif pocitac=="nuzky":
            print("Vyhra.")
        elif pocitac=="papir":
            print("Prohra.")
    elif human=="nuzky":
        if pocitac=="kamen":
            print("Prohra.")
        elif pocitac=="nuzky":
            print("Remiza.")
        elif pocitac=="papir":
            print("Vyhra.")
    elif human=="papir":
        if pocitac=="kamen":
            print("Vyhra.")
        elif pocitac=="nuzky":
            print("Prohra.")
        elif pocitac=="papir":
            print("Remiza.")
    elif human=="konec":
        break
    else:
        print("Asi mas neco blbe. Ja ne.")
