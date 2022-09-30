''' Reverso do número. Faça uma função que retorne o reverso de um número inteiro
informado.
'''

numeroDigitado = (input('Digite um número: '))


def reverso(numero):
    inverte = str(numero)
    print(inverte[::-1])


reverso(numeroDigitado)
