import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Suma de números")

        # LabelFrame principal
        self.labelframe1 = ttk.LabelFrame(self.ventana1, text="Suma de números")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)

        self.agregar_componentes()
        self.agregar_menu()

        self.ventana1.mainloop()

    # ------------------------------
    # COMPONENTES DEL LABELFRAME
    # ------------------------------
    def agregar_componentes(self):
        self.label1 = ttk.Label(self.labelframe1, text="Ingrese primer valor:")
        self.label1.grid(column=0, row=0, padx=5, pady=5, sticky="e")

        self.dato1 = tk.StringVar()
        self.entry1 = ttk.Entry(self.labelframe1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)

        self.label2 = ttk.Label(self.labelframe1, text="Ingrese segundo valor:")
        self.label2.grid(column=0, row=1, padx=5, pady=5, sticky="e")

        self.dato2 = tk.StringVar()
        self.entry2 = ttk.Entry(self.labelframe1, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)

        self.boton1 = ttk.Button(self.labelframe1, text="Sumar", command=self.sumar)
        self.boton1.grid(column=1, row=2, padx=5, pady=5, sticky="we")

    # ------------------------------
    # MENÚ SUPERIOR
    # ------------------------------
    def agregar_menu(self):
        self.menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)

        self.opciones = tk.Menu(self.menubar1, tearoff=0)
        self.opciones.add_command(label="Acerca de...", command=self.acerca)
        self.opciones.add_command(label="Salir", command=self.salir)

        self.menubar1.add_cascade(label="Opciones", menu=self.opciones)

    # ------------------------------
    # SUMA Y VALIDACIÓN
    # ------------------------------
    def sumar(self):
        if self.dato1.get() == "" or self.dato2.get() == "":
            mb.showerror("Error", "Debe ingresar los dos valores antes de sumar.")
            return

        try:
            suma = int(self.dato1.get()) + int(self.dato2.get())
            self.ventana1.title(f"La suma es {suma}")

        except ValueError:
            mb.showwarning("Advertencia", "Los valores deben ser números enteros.")

    # ------------------------------
    # ACERCA DE...
    # ------------------------------
    def acerca(self):
        mb.showinfo("Información",
                    "Programa educativo realizado con Python y Tkinter.\n"
                    "Ejemplo de messagebox, menús y validación.")

    # ------------------------------
    # SALIR CON CONFIRMACIÓN
    # ------------------------------
    def salir(self):
        respuesta = mb.askyesno("Confirmar salida", "¿Desea cerrar el programa?")
        if respuesta:
            sys.exit()


# Ejecutar
Aplicacion()
