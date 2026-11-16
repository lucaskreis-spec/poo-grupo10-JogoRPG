from scr.models.personagem import personagem

class Inimigo(personagem):
    def __init__(self, multcrit):
        super().__init__()
        self.__multcrit = multcrit

    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome}, causando {self.__multdano} de dano!")
        alvo.recebe_dano(self.__multdano)

    def receber_dano(self, dano):
        self.__multvida -= self.__multdano
        if self.__multvida <= 0:
            self.__multvida = 0
            print(f"{self.nome} foi morto!")
        else:
            print(f"Vida restante de{self.nome}: {self.__multvida}")

    def vivo(self):
        return self.__multvida > 0