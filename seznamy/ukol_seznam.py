zvirata = ["had", "pes", "andulka", "kočka", "králík"]
zvirata.sort()
print(zvirata)


def rozdvoj(seznam):
    vystupni_seznam=[]
    for polozka in seznam:
        dvojce=(polozka[1:], polozka)
        vystupni_seznam.append(dvojce)

    return vystupni_seznam


def sluc(seznam_dvojic):
    vystupni_seznam = []
    for polozka in seznam_dvojic:
        jednice=polozka[1]
        vystupni_seznam.append(jednice)

    return vystupni_seznam


dvojzvirata=rozdvoj(zvirata)
print(dvojzvirata)
dvojzvirata.sort()
zvirata=sluc(dvojzvirata)
print(zvirata)