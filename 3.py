def my_func(num1, num2, num3):
    return num1 + num2 + num3 - (min(num1, num2, num3))
# исключаем минимальное из суммы 3х
print('Sum of three numbers'.upper())
try:
    print(my_func(float(input('enter first number ')), float(input('enter second number ')), float(input('enter third number '))))
except:
    print('Error')

