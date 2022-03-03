
# PASSOS PARA QUEBRAR A CIFRA DE VIGENÈRE

# 1. Descobrir o tamanho da chave
#       a. Comparar a string com ela mesma fazendo 'shifts'
#       b. Encontrar os 'picos' de letras iguais, e assim o tamanho da palavra chave


# 2. Descobrir letra pro letra comparando a frequência das letras
#       a. A cada len(key) letras comparar os gráficos de frequência das letras

# 3. Decifrar

import string
import matplotlib.pyplot as plt



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
