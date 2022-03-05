import matplotlib.pyplot as plt

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

def showPlot(letter_dict):
    fig = plt.figure()

    names = list(letter_dict.keys())
    values = list(letter_dict.values())

    plt.bar(range(len(letter_dict)), values, tick_label=names)
    # plt.show()
    plt.draw()
    plt.waitforbuttonpress(0)
    plt.close(fig)