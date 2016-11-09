from random import randrange

body=0
while True:
    body=body+randrange(2,11)
    print(body)
    odpoved=input("chces dalsi kartu?")
    if odpoved=="ne":
        break
if body>21:
    print("Prohra")
elif body==21:
    print("Vyhra")
else:
    print("Taky dobry, ale chybelo ", 21-body, " bodu")
