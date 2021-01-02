def int_func(word):
    return word[0].upper() + word[1:]

print('capital letters in a line'.upper())

words = input('Enter text: ').split(' ')
newList = []
for word in words:
    newList.append(int_func(word))

print(' '.join(newList))