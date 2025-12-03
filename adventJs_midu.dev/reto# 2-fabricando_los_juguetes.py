def manufacture_gifts(gifts_to_produce):
    production_chain = []
    for gift in gifts_to_produce:
        if gift['quantity'] <= 0:
            continue
        else:
            for _ in range(gift['quantity']):
                production_chain.append(gift['toy'])
    return production_chain


production1 = [
    { 'toy': 'train', 'quantity': 0 },
    { 'toy': 'bear', 'quantity': -2 },
    { 'toy': 'puzzle', 'quantity': 1 }
]


result1 = manufacture_gifts(production1)
print(result1)