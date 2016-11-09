import random


mozna_cisla=list(range(1,50))
for i in range(6):
    random.shuffle(mozna_cisla)
    print(mozna_cisla.pop())
    
