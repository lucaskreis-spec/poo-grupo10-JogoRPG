from scr.models.personagemBASE import personagem

class oficial(personagem):
    def __init__(self):
        super().__init__()
        self.__forca = 5
        self.__resistencia = 4
        self.__vigor = 8
        self.__agilidade = 7