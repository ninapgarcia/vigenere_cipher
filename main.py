import break_cipher 
import cipher_decipher
import text_processing
import graphics

import numpy as np

#--------------------------------------------------------------------------------
def menu():
    message = input("Enter your message: ")
    key = input("Enter your key: ")

    return message.upper(), key.upper()
#--------------------------------------------------------------------------------


message, key = menu()
removed_chr_dict, new_message = text_processing.removingSpecialChr(message)

"""

print("\n-------------- CIPHER --------------\n")
cipher_message = cipher_decipher.cipherShift(new_message, key)
cipher_message_w_chr = text_processing.returnSpecialChr(removed_chr_dict, cipher_message)
print("CIPHERED MESSAGE: ", cipher_message_w_chr)


print("\n------------ DECRYPTOR -------------\n")
decrypted_message = cipher_decipher.decipherShift(cipher_message, key)
decrypted_message_w_chr = text_processing.returnSpecialChr(removed_chr_dict, decrypted_message)
print("DECIPHERED MESSAGE: ", decrypted_message_w_chr)

"""


print("\n-------------------- CIPHER --------------------\n")
cipher_message = cipher_decipher.cipherShift(new_message, key)
print("CIPHERED MESSAGE: ", text_processing.returnSpecialChr(removed_chr_dict, cipher_message))

print("\n----------------- DECRYPTOR -------------------\n")
decrypted_message = cipher_decipher.decipherShift(cipher_message, key)
print("DECIPHERED MESSAGE: ", decrypted_message)
equals = break_cipher.compareStrings(cipher_message)


print("\n---------------- EQUAL LETTERS -----------------\n")
equals_without_the_first_one = equals[1:]
power, freqs, best_guesses = break_cipher.guessKeySize(np.array(equals_without_the_first_one))

print("Key len guesses: ", best_guesses)
print("Real key len: " + str(len(key)))
print("Text ciphered size: ", len(decrypted_message))

graphics.plotEquals(equals_without_the_first_one, freqs, power)

# -------------------------------------------------------------
print("\n---------------- EQUAL LETTERS -----------------\n")
num_key = input("Number of letters in the KEYWORD: ")


print("\n---------------- LETTER DICT -----------------\n")
letter_dict = break_cipher.countLetters(cipher_message)
print(letter_dict)


# ISSO TA MOSTRANDO A FREQUENCIA DE TODAS AS LETRAS E NAO É ASSIM QUE É PRA FAZER
# TEM Q IR DE ACORDO COM LEN(KEY)
graphics.showPlot(letter_dict)




"""
TEXTO TESTE

Billy always listens to his mother. He always does what she says. If his mother says, "Brush your teeth," Billy brushes his teeth. If his mother says, "Go to bed," Billy goes to bed. Billy is a very good boy. A good boy listens to his mother. His mother doesn't have to ask him again. She asks him to do something one time, and she doesn't ask again. Billy is a good boy. He does what his mother asks the first time. She doesn't have to ask again. She tells Billy, "You are my best child." Of course Billy is her best child. Billy is her only child. Nancy wants to live a long time. She wants to live for one hundred years. She is five years old now. She wants to live 95 more years. Then she will be 100. Her father is 30 years old. He wants to live a long time, too. He wants to live for one hundred years. He wants to live for 70 more years. "Daddy, we will grow old together, okay?" Nancy said to her father. "Yes, honey, we will grow old together," he said to Nancy. Then Nancy smiled. She gave her daddy a big hug.

"""