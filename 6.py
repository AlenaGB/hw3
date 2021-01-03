def int_func(word):
    return word[0].upper() + word[1:]
# заглавная у первого слова
def int_func2(word):
    return word.title()
# заглавная у всех слов (метод title)

print('capital letters'.upper())

word = input('Enter text: ')

print(int_func(word))
print(int_func2(word))