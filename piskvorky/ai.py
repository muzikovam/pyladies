from random import randint, choice


def tah_pocitace(pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače."""

    pozice = -1
    cislo=[-1,1]

    #pokud je pole plne, vrati vyjimku
    if '-' not in pole:
        raise ValueError(print("Pole uz je plne."))

    #uklada do promenne opacny_symbol symbol protihrace, ktery ma hledat
    if symbol=="x":
        opacny_symbol="o"
    elif symbol=="o":
        opacny_symbol="x"
    else:
        raise ValueError()

    #nejdrive zkusi, jestli uz protihrac hral
    # prochazi pole od 0. pozice a hleda prvni pozici-index opacneho symbolu
    try:
            o=pole.index(opacny_symbol)

    #pokud ho nenajde, umisti na libovolne pole svuj symbol
    except:
        #dokud je pozice mensi nez nula (co na zacatku je) nebo vetsi nez delka prijateho pole
        # nebo pozice uz neni volna bude do promenne "pozice" ukladat nahodna cisla mezi 0 a delkou pozice
        #takze by se to melo provest jen jednou a ukoncit
        while pozice < 0 or pozice >= len(pole) or pole[pozice] != '-':
                pozice = randint(0, len(pole)-1)

    #pokud uz opacny symbol v poli je
    else:
        
        #do pole (seznamu) "indexy" se ukladaji vsechny pozice opacneho symbolu, ktere pole obsahuje
        #enumeate vraci index-pozici prvku a jeho hodnotu
        #i jsou pozice v poli a x je symbol
        #i for i jde tedy od 0 do posledniho prvku
        #prochazi "pole" po jednom a pokud je x opacny symbol, ulozi do promenne "indexy" "i", tedy pozici
        #opacneho symbolu
        indexy = [i for i, x in enumerate(pole) if x == opacny_symbol]

        

        #vyzkousi se jestli je pozice vubec mozna a neni mensi nebo vetsi nez pole nebo jestli neni policko obsazene
        while pozice < 0 or pozice >= len(pole) or pole[pozice] != '-':
            
            #do promenne "o" se ulozi nahodne cislo, tedy pozice z promenne "indexy", je tam tedy pozice nahodneho
            #opacneho symbolu
            o=choice(indexy)

            #promenna "pozice" se nastavi na pozici opacneho symbolu a pak k ni pricte nebo odecte jednicku, takze
            #se nastavina vedlejsi policko
            pozice=o+choice(cislo)
                




    return tah(pole, pozice, symbol)

def tah(pole, index, symbol):  # Ukazka DRY principu, vytahli jsme spolecny kod do jedne funkce
    """Vrátí herní pole s daným symbolem umístěným na danou pozici."""
    if pole[index]!="-":
        raise ValueError("hrajes na obsazene pole")
    return pole[:index] + symbol + pole[index + 1:]
