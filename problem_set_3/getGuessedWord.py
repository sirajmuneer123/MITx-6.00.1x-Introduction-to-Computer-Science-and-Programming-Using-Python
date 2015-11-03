#Printing Out the User's Guess
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    new_list=[]
    for char in secretWord:
        if char not in lettersGuessed:
            new_list.append('_')
        else:
            new_list.append(char)
    return ''.join(new_list)
            
