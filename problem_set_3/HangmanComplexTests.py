#  Hangman Complex Tests 
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ',len(secretWord),' letters long.'
    print '-------------'
    mistakesMade=8
    lettersGuessed=[]
    while mistakesMade>0:
	if isWordGuessed(secretWord, lettersGuessed)==True:
		print 'Congratulations, you won!'
		break
    	print 'You have %d guesses left.' %mistakesMade
        print 'Available letters: '+getAvailableLetters(lettersGuessed)
        print 'Please guess a letter:',
        charIn=raw_input().lower()
	if charIn in lettersGuessed:
		print 'Oops! You\'ve already guessed that letter: '+getGuessedWord(secretWord, lettersGuessed)
		print '-------------'
	elif charIn not in secretWord:
		mistakesMade -=1
		lettersGuessed.append(charIn)
		print 'Oops! That letter is not in my word: '+getGuessedWord(secretWord, lettersGuessed)
		print '-------------'
        
        elif charIn not in lettersGuessed:
        	lettersGuessed.append(charIn)
                print 'Good guess: '+getGuessedWord(secretWord, lettersGuessed)
		print '-------------'
       
    print 'Sorry, you ran out of guesses. The word was ',secretWord,'.' 
		







