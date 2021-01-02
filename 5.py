print('Sum of numbers'.upper())

summa = 0

try:
    while True:
        for number in map(int, input('Enter your number or any symbol to stop: ').split()):
            summa += number
        print(summa)
except ValueError:
    print('result: ', summa)
