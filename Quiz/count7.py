def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N==0:
        return 0
    else:
        if N%10==7:
            return 1+count7(N/10)
        else:
            return count7(N/10)
