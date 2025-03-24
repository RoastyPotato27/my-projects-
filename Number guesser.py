# RANDOM NUMBER GUESSER >
import random

# Range >
lowest =  1
highest = 1000

answer = random.randint(lowest,highest)
guesses = 0

# Keep guessing until u get the number >
is_running = True

print('Number guesser')
print(f'Find the number between {lowest} and {highest}')


while is_running:
    guess = input('Enter your guess: ')
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest or guess > highest:
            print('Number out of range.')
            print(f'Please select between {lowest} and {highest}')
        elif guess < answer:
            print('Too Low! Try Again!')
        elif guess > answer:
            print('Too High! Try Again!')
        else:
            print(f'Correct! The answer is {answer}')
            print(f'THe number of guesses used: {guesses}')
            is_running = False


    else:
        print('Invalid Guess.')
        print(f'Please select between {lowest} and {highest}')