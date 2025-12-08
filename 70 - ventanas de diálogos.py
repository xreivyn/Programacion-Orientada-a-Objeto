import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


class Aplicacion:

    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ventana Principal")
        self.ventana1.geometry("300x200")

        self.agregar_menu()

        self.ventana1.mainloop()

    def agregar_menu(self):
        self.menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)

        self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
        self.opciones1.add_command(label="Configurar ventana", command=self.configurar)

        self.menubar1.add_cascade(label="Opciones", menu=self.opciones1)

    def configurar(self):
        dialogo = DialogoTamano(self.ventana1)
        ancho, alto = dialogo.mostrar()

        # Validamos antes de aplicar cambios
        if ancho == "" or alto == "":
            mb.showerror("Error", "Debe ingresar ambos valores.")
            return

        if not ancho.isdigit() or not alto.isdigit():
            mb.showerror("Error", "Solo se aceptan números enteros.")
            return

        self.ventana1.geometry(ancho + "x" + alto)


class DialogoTamano:

    def __init__(self, ventanaprincipal):
        self.dialogo = tk.Toplevel(ventanaprincipal)
        self.dialogo.title("Configurar Tamaño")

        ttk.Label(self.dialogo, text="Ancho:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.dialogo, text="Alto:").grid(row=1, column=0, padx=5, pady=5)

        self.dato1 = tk.StringVar()
        self.entry1 = ttk.Entry(self.dialogo, textvariable=self.dato1)
        self.entry1.grid(row=0, column=1)
        self.entry1.focus()

        self.dato2 = tk.StringVar()
        self.entry2 = ttk.Entry(self.dialogo, textvariable=self.dato2)
        self.entry2.grid(row=1, column=1)

        btn = ttk.Button(self.dialogo, text="Confirmar", command=self.confirmar)
        btn.grid(row=2, column=1, pady=10)

        # Evita interacción con la ventana principal
        self.dialogo.grab_set()
        self.dialogo.protocol("WM_DELETE_WINDOW", self.confirmar)

    def mostrar(self):
        self.dialogo.wait_window()
        return (self.dato1.get(), self.dato2.get())

    def confirmar(self):
        self.dialogo.destroy()


aplicacion1 = Aplicacion()
