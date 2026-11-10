class personagem:
    def __init__(self):
        self.__classe = "base"
        self.__forca = 0
        self.__resistencia = 0
        self.__vigor = 0
        self.__agilidade = 0

    def __str__(self):
        print(f"======= INFO {(self.__classe).upper()} =======")
        print(f"| Força: {self.__forca} pontos |\n"
              f"| Resistência: {self.__resistencia} pontos |\n"
              f"| Vigor: {self.__vigor} pontos |\n"
              f"| Agilidade: {self.__agilidade} pontos |\n")

    def get_data(self):
        return self.__forca, self.__resistencia, self.__vigor, self.__agilidade
