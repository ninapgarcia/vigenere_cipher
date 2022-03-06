import matplotlib.pyplot as plt
import break_cipher 


#--------------------------------------------------------------------------------
def plotEquals(equals, freqs, power):
    fig = plt.figure(figsize=(22, 22))

    subplot_equals=fig.add_subplot(211)
    subplot_fourier=fig.add_subplot(212)

    subplot_equals.plot(equals)
    subplot_equals.title.set_text("Equals")

    subplot_fourier.plot(freqs,power)
    subplot_fourier.title.set_text("Fourier analysis")

    # plt.show()
    plt.draw()
    plt.waitforbuttonpress(0)
    plt.close(fig)

#--------------------------------------------------------------------------------

def showPlot(letter_dict, english_letter_frequency):

    key_press = True
    while key_press: 


        names_letters = list(letter_dict.keys())
        values_letters = list(letter_dict.values())
        
        names_english = list(english_letter_frequency.keys())
        values_english = list(english_letter_frequency.values())

        fig = plt.figure(figsize=(10, 7))


        subplot_letters=fig.add_subplot(211)
        subplot_english=fig.add_subplot(212)

        subplot_letters.bar(range(len(letter_dict)), values_letters, tick_label=names_letters)
        subplot_letters.title.set_text("Ciphered text letter frequency")

        subplot_english.bar(range(len(english_letter_frequency)), values_english, tick_label=names_english)
        subplot_english.title.set_text("English letter frequency")



        plt.draw()
        key_press = plt.waitforbuttonpress(0)
        plt.close(fig)

        letter_dict = break_cipher.shiftDict(letter_dict)