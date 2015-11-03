# Problem 1: Encryption (buildCoder) 
import string
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO  l_str=string.ascii_lowercase
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

    

