# ============================================
# 1. Clase Animal con Perro y Gato
# ============================================

class Animal:
    def hablar(self):
        return "El animal hace un sonido."

class Perro(Animal):
    def hablar(self):
        return "El perro dice: ¡Guau!"

class Gato(Animal):
    def hablar(self):
        return "El gato dice: ¡Miau!"


# ============================================
# 2. Clase Empleado con Gerente y Técnico
# ============================================

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bono(self):
        return 0  # se sobrescribe en clases hijas


class Gerente(Empleado):
    def calcular_bono(self):
        return self.salario * 0.20  # 20%


class Tecnico(Empleado):
    def calcular_bono(self):
        return self.salario * 0.10  # 10%


# ============================================
# 3. Clase Figura con Círculo y Cuadrado
# ============================================

class Figura:
    def area(self):
        return 0  # se sobrescribe


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio ** 2)


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


# ============================================
# 4. Clase Vehículo con Carro y Bicicleta
# ============================================

class Vehiculo:
    def mover(self):
        return "El vehículo se está moviendo."


class Carro(Vehiculo):
    def mover(self):
        return "El carro avanza por la carretera."


class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta se mueve pedaleando."


# ============================================
# 5. Clase Dispositivo con Laptop y Teléfono
# ============================================

class Dispositivo:
    def encender(self):
        return "El dispositivo está encendiendo."


class Laptop(Dispositivo):
    def encender(self):
        return "La laptop está iniciando el sistema."


class Telefono(Dispositivo):
    def encender(self):
        return "El teléfono está encendiendo y mostrando el logo."


# ============================================
# PRUEBAS (Opcionales, pero útiles para ver funcionamiento)
# ============================================

if __name__ == "__main__":
    # Animal
    print(Perro().hablar())
    print(Gato().hablar())

    # Empleados
    gerente = Gerente("Carlos", 50000)
    tecnico = Tecnico("Ana", 30000)
    print(f"Bono Gerente: {gerente.calcular_bono()}")
    print(f"Bono Técnico: {tecnico.calcular_bono()}")

    # Figuras
    print(f"Área del círculo: {Circulo(5).area()}")
    print(f"Área del cuadrado: {Cuadrado(4).area()}")

    # Vehículos
    print(Carro().mover())
    print(Bicicleta().mover())

    # Dispositivos
    print(Laptop().encender())
    print(Telefono().encender())
