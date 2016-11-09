
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7

    hold=-2
    i=0

    for i, x in enumerate(S):
        print("S je: ",S)
        if x.isdigit():
            if i==0:
                pass
            else:
                y=S[:i]
                pocitadlo=zkouska(y)
                if pocitadlo>hold:
                    hold=pocitadlo
                S=S[i+1:]

                for i, x in enumerate(S):
                    if x.isdigit():
                        if i==0:
                            pass
                        else:
                            y=S[:i]
                            pocitadlo=zkouska(y)
                            if pocitadlo>hold:
                                hold=pocitadlo
                        S=S[i+1:]


    pocitadlo=zkouska(S)
    if pocitadlo>hold:
        hold=pocitadlo
    return hold

def zkouska(y):
    i=0
    j=0
    if is_digit(y)==True:
        return -1

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
def is_digit(retezec):
    for i, x in enumerate(retezec):
        if x.isdigit():
            return True
    return False


print(solution("a0Ba"))
print(solution("a0aa"))
print(solution("aa8aaaaaaaA2a"))
print(solution("a0aaaaaaaa0aaA"))



def test_solution():
    assert solution("a0Ba")==2
    assert solution("a0aa")==-1
    assert solution("aa8aaaaaaaA2a")==8
    assert solution("a0aaaaaaaa0aaA")==3
