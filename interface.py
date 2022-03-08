

def menu():
    print("\n\n--------------------------- VIGENERE CIPHER ---------------------------\n")

    while True:
        print("1. Cipher and decipher message")
        print("2. Break cipher")
        print("0. Exit")
        action = input("Choose your action: ")[0]
        if action.isalpha() or 0 < int(action) > 2:
            print("\nInvalid input!")
        else:
            break

    return action 


def break_cipher_mannualy():
    print("\nHow do you want to break the cipher?\n")
    while True:
        print("0. Authomatically")
        print("1. Mannualy")
        mannualy = input("Choose your action: ")[0]
        if mannualy.isalpha() or 0 < int(mannualy) > 1:
            print("\nInvalid input!")
        else:
            break

    return mannualy 





