import string


def filter_gifts(gifts):
    goodGifts = []  
    accept=True
    
    for gift in gifts:
        for char in gift:

            if char in string.punctuation:
                accept=False

        if accept:
            goodGifts.append(gift)

        accept=True
    return goodGifts


