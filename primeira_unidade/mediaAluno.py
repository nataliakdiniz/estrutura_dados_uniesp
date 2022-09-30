'''1 - Faça um programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c) A mensagem "Aprovado com Distinção", se a média for igual a 10. '''
primeiraNota = float(input('Digite sua primeira nota: '))
segundaNota = float(input('Digite sua segunda nota: '))
terceiraNota = float(input('Digite sua terceira nota: '))

media = (primeiraNota + segundaNota + terceiraNota) / 3
print('A sua média foi: ', media)
if media < 7.0:
    print('Reprovado')
elif media < 10:
    print('Aprovado')
else:
    print('Aprovado com Distinção!')
