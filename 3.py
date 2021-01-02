def my_func(num1, num2, num3):
    try:
        num1 = float(input('enter first number '))
        num2 = float(input('enter second number '))
        num3 = float(input('enter third number '))
        return num1 + num2 + num3 - (min(num1, num2, num3))
    except:
        print('Error')
        exit()

print(my_func(0,0,0))