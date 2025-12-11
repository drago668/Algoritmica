

def decode_santa_pin(code: str) -> str:
    results = []
    datos = code.strip('[').strip(']').split('][')
    for dato in datos:
        number = ''
        for char in dato:
            if char.isdigit():
                number = char   
            else:
                if char == '+':
                    number = (int(number) + 1) % 10
                elif char == '-':
                    number = (int(number) - 1) % 10
                elif char == '<':
                    results.append(results[-1])
        if number != '':
            results.append(int(number))
            number = ''
    result = "".join(str(char) for char in results)
    if len(result) < 4:
        return None
    return result


print(decode_santa_pin('[1+][2-]'))

