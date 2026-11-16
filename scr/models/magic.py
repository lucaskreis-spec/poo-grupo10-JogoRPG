from scr.models.personagem import personagem
import random

class Magic(personagem):
    def __init__(self, chancritesp, chancritnor):
        super().__init__()
        self.chancritesp = 0.30
        self.chancritnor = 0.20

    def ataca(self, alvo):
        sorteio = random.random()
        if sorteio < self.chancritnor:
            self.__multdano = self.__multdano * self.__multcrit
        print(f"{self.nome} ataca {alvo.nome}, causando {self.__multdano} de dano!")
        alvo.recebe_dano(self.__multdano)