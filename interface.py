import colors
import break_cipher

#--------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------
def chooseLanguageDict():
    while True:
        print("\nChoose the Language of your ciphered text")
        print("1. English")
        print("2. Portuguese")
        lang = input(">")[0]
        if lang.isalpha() or 1 < int(lang) > 2:
            print("\nInvalid input!")
        else:
            break

    if int(lang) == 1:
        lang_dict = break_cipher.ENGLISH_LETTER_FREQUENCY
    elif int(lang) == 2:
        lang_dict = break_cipher.PORTUGUESE_LETTER_FREQUENCY


    return lang_dict 

#--------------------------------------------------------------------------------
def break_cipher_mannualy():
    print(colors.CYAN, "\n-> To break the cipher your text must have at least 1000 characteres and be ciphered with a key that has 2 to 20 characteres!", colors.RESET)
    print("\nHow do you want to break the cipher?\n")
    while True:
        print("0. Authomatically")
        print("1. Mannualy")
        mannualy = input("Choose your action: ")[0]
        if mannualy.isalpha() or 0 < int(mannualy) > 1:
            print("\nInvalid input!")
        else:
            break

    return int(mannualy) 
    
#--------------------------------------------------------------------------------





