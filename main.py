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

# graphics.plotEquals(equals_without_the_first_one, freqs, power)

# -------------------------------------------------------------
print("\n---------------- EQUAL LETTERS -----------------\n")
key_size = len(key) # input("Number of letters in the KEYWORD: ")


print("\n---------------- RESULT -----------------\n")
guessed_key = break_cipher.findKey(cipher_message, key_size, break_cipher.ENGLISH_LETTER_FREQUENCY)
print("Real key len: " + str(len(key)))
print("Text ciphered size: ", len(decrypted_message))

print("Guessed key: ", guessed_key)



"""
TEXTO TESTE

Billy always listens to his mother. He always does what she says. If his mother says, "Brush your teeth," Billy brushes his teeth. If his mother says, "Go to bed," Billy goes to bed. Billy is a very good boy. A good boy listens to his mother. His mother doesn't have to ask him again. She asks him to do something one time, and she doesn't ask again. Billy is a good boy. He does what his mother asks the first time. She doesn't have to ask again. She tells Billy, "You are my best child." Of course Billy is her best child. Billy is her only child. Nancy wants to live a long time. She wants to live for one hundred years. She is five years old now. She wants to live 95 more years. Then she will be 100. Her father is 30 years old. He wants to live a long time, too. He wants to live for one hundred years. He wants to live for 70 more years. "Daddy, we will grow old together, okay?" Nancy said to her father. "Yes, honey, we will grow old together," he said to Nancy. Then Nancy smiled. She gave her daddy a big hug.

"""

""""

“Barbie Girl” received critical acclaim. Stephen Thomas Erlewine from AllMusic called the song "one of those inexplicable pop culture phenomena" and "insanely catchy", describing it as a "bouncy, slightly warped Euro-dance song that simultaneously sends up femininity and Barbie dolls."[4] Larry Flick from Billboard wrote that "with her squeaky, high-pitched delivery, Lene Grawford Nystrom fronts this giddy pop/dance ditty as if she were Barbie, gleefully verbalizing many of the twisted things people secretly do with the doll." He noted that "at the same time, she effectively rants about the inherent misogyny of Barbie with a subversive hand", adding that Rene Dif is an "equally playful and biting presence, as he embodies male counterpart Ken with an amusing leer."[10] Scottish newspaper Daily Record stated, "Love them or hate them, you have to admit Aqua's silly doll song is pure pop and the video is great, too".[11] David Browne from Entertainment Weekly described it as a "dance-floor novelty that alludes to the secret, less-than-wholesome life of every little girl's fave doll."[12] Another editor, Jeremy Helligar commented, "There must be something in that Northern European water. Like recent tunes by their Swedish-pop counterparts Ace of Base and the Cardigans, these Danish newcomers' frothy debut is fun, fun, fun — but oh so disposable."[13] Insider stated that "Barbie Girl" is "sugary sweet" and "totally catchy".[14] A reviewer from People Magazine called it "the year's best novelty record, a cartoonish anthem you'll need surgery to remove from your head."[15] Also Pop Rescue wrote that "this song is fun, undoubtedly catchy, and bouncy, with the personas of Barbie and Ken fitting perfectly with the vocal contrast."[16]


"""