from scr.models.personagemBASE import personagem

class artilheiro(personagem):
    def __init__(self):
        super().__init__()
        self.__forca = 9
        self.__resistencia = 6
        self.__vigor = 4
        self.__agilidade = 3