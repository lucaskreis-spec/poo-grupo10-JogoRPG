from scr.models.personagem import personagem
import random

class Ranged(personagem):
    def __init__(self, chancritesp, chancritnor):
        super().__init__()
        self.__chancritesp = 0.10
        self.__chancritnor = 0.30

    def ataque(self, alvo):
        sorteio = random.random()
        if sorteio < self.__chancritnor:
            self.__multdano = self.__multdano * self.__multcrit
        print(f"{self.nome} ataca {alvo.nome}, causando {self.__multdano} de dano!")
        alvo.receber_dano(self.__multdano)

    def ataque_esp(self, alvo):
        sorteio = random.random()
        if sorteio < self.__chancritesp:
            self.__multdano = (self.__multdano * 1.5) * self.__multcrit
            print(f"{self.nome} usa Rajada, causando {self.__multdano} de dano!")
            alvo.receber_dano(self.__multdano)
