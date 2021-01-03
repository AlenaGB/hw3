def int_func(word):
    return word[0].upper() + word[1:]

print('capital letters in a line'.upper())

words = input('Enter text: ').split(' ')
# строка разбивается на список
newList = []
for word in words:
    newList.append(int_func(word))
# каждый элемент обращается к функции и добавляется в список
print(' '.join(newList))