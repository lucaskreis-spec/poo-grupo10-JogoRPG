import tkinter as tk
from tkinter.font import Font

class window:
    def setwindow():
        flap = tk.Tk()
        icon = tk.PhotoImage(file=r'scr/images/icon.png')

        flap.iconphoto(True, icon)
        flap.geometry('690x480')
        flap.configure(background='black')
        flap.resizable(False, False)
        return flap

    def defCreatorFlap(flap):
        flap.title('Personalize seu personagem')

        title_lab = tk.Label(text='Personalize seu personagem', font=Font(size=20 ,family='Arial'))
        title_lab.pack(pady=30, side=tk.TOP)

        name_frame = tk.Frame()
        name_lab = tk.Label(text='Nome:')
        name_lab.pack(pady=10)
        name_entry = tk.Entry(flap)
        name_entry.pack()

        classe_lab = tk.Label(text='Classe:')
        classe_lab.pack(pady=10)
        classe_entry = tk.Entry(flap)
        classe_entry.pack()

        dif_lab = tk.Label(text='Dificuldade:')
        dif_lab.pack(pady=10)
        dif_entry = tk.Entry(flap)
        dif_entry.pack()