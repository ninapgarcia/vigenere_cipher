

def menu():
    print("\n\n--------------------------- VIGENERE CIPHER ---------------------------\n")

    while True:
        print("1. Cipher and decipher message")
        print("2. Break cipher")
        print("0. Exit")
        action = input("Choose your action: ")
        if action.isalpha() or 0 < int(action) > 2:
            print("\nInvalid input!")
        else:
            break

    return action 




