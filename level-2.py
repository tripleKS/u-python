
print('===== has 3 3 =====')
def has_33(nums):
    first3 = False
    for num in nums:
        if num == 3 and first3:
            return True
        elif num == 3:
            first3 = True
        else:
            first3 = False
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, -3, 3, 1, -3, 3, 1, -3, 3, 1, -3, 3, 1, 3, 3]))

print('\n===== PAPER DOLL =====')
def paper_doll(text):
    letters = [lt for lt in text]
    result = []
    for letter in letters:
        result += letter*3
    return ''.join(result)

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

print('\n===== BLACKJACK =====')
def blackjack(a,b,c):
    result = a+b+c
    if result <= 21:
        return result
    elif a == 11 or b == 11 or c == 11:
        return result - 10
    else:
        return 'BUST'

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))


print('\n===== SUMMER OF 69 =====')
def summer_69(arr):
    skip = False
    result = 0
    for num in arr:
        if not skip:
            if num == 6:
                skip = True
            else:
                result += num
        else:
            if num == 9:
                skip = False

    return result

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11, 6,6,7,9,10]))
