# Credit card Validator >
# Input >
Number = input('Enter Credid Card Number: ')
Number = Number.replace('-', '')
Number = Number.replace(' ', '')
Number = Number[::-1]

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# adding odd places >
for n in Number[::2]:
    sum_odd_digits += int(n)  

# Doubling second digit >
for n in Number[1::2]:
    n = int(n) * 2
    if n >= 10:
        sum_even_digits = 1 + (n % 10)
    else:
        sum_odd_digits += n

# Total >
total = sum_odd_digits + sum_even_digits

# valid or no >
if total % 10 == 0:
    print('Valid.')
else:
    print('Invalid.')