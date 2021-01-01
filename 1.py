print('Convert RUB / USD ')

def convert (rub, rate):
    try:
        rub = float(input('How many rubles do you want to convert to euros '))
        rate = float(input(('What is the currenst exchange rate ')))
        return rub / rate
    except ZeroDivisionError:
        print('Incorrect input data')
        exit()

print('You have {:.3} euros in your account'.format(convert(0,0)))