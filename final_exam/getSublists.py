#  Problem 4 - Part 1 

def getSublists(L, n):
    return [L[i:i+n] for i in range(len(L)) if i+n <=len(L)]
 
    
