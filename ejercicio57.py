import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1= tk.Tk()
        self.ventana1.title("Mi primera ventana")
        self.ventana1.geometry("400x300")
        self.ventana1.mainloop()


app= Aplicacion()

