"""6. Implemente uma função chamada TPilha, que receba um vetor de
inteiros com 15 elementos. Para cada um deles, como segue:
- se o número for par, insira-o na pilha;
- se o número lido for ímpar, retire um número da pilha;
- Ao final, esvazie a pilha imprimindo os elementos."""


def TPilha(vetor):
    stack = []

    if len(vetor) == 15:
        for i in range(len(vetor)):
            if vetor[i] % 2 == 0:
                stack.append(vetor[i])
            else:
                if len(stack) > 0:
                    continue

        for i in range(len(stack)):
            print(stack.pop(0))


x = TPilha([12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 33, 43, 53, 63, 73])
