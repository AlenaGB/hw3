def student():
    person = {'Name':'', 'Surname':'','Birthday':'','City':'', 'Email':'','Telephon number':'' }
    for f in person.keys():
        value = input(f'Enter your {f} ')
        person[f] = str(value)

    print('My name is', person['Name'],person['Surname'], 'I was born in', person['City'], person['Birthday'], 'My contacts:', person['Email'], person['Telephon number'])

print('Questionnaire'.upper())

student()