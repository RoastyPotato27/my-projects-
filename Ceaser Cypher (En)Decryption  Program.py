# CAESER CYPHER DECRYPTION PROGRAM >
print('**Caeser Cypher Decryption Program**')

# Input >
choice = input('What do you want to do?(Encrypt or Decrypt): ').lower()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
brute_frc = str(input('Brute force?(Yes/No): '))
# Loop >
if brute_frc == 'No':
    def decrypt(message,offset):
        decrypted = ''
        for character in message:
            if character in alphabets:
                character_value = alphabets.find(character)
                decrypted += alphabets[(character_value + offset) % 26]
                    
            else:
                decrypted += character

        return decrypted


    def encrypt(message, offset):
        encrypted = ''
        for character in message:
            if character in alphabets:
                character_value = alphabets.find(character)
                encrypted += alphabets[(character_value - offset) % 26]
                    
            else:
                encrypted += character

        return encrypted

if choice == 'encrypt' or choice == 'decrypt':
    message = input('Enter message: ').lower()
    offset = int(input('Enter Offset here: '))

    if choice == 'encrypt':
        result = encrypt(message, offset)
        print('Encrypted message:', result)
    elif choice == 'decrypt':
        result = decrypt(message, offset)
        print('Decrypted message:', result)


    else:
        print('Invalid Choice! \n Choose between **Encrypt** and **Decrypt**')

        
# ====== BROKEN PART==========
# Forced Decryption >
if brute_frc == 'Yes':
    for i in range(1,26):
        print('Offset: {}'.format(i))
        print('\t {}'.format(message, i))
