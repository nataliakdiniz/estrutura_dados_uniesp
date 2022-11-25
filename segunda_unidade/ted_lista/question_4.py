"""4. Construa uma Fila de Prioridade utilizando a linguagem Python em que sejam
implementadas as funções para inserção de um novo elemento (inteiro) na fila e a
remoção do elemento de mais alta prioridade"""

import numpy as np


class FilaPrioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self._topo = -1
        self._valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self._topo == -1

    def __fila_cheia(self):
        return self._topo == self.capacidade - 1

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("A fila está cheia!")
        else:
            self._topo += 1
            self._valores[self._topo] = valor

    def remover_maior_prioridade(self):
        if self.__fila_vazia():
            print("Fila vazia!")
        else:
            maior_prioridade = 0
            index_maior_prioridade = 0
            for index in range(0, self._topo + 1):
                if self._valores[index] > maior_prioridade:
                    maior_prioridade = self._valores[index]
                    index_maior_prioridade = index

            print(f"Elemento de maior prioridade: '{maior_prioridade}'")
            self._valores = np.delete(self._valores, index_maior_prioridade)
            self._topo = self._topo - 1

    def items_da_fila(self):
        fila_como_string = ""
        for i in range(self._topo+1):
            fila_como_string += str(self._valores[i])
            if i != self._topo:
                fila_como_string += ','
        print(f"[{fila_como_string}]")


if __name__ == '__main__':
    prioridade = FilaPrioridade(5)

    prioridade.enfileirar(10)
    prioridade.enfileirar(20)
    prioridade.enfileirar(30)
    prioridade.enfileirar(40)
    prioridade.enfileirar(50)

    prioridade.items_da_fila()
    prioridade.remover_maior_prioridade()
