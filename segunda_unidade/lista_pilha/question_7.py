"""7. Escreva uma função chamada TPilha2 que recebe como parâmetro 2
pilhas (N e P) e um vetor de inteiros. Para cada um:
- se positivo, inserir na pilha P;
- se negativo, inserir na pilha N;
- se zero, retirar um elemento de cada pilha."""


def TPilha2(N, P, vetor):
    for i in range(len(vetor)):
        if vetor[i] == 0:
            if len(N) > 0:
                print(f"Valor retirado: {N[len(N)-1]}")
                N.pop()
            if len(P) > 0:
                print(f"Valor retirado: {P[len(P) - 1]}")
                P.pop()
        elif vetor[i] > 0:
            P.append(vetor[i])
        else:
            N.append(vetor[i])

    print(f"Os valores negativos: {N}. Os valores positivos: {P}")


parametros = TPilha2([], [], [5, -6, 2, 5, -1, -3, 9, 1, -2, 0, -4])
