def my_func(x,y):
    if x > 0 and y < 0:
        return x ** y
    else:
        print('error')
        exit()
# с помощью операции возведения в степень
def my_func2(x,y):
    if x > 0 and y < 0:
        result = 1
        while y != 0:
            result *= x
            y = y + 1
        return 1 / result
    else:
        print('x must be > 0, y < 0')
        exit()
# при помощи цикла

print('exponentiation'.upper())

print('result 1. x^y= {:.2}'.format(my_func(float(input('x= ')), int(input('y= ')))))

print('result 2. x^y= {:.2}'.format(my_func2(float(input('x= ')), int(input('y= ')))))

