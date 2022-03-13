import matplotlib.pyplot as plt
import break_cipher 

def showFrequencyPlot(power, freqs):
    plt.plot(freqs, power)
    plt.xlabel("Frequency (s)")
    plt.ylabel("Fourier Power Spectrum")
    plt.show()

#--------------------------------------------------------------------------------
def showDistributionPlotInteractive(letter_dict, letter_frequency):

    key_press = True
    cont = -1
    while key_press: 
        names_letters = list(letter_dict.keys())
        values_letters = list(letter_dict.values())
        
        names_english = list(letter_frequency.keys())
        values_english = list(letter_frequency.values())

        fig = plt.figure(figsize=(10, 7))

        subplot_letters=fig.add_subplot(211)
        subplot_english=fig.add_subplot(212)

        subplot_letters.bar(range(len(letter_dict)), values_letters, tick_label=names_letters)
        subplot_letters.title.set_text("Ciphered text letter frequency")

        subplot_english.bar(range(len(letter_frequency)), values_english, tick_label=names_english)
        subplot_english.title.set_text("Letter frequency")

        plt.draw()
        key_press = plt.waitforbuttonpress(0)
        plt.close(fig)

        letter_dict = break_cipher.shiftDict(letter_dict)
        cont += 1
    
    while(cont >= 26):
        cont -= 26

    return list(letter_frequency.keys())[cont]

#--------------------------------------------------------------------------------

def showDistributionPlot(letter_dict, letter_frequency):

    names_letters = list(letter_dict.keys())
    values_letters = list(letter_dict.values())
    
    names_english = list(letter_frequency.keys())
    values_english = list(letter_frequency.values())

    fig = plt.figure(figsize=(10, 7))

    subplot_letters=fig.add_subplot(211)
    subplot_english=fig.add_subplot(212)

    subplot_letters.bar(range(len(letter_dict)), values_letters, tick_label=names_letters)
    subplot_letters.title.set_text("Ciphered text letter frequency")

    subplot_english.bar(range(len(letter_frequency)), values_english, tick_label=names_english)
    subplot_english.title.set_text("English letter frequency")

    plt.draw()
    plt.waitforbuttonpress(0)
    plt.close(fig)

    letter_dict = break_cipher.shiftDict(letter_dict)
#--------------------------------------------------------------------------------
