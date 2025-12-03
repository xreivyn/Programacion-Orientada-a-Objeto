import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# -------------------------
# Clase para manejar MySQL
# -------------------------
class ArticulosBD:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="bd1"
        )
        self.cursor = self.conexion.cursor()

    def insertar(self, descripcion, precio):
        sql = "INSERT INTO articulos (descripcion, precio) VALUES (%s, %s)"
        datos = (descripcion, precio)
        self.cursor.execute(sql, datos)
        self.conexion.commit()

    def consultar_codigo(self, codigo):
        sql = "SELECT descripcion, precio FROM articulos WHERE codigo=%s"
        self.cursor.execute(sql, (codigo,))
        return self.cursor.fetchone()

    def listar_todos(self):
        self.cursor.execute("SELECT codigo, descripcion, precio FROM articulos")
        return self.cursor.fetchall()


# -------------------------
# Interfaz gráfica Tkinter
# -------------------------
class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mantenimiento de artículos")

        self.bd = ArticulosBD()

        # Creamos las pestañas
        self.notebook = ttk.Notebook(self.ventana)
        self.notebook.pack(fill="both", expand=True)

        self.tab_carga = ttk.Frame(self.notebook)
        self.tab_consulta = ttk.Frame(self.notebook)
        self.tab_listado = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_carga, text="Carga de artículos")
        self.notebook.add(self.tab_consulta, text="Consulta por código")
        self.notebook.add(self.tab_listado, text="Listado completo")

        self.pestana_carga()
        self.pestana_consulta()
        self.pestana_listado()

    # ---------------------------
    # PESTAÑA: Carga de artículos
    # ---------------------------
    def pestana_carga(self):
        ttk.Label(self.tab_carga, text="Descripción:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        ttk.Label(self.tab_carga, text="Precio:").grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.descripcion = tk.Entry(self.tab_carga, width=30)
        self.precio = tk.Entry(self.tab_carga, width=30)

        self.descripcion.grid(row=0, column=1)
        self.precio.grid(row=1, column=1)

        ttk.Button(self.tab_carga, text="Confirmar", command=self.guardar_articulo)\
            .grid(row=2, column=1, pady=10)

    def guardar_articulo(self):
        desc = self.descripcion.get()
        precio = self.precio.get()

        if desc == "" or precio == "":
            messagebox.showerror("Error", "Completa todos los campos")
            return

        try:
            self.bd.insertar(desc, float(precio))
            messagebox.showinfo("Éxito", "Artículo cargado")
            self.descripcion.delete(0, tk.END)
            self.precio.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Ocurrió un problema al insertar")

    # -------------------------------
    # PESTAÑA: Consulta por código
    # -------------------------------
    def pestana_consulta(self):
        ttk.Label(self.tab_consulta, text="Código:").grid(row=0, column=0, padx=10, pady=10)

        self.cod_buscar = tk.Entry(self.tab_consulta, width=20)
        self.cod_buscar.grid(row=0, column=1, pady=10)

        ttk.Button(self.tab_consulta, text="Consultar", command=self.buscar_articulo)\
            .grid(row=1, column=1)

        ttk.Label(self.tab_consulta, text="Descripción:").grid(row=2, column=0)
        ttk.Label(self.tab_consulta, text="Precio:").grid(row=3, column=0)

        self.res_desc = tk.Entry(self.tab_consulta, width=30)
        self.res_precio = tk.Entry(self.tab_consulta, width=30)

        self.res_desc.grid(row=2, column=1)
        self.res_precio.grid(row=3, column=1)

    def buscar_articulo(self):
        codigo = self.cod_buscar.get()

        if codigo == "":
            messagebox.showerror("Error", "Ingresa un código")
            return

        datos = self.bd.consultar_codigo(codigo)

        if datos:
            self.res_desc.delete(0, tk.END)
            self.res_precio.delete(0, tk.END)

            self.res_desc.insert(0, datos[0])
            self.res_precio.insert(0, datos[1])
        else:
            messagebox.showinfo("No encontrado", "No existe un artículo con ese código")

    # -------------------------------
    # PESTAÑA: Listado completo
    # -------------------------------
    def pestana_listado(self):
        ttk.Button(self.tab_listado, text="Listado completo", command=self.listar)\
            .pack(pady=10)

        self.caja = tk.Text(self.tab_listado, width=50, height=15)
        self.caja.pack()

    def listar(self):
        self.caja.delete("1.0", tk.END)
        datos = self.bd.listar_todos()

        for fila in datos:
            self.caja.insert(tk.END, f"Código: {fila[0]} - {fila[1]} - ${fila[2]}\n")


# Ejecutar App
ventana = tk.Tk()
app = App(ventana)
ventana.mainloop()
