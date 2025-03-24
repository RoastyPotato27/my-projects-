# COMPOUND INTEREST CALCULATOR >

principle = 0
rate = 0
time = 0

# Principle >
while principle <= 0:
    principle = float(input('Enter Principle amount: '))
    if principle <= 0:
        print('Principle can not be less than or equal to 0')


# Rate >
while rate <= 0:
    rate = float(input('Enter Rate of interest: '))
    if rate <= 0:
        print('Rate of interest can not be less than or equal to 0')


# Time >
while time <= 0:
    time = int(input('Enter Time: '))
    if time <= 0:
        print('Time can not be less than or equal to 0')



Total = principle * (1 + rate/100)**time
print(f'Balance after {time} year/s: ${Total:.2f}')