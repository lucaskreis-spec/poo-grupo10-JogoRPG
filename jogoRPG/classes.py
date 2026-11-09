# SISTEMA DE CLASSES DE JOGO RPG DE PRIMEIRA GUERRA MUNDIAL

# CLASSE PAI ----------------------------------------------------------

class personagem:
    def __init__(self, forca, resistencia, vigor, agilidade):
        self.__classe = "base"
        self.__forca = forca
        self.__resistencia = resistencia
        self.__vigor = vigor
        self.__agilidade = agilidade

    def __str__(self):
        print(f"======= INFO {(self.__classe).upper()} =======")
        print(f"| Força: {self.__forca} pontos |\n"
              f"| Resistência: {self.__resistencia} pontos |\n"
              f"| Vigor: {self.__vigor} pontos |\n"
              f"| Agilidade: {self.__agilidade} pontos |\n")

# CLASSES FILHAS ----------------------------------------------------------

class fuzileiro:
    def __init__(self, forca, resistencia, vigor, agilidade):
        super().__init__(forca, resistencia, vigor, agilidade)

class medico:
    def __init__(self, forca, resistencia, vigor, agilidade):
        super().__init__(forca, resistencia, vigor, agilidade)

class artilheiro:
    def __init__(self, forca, resistencia, vigor, agilidade):
        super().__init__(forca, resistencia, vigor, agilidade)

class oficial:
    def __init__(self, forca, resistencia, vigor, agilidade, subordinados):
        super().__init__(forca, resistencia, vigor, agilidade)
        self.subordinados = subordinados