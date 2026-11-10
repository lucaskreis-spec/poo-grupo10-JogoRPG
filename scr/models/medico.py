from scr.models.personagemBASE import personagem

class medico(personagem):
    def __init__(self):
        super().__init__()
        self.__forca = 5
        self.__resistencia = 3
        self.__vigor = 7
        self.__agilidade = 8