from scr.models.personagem import personagem
import random

class Magic(personagem):
    def __init__(self, chancritesp, chancritnor):
        super().__init__()
        self.__chancritesp = 0.30
        self.__chancritnor = 0.20

    def ataque(self, alvo):
        sorteio = random.random()
        if sorteio < self.__chancritnor:
            self.__multdano = self.__multdano * self.__multcrit
        print(f"{self.nome} ataca {alvo.nome}, causando {self.__multdano} de dano!")
        alvo.recebe_dano(self.__multdano)

    def ataque_esp(self, alvo):
        sorteio = random.random()
        if sorteio < self.__chancritesp:
            self.__multdano = (self.__multdano * 1.5) * self.__multcrit
            print(f"{self.nome} usa Bola de Fogo, causando {self.__multdano} de dano!")

