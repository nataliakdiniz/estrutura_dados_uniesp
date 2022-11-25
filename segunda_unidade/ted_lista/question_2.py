"""2.Desenvolva um programa em Python utilizando uma Pilha de acordo com a situação
problema: Armazene as placas dos carros de luxos (apenas os números) que estão
estacionados em um rua sem saída. Dado uma placa verifique se o carro está estacionado
na rua. Caso esteja, informe a sequência de carros que deverá ser retirada para que o
carro em questão consiga sair."""

import numpy as np


class Street:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimo_carro = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def __street_cheia(self):
        if self.ultimo_carro == self.capacidade - 1:
            return True

        else:
            return False

    def street_vazia(self):
        if self.ultimo_carro == -1:
            return True

        else:
            return False

    def estacionar(self, placa):
        if self.__street_cheia():
            print("Rua cheia!")

        else:
            self.ultimo_carro += 1
            self.valores[self.ultimo_carro] = placa

    def retirar(self):
        if self.street_vazia():
            print("Pilha vazia!")
            return -1

        else:
            valor = self.valores[self.ultimo_carro]
            self.ultimo_carro -= 1
            return valor

    def ver_ultimo_carro(self):
        if self.ultimo_carro != -1:
            return self.valores[self.ultimo_carro]
        else:
            return -1

    def verificar_placa(self, placa):
        if self.street_vazia():
            return False

        else:
            if placa in self.valores:
                for i in range(self.ultimo_carro + 1):
                    if placa == self.valores[i]:
                        global posicao_carro
                        posicao_carro = i
                        break

                carros_retirar = self.ultimo_carro - posicao_carro
                print(
                    f"É necessário retirar {carros_retirar} carro(s) para o veículo de placa {placa} sair!")
                return True
            else:
                return False


if __name__ == "__main__":
    c = Street(5)
    c.estacionar(5987)
    c.estacionar(5678)
    c.estacionar(4343)
    c.estacionar(2356)
    c.estacionar(6547)
    print(c.verificar_placa(4343))
