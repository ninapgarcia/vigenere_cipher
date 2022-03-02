

#--------------------------------------------------------------------------------
def cipherShift(message, key):
    ciphered_message = ""
    for m in range(len(message)):
        k = m
        # extend key
        while len(key) <= k:
            k -= len(key)

        ciphered_message += chr(ord(message[m]) + ord(key[k]) - ord('A'))
        if ord(ciphered_message[m]) > ord('Z'):
            ciphered_message = ciphered_message[:-1]
            ciphered_message += chr(ord(ciphered_message[m]) - (ord('Z') - ord('A') + 1))
    
    return ciphered_message

#--------------------------------------------------------------------------------
def decipherShift(message, key):
    deciphered_message = ""
    for m in range(len(message)):
        k = m

        # extend key
        while len(key) <= k:
            k -= len(key)

        deciphered_message += chr(ord(message[m]) - (ord(key[k]) - ord('A')))
        if ord(deciphered_message[m]) < ord('A'):
            deciphered_message = deciphered_message[:-1]
            deciphered_message += chr((ord('Z') - ord('A')) + 1)

    return deciphered_message

#--------------------------------------------------------------------------------
