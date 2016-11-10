from random import randint
from ai import tah_pocitace
from util import tah

def vyhodnot(pole):
    if 'xxx' in pole:
        return 'x'
    elif 'ooo' in pole:
        return 'o'
    elif '-' not in pole:  # Nikdy nepouzivejte not '-' in pole, je to mene citelne
        return '!'
    else:
        return '-'





def tah_hrace(pole):
    """Získá od uživatele pozici, kam chce táhnout, a vrátí pole se zaznamenaným tahem hráče."""
    while True:

        try:
            pozice=int(input('Kam chceš hrát? (0..{})'.format(len(pole) - 1)))
        except ValueError:
            print('To neni číslo!')
        else:
            if pozice < 0 or pozice >= len(pole):
                print('Nemůžeš hrát venku z pole!')
            elif pole[pozice] != '-':
                print('Tam není volno!')
            else:
                return tah(pole, pozice, 'o')






def piskvorky1d():
    pole = '-' * 20
    i = 0
    while True:
        if i % 2 == 0:
            pole = tah_hrace(pole)
        else:
            pole = tah_pocitace(pole, "x")
        print(pole)

        if vyhodnot(pole) == 'o':
            print('Vyhrál hráč.')
        elif vyhodnot(pole) == 'x':
            print('Vyhrál počítač.')
        elif vyhodnot(pole) == '!':
            print('Remíza!')

        if vyhodnot(pole) != '-':
            break

        i += 1
