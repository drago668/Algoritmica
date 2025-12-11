def find_unique_toy(toy: str) -> str:
    # Code here
    char_count = {}
    for char in toy:
        key = char.lower()
        if key in char_count:
            char_count[key] += 1
        else:
            char_count[key] = 1
    for char in toy:
        if char_count[char.lower()] == 1:
            return char
    return ''


print(find_unique_toy('Gift'))
print(find_unique_toy('sS'))
print(find_unique_toy('reindeeR'))
print(find_unique_toy('AaBbCc'))
print(find_unique_toy('abcDEF'))
print(find_unique_toy('aAaAaAF'))
print(find_unique_toy('sTreSS'))
print(find_unique_toy('z'))