def max_depth(s: str) -> int:
    # Code here
    current_depth = 0
    max_depth = 0
    for char in s:
        if char == '[':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        if char == ']':
            current_depth -= 1
            if current_depth < 0:
                return -1
            
    if current_depth != 0:
        return -1
    return max_depth 


print(max_depth('[]'))  # -> 1
print(max_depth('[[]]'))  # -> 2
print(max_depth('[][]'))  # -> 1
print(max_depth('[[][]]'))  # -> 2
print(max_depth('[[[]]]'))  # -> 3
print(max_depth('[][[]][]'))  # -> 2


print(max_depth(']['))  # -> -1
print(max_depth('[[['))  # -> -1
print(max_depth('[]]]'))  # -> -1
print(max_depth('[][]['))  # -> -1


