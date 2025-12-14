#include <iostream>
#include <vector>
#include <string>
#include <cctype>

using namespace std;

/* ===== VECTORES ===== */
vector<string> usuarios;
vector<string> contrasenas;

/* ===== FUNCION: VERIFICAR CONTRASEÑA ===== */
bool VerificarContrasena(string pass) {
    bool mayuscula = false;
    bool minuscula = false;
    bool numero = false;

    if (pass.length() < 8)
        return false;

    for (char c : pass) {
        if (isupper(c)) mayuscula = true;
        if (islower(c)) minuscula = true;
        if (isdigit(c)) numero = true;
    }

    return mayuscula && minuscula && numero;
}

/* ===== FUNCION: REGISTRAR USUARIO ===== */
void RegistrarUsuario() {
    string usuario, pass;

    cout << "Usuario: ";
    cin >> usuario;

    cout << "Contrasena: ";
    cin >> pass;

    usuarios.push_back(usuario);
    contrasenas.push_back(pass);

    cout << "Usuario registrado correctamente.\n";
}

/* ===== FUNCION: GENERAR ALERTAS ===== */
void GenerarAlertas() {
    for (size_t i = 0; i < usuarios.size(); i++) {
        if (!VerificarContrasena(contrasenas[i])) {
            cout << "⚠ ALERTA: La contrasena del usuario "
                 << usuarios[i]
                 << " es DEBIL.\n";
        }
    }
}

/* ===== FUNCION: MOSTRAR USUARIOS ===== */
void MostrarUsuarios() {
    if (usuarios.empty()) {
        cout << "No hay usuarios registrados.\n";
        return;
    }

    for (size_t i = 0; i < usuarios.size(); i++) {
        cout << "Usuario: " << usuarios[i] << endl;
    }
}

/* ===== MAIN ===== */
int main() {
    int opcion;

    do {
        cout << "\n===== GESTOR DE CONTRASENAS =====\n";
        cout << "1. Registrar usuario\n";
        cout << "2. Ver usuarios registrados\n";
        cout << "3. Generar alertas de contrasenas debiles\n";
        cout << "0. Salir\n";
        cout << "Opcion: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                RegistrarUsuario();
                break;
            case 2:
                MostrarUsuarios();
                break;
            case 3:
                GenerarAlertas();
                break;
            case 0:
                cout << "Saliendo del sistema...\n";
                break;
            default:
                cout << "Opcion invalida.\n";
        }

    } while (opcion != 0);

    return 0;
}

