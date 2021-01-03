print('Sum of numbers'.upper())

# реализация с циклом

# summa = 0
# try:
#     while True:
#         for number in map(int, input('Enter your number or any symbol to stop: ').split()):
#             summa += number
#         print(summa)
# except ValueError:
#     print('result: ', summa)

#  реализация с функцией

def listsum(numList):
    for i in numList:
        global theSum
        theSum = theSum + i

theSum = 0
try:
    while True:
        result = (listsum(map(int, input('Enter your number or any symbol to stop: ').split())))
        print(theSum)
except ValueError:
    print('result: ', theSum)
