from clases.nota import Nota

class Agenda:
    def __init__(self, usuario):
        self.usuario = usuario

    def mostrar_agenda(self):
        """Muestra las opciones principales de la agenda al usuario."""
        while True:
            print("\n===== Agenda de Usuario =====")
            print("1. Notas")
            print("2. Calendario (Próximamente)")
            print("3. Grupo (Próximamente)")
            print("4. Ver perfil")
            print("5. Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                Nota.gestionar_notas(self.usuario)  # Llama directamente a la gestión de notas
            elif opcion == "4":
                self.ver_perfil()
            elif opcion == "5":
                confirmacion = input("¿Está seguro que desea cerrar sesión? (s/n): ").lower()
                if confirmacion == "s":
                    print("Cerrando sesión...")
                    break
            else:
                print("Opción no válida o en desarrollo. Intente de nuevo.")

    def ver_perfil(self):
        """Muestra la información del perfil del usuario."""
        print(f"\n===== Perfil de Usuario =====")
        print(f"ID de Usuario: {self.usuario.id_usuario}")
        print(f"Nombre de Usuario: {self.usuario.nombre_usuario}")
        print(f"Correo Electrónico: {self.usuario.correo_electronico}")
