from tkinter import *

from scr.models.personagemBASE import personagem
from scr.models.fuzileiro import fuzileiro
from scr.models.medico import medico
from scr.models.artilheiro import artilheiro
from scr.models.oficial import oficial

fuzileiro_ = fuzileiro()

root = Tk()

forcalabel = Label(root, text="força")
resistencialabel = Label(root, text="resistência")
vigotlabel = Label(root, text="vigor")
agilidadelabel = Label(root, text="agilidade")

forcadatalabel = Label(root, text=str(fuzileiro_.get_data()[0]))
resistenciadatalabel = Label(root, text=str(fuzileiro_.get_data()[1]))
vigordatalabel = Label(root, text=str(fuzileiro_.get_data()[2]))
agilidadedatalabel = Label(root, text=str(fuzileiro_.get_data()[3]))

forcalabel.grid(row=1, column=0)
resistencialabel.grid(row=2, column=0)
vigotlabel.grid(row=3, column=0)
agilidadelabel.grid(row=4, column=0)

forcadatalabel.grid(row=1, column=1)
resistenciadatalabel.grid(row=2, column=1)
vigordatalabel.grid(row=3, column=1)
agilidadedatalabel.grid(row=4, column=1)

root.mainloop()