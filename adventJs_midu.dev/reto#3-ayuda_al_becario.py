def draw_gift(size, symbol):
    # Code here
    gift_wrapped = ""   
    if size >= 2:
        wrapper = symbol * size
        gift = symbol + (" " * (size - 2)) + symbol + "\n"
        gift_wrapped = wrapper + "\n" + gift * (size - 2) + wrapper
    else:
        gift_wrapped = ""
    return gift_wrapped


g1 = draw_gift(3, '#')
print(g1)