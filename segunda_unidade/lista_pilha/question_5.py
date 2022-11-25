"""5.Utilizando uma pilha resolver o exercício a seguir:
Dada uma sequência contendo N (N &gt;0) números reais, imprimi-la na
ordem inversa."""


import numpy as np


class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def __pilha_cheia(self):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False

    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print("A pilha está cheia!")
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print("A pilha está vázia!")
            return -1
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor

    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1

    def imprimir_inversamente(self):
        pilha_inversa = []
        for i in self.valores[::-1]:
            pilha_inversa.append(i)

        return pilha_inversa


pilha = Pilha(5)
pilha.empilhar(4)
pilha.empilhar(6)
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(9)
pilha.empilhar(7)

print(pilha.imprimir_inversamente())
