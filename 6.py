def int_func(word):
    return word[0].upper() + word[1:]

def int_func2(word):
    return word.title()
# method title for all words

print('capital letters'.upper())

word = input('Enter text: ')

print(int_func(word))
print(int_func2(word))