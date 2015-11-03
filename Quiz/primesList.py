def primesList(N):
    '''
    N: an integer
    '''
    # Your code hdef prime(n):
    a=[]
    for num in range(2,N+1):
        flag=0
        for div in range(2,num):
            if num%div==0:
                flag=1
                break
        if flag==0:        
            a.append(num)
    return a
    
      
