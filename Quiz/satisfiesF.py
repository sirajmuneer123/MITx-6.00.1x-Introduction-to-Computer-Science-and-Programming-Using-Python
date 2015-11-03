# Paste your function here
def satisfiesF(L):
    temp=L[:]
    for string in temp:
        if f(string)==False:
            L.remove(string)
    return len(L) 
run_satisfiesF(L, satisfiesF)

