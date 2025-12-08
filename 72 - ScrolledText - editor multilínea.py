import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Copiar Texto entre ScrolledText")
        
        # Primer ScrolledText
        self.scrolledtext1 = st.ScrolledText(self.ventana1, width=50, height=10)
        self.scrolledtext1.grid(column=0, row=0, padx=10, pady=10)
        
        # Frame con controles para definir región a copiar
        self.framecopia()
        
        # Segundo ScrolledText
        self.scrolledtext2 = st.ScrolledText(self.ventana1, width=50, height=10)
        self.scrolledtext2.grid(column=0, row=2, padx=10, pady=10)
        
        self.ventana1.mainloop()

    def framecopia(self):
        self.labelframe1 = ttk.LabelFrame(self.ventana1, text="Región a copiar")
        self.labelframe1.grid(column=0, row=1, padx=5, pady=5, sticky="w")
        
        # Desde fila
        self.label1 = ttk.Label(self.labelframe1, text="Desde fila:")
        self.label1.grid(column=0, row=0, padx=5, pady=5, sticky="e")
        self.dato1 = tk.StringVar()
        self.entry1 = ttk.Entry(self.labelframe1, textvariable=self.dato1, width=10)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        
        # Desde columna
        self.label2 = ttk.Label(self.labelframe1, text="Desde columna:")
        self.label2.grid(column=0, row=1, padx=5, pady=5, sticky="e")
        self.dato2 = tk.StringVar()
        self.entry2 = ttk.Entry(self.labelframe1, textvariable=self.dato2, width=10)
        self.entry2.grid(column=1, row=1, padx=5, pady=5)
        
        # Hasta fila
        self.label3 = ttk.Label(self.labelframe1, text="Hasta fila:")
        self.label3.grid(column=0, row=2, padx=5, pady=5, sticky="e")
        self.dato3 = tk.StringVar()
        self.entry3 = ttk.Entry(self.labelframe1, textvariable=self.dato3, width=10)
        self.entry3.grid(column=1, row=2, padx=5, pady=5)
        
        # Hasta columna
        self.label4 = ttk.Label(self.labelframe1, text="Hasta columna:")
        self.label4.grid(column=0, row=3, padx=5, pady=5, sticky="e")
        self.dato4 = tk.StringVar()
        self.entry4 = ttk.Entry(self.labelframe1, textvariable=self.dato4, width=10)
        self.entry4.grid(column=1, row=3, padx=5, pady=5)
        
        # Botón copiar
        self.boton1 = ttk.Button(self.labelframe1, text="Copiar", command=self.copiar)
        self.boton1.grid(column=1, row=4, padx=10, pady=10)

    def copiar(self):
        try:
            # Obtener valores desde los Entry
            iniciofila = self.dato1.get()
            iniciocolumna = self.dato2.get()
            finfila = self.dato3.get()
            fincolumna = self.dato4.get()
            
            # Extraer texto del primer ScrolledText
            datos = self.scrolledtext1.get(f"{iniciofila}.{iniciocolumna}", f"{finfila}.{fincolumna}")
            
            # Limpiar y pegar en el segundo ScrolledText
            self.scrolledtext2.delete("1.0", tk.END)
            self.scrolledtext2.insert("1.0", datos)
        except tk.TclError:
            # Manejo de error si los índices son inválidos
            tk.messagebox.showerror("Error", "Valores de fila/columna inválidos")

# Ejecutar la aplicación
aplicacion1 = Aplicacion()
