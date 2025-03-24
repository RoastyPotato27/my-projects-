# TEMPERATURE CONVERSION >

# Input >
unit = input('What unit do you want to convert to?(C or F) : ')
temp = float(input('Enter temperature: '))

# if statemet >
if unit == 'F':
    f =  (temp * 9) /5 + 32
    print(f'The Temperature in Farenheit is {f}')

elif unit == 'C':
    c = (temp -32) * 5/9
    print(f'The Temperature in Celcius is {c}')

else:
    print(f'{unit} is an invalid unit')