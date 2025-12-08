import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Artículos")
        self.ventana.geometry("300x230")

        # -------- FRAME ARTÍCULO --------
        self.frame_articulo = ttk.LabelFrame(self.ventana, text="Articulo")
        self.frame_articulo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ttk.Label(self.frame_articulo, text="Código de artículo: ").grid(row=0, column=0, sticky="e", pady=3)
        self.codigo = ttk.Entry(self.frame_articulo, width=20)
        self.codigo.grid(row=0, column=1, pady=3)

        ttk.Label(self.frame_articulo, text="Descripción: ").grid(row=1, column=0, sticky="e", pady=3)
        self.descripcion = ttk.Entry(self.frame_articulo, width=20)
        self.descripcion.grid(row=1, column=1, pady=3)

        ttk.Label(self.frame_articulo, text="Precio: ").grid(row=2, column=0, sticky="e", pady=3)
        self.precio = ttk.Entry(self.frame_articulo, width=20)
        self.precio.grid(row=2, column=1, pady=3)

        # -------- FRAME OPERACIONES --------
        self.frame_operaciones = ttk.LabelFrame(self.ventana, text="Operaciones")
        self.frame_operaciones.grid(row=1, column=0, padx=10, pady=10)

        ttk.Button(self.frame_operaciones, text="Alta", width=10).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(self.frame_operaciones, text="Baja", width=10).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.frame_operaciones, text="Modificación", width=12).grid(row=0, column=2, padx=5, pady=5)

        self.ventana.mainloop()

Aplicacion()
