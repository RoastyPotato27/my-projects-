# Encryption Program >
import random 
import string

# Defining >
chars = ' ' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# Encryption >
msg = input('Enter Message Here:')
encrypted = ''

for letter in msg:
    index = chars.index(letter)
    encrypted += key[index]

print(f'Encrypted Text:{encrypted}')

# Decryption >
Cypher = input('Enter Cyper Here:')
decrypted = ''

for letter in Cypher:
    index = key.index(letter)
    decrypted += chars[index]

print(f'Decrypted Text:{decrypted}')