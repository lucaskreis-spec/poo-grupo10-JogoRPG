class personagem:
    def __init__(self, nome, classe, dificuldade):
        self.nome = nome
        self.classe = classe
        self.dificuldade = dificuldade

        self.__multdano = 0
        self.__multvida = 0
        self.__multdefesa = 0
        self.__multcrit = 2

    def ataca(self, alvo):
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


