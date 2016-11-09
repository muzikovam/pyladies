from random import randrange
a=0
b=0
c=0
d=0
i=0
print ("Hrac A hazi kostkou")
while i!=6:
    i=randrange(1,7)
    print(i)
    a=a+1
print ("Hrac B hazi kostkou")
i=0
while i!=6:
    i=randrange(1,7)
    print(i)
    b=b+1
print ("Hrac C hazi kostkou")
i=0
while i!=6:
    i=randrange(1,7)
    print(i)
    c=c+1
print ("Hrac D hazi kostkou")
i=0
while i!=6:
    i=randrange(1,7)
    print(i)
    d=d+1
if a>b and a>c and a>d:
    print ("Vyhrava hrac A")
elif b>a and b>c and b>d:
    print ("Vyhrava hrac B")
elif c>b and c>a and c>d:
    print ("Vyhrava hrac C")
else:
    print ("Vzhrava hrac D")
