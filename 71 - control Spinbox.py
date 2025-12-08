import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random

class Aplicacion:
    def __init__(self):
        # Ventana principal
        self.ventana1 = tk.Tk()
        self.ventana1.title("Sorteo de Equipaje")
        
        # Label de instrucción
        self.label1 = ttk.Label(self.ventana1, text="Seleccione la cantidad de bultos:")
        self.label1.grid(column=0, row=0, padx=10, pady=10)
        
        # Spinbox para seleccionar bultos
        self.spinbox1 = ttk.Spinbox(self.ventana1, from_=0, to=100, width=10, state='readonly')
        self.spinbox1.set(0)        
        self.spinbox1.grid(column=1, row=0, padx=10, pady=10)
        
        # Botón para sortear
        self.boton1 = ttk.Button(self.ventana1, text="Sortear", command=self.sortear)
        self.boton1.grid(column=0, row=1, padx=10, pady=10)
        
        # Label para mostrar el resultado
        self.label2 = ttk.Label(self.ventana1, text="", width=20, anchor="center")
        self.label2.grid(column=1, row=1, padx=10, pady=10)
        
        self.ventana1.mainloop()

    def sortear(self):
        bultos = int(self.spinbox1.get())
        if bultos == 0:
            mb.showerror("Cuidado", "Debe seleccionar un valor distinto a cero en bultos")
        else:
            # Generar un valor aleatorio entre 1 y 3
            valor = random.randint(1, 3)
            if valor == 1:
                self.label2.configure(text="Se deben revisar", background="red", foreground="white")
            else:
                self.label2.configure(text="No se revisan", background="green", foreground="white")

# Crear la aplicación
aplicacion1 = Aplicacion()
