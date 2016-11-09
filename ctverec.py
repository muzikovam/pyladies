a=float(input("zadej delku strany v cm: "))
nepravdiva_hodnota=a<0
if nepravdiva_hodnota:
    print("debile")
elif a==0:
    print("Nulova delka? Rly?")
else:
    print("Obsah ctverce se stranou", a, "je", a*a, "cm2.")
    print("Obvod ctverce se stranou", a, "je", 4*a, "cm.")
    print("Kdyby to byl kruh, tak s polomerem", a, "by mel obvod", 2*3.1415*a, "cm.")
print("A todle se tady ukaze vzdycky.")
