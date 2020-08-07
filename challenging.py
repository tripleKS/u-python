print('==== SPY GAME ====')
def spy_game(nums):
    preceding0 = 0
    for num in nums:
        if num == 0:
            preceding0 += 1
        elif num == 7:
            if preceding0 >= 2:
                return True
    return False



print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0,4,5,0,0,4,5,0,4,5,0,4,5,0,4,5,7]))
print(spy_game([1,0,7,2,4,5,0,7]))


print('\n==== COUNT PRIMES ====')
def is_prime(num):
    for i in range(2, round(num/2)):
        if num % i == 0:
            return False
    return True

def count_primes(num):
    if num < 2:
        return 0
    if num == 2:
        return 1
    if num == 3 or num == 4:
        return 2
    if num == 5 or num == 6:
        return 3
    if num >= 7 and num < 11:
        return 4   

    primes = 4;
    for el in range(11,num+1):
        if is_prime(el):
            primes += 1

    return primes

print(count_primes(100))
print(count_primes(200))

print('\n==== PRINT BIG ====')

