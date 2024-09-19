import os
from clases.agenda import Agenda
from clases.usuario import Usuario

def limpiar_consola():
    """Limpia la consola en Windows."""
    os.system("cls")

def main():
    while True:
        limpiar_consola()  # Limpiar la consola antes de mostrar el menú
        print("\n===== Bienvenido al sistema =====")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Recuperar contraseña")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Usuario.registrar_usuario()  # Registrar un nuevo usuario
            input("\nPresione Enter para continuar...")  # Pausa antes de limpiar la consola
            limpiar_consola()  # Limpiar la consola después de registrar
        elif opcion == "2":
            usuario = Usuario.iniciar_sesion()  # Iniciar sesión
            if usuario:
                print(f"\nBienvenido de nuevo, {usuario.nombre_usuario}!")
                agenda = Agenda(usuario=usuario)  # Crea la agenda para el usuario
                agenda.mostrar_agenda()  # Inicia la interacción con la agenda
            input("\nPresione Enter para continuar...")  # Pausa antes de limpiar la consola
            limpiar_consola()  # Limpiar la consola después del inicio de sesión
        elif opcion == "3":
            Usuario.recuperar_contrasena()  # Recuperar la contraseña
            input("\nPresione Enter para continuar...")  # Pausa antes de limpiar la consola
            limpiar_consola()  # Limpiar la consola después de la recuperación de contraseña
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")  # Pausa antes de limpiar la consola
            limpiar_consola()  # Limpiar la consola después de una opción no válida

if __name__ == "__main__":
    main()
