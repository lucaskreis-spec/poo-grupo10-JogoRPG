class personagem:
    def __init__(self):
        self.nome = "null"
        self.classe = "null"
        self.dificuldade = "null"

        self.__multdano = 0
        self.__multvida = 0
        self.__multdefesa = 0
        self.__multcrit = 2

    def ataque_comum(personagem):
        personagem.ataque()

    def ataque_especial(personagem):
        personagem.ataque_especial()


    def receber_dano(self, dano):
        self.__multvida -= self.__multdano
        if self.__multvida <= 0:
            self.__multvida = 0
            print(f"{self.nome} foi morto!")
        else:
            print(f"Vida restante de{self.nome}: {self.__multvida}")

    def vivo(self):
        return self.__multvida > 0


