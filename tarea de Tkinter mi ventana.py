import tkinter as tk
from tkinter import ttk, colorchooser

# ---------------------------
# Ventana principal
# ---------------------------
ventana = tk.Tk()
ventana.title("Aplicación Tkinter Mejorada")
ventana.geometry("900x600")
ventana.configure(bg="#e9eef1")  # Fondo suave


# ---------------------------
# Estilos
# ---------------------------
style = ttk.Style()
style.configure("TNotebook.Tab", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("Title.TLabel", font=("Arial", 18, "bold"), background="#e9eef1")
style.configure("Text.TLabel", font=("Arial", 14), background="#e9eef1")


# ---------------------------
# Menú Superior
# ---------------------------
def salir():
    ventana.quit()

def elegir_color():
    global color_dibujo
    color_dibujo = colorchooser.askcolor()[1]

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Elegir color del pincel", command=elegir_color)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
barra_menu.add_cascade(label="Opciones", menu=menu_archivo)


# ---------------------------
# Notebook (pestañas)
# ---------------------------
notebook = ttk.Notebook(ventana)
notebook.pack(fill="both", expand=True)


# ------------------------------------------------
# 1. Bienvenida
# ------------------------------------------------
tab1 = tk.Frame(notebook, bg="#e9eef1")
notebook.add(tab1, text="Bienvenida")

ttk.Label(tab1, text="¡Bienvenido a la aplicación Tkinter Mejorada!", 
         style="Title.TLabel").pack(pady=80)


# ------------------------------------------------
# 2. Mostrar texto
# ------------------------------------------------
tab2 = tk.Frame(notebook, bg="#e9eef1")
notebook.add(tab2, text="Mostrar Texto")

ttk.Label(tab2, text="Escribe un mensaje:", style="Text.TLabel").pack(pady=10)

entrada_texto = tk.Entry(tab2, font=("Arial", 14), width=40)
entrada_texto.pack()

def mostrar_texto():
    texto = entrada_texto.get()
    label_muestra.config(text=f"Escribiste: {texto}")

ttk.Button(tab2, text="Mostrar", command=mostrar_texto).pack(pady=10)

label_muestra = ttk.Label(tab2, text="", style="Text.TLabel")
label_muestra.pack()


# ------------------------------------------------
# 3. Calculadora
# ------------------------------------------------
tab3 = tk.Frame(notebook, bg="#e9eef1")
notebook.add(tab3, text="Calculadora")

ttk.Label(tab3, text="Número 1:", style="Text.TLabel").pack()
num1 = tk.Entry(tab3, font=("Arial", 14))
num1.pack()

ttk.Label(tab3, text="Número 2:", style="Text.TLabel").pack()
num2 = tk.Entry(tab3, font=("Arial", 14))
num2.pack()

def sumar():
    try:
        n1 = float(num1.get())
        n2 = float(num2.get())
        label_resultado.config(text=f"Resultado: {n1 + n2}")
    except ValueError:
        label_resultado.config(text="❌ Introduce números válidos")

ttk.Button(tab3, text="Sumar", command=sumar).pack(pady=10)

label_resultado = ttk.Label(tab3, text="", style="Title.TLabel")
label_resultado.pack()


# ------------------------------------------------
# 4. Lista de Elementos
# ------------------------------------------------
tab4 = tk.Frame(notebook, bg="#e9eef1")
notebook.add(tab4, text="Lista")

lista = tk.Listbox(tab4, font=("Arial", 14), width=40, height=10)
lista.pack(pady=10)

entrada_lista = tk.Entry(tab4, font=("Arial", 14))
entrada_lista.pack()

def agregar_elemento():
    elemento = entrada_lista.get()
    if elemento:
        lista.insert(tk.END, elemento)
        entrada_lista.delete(0, tk.END)

ttk.Button(tab4, text="Agregar Elemento", command=agregar_elemento).pack(pady=10)


# ------------------------------------------------
# 5. Canvas para dibujar
# ------------------------------------------------
tab5 = tk.Frame(notebook, bg="#e9eef1")
notebook.add(tab5, text="Dibujar")

color_dibujo = "black"

canvas = tk.Canvas(tab5, bg="white", width=800, height=500)
canvas.pack(pady=20)

def dibujar(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x+3, y+3, fill=color_dibujo, outline=color_dibujo)

canvas.bind("<B1-Motion>", dibujar)


# ---------------------------
# Ejecutar la app
# ---------------------------
ventana.mainloop()
