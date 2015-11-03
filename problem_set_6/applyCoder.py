# Problem 1: Encryption (applyCoder)
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    new_txt=''
    for i in range(len(text)):
        if text[i] in coder:
            new_txt +=coder[text[i]]
        else:
            new_txt +=text[i]
    return new_txt

