
# PASSOS PARA QUEBRAR A CIFRA DE VIGENÈRE

# 1. Descobrir o tamanho da chave
#       a. Comparar a string com ela mesma fazendo 'shifts'
#       b. Encontrar os 'picos' de letras iguais, e assim o tamanho da palavra chave


# 2. Descobrir letra pro letra comparando a frequência das letras
#       a. A cada len(key) letras comparar os gráficos de frequência das letras

# 3. Decifrar

import string
import matplotlib.pyplot as plt
import numpy as np

from scipy import fftpack
from scipy.signal import argrelextrema
from scipy import stats


ENGLISH_LETTER_FREQUENCY = {
'A' : 8.12,
'B' : 1.49,
'C' : 2.71,
'D' : 4.32,
'E' : 12.0,
'F' : 2.30,
'G' : 2.03,
'H' : 5.92,
'I' : 7.31,
'J' : 0.10,
'K' : 0.69,
'L' : 3.98,
'M' : 2.61,
'N' : 6.95,
'O' : 7.68,
'P' : 1.82,
'Q' : 0.11,
'R' : 6.02,
'S' : 6.28,
'T' : 9.10,
'U' : 2.88,
'V' : 1.11,
'W' : 2.09,
'X' : 0.17,
'Y' : 2.11,
'Z' : 0.07 }


#--------------------------------------------------------------------------------

def shiftString(string, shift):
    first = string[0:(len(string) - shift)] 
    second = string[(len(string) - shift):] 
    shifted_string = second + first

    return shifted_string

#--------------------------------------------------------------------------------

def compareStrings(ciphered_text):
    
    equals = []

    for i in range(len(ciphered_text)):
        cont = 0
        shifted_string = shiftString(ciphered_text, i)
        for j in range(len(ciphered_text)):
            if ciphered_text[j] == shifted_string[j]:
                cont += 1
        
        equals.append(cont)
    
    return equals


#--------------------------------------------------------------------------------

def countLetters(ciphered_text, key_size, offset):
    letter_dict = dict.fromkeys(string.ascii_uppercase, 0)

    for i in range(len(ciphered_text)):
        if (i-offset) % key_size == 0:
            letter_dict[ciphered_text[i]] += 1
    
    for key in letter_dict.keys():
        letter_dict[key] = 100*letter_dict[key]/len(ciphered_text)

    return letter_dict

#--------------------------------------------------------------------------------
    
def guessByMode(power, freqs):
    copy_power = power.copy()
    frequencies = []
    
    for _ in range(10):
        max_power_index = np.argmax(copy_power)
        frequencies.append(freqs[max_power_index])
        copy_power[max_power_index] = 0

    frequencies = sorted(frequencies)
    frequencies.reverse()
    aux_frequencies_list = frequencies[1:]
    aux_frequencies_list.append(0)

    raw_guesses = (np.abs(np.array(frequencies) - np.array(aux_frequencies_list)))**(-1)

    guesses = []
    for x in raw_guesses:
        if(not int(round(x)) == 1377):
            guesses.append(x)

    guesses = np.round(np.array(guesses))

    # print("Guesses by mode: ", guesses)
    return stats.mode(guesses).mode[0]

#--------------------------------------------------------------------------------

def guessByBiggestPower(power, freqs):
    max_power_index = np.argmax(power)
    frequency_max_power = freqs[max_power_index]
    return round(1/frequency_max_power)

#--------------------------------------------------------------------------------

def guessBySTDThreshold(power, freqs):
    local_power_maxes = argrelextrema(power, np.greater)
    power_mean = np.mean(power)
    power_std = np.std(power)
    frequency_guesses = []
    for local_max_index in local_power_maxes[0]:
        if( power[local_max_index] > (power_mean+2*power_std)):
            frequency_guesses.append(freqs[local_max_index])
    size_guess = round(1/frequency_guesses[0])
    return size_guess


def guessBySTDThresholdNina(power, freqs):
    local_power_maxes = argrelextrema(power, np.greater)
    power_mean = np.mean(power)
    power_std = np.std(power)
    max_power = np.max(power)
    power_threshold = 0.4 * max_power

    # frequency_guesses = []
    # for local_max_index in local_power_maxes[0]:
    #     if( power[local_max_index] > (power_threshold)):
    #         frequency_guesses.append(freqs[local_max_index])

    frequency_guesses = []
    for p in power:
        if( p > (power_threshold)):
            frequency_guesses.append(freqs[list(power).index(p)])

    size_guess = round(1/frequency_guesses[0])
    return size_guess

#--------------------------------------------------------------------------------

def guessKeySize(equals):
    # Set sample frequency
    sample_freq = fftpack.fftfreq(equals.size, d=1)

    # Apply the fast fourier transform to signal
    sig_fft = fftpack.fft(equals)

    # Create frequecy axis 
    pidxs = np.where(sample_freq > 0)
    freqs = sample_freq[pidxs]

    # Get the power frequency espectrum
    power = np.abs(sig_fft)[pidxs]
    
    # Apply different methods to get the guesses
    key_size_by_mode = guessByMode(power,freqs)
    key_size_biggest_power = guessByBiggestPower(power, freqs)
    key_size_STD = guessBySTDThreshold(power, freqs)
    key_size_nina = guessBySTDThresholdNina(power, freqs)
    best_guesses = [int(key_size_by_mode), key_size_biggest_power, key_size_STD, key_size_nina]
    
    return power, freqs, best_guesses

#--------------------------------------------------------------------------------

def shiftDict(letter_dict):
    new_dict = {}
    old_dict = letter_dict.copy()
    letter_dict.pop(list(letter_dict.keys())[0])
    new_dict.update(letter_dict)
    new_dict[list(old_dict.keys())[0]] = old_dict[list(old_dict.keys())[0]]

    return new_dict

def compareFrequencyPlots(letter_dict, english_letter_frequency):
    diff = 0
    for i in range(len(letter_dict)):
        diff += abs(list(letter_dict.values())[i]-list(english_letter_frequency.values())[i])
    return diff

#----------------------------------------------------------------------------------
def findKey(cipher_message, key_size, english_letter_frequency):
    guessed_key = ""
    for offset in range(key_size):
        letter_dict = countLetters(cipher_message, key_size, offset)
        diff = 100
        desired_index = 0
        for i in range(len(english_letter_frequency)):
            new_diff = compareFrequencyPlots(letter_dict, english_letter_frequency)
            if(new_diff < diff):
                diff = new_diff
                desired_index = i
            letter_dict = shiftDict(letter_dict)
        guessed_key += list(english_letter_frequency.keys())[desired_index]

    return guessed_key