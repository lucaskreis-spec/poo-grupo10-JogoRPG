from tkinter import *

from scr.models.personagem import personagem
from scr.models.ranged import ranged
from scr.models.magic import magic
from scr.models.melee import melee
from scr.models.summoner import summoner

summoner_ = summoner()

janela = Tk()
icon = PhotoImage(file=r'scr/images/icon.png')

janela.iconphoto(True, icon)
janela.title('Personalize seu personagem')
janela.geometry('690x480')
janela.configure(background='black')

#forcalabel = Label(root, text="força")
#resistencialabel = Label(root, text="resistência")
#vigotlabel = Label(root, text="vigor")
#agilidadelabel = Label(root, text="agilidade")

#forcadatalabel = Label(root, text=str(fuzileiro_.get_data()[0]))
#resistenciadatalabel = Label(root, text=str(fuzileiro_.get_data()[1]))
#vigordatalabel = Label(root, text=str(fuzileiro_.get_data()[2]))
#agilidadedatalabel = Label(root, text=str(fuzileiro_.get_data()[3]))

#forcalabel.grid(row=1, column=0)
#resistencialabel.grid(row=2, column=0)
#vigotlabel.grid(row=3, column=0)
#agilidadelabel.grid(row=4, column=0)

#forcadatalabel.grid(row=1, column=1)
#resistenciadatalabel.grid(row=2, column=1)
#vigordatalabel.grid(row=3, column=1)
#agilidadedatalabel.grid(row=4, column=1)

janela.mainloop()