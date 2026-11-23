from scr.models.personagem import personagem
import random

class Inimigo(personagem):
    def __init__(self, multcrit):
        super().__init__()
        self.__multcrit = multcrit
        self.__chancritnor = 0.20

    def ataque(self, alvo):
        sorteio = random.random()
        if sorteio < self.__chancritnor:
            self.__multdano = (self.__multdano * self.__multcrit) * self.__multdanodif
        print(f"{self.nome} ataca {alvo.nome}, causando {self.__multdano} de dano!")
        alvo.receber_dano(self.__multdano)

    def receber_dano(self, dano):
        self.__multvida -= self.__multdano
        if self.__multvida <= 0:
            self.__multvida = 0
            print(f"{self.nome} foi morto!")
        else:
            print(f"Vida restante de{self.nome}: {self.__multvida}")

    def vivo(self):
        return self.__multvida > 0