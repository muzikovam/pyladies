from random import randrange
def vyhodnot(string):
    iks="xxx" in string
    ocko="ooo" in string
    pomlcka="-" in string
    if iks == True:
        return "x"
    elif ocko == True:
        return "o"
    elif pomlcka == False:
        return "!"
    else:
        return "-"

def tah(a, b, c):
    retezec=a[:b]+c+a[b+1:]
    return retezec

def tah_hrace(field):
    while True:
        cislo_policka = int(input("Zadej na jaky pole chces hrat: ")) -1
        if cislo_policka>=1 and cislo_policka<=20:
            break
        else:
            print("Nespravny vstup")

    pole=tah(field, cislo_policka, "x")
    return pole

def tah_pocitace(field):
    while True:
        cislo_policka=randrange(1, 21)
        if field[cislo_policka-1]=="-":
            break
    pole=tah(field, cislo_policka, "o")
    return pole

def piskvorky1d():
    pole="--------------------"
    while vyhodnot(pole)=="-":
        pole=tah_hrace(pole)
        print(pole)
        print("stav po tahu hrace:", vyhodnot(pole))
        if vyhodnot(pole)!="-":
            break
        pole=tah_pocitace(pole)
        print(pole)
        print("stav po tahu pocitace:", vyhodnot(pole))
    return vyhodnot(pole)

print("Vyhrava: ", piskvorky1d())
