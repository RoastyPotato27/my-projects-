# ARMSTRONG NUMBER >

num = int(input('Enter Number here: '))

num_str = str(num)
num_digits = len(num_str)

power_sum = 0
temp_num = num

while temp_num > 0:
    digit = temp_num %10
    power_sum += digit ** num_digits
    temp_num //= 10


if power_sum == num:
    print('Number is Armstrong Number.')

else:
    print('Number is not Armstrong Number.')
