
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


"""
Cilem je nalezt nejdelsi substringy v retezci predanem funkci.
Substring nesmi obsahovat cislo a musi obsahovat minimalne jedno velke pismeno.
Tato funkce byla soucasti prijimaciho pohovoru do spolecnosti Seznam.cz
"""
import re
def solution(S):

    retezce = re.split("\d+", S)
    hold=-2
    for r in retezce:
        pocitadlo = zkouska(r)
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
