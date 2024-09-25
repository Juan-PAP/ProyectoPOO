import os
from clases.nota import Nota

def limpiar_consola():
    """Limpia la consola en Windows."""
    os.system("cls")

def mostrar_mensaje(mensaje):
    """Muestra un mensaje en pantalla y espera que el usuario presione Enter."""
    print(mensaje)
    input("Presione Enter para continuar...")

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
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.gestionar_notas()
            elif opcion == "2" or opcion == "3":
                mostrar_mensaje("Opción en desarrollo. Intente de nuevo.")
            elif opcion == "4":
                self.mostrar_perfil()
            elif opcion == "5":
                if self.confirmar_cierre_sesion():
                    break
            elif opcion == "6":
                print("Saliendo de la agenda...")
                break
            else:
                mostrar_mensaje("Opción no válida. Intente de nuevo.")

    def gestionar_notas(self):
        """Gestiona las notas del usuario."""
        limpiar_consola()  # Limpia la consola antes de gestionar notas
        Nota.gestionar_notas(self.usuario)  # Llama directamente a la gestión de notas
        limpiar_consola()  # Limpia la consola después de gestionar notas

    def mostrar_perfil(self):
        """Muestra la información del perfil del usuario."""
        limpiar_consola()  # Limpia la consola antes de mostrar el perfil
        print(f"\n===== Perfil de Usuario =====")
        print(f"ID de Usuario: {self.usuario.id_usuario}")
        print(f"Nombre de Usuario: {self.usuario.nombre_usuario}")
        print(f"Correo Electrónico: {self.usuario.correo_electronico}")
        mostrar_mensaje("")

    def confirmar_cierre_sesion(self):
        """Pregunta al usuario si desea cerrar sesión."""
        confirmacion = input("¿Está seguro que desea cerrar sesión? (s/n): ").lower()
        return confirmacion == "s"

