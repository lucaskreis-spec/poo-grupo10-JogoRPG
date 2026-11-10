from scr.models.personagemBASE import personagem

class fuzileiro(personagem):
    def __init__(self):
        super().__init__()
        self.__forca = 7
        self.__resistencia = 6
        self.__vigor = 5
        self.__agilidade = 5