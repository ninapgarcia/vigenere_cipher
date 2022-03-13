import break_cipher 
import cipher_decipher
import text_processing
import graphics
import interface
import colors

import numpy as np

while True:
    action = int(interface.menu())

    # chipher and decipher
    if action == 1:

        message, key = cipher_decipher.get_message_and_key()

        removed_chr_dict, new_message = text_processing.removingSpecialChr(message)
        cipher_message = cipher_decipher.cipherShift(new_message, key)
        cipher_message_w_chr = text_processing.returnSpecialChr(removed_chr_dict, cipher_message)

        print(colors.CYAN, "\n-> CIPHERED MESSAGE: ", colors.RESET, cipher_message_w_chr, "\n")

        decrypted_message = cipher_decipher.decipherShift(cipher_message, key)
        decrypted_message_w_chr = text_processing.returnSpecialChr(removed_chr_dict, decrypted_message)

        print(colors.CYAN, "\n-> DECIPHERED MESSAGE: ", colors.RESET, decrypted_message_w_chr, "\n")

    # break cipher
    elif action == 2:
        
        # choose language
        lang_dict = interface.chooseLanguageDict()

        mannualy = interface.break_cipher_mannualy()

        ciphered_text = break_cipher.get_ciphered_text()
        removed_chr_dict, ciphered_text = text_processing.removingSpecialChr(ciphered_text)

        
        equals = break_cipher.compareStrings(ciphered_text)

        # break the cipher mannualy
        if mannualy == 1:
            guessed_key = ""
            power, freqs, best_guesses = break_cipher.guessKeySize(np.array(equals)) 
            graphics.showFrequencyPlot(power, freqs)
            key_size = int(input("Your Key size guess: "))
            print(colors.CYAN, "\nOpening distribution plots", colors.RESET)
            print("   >> Press ENTER to shift the plot")
            print("   >> Click the screen to make the letter guess")


            for offset in range(key_size):
                letter_dict = break_cipher.countLetterFrequency(ciphered_text, key_size, offset)
                guessed_key += graphics.showDistributionPlotInteractive(letter_dict, lang_dict)

        # break the cipher autommaticaly
        elif mannualy == 0:
            power, freqs, best_guesses = break_cipher.guessKeySize(np.array(equals)) 
            print(colors.RED, best_guesses, colors.RESET)
            # using guessedByThresholdNormalized()
            key_size = int(best_guesses[1]) 
            guessed_key = break_cipher.findKey(ciphered_text, key_size, lang_dict)
            print("Text size: ", len(ciphered_text))


        print(colors.CYAN, "\n\n-> GUESSED KEY: ", colors.RESET, guessed_key)
        decrypted_message = cipher_decipher.decipherShift(ciphered_text, guessed_key)
        decrypted_message_w_chr = text_processing.returnSpecialChr(removed_chr_dict, decrypted_message)
        print(colors.CYAN, "\n-> DECIPHERED MESSAGE: ", colors.RESET, decrypted_message_w_chr)

    # exit
    elif action == 0:
        break




"""
Test Texts

ENGLISH
> “Barbie Girl” received critical acclaim. Stephen Thomas Erlewine from AllMusic called the song "one of those inexplicable pop culture phenomena" and "insanely catchy", describing it as a "bouncy, slightly warped Euro-dance song that simultaneously sends up femininity and Barbie dolls."[4] Larry Flick from Billboard wrote that "with her squeaky, high-pitched delivery, Lene Grawford Nystrom fronts this giddy pop/dance ditty as if she were Barbie, gleefully verbalizing many of the twisted things people secretly do with the doll." He noted that "at the same time, she effectively rants about the inherent misogyny of Barbie with a subversive hand", adding that Rene Dif is an "equally playful and biting presence, as he embodies male counterpart Ken with an amusing leer."[10] Scottish newspaper Daily Record stated, "Love them or hate them, you have to admit Aqua's silly doll song is pure pop and the video is great, too".[11] David Browne from Entertainment Weekly described it as a "dance-floor novelty that alludes to the secret, less-than-wholesome life of every little girl's fave doll."[12] Another editor, Jeremy Helligar commented, "There must be something in that Northern European water. Like recent tunes by their Swedish-pop counterparts Ace of Base and the Cardigans, these Danish newcomers' frothy debut is fun, fun, fun — but oh so disposable."[13] Insider stated that "Barbie Girl" is "sugary sweet" and "totally catchy".[14] A reviewer from People Magazine called it "the year's best novelty record, a cartoonish anthem you'll need surgery to remove from your head."[15] Also Pop Rescue wrote that "this song is fun, undoubtedly catchy, and bouncy, with the personas of Barbie and Ken fitting perfectly with the vocal contrast."[16]
> Sleep is a naturally recurring state of mind and body, characterized by altered consciousness, relatively inhibited sensory activity, reduced muscle activity and inhibition of nearly all voluntary muscles during rapid eye movement (REM) sleep,[1] and reduced interactions with surroundings.[2] It is distinguished from wakefulness by a decreased ability to react to stimuli, but more reactive than a coma or disorders of consciousness, with sleep displaying different, active brain patterns. Sleep occurs in repeating periods, in which the body alternates between two distinct modes: REM sleep and non-REM sleep. Although REM stands for "rapid eye movement", this mode of sleep has many other aspects, including virtual paralysis of the body. A well-known feature of sleep is the dream, an experience typically recounted in narrative form, which resembles waking life while in progress, but which usually can later be distinguished as fantasy. During sleep, most of the body's systems are in an anabolic state, helping to restore the immune, nervous, skeletal, and muscular systems;[3] these are vital processes that maintain mood, memory, and cognitive function, and play a large role in the function of the endocrine and immune systems.[4] The internal circadian clock promotes sleep daily at night. The diverse purposes and mechanisms of sleep are the subject of substantial ongoing research.[5] Sleep is a highly conserved behavior across animal evolution.[6] Humans may suffer from various sleep disorders, including dyssomnias such as insomnia, hypersomnia, narcolepsy, and sleep apnea; parasomnias such as sleepwalking and rapid eye movement sleep behavior disorder; bruxism; and circadian rhythm sleep disorders. The use of artificial light has substantially altered humanity's sleep patterns.[7] One common source of artificial light are modern devices such as smartphones or televisions which have been shown to affect sleep health. Blue light, a specific type of artificial light, can disrupt the release of the hormone melatonin which aids in helping to facilitate sleepiness.[8]

PORTUGUESE
> Barbie é uma boneca utilizada como brinquedo infantil, criada pela empresa americana Mattel em 9 de março de 1959. Ela foi criada pela empresária Ruth Handler e foi baseada na boneca alemã Bild Lilli, que mais tarde foi comprada pela Mattel. A Barbie é a protagonista de uma marca de bonecas e acessórios da Mattel, contando com outros membros da família e modelos de bonecas colecionáveis. A boneca tem sido influente na indústria de brinquedos por mais de sessenta anos, além de ter sido alvo de controvérsias e processos judiciais referentes a sua aparência e estilo de vida. A Mattel já vendeu mais de um bilhão de bonecas Barbie, tornando-a a linha de produtos mais lucrativa da empresa. A marca de bonecas expandiu-se para uma franquia de mídia com o lançamento de uma série de filmes de animação, iniciada em 2001. Além dos filmes, tornou-se um veículo para a venda de outras mercadorias como roupas, série de animação, jogos eletrônicos entre outros produtos. As vendas de bonecas Barbie começaram a cair acentuadamente entre 2014 e 2016. Em 2020, a Mattel vendeu US$ 1,35 bilhão em bonecas e acessórios da marca e este foi seu melhor crescimento de vendas em duas décadas, um aumento de US$ 950 milhões em comparação ao ano de 2017.
> Sono (do latim somnus, com o mesmo significado) é um estado ordinário de consciência, complementar ao da vigília (ou *estado desperto), em que há repouso normal e periódico, caracterizado, tanto no ser humano como nos outros vertebrados, pela suspensão temporária da atividade perceptivo-sensorial e motora voluntária. Ao dizer-se complementar, em conjugação com ordinário, quer-se significar tão somente que, na maioria dos indivíduos (com destaque, aqui, para os humanos), tais estados de consciência alternam-se, complementando-se ordinária, periódica e regularmente. O estado de sono é caracterizado por um padrão de ondas cerebrais típico, essencialmente diferente do padrão do estado de vigília, bem como do verificado nos demais estados de consciência. Dormir, nesta acepção, significa passar do estado de vigília para o estado de sono. No ser humano, o ciclo do sono era formado por cinco estágios, mas atualmente são quatro, pois os estágios N3 e N4 fundiram-se em N3, e duram cerca de noventa minutos (podendo chegar a 120 minutos).[carece de fontes] Ele se repete durante quatro ou cinco vezes durante o sono. Do que se tem registro na literatura especializada, o período mais longo que uma pessoa já conseguiu ficar sem dormir foi de onze dias.


"""