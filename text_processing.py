import unidecode


#--------------------------------------------------------------------------------
# Function to remove special characteres from the text
def removingSpecialChr(text):
    # remove accents from text
    text = unidecode.unidecode(text)
    # text with no special characteres
    new_text = ""
    # dict with the removed characteres and their index
    removed_chr_dict = {}

    for i in range(len(text)):
        if not text[i].isalpha():
            removed_chr_dict[i] = text[i]
        else:
            new_text += text[i]

    return removed_chr_dict, new_text

#--------------------------------------------------------------------------------
# Function to return special characteres to the text
def returnSpecialChr(removed_chr_dict, text):
    for i in removed_chr_dict:
        text = text[:i] + removed_chr_dict[i] + text[i:]
    
    return text

#--------------------------------------------------------------------------------
