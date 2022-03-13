from joblib import PrintTime
import break_cipher 
import text_processing
import random
import string
import cipher_decipher
import numpy as np



def generateRandomKey(alphabet):
    word = ""
    word_size = random.randint(2, 15)
    for _ in range(word_size):
        word += alphabet[random.randint(0, 25)]

    return word


ITERATIONS = 10000

# accuracy test
counters = [0,0]
text = "\"Barbie Girl\" received critical acclaim. Stephen Thomas Erlewine from AllMusic called the song \"one of those inexplicable pop culture phenomena\" and \"insanely catchy\", describing it as a \"bouncy, slightly warped Euro-dance song that simultaneously sends up femininity and Barbie dolls.\"[4] Larry Flick from Billboard wrote that \"with her squeaky, high-pitched delivery, Lene Grawford Nystrom fronts this giddy pop/dance ditty as if she were Barbie, gleefully verbalizing many of the twisted things people secretly do with the doll.\" He noted that \"at the same time, she effectively rants about the inherent misogyny of Barbie with a subversive hand\", adding that Rene Dif is an \"equally playful and biting presence, as he embodies male counterpart Ken with an amusing leer.\"[10] Scottish newspaper Daily Record stated, \"Love them or hate them, you have to admit Aqua's silly doll song is pure pop and the video is great, too\".[11] David Browne from Entertainment Weekly described it as a \"dance-floor novelty that alludes to the secret, less-than-wholesome life of every little girl's fave doll.\"[12] Another editor, Jeremy Helligar commented, \"There must be something in that Northern European water. Like recent tunes by their Swedish-pop counterparts Ace of Base and the Cardigans, these Danish newcomers' frothy debut is fun, fun, fun — but oh so disposable.\"[13] Insider stated that \"Barbie Girl\" is \"sugary sweet\" and \" totally catchy\".[14] A reviewer from People Magazine called it \"the year's best novelty record, a cartoonish anthem you'll need surgery to remove from your head.\"[15] Also Pop Rescue wrote that \"this song is fun, undoubtedly catchy, and bouncy, with the personas of Barbie and Ken fitting perfectly with the vocal contrast.\"[16]"

for _ in range(ITERATIONS):
    alphabet = string.ascii_uppercase
    key = generateRandomKey(alphabet)

    removed_chr_dict, text = text_processing.removingSpecialChr(text)
    text = text.upper()
    ciphered_text = cipher_decipher.cipherShift(text, key)
    equals = break_cipher.compareStrings(ciphered_text)
    equals = equals[1:]
    power, freqs, best_guesses = break_cipher.guessKeySize(np.array(equals))

    best_guesses.append(len(key))

    for i in range(len(best_guesses)):
        guessed_key_size = int(best_guesses[i])
        guessed_key = break_cipher.findKey(ciphered_text, guessed_key_size, break_cipher.ENGLISH_LETTER_FREQUENCY)
        if guessed_key == key:
            counters[i] += 1

accuracy = np.array(counters)/ITERATIONS


# By Mode, Biggest Power, Threshold, NinaThreshold, Know size
print("ACCURACY: ", accuracy)



# Para 10000 iterações com senhas (2, 15)          - 0.4 de Threshold
# ACCURACY:  [0.8938    0.9467]


# Para 1000 iterações com senhas (2, 15)          - 0.45 de Threshold
# ACCURACY:  [0.882     0.923]


# Para 10000 iterações com senhas (2, 15)          - 0.37 de Threshold
# ACCURACY:  [0.8927    0.9568]