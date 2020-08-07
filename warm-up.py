print('====== even lesser ======')

def is_even(a):
    return a % 2 == 0

def lesser_of_two_evens(a,b):
    if is_even(a) and is_even(b):
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(2,5))


print('====== animal cracker ======')

def animal_crackers(text):
    words = text.split()
    return words[0][0] == words[1][0]
    #    return words[0][0].lower() == words[0][0].lower()

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


print('====== make 20 ======')
def makes_twenty(n1,n2):
    return n1 == 20 or n2 == 20 or n1+n2 == 20:

print(makes_twenty(20,10))
print(makes_twenty(10,10))
print(makes_twenty(10,1))