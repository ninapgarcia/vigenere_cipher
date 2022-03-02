import string

def menu():
    message = input("Enter your message: ")
    key = input("Enter your key: ")

    return message, key


def cipherShift(message, key):
    message = message.upper()
    key = key.upper()
    cipher = ""
    for m in range(len(message)):
        k = m
        while len(key) <= k:
            k -= len(key)

        cipher += chr(ord(message[m]) + ord(key[k]) - ord('A'))
        if ord(cipher[m]) > ord('Z'):
            cipher = cipher[:-1]
            cipher += chr(ord(cipher[m]) - (ord('Z') - ord('A') + 1))
    
    return cipher


def decryptorShift(message, key):
    message = message.upper()
    key = key.upper()
    decrypted = ""
    for m in range(len(message)):
        k = m
        while len(key) <= k:
            k -= len(key)

        decrypted += chr(ord(message[m]) - (ord(key[k]) - ord('A')))
        if ord(decrypted[m]) < ord('A'):
            decrypted = decrypted[:-1]
            decrypted += chr((ord('Z') - ord('A')) + 1)
        

    return decrypted
