with open('test.txt','w') as new_file:
    new_file.write('blala\nblalal\tskhjkh')


with open('test.txt') as new_file:
    content = new_file.read()

print(content)


counter = 1
while counter < 10:
    pass
    counter += 1
    print('Counter {}'.format(counter))
else:
    counter -= 2
    print('end')

pass

s = 0

S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]

M = [x for x in S if x % 2 == 0]

print(M)

input('Please enter any number within range 0..90')