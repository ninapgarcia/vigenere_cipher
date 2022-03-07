
#--------------------------------------------------------------------------------
def get_message_and_key():
    message = input("\nEnter your message: ")
    key = input("Enter your key: ")

    return message.upper(), key.upper()

#--------------------------------------------------------------------------------
# Funcion to cipher the message
def cipherShift(message, key):
    ciphered_message = ""
    for m in range(len(message)):
        k = m
        # extend key
        while len(key) <= k:
            k -= len(key)

        ciphered_message += chr(ord(message[m]) + ord(key[k]) - ord('A'))

        if ord(ciphered_message[m]) > ord('Z'):
            new_letter = chr(ord(ciphered_message[m]) - (ord('Z') - ord('A') + 1))
            ciphered_message = ciphered_message[:-1] + new_letter
    
    return ciphered_message

#--------------------------------------------------------------------------------
# Funcion to decipher the message
def decipherShift(message, key):
    deciphered_message = ""
    for m in range(len(message)):
        k = m

        # extend key
        while len(key) <= k:
            k -= len(key)

        deciphered_message += chr(ord(message[m]) - (ord(key[k]) - ord('A')))
        if ord(deciphered_message[m]) < ord('A'):
            new_letter = chr(ord(deciphered_message[m]) + (ord('Z') - ord('A') + 1))
            deciphered_message = deciphered_message[:-1] + new_letter

    return deciphered_message

#--------------------------------------------------------------------------------

