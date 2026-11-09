class personagem:
    def __init__(self, forca, resistencia, vigor, agilidade):
        self.forca = forca
        self.resistencia = resistencia
        self.vigor = vigor
        self.agilidade = agilidade

    def info(self):
        print("======= INFO PERSONAGEM =======")
        print(f"| Força: {self.forca} pontos |\n"
              f"| Resistência: {self.resistencia} pontos |\n"
              f"| Vigor: {self.vigor} pontos |\n"
              f"| Agilidade: {self.agilidade} pontos |\n")

personagem1 = personagem(1, 2, 3, 4)
personagem1.info()