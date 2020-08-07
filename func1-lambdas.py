def up_low(s):
    lowLetters = 0
    letters = [letter for letter in s]
    upLetters = len(list(filter(lambda l: l.isupper(), letters)))
    print(upLetters)


# up_low('gDFGkjh')

def multiply(numbers):  
    res = 1
    for num in numbers:
        res *= num
    return res

res = multiply([1,2,3,-4])
print(res)


def palindrome(s):
    lengthS = len(s)
    for i in range(0,lengthS):
        if s[i] != s[lengthS - 1 - i]:
            return False
    return True

print(palindrome('adac'))