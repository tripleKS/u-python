import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(' ', '')
    return set([letter.lower() for letter in str1]) == set([l for l in alphabet])

isPan = ispangram("The quick brown fox jumps over the lazy dog")
print(isPan)