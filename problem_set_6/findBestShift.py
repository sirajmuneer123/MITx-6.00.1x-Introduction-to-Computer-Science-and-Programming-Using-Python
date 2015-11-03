#  Problem 2: Decryption (findBestShift) 
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    rWords=0
    bShift=0
    for i in range(26):
        new_text=applyCoder(text,buildCoder(i))
        iWords=new_text.split(' ')
        count=0
        for st in iWords:
            if isWord(wordList,st):
                count +=1
        if count > rWords:
            rWords=count
            bShift=i
    return bShift

