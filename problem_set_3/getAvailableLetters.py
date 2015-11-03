# Printing Out all Available Letters 
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    new_list=[]
    for char in string.ascii_lowercase:
        if char not in lettersGuessed:
            new_list.append(char)
    return ''.join(new_list)
