
#--------------------------------------------------------------------------------
def get_message_and_key():
    message = input("\nEnter your message: ")
    key = input("Enter your key: ")

    return message.upper(), key.upper()

#--------------------------------------------------------------------------------
def cipherShift(message, key):
    ciphered_message = ""
    for message_index in range(len(message)):
        key_index = message_index
        # extend key
        while len(key) <= key_index:
            key_index -= len(key)

        ciphered_message += chr(ord(message[message_index]) + ord(key[key_index]) - ord('A'))

        if ord(ciphered_message[message_index]) > ord('Z'):
            new_letter = chr(ord(ciphered_message[message_index]) - (ord('Z') - ord('A') + 1))
            ciphered_message = ciphered_message[:-1] + new_letter
    
    return ciphered_message

#--------------------------------------------------------------------------------
def decipherShift(message, key):
    deciphered_message = ""
    for message_index in range(len(message)):
        key_index = message_index

        # extend key
        while len(key) <= key_index:
            key_index -= len(key)

        deciphered_message += chr(ord(message[message_index]) - (ord(key[key_index]) - ord('A')))
        if ord(deciphered_message[message_index]) < ord('A'):
            new_letter = chr(ord(deciphered_message[message_index]) + (ord('Z') - ord('A') + 1))
            deciphered_message = deciphered_message[:-1] + new_letter

    return deciphered_message

#--------------------------------------------------------------------------------

