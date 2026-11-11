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

janela.mainloop()