import tkinter as tk
from tkinter import ttk


# ----------------- VENTANA USANDO PACK -----------------
class VentanaPack:
    def __init__(self):
        self.vent = tk.Toplevel()
        self.vent.title("Ejemplo PACK")

        ttk.Button(self.vent, text="Botón 1").pack(side=tk.TOP, fill=tk.BOTH)
        ttk.Button(self.vent, text="Botón 2").pack(side=tk.TOP, fill=tk.BOTH)
        ttk.Button(self.vent, text="Botón 3").pack(side=tk.TOP, fill=tk.BOTH)
        ttk.Button(self.vent, text="Botón 4").pack(side=tk.LEFT)
        ttk.Button(self.vent, text="Botón 5").pack(side=tk.RIGHT)
        ttk.Button(self.vent, text="Botón 6").pack(side=tk.RIGHT)
        ttk.Button(self.vent, text="Botón 7").pack(side=tk.RIGHT)


# ----------------- VENTANA USANDO GRID -----------------
class VentanaGrid:
    def __init__(self):
        self.vent = tk.Toplevel()
        self.vent.title("Ejemplo GRID")

        ttk.Button(self.vent, text="Botón 1").grid(column=0, row=0)
        ttk.Button(self.vent, text="Botón 2").grid(column=1, row=0)

        ttk.Button(self.vent, text="Botón 3").grid(column=2, row=0, rowspan=2, sticky="ns")

        ttk.Button(self.vent, text="Botón 4").grid(column=0, row=1)
        ttk.Button(self.vent, text="Botón 5").grid(column=1, row=1)

        ttk.Button(self.vent, text="Botón 6").grid(column=0, row=2, columnspan=3, sticky="we")


# ----------------- VENTANA USANDO PLACE -----------------
class VentanaPlace:
    def __init__(self):
        self.vent = tk.Toplevel()
        self.vent.title("Ejemplo PLACE")
        self.vent.geometry("800x600")
        self.vent.resizable(False, False)

        ttk.Button(self.vent, text="Confirmar").place(x=680, y=550, width=90, height=30)
        ttk.Button(self.vent, text="Cancelar").place(x=580, y=550, width=90, height=30)


# ----------------- VENTANA PRINCIPAL -----------------
class AplicacionPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Demostración de Layout Managers")

        ttk.Label(self.root, text="Selecciona un Layout para visualizar:", font=("Arial", 12)).pack(pady=15)

        ttk.Button(self.root, text="Ver ejemplo PACK", command=self.abrir_pack).pack(pady=10)
        ttk.Button(self.root, text="Ver ejemplo GRID", command=self.abrir_grid).pack(pady=10)
        ttk.Button(self.root, text="Ver ejemplo PLACE", command=self.abrir_place).pack(pady=10)

        self.root.mainloop()

    def abrir_pack(self):
        VentanaPack()

    def abrir_grid(self):
        VentanaGrid()

    def abrir_place(self):
        VentanaPlace()


AplicacionPrincipal()
