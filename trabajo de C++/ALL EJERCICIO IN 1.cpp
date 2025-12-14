#include <iostream>
using namespace std;

/* ===== EJERCICIO 1 ===== */
void ejercicio1() {
    int a, b;
    cout << "Digite dos numeros enteros: ";
    cin >> a >> b;

    cout << "Suma: " << a + b << endl;
    cout << "Resta: " << a - b << endl;
    cout << "Multiplicacion: " << a * b << endl;
    cout << "Division: " << (float)a / b << endl;
}

/* ===== EJERCICIO 2 ===== */
void ejercicio2() {
    string nombre;
    int edad;
    float estatura;

    cout << "Nombre: ";
    cin >> nombre;
    cout << "Edad: ";
    cin >> edad;
    cout << "Estatura: ";
    cin >> estatura;

    cout << "\n--- FICHA ---\n";
    cout << "Nombre: " << nombre << endl;
    cout << "Edad: " << edad << endl;
    cout << "Estatura: " << estatura << endl;
}

/* ===== EJERCICIO 3 ===== */
void ejercicio3() {
    float celsius, fahrenheit;
    cout << "Digite grados Celsius: ";
    cin >> celsius;

    fahrenheit = (celsius * 9 / 5) + 32;
    cout << "Fahrenheit: " << fahrenheit << endl;
}

/* ===== EJERCICIO 4 ===== */
void ejercicio4() {
    float base, altura;
    cout << "Base: ";
    cin >> base;
    cout << "Altura: ";
    cin >> altura;

    cout << "Area del rectangulo: " << base * altura << endl;
}

/* ===== EJERCICIO 5 ===== */
struct Estudiante {
    string nombre;
    int edad;
    float promedio;
};

void ejercicio5() {
    Estudiante e[3];
    int mejor = 0;

    for (int i = 0; i < 3; i++) {
        cout << "Nombre: ";
        cin >> e[i].nombre;
        cout << "Edad: ";
        cin >> e[i].edad;
        cout << "Promedio: ";
        cin >> e[i].promedio;

        if (e[i].promedio > e[mejor].promedio)
            mejor = i;
    }

    cout << "\nMejor promedio: " << e[mejor].nombre
         << " (" << e[mejor].promedio << ")" << endl;
}

/* ===== EJERCICIO 6 ===== */
struct Producto {
    string nombre;
    float precio;
    int cantidad;
};

void ejercicio6() {
    Producto p[5];
    float total = 0;

    for (int i = 0; i < 5; i++) {
        cout << "Nombre: ";
        cin >> p[i].nombre;
        cout << "Precio: ";
        cin >> p[i].precio;
        cout << "Cantidad: ";
        cin >> p[i].cantidad;

        total += p[i].precio * p[i].cantidad;
    }

    cout << "Valor total del inventario: " << total << endl;
}

/* ===== EJERCICIO 7 ===== */
void ejercicio7() {
    int num;
    cout << "Digite un numero: ";
    cin >> num;

    for (int i = 1; i <= 12; i++) {
        cout << num << " x " << i << " = " << num * i << endl;
    }
}

/* ===== EJERCICIO 8 ===== */
void ejercicio8() {
    int num, suma = 0;

    do {
        cout << "Digite un numero (0 para salir): ";
        cin >> num;
        suma += num;
    } while (num != 0);

    cout << "Suma total: " << suma << endl;
}

/* ===== EJERCICIO 9 ===== */
void ejercicio9() {
    int op, a, b;

    do {
        cout << "\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Salir\nOpcion: ";
        cin >> op;

        if (op >= 1 && op <= 3) {
            cout << "Digite dos numeros: ";
            cin >> a >> b;
        }

        switch (op) {
            case 1: cout << "Resultado: " << a + b << endl; break;
            case 2: cout << "Resultado: " << a - b << endl; break;
            case 3: cout << "Resultado: " << a * b << endl; break;
        }
    } while (op != 4);
}

/* ===== EJERCICIO 10 ===== */
void ejercicio10() {
    int num, pares = 0, impares = 0;

    for (int i = 1; i <= 10; i++) {
        cout << "Digite un numero: ";
        cin >> num;

        if (num % 2 == 0)
            pares++;
        else
            impares++;
    }

    cout << "Pares: " << pares << endl;
    cout << "Impares: " << impares << endl;
}

/* ===== MAIN ÚNICO ===== */
int main() {
    int opcion;

    do {
        cout << "\n===== MENU =====\n";
        cout << "1. Operaciones basicas\n";
        cout << "2. Datos personales\n";
        cout << "3. Celsius a Fahrenheit\n";
        cout << "4. Area del rectangulo\n";
        cout << "5. Estudiantes\n";
        cout << "6. Inventario\n";
        cout << "7. Tabla de multiplicar\n";
        cout << "8. Suma hasta 0\n";
        cout << "9. Menu matematico\n";
        cout << "10. Pares e impares\n";
        cout << "0. Salir\n";
        cout << "Opcion: ";
        cin >> opcion;

        switch (opcion) {
            case 1: ejercicio1(); break;
            case 2: ejercicio2(); break;
            case 3: ejercicio3(); break;
            case 4: ejercicio4(); break;
            case 5: ejercicio5(); break;
            case 6: ejercicio6(); break;
            case 7: ejercicio7(); break;
            case 8: ejercicio8(); break;
            case 9: ejercicio9(); break;
            case 10: ejercicio10(); break;
        }

    } while (opcion != 0);

    return 0;
}

