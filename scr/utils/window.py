import tkinter as tk
from tkinter.font import Font
from scr.data import classes
from scr.data import configs

class window:
    def __init__(self):
        self.flap = 0
        self.currentclass_ = classes.classes[0]
        self.currentclassidx_ = 0

        self.classe_but = 0

    def setwindow(self):
        self.flap = tk.Tk()
        icon = tk.PhotoImage(file=r'scr/images/icon.png')

        self.flap.iconphoto(True, icon)
        self.flap.geometry('690x480')
        self.flap.configure(background='black')
        self.flap.resizable(False, False)
        return self.flap

    def defCreatorFlap(self):
        current = 0

        self.flap.title('Personalize seu personagem')

        title_lab = tk.Label(text='MENU DE CRIAÇÃO',
                             font=Font(family='Arial', size=25),
                             fg='white',
                             bg='black',
                             relief='raised',
                             bd=10,
                             padx=10,
                             pady=10
                             )
        title_lab.pack(pady=30)

        name_lab = tk.Label(text='Nome:')
        name_lab.pack(pady=10)
        name_entry = tk.Entry(self.flap)
        name_entry.pack()

        print(self.currentclass_)

        classe_lab = tk.Label(text='Classe:')
        classe_lab.pack(pady=10)
        self.classe_but = tk.Button(self.flap, text=classes.classes[current][0])
        self.classe_but.config(command=self.change_class)
        self.classe_but.pack(pady=10)
        self.classe_but.pack()

        dif_lab = tk.Label(text='Dificuldade:')
        dif_lab.pack(pady=10)
        dif_entry = tk.Entry(self.flap)
        dif_entry.pack()

    def change_class(self):
        if classes.classes.index(self.currentclass_) >= len(classes.classes) - 1:
            self.currentclassidx_ = 0
            self.currentclass_[0] = classes.classes[self.currentclassidx_]
        else:
            self.currentclassidx_ += 1
            self.currentclass_ = classes.classes[self.currentclassidx_]
        self.classe_but.config(text=classes.classes[self.currentclassidx_][0])
        self.classe_but.pack()

    def change_mode(self):
        if configs.difs.index(self.currentclassidx_) >= len(configs.difs) - 1:
            self.currentclassidx_ = 0
            self.currentclass_[0] = configs.difs[self.currentclassidx_]
        else:
            self.currentclassidx_ += 1
            self.currentclass_ = configs.difs[self.currentclassidx_]
        self.classe_but.config(text=configs.difs[self.currentclassidx_][0])
        self.classe_but.pack()