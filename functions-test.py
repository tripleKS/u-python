def funct_1():
    print('Hello silent')

def funct_2(name):
    print(f'hello {name}')

def my_func(*args):
    print(type(args))
    print(args)
    for el in args:
        print(el)


def myfunc(input):
    letters = [letter for letter in input]
    i = 0
    for letter in letters:
        if (i+1)%2 == 1:
            letters[i] = letter.lower()
        else:
            letters[i] = letter.upper()      
        i += 1
    
    return ''.join(letters) 

print(myfunc('Hel2'))