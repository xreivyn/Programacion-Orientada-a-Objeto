class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


class Coche:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad

    def aumentar_velocidad(self, incremento):
        self.velocidad += incremento
        print(f"Velocidad actual: {self.velocidad}")


class CuentaBancaria:
    def __init__(self, titular, balance):
        self.titular = titular
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Nuevo balance: {self.balance}")

    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("Fondos insuficientes:")
        else:
            self.balance -= cantidad
            print(f"Nuevo balance: {self.balance}")


class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def calcular_promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0


if __name__ == "__main__":
    # Ejemplo de uso
    usuario1 = Usuario("Juan", 30)
    usuario1.mostrar_datos()

    rectangulo1 = Rectangulo(5, 10)
    area1 = rectangulo1.calcular_area()
    print(f"El área del rectángulo es: {area1}")

    coche1 = Coche("Toyota", 60)
    coche1.aumentar_velocidad(20)

    cuenta1 = CuentaBancaria("Ana", 1000)
    cuenta1.depositar(500)
    cuenta1.retirar(200)
    cuenta1.retirar(2000)

    estudiante1 = Estudiante("Carlos", [85, 90, 78, 92])
    promedio1 = estudiante1.calcular_promedio()
    print(f"El promedio de {estudiante1.nombre} es: {promedio1}")
                                 