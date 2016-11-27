
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


"""
Cilem je nalezt nejdelsi substringy v retezci predanem funkci.
Substring nesmi obsahovat cislo a musi obsahovat minimalne jedno velke pismeno.
Tato funkce byla soucasti prijimaciho pohovoru do spolecnosti Seznam.cz
"""
def solution(S):
   

    hold=-2
    indexy = [i for i, x in enumerate(S) if x.isdigit()]
    if len(indexy)==1:
        y = S[:indexy[0]]
        pocitadlo = zkouska(y)
        if pocitadlo > hold:
            hold = pocitadlo
        y = S[indexy[0]+1:]
        pocitadlo = zkouska(y)
        if pocitadlo > hold:
            hold = pocitadlo
    elif len(indexy) == 2:
        y = S[:indexy[0]]
        pocitadlo = zkouska(y)
        if pocitadlo > hold:
            hold = pocitadlo
        y = S[indexy[0] + 1:indexy[1]]
        pocitadlo = zkouska(y)
        if pocitadlo > hold:
            hold = pocitadlo
        y = S[indexy[1] + 1:]
        pocitadlo = zkouska(y)
        if pocitadlo > hold:
            hold = pocitadlo

    else:
        y = S[:indexy[0]]
        pocitadlo = zkouska(y)
        if pocitadlo > hold:
            hold = pocitadlo
        for i in range(len(indexy)-2):
            y = S[indexy[i+1] + 1:indexy[i+2]]
            pocitadlo = zkouska(y)
            if pocitadlo > hold:
                hold = pocitadlo
        y = S[indexy[-1] + 1:]
        pocitadlo = zkouska(y)
        if pocitadlo > hold:
            hold = pocitadlo


    return hold


def zkouska(y):
    j=0
    if len(y)<=1:
        return -1
    else:
        for i in range(len(y)):
            if y[i].isupper():
                j+=1
            else:
                pass
    if j==0:
        return -1
    else:
        return len(y)




#print(solution("a0Ba"))
#print(solution("a0aa"))
#print(solution("aa8aaaaaaaA2a"))
#print(solution("a0aaaaaaaa0aaA"))
#print(solution("a0aaaaaaaa0aaA6aaaaaAaa"))


def test_solution():
    assert solution("a0Ba")==2
    assert solution("a0aa")==-1
    assert solution("aa8aaaaaaaA2a")==8
    assert solution("a0aaaaaaaa0aaA")==3
    assert solution("a0aaaaaaaa0aaA6aaaaaAaa")==8
