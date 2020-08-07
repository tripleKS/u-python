st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if word[0] == 's':
        print(word)


print([number for number in range(0,11) if number % 2 == 0])

st = 'Print every word in this sentence that has an even number of letters'
[print(f"even!{word}") for word in st.split() if len(word)%2 == 0]

df = []
df.insert()