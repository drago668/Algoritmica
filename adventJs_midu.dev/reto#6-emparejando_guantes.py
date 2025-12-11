from typing import List, Dict


# intento 1 con fallas
def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
    # Code here
    paired_gloves = []
    gloves_list = [glove['color'] + glove['hand'] for glove in gloves]
    for glove in gloves_list:
        if glove == '':
            continue
        color = glove[:-1]  # quita la mano
        oppositive_glove = color + ('R' if 'L' in glove else 'L')  # encuentra la mano opuesta if blueR -> blueL
        indice = next((index for index, g in enumerate(gloves_list) if g == oppositive_glove), -1)
        if indice > 0:
            paired_gloves.append(color)
            gloves_list[indice] = ''
    return paired_gloves



# intento 2 


def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
    paired_gloves = []
    arreglo_auxiliar = {}
    for glove in gloves:
        llave = glove['color'] + glove['hand']
        llave_opuesta = glove['color'] + ('R' if glove['hand'] == 'L' else 'L')
        if arreglo_auxiliar.get(llave_opuesta):
            paired_gloves.append(glove['color'])
            arreglo_auxiliar[llave_opuesta] -= 1
        else:
            if arreglo_auxiliar.get(llave):
                arreglo_auxiliar[llave] += 1
            else:
                arreglo_auxiliar[llave] = 1
        print(arreglo_auxiliar)
    return paired_gloves


gloves = [
    {'hand': 'L', 'color': 'red'},
    {'hand': 'R', 'color': 'red'},
    {'hand': 'R', 'color': 'green'},
    {'hand': 'L', 'color': 'blue'},
    {'hand': 'L', 'color': 'green'}
]

print(match_gloves(gloves))
# Respuesta del reto de AdventJS #6