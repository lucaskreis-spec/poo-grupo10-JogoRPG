import tkinter as tk
from tkinter.font import Font
from scr.data import classes
from scr.data import modes
from scr.data import playerdata

class window:
    def __init__(self):
        self.flap = 0

    def setwindow(self):
        self.flap = tk.Tk()
        icon = tk.PhotoImage(file=r'scr/images/icon.png')

        self.flap.iconphoto(True, icon)
        self.flap.geometry('690x480')
        self.flap.configure(background='black')
        self.flap.resizable(False, False)
        return self.flap

class menu(window):
    def __init__(self):
        super().__init__()
        self.name_entry = 0
        self.currentclass_ = classes.classes[0]
        self.currentclassidx_ = 0
        self.currentmode_ = modes.modes[0]
        self.currentmodeidx_ = 0

        self.mode_but = 0
        self.classe_but = 0

    def defCreatorFlap(self):
        current = 0

        self.flap.title('Personalize seu personagem')

        title_lab = tk.Label(text='MENU DE CRIAÇÃO',
                             font=Font(family='Arial', size=25),
                             fg='white',
                             bg='black',
                             relief='raised',
                             bd=10,
                             padx=5,
                             pady=5
                             )
        title_lab.pack(pady=15)

        name_lab = tk.Label(text='Nome:',
                            font=Font(family='Arial', size=15),
                            bg="#1c1c1c",
                            fg="#ffffff")

        name_lab.pack(pady=10)

        self.name_entry = tk.Entry(self.flap,
                              bg="#1c1c1c",
                              fg="#ffffff")
        self.name_entry.pack()

        classe_lab = tk.Label(text='Classe:',
                              font=Font(family='Arial', size=15),
                              bg="#1c1c1c",
                              fg="#ffffff")

        classe_lab.pack(pady=10)
        self.classe_but = tk.Button(self.flap,text=classes.classes[current][0],
                                    bg="#1c1c1c",
                                    fg="#ffffff")

        self.classe_but.config(command=self.change_class)
        self.classe_but.pack(pady=10)
        self.classe_but.pack()

        dif_lab = tk.Label(text='Dificuldade:',
                           font=Font(family='Arial', size=15),
                           bg="#1c1c1c",
                           fg="#ffffff")

        dif_lab.pack(pady=10)
        self.mode_but = tk.Button(self.flap,
                                  text=modes.modes[current][0],
                                  bg="#1c1c1c",
                                  fg="#ffffff")
        self.mode_but.config(command=self.change_mode)
        self.mode_but.pack(pady=10)
        self.mode_but.pack()

        criar_but = tk.Button(self.flap,
                              text='Criar',
                              font=Font(family='Arial', size=15),
                              bg="#1c1c1c",
                              fg="#ffffff")
        criar_but.config(command=self.def_data)
        criar_but.pack(pady=20)

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

        if modes.modes.index(self.currentmode_) >= len(modes.modes) - 1:
            self.currentmodeidx_ = 0
            self.currentmode_ = modes.modes[self.currentmodeidx_]
        else:
            self.currentmodeidx_ += 1
            self.currentmode_ = modes.modes[self.currentmodeidx_]
        self.mode_but.config(text=modes.modes[self.currentmodeidx_])
        self.mode_but.pack()

    def def_data(self):
        playerdata.nome = self.name_entry.get()
        playerdata.classe = classes.classes[self.currentclassidx_][0]
        playerdata.dificuldade = modes.modes[self.currentmodeidx_]
        playerdata.classe_instance = classes.classes[self.currentclassidx_][1]
        playerdata.classe_instance.nome = playerdata.nome
        playerdata.classe_instance.classe = playerdata.classe
        playerdata.classe_instance.dificuldade = playerdata.dificuldade

        self.flap.destroy()

        windowclass = status()
        windowclass.setwindow()
        windowclass.defstatusflap()
        windowclass.flap.mainloop()

class status(window):
    def __init__(self):
        super().__init__()

    def defstatusflap(self):
        self.flap.title('Seu perfil')

        title_lab = tk.Label(text='SEU PERFIL',
                             font=Font(family='Arial', size=25),
                             fg='white',
                             bg='black',
                             relief='raised',
                             bd=10,
                             padx=5,
                             pady=5
                             )
        title_lab.pack(pady=15)

        name_lab = tk.Label(text=f'nome: {playerdata.nome}',
                            font=Font(family='Arial', size=17),
                            bg="#1c1c1c",
                            fg="#ffffff")
        name_lab.pack(pady=15)

        cla_lab = tk.Label(text=f'classe: {playerdata.classe}',
                            font=Font(family=playerdata.dificuldade, size=17),
                            bg="#1c1c1c",
                            fg="#ffffff")
        cla_lab.pack(pady=15)

        dif_lab = tk.Label(text=f'dificuldade: {playerdata.dificuldade}',
                            font=Font(family=playerdata.dificuldade, size=17),
                            bg="#1c1c1c",
                            fg="#ffffff")
        dif_lab.pack(pady=15)

