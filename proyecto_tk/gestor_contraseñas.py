# gestor_contraseñas.py
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import bcrypt
import random
import string
import datetime

# -------------------------
# CONFIGURACIÓN CONEXIÓN MySQL
# -------------------------
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "passwd": "",
    "database": "bd_passwords"
}

# -------------------------
# LISTA CORTA DE CONTRASEÑAS COMUNES (ejemplo)
# -------------------------
COMMON_PASSWORDS = {
    "123456","password","12345678","qwerty","abc123","111111","123456789",
    "12345","1234","1234567","dragon","iloveyou","monkey","letmein"
}

# -------------------------
# Clase para la base de datos
# -------------------------
class UsuariosDB:
    def __init__(self):
        self.conexion = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conexion.cursor()

    def registrar_usuario(self, username, password_hash):
        sql = "INSERT INTO usuarios (username, password_hash) VALUES (%s, %s)"
        try:
            self.cursor.execute(sql, (username, password_hash))
            self.conexion.commit()
            return True, None
        except mysql.connector.IntegrityError as e:
            return False, "El nombre de usuario ya existe"
        except Exception as e:
            return False, str(e)

    def obtener_usuario(self, username):
        sql = "SELECT id, username, password_hash, created_at FROM usuarios WHERE username=%s"
        self.cursor.execute(sql, (username,))
        return self.cursor.fetchone()

    def listar_usuarios(self):
        sql = "SELECT id, username, created_at FROM usuarios ORDER BY created_at DESC"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

# -------------------------
# Funciones de seguridad
# -------------------------
def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def check_password(password: str, password_hash: bytes) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), password_hash)

def verificar_contrasena(password: str):
    """Devuelve (puntuacion, lista_de_alertas)"""
    alerts = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        alerts.append("Menos de 8 caracteres")

    if any(c.islower() for c in password):
        score += 1
    else:
        alerts.append("No contiene minúscula")

    if any(c.isupper() for c in password):
        score += 1
    else:
        alerts.append("No contiene mayúscula")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        alerts.append("No contiene dígito")

    special = set(string.punctuation)
    if any(c in special for c in password):
        score += 1
    else:
        alerts.append("No contiene carácter especial")

    # bonus por longitud >= 12
    if len(password) >= 12:
        score += 1

    # check common passwords (lowercase)
    if password.lower() in COMMON_PASSWORDS:
        alerts.append("Contraseña demasiado común")
        # penalizar ligeramente
        score = max(0, score-2)

    return score, alerts

def nivel_from_score(score: int):
    if score <= 2:
        return "Débil"
    if score <= 4:
        return "Media"
    return "Fuerte"

def generar_contrasena(longitud=12):
    if longitud < 6:
        longitud = 6
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        pwd = ''.join(random.choice(chars) for _ in range(longitud))
        score, alerts = verificar_contrasena(pwd)
        if score >= 4:
            return pwd

# -------------------------
# Interfaz gráfica
# -------------------------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Contraseñas Seguras")
        self.db = UsuariosDB()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=8, pady=8)

        self.tab_registrar = ttk.Frame(self.notebook)
        self.tab_check = ttk.Frame(self.notebook)
        self.tab_listar = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_registrar, text="Registrar Usuario")
        self.notebook.add(self.tab_check, text="Verificar / Generar")
        self.notebook.add(self.tab_listar, text="Listado de Usuarios")

        self.build_registrar()
        self.build_check()
        self.build_listar()

    # ---------- Registro ----------
    def build_registrar(self):
        frm = self.tab_registrar
        ttk.Label(frm, text="Usuario:").grid(row=0, column=0, pady=6, sticky="e")
        self.entry_user = ttk.Entry(frm, width=30)
        self.entry_user.grid(row=0, column=1, pady=6)

        ttk.Label(frm, text="Contraseña:").grid(row=1, column=0, pady=6, sticky="e")
        self.entry_pwd = ttk.Entry(frm, width=30, show="*")
        self.entry_pwd.grid(row=1, column=1, pady=6)

        btn = ttk.Button(frm, text="Registrar", command=self.registrar)
        btn.grid(row=2, column=1, pady=8, sticky="w")

        ttk.Button(frm, text="Generar segura (12)", command=self.llenar_contrasena_generada)\
            .grid(row=2, column=1, sticky="e")

        self.lbl_result_reg = ttk.Label(frm, text="", foreground="green")
        self.lbl_result_reg.grid(row=3, column=0, columnspan=2)

    def llenar_contrasena_generada(self):
        pwd = generar_contrasena(12)
        self.entry_pwd.delete(0, tk.END)
        self.entry_pwd.insert(0, pwd)
        messagebox.showinfo("Contraseña generada", "Se ha generado una contraseña segura y fue colocada en el campo.")

    def registrar(self):
        user = self.entry_user.get().strip()
        pwd = self.entry_pwd.get()

        if not user or not pwd:
            messagebox.showerror("Error", "Completa usuario y contraseña")
            return

        score, alerts = verificar_contrasena(pwd)
        nivel = nivel_from_score(score)
        if nivel == "Débil":
            if not messagebox.askyesno("Contraseña débil",
                                       "La contraseña es débil. ¿Deseas registrarla igual?"):
                return

        hashed = hash_password(pwd)
        ok, err = self.db.registrar_usuario(user, hashed.decode('utf-8') if isinstance(hashed, bytes) else hashed)
        if ok:
            self.lbl_result_reg.config(text="Usuario registrado correctamente")
            self.entry_user.delete(0, tk.END)
            self.entry_pwd.delete(0, tk.END)
            self.refresh_list()
        else:
            messagebox.showerror("Error al registrar", err or "Error desconocido")

    # ---------- Verificación / Generador ----------
    def build_check(self):
        frm = self.tab_check
        ttk.Label(frm, text="Contraseña a verificar:").grid(row=0, column=0, pady=6)
        self.entry_check = ttk.Entry(frm, width=40, show="*")
        self.entry_check.grid(row=0, column=1, pady=6)

        ttk.Button(frm, text="Verificar", command=self.verificar).grid(row=1, column=1, sticky="w")
        ttk.Button(frm, text="Generar contraseña segura", command=self.generar_y_mostrar).grid(row=1, column=1, sticky="e")

        self.txt_alerts = tk.Text(frm, width=60, height=10)
        self.txt_alerts.grid(row=2, column=0, columnspan=2, pady=8)

    def verificar(self):
        pwd = self.entry_check.get()
        if not pwd:
            messagebox.showerror("Error", "Ingresa una contraseña")
            return
        score, alerts = verificar_contrasena(pwd)
        nivel = nivel_from_score(score)
        self.txt_alerts.delete("1.0", tk.END)
        self.txt_alerts.insert(tk.END, f"Nivel: {nivel}\nPuntuación: {score}\n")
        if alerts:
            self.txt_alerts.insert(tk.END, "Alertas:\n- " + "\n- ".join(alerts))
        else:
            self.txt_alerts.insert(tk.END, "No se encontraron problemas. ✅")

    def generar_y_mostrar(self):
        pwd = generar_contrasena(14)
        self.entry_check.delete(0, tk.END)
        self.entry_check.insert(0, pwd)
        messagebox.showinfo("Generada", "Se generó una contraseña segura y fue colocada en el campo.")

    # ---------- Listado ----------
    def build_listar(self):
        frm = self.tab_listar
        ttk.Button(frm, text="Actualizar lista", command=self.refresh_list).pack(pady=6)
        self.tree = ttk.Treeview(frm, columns=("id","user","created"), show="headings", height=10)
        self.tree.heading("id", text="ID")
        self.tree.heading("user", text="Usuario")
        self.tree.heading("created", text="Creado")
        self.tree.column("id", width=40)
        self.tree.column("user", width=180)
        self.tree.column("created", width=160)
        self.tree.pack(padx=6, pady=6)
        self.refresh_list()

    def refresh_list(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        filas = self.db.listar_usuarios()
        for fila in filas:
            id_, user, created = fila
            if isinstance(created, (datetime.datetime,)):
                created = created.strftime("%Y-%m-%d %H:%M:%S")
            self.tree.insert("", tk.END, values=(id_, user, created))

# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
