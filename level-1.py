print('======== OLD MACDONALD =======')
def old_macdonald(name):
    first_part = name[:3]
    second_part = name[3:]

    print(first_part)
    print(second_part)

    return first_part.capitalize() + second_part.capitalize()
    # letters = [el for el in name]
    # nameLength = len(letters)
    # if nameLength > 0: 
    #     letters[0] = letters[0].upper()
    # if nameLength >= 4:
    #     letters[3] = letters[3].upper()
    # return ''.join(letters)

print(old_macdonald('macdonald'))
print(old_macdonald('macdoNald'))
print(old_macdonald('mac'))
print(old_macdonald(''))

print('\n======== MASTER YODA =======')
def master_yoda(text):
    words = text.split()
    words.reverse()
    return ' '.join(words)

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

print('\n======== ALMOST THERE =======')
def almost_there(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10  

print(almost_there(96))
print(almost_there(150))
print(almost_there(209))