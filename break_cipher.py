
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
from scipy.signal import find_peaks
from scipy.signal import argrelextrema



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

def countLetters(text):
    letter_dict = dict.fromkeys(string.ascii_uppercase, 0)
    for letter in text:
        print(letter_dict)
        letter_dict[letter] += 1
    
    return letter_dict

#--------------------------------------------------------------------------------

def showPlot(letter_dict):
    names = list(letter_dict.keys())
    values = list(letter_dict.values())

    plt.bar(range(len(letter_dict)), values, tick_label=names)
    plt.show()

#--------------------------------------------------------------------------------

def getPeeks(equals):
    # Set sample frequency
    sample_freq = fftpack.fftfreq(equals.size, d=1)
    # Apply the fast fourier transform to signal
    sig_fft = fftpack.fft(equals)

    # Create frequecy axis 
    pidxs = np.where(sample_freq > 0)
    freqs = sample_freq[pidxs]

    # Get the power frequency espectrum
    power = np.abs(sig_fft)[pidxs]
    
    # Find signal peeks
    max_power = np.max(power)
    max_power_index = np.argmax(power)

    # Index max power -> It's a multiple of fundamental frequency -> Our objective
    frequency_max_power = freqs[max_power_index]
    print("Max power frequency: ", frequency_max_power)

    # Get all power maxes
    local_power_maxes = argrelextrema(power, np.greater)
    print(len(local_power_maxes[0])) 
    THRESHOLD = 0.02

    power_mean = np.mean(power)
    power_std = np.std(power)
    print("Media das potencias: "+ str(np.mean(power)))
    print("Variancia das potencias: "+ str(np.std(power)))

    frequency_guesses = []
    for local_max_index in local_power_maxes[0]:
        if(freqs[max_power_index] == freqs[local_max_index]):
            print("MAXIMO: ", freqs[local_max_index])
        elif( power[local_max_index] > (power_mean+2*power_std)):
            print("MULTIPLO: ", freqs[local_max_index], freqs[max_power_index]%freqs[local_max_index])
            # Desse jeito reduz-se muuito a quantidade de candidatos, mas ainda dá até uns 20 dependendo da chave
            frequency_guesses.append(freqs[local_max_index])

    # Funciona muitas vezes, mas nem sempre, não sei bem mais o que pensar - Código tá feio mas tá facil de organizar kkk
    # Uma coisa q pensei com essa lista é que se pá a gente pode iterar sobre ela nas outras etapas, depois explico kkk
    print("FrequencyGuesses: ", frequency_guesses)
    print("FrequencyGuessFavorite: ", frequency_guesses[0])
    print("KeywordGuesses: ", np.round(1/np.array(frequency_guesses)))
    print("Favorite keyword size guess: ", round(1/frequency_guesses[0]))
    plt.figure()
    plt.plot(freqs, power)
    plt.xlabel('Frequencia [Hz]')
    plt.ylabel('Energia')

    plt.show()


