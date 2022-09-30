'''Faça um Programa que peça a temperatura em graus Fahrenheit, 
transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).'''


def converter_fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


fahrenheit = float(input("Digite a temperatura em fahrenheit: "))
resultado = converter_fahrenheit_celsius(fahrenheit)

print('A temperatura em Celsius é: ', resultado)
