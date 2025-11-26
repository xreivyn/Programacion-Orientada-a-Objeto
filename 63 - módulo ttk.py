import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Variable global para compartir el valor entre ventanas
valor_compartido = None

class Aplicacion:
    def __init__(self):
        global valor_compartido
        self.valor=1
        self.ventana1=tk.Tk()
        self.ventana1.title("Ventana 1: Incremento")
        self.label1=ttk.Label(self.ventana1, text=self.valor)
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="red")

        self.boton1=ttk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1)

        self.boton2=ttk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)

        self.boton3=ttk.Button(self.ventana1, text="Siguiente", command=self.siguiente)
        self.boton3.grid(column=0, row=3)

        self.ventana1.mainloop()

    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)

    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)

    def siguiente(self):
        global valor_compartido
        valor_compartido = self.valor
        self.ventana1.destroy()
        AplicacionSiguiente()


class AplicacionSiguiente:
    def __init__(self):
        self.ventana2=tk.Tk()
        self.ventana2.title("Ventana 2: Validación Incremento")
        
        self.label1=ttk.Label(self.ventana2, text="Ingrese el valor del incremento de la ventana anterior:")
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        
        self.entry1=ttk.Entry(self.ventana2)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        
        self.label_resultado=ttk.Label(self.ventana2, text="", foreground="red")
        self.label_resultado.grid(column=0, row=1, columnspan=2, pady=5)
        
        self.label_credenciales=ttk.Label(self.ventana2, text="Credenciales para la siguiente ventana: juan / abc123", foreground="blue")
        self.label_credenciales.grid(column=0, row=2, columnspan=2, pady=5)
        
        self.boton_siguiente=ttk.Button(self.ventana2, text="Siguiente", command=self.siguiente)
        self.boton_siguiente.grid(column=0, row=3, columnspan=2, pady=5)
        
        self.boton_volver=ttk.Button(self.ventana2, text="Volver", command=self.volver)
        self.boton_volver.grid(column=0, row=4, columnspan=2, pady=5)
        
        self.ventana2.mainloop()
    
    def siguiente(self):
        global valor_compartido
        if self.entry1.get() == str(valor_compartido):
            self.ventana2.destroy()
            AplicacionTercera()
        else:
            self.label_resultado.config(text="¡Valor incorrecto! No puede avanzar.")
    
    def volver(self):
        self.ventana2.destroy()
        Aplicacion()


class AplicacionTercera:
    def __init__(self):
        self.ventana3=tk.Tk()
        self.ventana3.title("Ventana 3: Login")
        
        self.label1=ttk.Label(self.ventana3, text="Ingrese nombre de usuario:")
        self.label1.grid(column=0, row=0, padx=5, pady=5)
        
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana3, width=30, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        
        self.label2=ttk.Label(self.ventana3, text="Ingrese clave:")
        self.label2.grid(column=0, row=1, padx=5, pady=5)
        
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.ventana3, width=30, textvariable=self.dato2, show="*")
        self.entry2.grid(column=1, row=1, padx=5, pady=5)
        
        self.label_error=ttk.Label(self.ventana3, text="", foreground="red")
        self.label_error.grid(column=0, row=2, columnspan=2)

        self.boton1=ttk.Button(self.ventana3, text="Ingresar", command=self.ingresar)
        self.boton1.grid(column=1, row=3, pady=5)
        
        self.boton_volver=ttk.Button(self.ventana3, text="Volver", command=self.volver)
        self.boton_volver.grid(column=0, row=4, columnspan=2, pady=5)
        
        self.ventana3.mainloop()

    def ingresar(self):
        if self.dato1.get()=="juan" and self.dato2.get()=="abc123":
            self.ventana3.destroy()
            AplicacionCuarta()
        else:
            self.label_error.config(text="Usuario o clave incorrectos")
    
    def volver(self):
        self.ventana3.destroy()
        AplicacionSiguiente()


class AplicacionCuarta:
    def __init__(self):
        self.ventana4=tk.Tk()
        self.ventana4.title("Ventana 4: Género de Juan")
        
        self.label_pregunta=ttk.Label(self.ventana4, text="¿Qué género es Juan?")
        self.label_pregunta.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

        self.seleccion=tk.IntVar()
        self.radio1=ttk.Radiobutton(self.ventana4, text="Hombre", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=1)
        self.radio2=ttk.Radiobutton(self.ventana4, text="Mujer", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=1)
        
        self.label_resultado=ttk.Label(self.ventana4, text="", foreground="red")
        self.label_resultado.grid(column=0, row=2, columnspan=2, pady=5)

        self.boton_siguiente=ttk.Button(self.ventana4, text="Siguiente", command=self.siguiente)
        self.boton_siguiente.grid(column=0, row=3, columnspan=2, pady=5)
        
        self.boton_volver=ttk.Button(self.ventana4, text="Volver", command=self.volver)
        self.boton_volver.grid(column=0, row=4, columnspan=2, pady=5)
        
        self.ventana4.mainloop()

    def siguiente(self):
        if self.seleccion.get() == 1: # Hombre
            self.ventana4.destroy()
            AplicacionQuinta()
        elif self.seleccion.get() == 2: # Mujer
            self.label_resultado.config(text="Incorrecto. Juan es Hombre.")
        else:
            self.label_resultado.config(text="Debe seleccionar una opción.")

    def volver(self):
        self.ventana4.destroy()
        AplicacionTercera()


class AplicacionQuinta:
    def __init__(self):
        self.ventana5=tk.Tk()
        self.ventana5.title("Ventana 5: Lenguaje de Juan")
        
        self.label_pregunta=ttk.Label(self.ventana5, text="¿Qué lenguaje está aprendiendo Juan?")
        self.label_pregunta.grid(column=0, row=0, padx=5, pady=5)

        self.seleccion1=tk.BooleanVar()
        self.check1=ttk.Checkbutton(self.ventana5, text="Python", variable=self.seleccion1)
        self.check1.grid(column=0, row=1, sticky="w", padx=20)
        
        self.seleccion2=tk.BooleanVar()
        self.check2=ttk.Checkbutton(self.ventana5, text="C++", variable=self.seleccion2)
        self.check2.grid(column=0, row=2, sticky="w", padx=20)
        
        self.seleccion3=tk.BooleanVar()
        self.check3=ttk.Checkbutton(self.ventana5, text="Java", variable=self.seleccion3)
        self.check3.grid(column=0, row=3, sticky="w", padx=20)
        
        self.label_resultado=ttk.Label(self.ventana5, text="", foreground="red")
        self.label_resultado.grid(column=0, row=4, pady=5)

        self.boton_siguiente=ttk.Button(self.ventana5, text="Siguiente", command=self.siguiente)
        self.boton_siguiente.grid(column=0, row=5, pady=5)
        
        self.boton_volver=ttk.Button(self.ventana5, text="Volver", command=self.volver)
        self.boton_volver.grid(column=0, row=6, pady=5)
        
        self.ventana5.mainloop()

    def siguiente(self):
        # Validar que SOLO Python esté seleccionado
        if self.seleccion1.get() and not self.seleccion2.get() and not self.seleccion3.get():
            self.ventana5.destroy()
            AplicacionSexta()
        else:
            self.label_resultado.config(text="Incorrecto. Juan está aprendiendo solo Python.")

    def volver(self):
        self.ventana5.destroy()
        AplicacionCuarta()


class AplicacionSexta:
    def __init__(self):
        self.ventana6=tk.Tk()
        self.ventana6.title("Ventana 6: Frutas Favoritas")
        
        self.label1=ttk.Label(self.ventana6, text="Selecciona tus frutas favoritas:")
        self.label1.grid(column=0, row=0, padx=5, pady=5)

        self.listbox1=tk.Listbox(self.ventana6, selectmode=tk.MULTIPLE)
        self.listbox1.grid(column=0, row=1, padx=5, pady=5)
        
        frutas = ["Manzana", "Pera", "Naranja", "Sandía", "Melón", "Uva", "Fresa"]
        for fruta in frutas:
            self.listbox1.insert(tk.END, fruta)
            
        self.boton_finalizar=ttk.Button(self.ventana6, text="Finalizar", command=self.finalizar)
        self.boton_finalizar.grid(column=0, row=2, pady=5)
        
        self.label_final=ttk.Label(self.ventana6, text="", foreground="green", font=("Arial", 12, "bold"))
        self.label_final.grid(column=0, row=3, pady=10)
        
        self.boton_volver=ttk.Button(self.ventana6, text="Volver", command=self.volver)
        self.boton_volver.grid(column=0, row=4, pady=5)
        
        self.ventana6.mainloop()

    def finalizar(self):
        seleccion = self.listbox1.curselection()
        if len(seleccion) > 0:
            frutas_seleccionadas = [self.listbox1.get(i) for i in seleccion]
            mensaje = f"¡Felicidades! Has completado el recorrido.\nTus frutas: {', '.join(frutas_seleccionadas)}"
            self.label_final.config(text=mensaje)
        else:
            self.label_final.config(text="¡Felicidades! Has completado el recorrido.")

    def volver(self):
        self.ventana6.destroy()
        AplicacionQuinta()


aplicacion1=Aplicacion()
