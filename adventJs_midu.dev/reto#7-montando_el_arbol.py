

def draw_tree(height, ornament, frequency):
    # Code here
    tree = ''
    default_symbol = '*'
    coeficiente = 0
    ornament_frecuency = 0
    for i in range(height):
        tree += ' ' * (int(height-i-1))
        coeficiente += 1
        symbol = default_symbol
        for _ in range(i + coeficiente):
            ornament_frecuency += 1
            if ornament_frecuency % frequency == 0:
                symbol = ornament
            else:
                symbol = default_symbol
            tree += symbol
        tree += '\n'
    tree += ' ' * (int(height) - 1) + '#'
    return tree


print(draw_tree(5, '0', 2))
#     *
#    0*0
#   *0*0*
#  0*0*0*0
# *0*0*0*0*
#     #
print(draw_tree(3, 'o', 3))
#   *
#  *o*
# *o**o
#  #
print(draw_tree(4, '+', 1))
#    +
#   +++
#  +++++
# +++++++
#   #
# Respuesta del reto de AdventJS #7
