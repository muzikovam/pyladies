def delitelnych3(od, do):

    s=[]
    for i in range(od, do):

        if i%3==0:
            s.append(i)
    return s




vystup=delitelnych3(67,102)
print(vystup)
print("Pocet cisel je ", len(vystup))
