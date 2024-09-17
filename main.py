# main.py

from clases.usuario import Usuario

def main():
    while True:
        print("Bienvenido al sistema")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Usuario.registrar_usuario()
        elif opcion == "2":
            usuario = Usuario.iniciar_sesion()
            if usuario:
                # Aquí puedes agregar lógica adicional para usuarios autenticados
                print(f"Bienvenido de nuevo, {usuario.nombre_usuario}!")
        elif opcion == "3":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
