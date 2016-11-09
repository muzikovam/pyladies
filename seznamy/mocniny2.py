def mocniny(pocet):
    s=[]
    for i in range(pocet):
        s.append(2**i)
    print(s)

pocet=int(input("zadej pocet mocnin: "))
mocniny(pocet)
