# Problem 1: Encryption (applyShift)
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.import string
    def buildCoder(shift):
        l_str=string.ascii_lowercase
        u_str=string.ascii_uppercase
        l_new=l_str[shift:]
        l_new +=l_str[:shift]
        u_new=u_str[shift:]
        u_new +=u_str[:shift]
        dic={}
        for i in range(26):
                dic[u_str[i]]=u_new[i]
        for i in range(26):
                dic[l_str[i]]=l_new[i]
        return dic


    def applyCoder(text, coder):
        new_txt=''
        for i in range(len(text)):
                if text[i] in coder:
                        new_txt +=coder[text[i]]
                else:
                        new_txt +=text[i]
        return new_txt

    return applyCoder(text,buildCoder(shift))
    

