from tkinter import *
from scr.utils.window import menu

from scr.models.personagem import personagem
from scr.models.ranged import Ranged
from scr.models.magic import Magic
from scr.models.melee import Melee
from scr.models.summoner import Summoner

windowclass = menu()
windowclass.setwindow()
windowclass.defCreatorFlap()
windowclass.flap.mainloop()