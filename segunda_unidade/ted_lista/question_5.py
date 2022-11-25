"""5. Escreva um programa em Python que simule o controle de uma pista de decolagem de
aviões em um aeroporto. Neste programa, o usuário deve ser capaz de realizar as
seguintes tarefas:
a. Listar o número de aviões aguardando na fila de decolagem;
b. Autorizar a decolagem do primeiro avião da fila;
c. Adicionar um avião à fila de espera;
d. Listar todos os aviões na fila de espera;
e. Listar as características do primeiro avião da fila."""
import numpy as np


class Aeroporto:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_avioes = 0
        self.avioes = np.empty(self.capacidade, dtype=int)
        self.identificacao_letra = np.chararray(self.capacidade, unicode=True)
        self.identificacao_num = np.chararray(self.capacidade, unicode=True)

    def __pista_vazia(self):
        if self.numero_avioes == 0:
            return True
        else:
            return False

    def __pista_cheia(self):
        if self.numero_avioes == self.capacidade:
            return True
        else:
            return False

    def add_lista_espera(self, aviao, identificacao_letra: str, identificacao_num: str):
        if self.__pista_cheia():
            print("A pista está cheia de aviões!")
            return

        if self.final == self.capacidade - 1:
            self.final = -1

        self.final += 1
        self.avioes[self.final] = aviao
        self.identificacao_letra[self.final] = identificacao_letra
        self.identificacao_num[self.final] = identificacao_num
        self.numero_avioes += 1

    def autorizar_decolagem(self):
        if self.__pista_vazia():
            print('Todos os aviões já decolaram!')
            return

        temp = self.avioes[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        else:
            self.numero_avioes -= 1
            return temp

    def caracteristicas_primeiro_aviao(self):
        if self.__pista_vazia():
            print("Não há aviões na fila!!")
        else:
            primeiro_aviao = self.avioes[self.inicio]
            letra_primeiro_aviao = self.identificacao_letra[self.inicio]
            num_primeiro_aviao = self.identificacao_num[self.inicio]

            print(
                f"""O avião a decolar é o: {primeiro_aviao}. Com a seguinte letra: {letra_primeiro_aviao}, e com a identificação de n {num_primeiro_aviao}.\n""")

    def num_avioes(self):
        if self.__pista_vazia():
            print("Não há aviões na fila!!")
        else:
            print(f"Existem {self.numero_avioes} aviões na fila!\n")

    def listar_avioes(self):
        for i in range(len(self.avioes)):
            print(f"""Aguarde! Fila de espera: Avião {self.avioes[i]}\n""")


if __name__ == "__main__":
    aviao = Aeroporto(9)
    aviao.add_lista_espera(55, "FFFF", "6")
    aviao.add_lista_espera(66, "GGGG", "7")
    aviao.add_lista_espera(77, "HHHH", "8")
    aviao.add_lista_espera(99, "IIII", "9")
    aviao.add_lista_espera(88, "JJJJ", "10")

    aviao.num_avioes()
    aviao.caracteristicas_primeiro_aviao()
    aviao.listar_avioes()
    aviao.autorizar_decolagem()
    aviao.num_avioes()
