import string


def filter_gifts(gifts):
    good_Gifts = [] 
    accept = True
    
    for gift in gifts:
        for char in gift:

            if char in string.punctuation:
                accept = False

        if accept:
            good_Gifts.append(gift)

        accept = True
    return good_Gifts


