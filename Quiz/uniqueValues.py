def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    v=[]
    d={}
    l=[]
    for key,value in aDict.iteritems():
        if value not in d.values():
            d[key]=value
        else:
            v.append(value)
    for key1,value1 in sorted(d.iteritems()):
        if value1 not in v:
            l.append(key1)
    return l

             
