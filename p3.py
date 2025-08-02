s= "aaeecdcfvd"
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
for char in s:
    if freq[char] ==1:
        print(char)
        break       