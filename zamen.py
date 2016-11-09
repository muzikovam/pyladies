def zamen(a, b, c):
    return a.replace(a[b],c)

print(zamen('palec', 0, 'v') == 'valec')
print(zamen('valec', 2, 'j') == 'vajec')
zamena=zamen("nevim", 3, "z")
print(zamena)
