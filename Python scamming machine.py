# Slot Macine >

# Importing > 
import random

# Defining >
def spin_rows():
     symbols = ['💩','🍉','🍋','🔔','⭐']

     return [random.choice(symbols) for _ in range(3)]

def print_rows(rows):
    print('**************')
    print(' | '.join(rows))
    print('**************')

def payout(rows,bet):
    if rows[0] == rows[1] == rows[2]:
        if rows[0] == '💩':
            return bet * 0
        elif rows[0] == '🍉':
            return bet * 2
        elif rows[0] == '🍋':
            return bet * 5
        elif rows[0] == '🔔':
            return bet * 10
        elif rows[0] == '⭐':
            return bet * 50
    return 0

def main():
    balance = 100

    print('************************************')
    print('Welcome to Python Scamming Services.')
    print('Symbols: 💩  🍉  🍋  🔔  ⭐')
    print('************************************')

    while balance > 0:
        print(f'Current Balance: ${balance}')
        bet = input('Place your bet:')

        if not bet.isdigit():
            print('Enter valid amount')
            continue
        
        bet = int(bet)
        if bet > balance:
            print('Insufficient Funds.')
        
        elif bet <= 0:
            print('Bet must be greater than 0.')
            continue
        balance -= bet

        rows = spin_rows()
        print('Spinning.....\n')
        print_rows(rows)
        pay = payout(rows, bet)

        if pay > 0:
            print(f'You won ${pay}')
        else:
            print('You lost this round.')
        
        balance += pay
        again = input('Wanna get scammed again?(Y/N): ').upper()
        if again != 'Y':
            break
    
    print('************************************')
    print(f"Game over. Final Balance: ${balance}")
    print('************************************')


if __name__ == '__main__':
    main()
