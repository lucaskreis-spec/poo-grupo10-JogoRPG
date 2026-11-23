class personagem:
    def __init__(self):
        self.nome = "null"
        self.classe = "null"
        self.dificuldade = "null"

        self.__multdano = 15
        self.__multvida = 100
        self.__multdefesa = 0
        self.__multcrit = 2
        self.__multdanodif = 1

    @property
    def multvida(self) -> int:
        return self.__multvida

    @property
    def dificuldade(self) -> str:
        return self.dificuldade

    @dificuldade.setter
    def dificuldade(self, valor):
        if self.dificuldade == "normal":
            self.__multdanodif = 1
        elif self.dificuldade == "difícil":
            self.__multdanodif = 1.33
        else:
            print("Dificuldade invalida! Selecione uma dificuldade.")

    @multvida.setter
    def multvida(self, valor: int) -> None:
        self.__multvida = max(0, min(valor, self.__multvida))

    def ataque_comum(personagem):
        personagem.ataque_comum()

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

    def __str__(self):
        return f"{self.nome} {self.classe} {self.__multvida, self.__multdefesa, self.__multdano, self.__multcrit}"

