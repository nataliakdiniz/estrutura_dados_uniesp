"""1. Escrever uma função que receba como parâmetro uma pilha. A função deve retornar o maior elemento da pilha. A passagem deve ser por valor ou referência?"""

"""A passagem deve ser por valor!"""




import numpy as np
def larger_element(stack):
    larger = stack[0]
    for i in range(len(stack)):
        if stack[i] > larger:
            larger = stack[i]
    return larger


element = larger_element([1000, 435, 576, 12, 9])
print(element)
