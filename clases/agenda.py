from clases.nota import Nota
import os


def limpiar_consola():
    """Limpia la consola en Windows."""
    os.system("cls")


class Agenda:
    def __init__(self, usuario):
        self.usuario = usuario

    def mostrar_agenda(self):
        """Muestra las opciones principales de la agenda al usuario."""
        while True:
            limpiar_consola()  # Limpia la consola al mostrar el menú
            print("\n===== Agenda de Usuario =====")
            print("1. Notas")
            print("2. Calendario (Próximamente)")
            print("3. Grupo (Próximamente)")
            print("4. Ver perfil")
            print("5. Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                limpiar_consola()  # Limpia la consola antes de gestionar notas
                Nota.gestionar_notas(self.usuario)  # Llama directamente a la gestión de notas
                limpiar_consola()  # Limpia la consola después de gestionar notas
            elif opcion == "4":
                limpiar_consola()  # Limpia la consola antes de mostrar el perfil
                self.ver_perfil()
                input("Presione Enter para continuar...")
                limpiar_consola()  # Limpia la consola después de mostrar el perfil
            elif opcion == "5":
                confirmacion = input("¿Está seguro que desea cerrar sesión? (s/n): ").lower()
                if confirmacion == "s":
                    print("Cerrando sesión...")
                    limpiar_consola()  # Limpia la consola después de cerrar sesión
                    break
            else:
                print("Opción no válida o en desarrollo. Intente de nuevo.")
                input("Presione Enter para continuar...")
                limpiar_consola()  # Limpia la consola después de mostrar el mensaje de error

    def ver_perfil(self):
        """Muestra la información del perfil del usuario."""
        print(f"\n===== Perfil de Usuario =====")
        print(f"ID de Usuario: {self.usuario.id_usuario}")
        print(f"Nombre de Usuario: {self.usuario.nombre_usuario}")
        print(f"Correo Electrónico: {self.usuario.correo_electronico}")
