
def convert (rub, rate):
    try:
        return rub / rate
    except ZeroDivisionError:
        #деление на 0
        print('Incorrect input data')
        exit()

print('Convert RUB / USD '.upper())

print('You have {:.3} euros in your account '.format(convert(float(input('How many rubles do you want to convert to euros ')),float(input(('What is the currenst exchange rate '))))))