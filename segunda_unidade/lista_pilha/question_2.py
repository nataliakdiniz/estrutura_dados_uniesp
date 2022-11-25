"""2. Escreva uma função que receba como parâmetro duas pilhas e
verifique de elas são iguais. Duas pilhas são iguais se possuem os
mesmos elementos, na mesma ordem."""


def equalStack(stack1, stack2):
    if stack1 == stack2:
        return True
    else:
        return False


firstStack = equalStack([88, 89, 90, 91], [88, 89, 90])
secondStack = equalStack([-1, -2, -4], [-1, -2, -4])
print(firstStack)
print(secondStack)
