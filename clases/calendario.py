# clases/calendario.py
import os
import calendar
from datetime import datetime
from clases.evento import Evento
from clases.nota import Nota


def limpiar_consola():
    """Limpia la consola en Windows."""
    os.system("cls")


class Calendario:
    def __init__(self):
        self.eventos = []

    def mostrar_menu(self, usuario):
        """Muestra el menú de opciones para el calendario."""
        while True:
            limpiar_consola()
            print("\n===== Calendario =====")
            print("1. Ver calendario del mes")
            print("2. Crear evento")
            print("3. Editar evento")
            print("4. Eliminar evento")
            print("5. Ver eventos")
            print("6. Regresar al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.imprimir_calendario()
            elif opcion == "2":
                self.crear_evento(usuario)
            elif opcion == "3":
                self.editar_evento()
            elif opcion == "4":
                self.eliminar_evento()
            elif opcion == "5":
                self.mostrar_eventos()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                input("Presione Enter para continuar...")

    def imprimir_calendario(self):
        """Imprime el calendario del mes actual."""
        year = datetime.now().year
        month = datetime.now().month
        cal = calendar.TextCalendar(calendar.SUNDAY)
        limpiar_consola()
        print(cal.formatmonth(year, month))
        input("Presione Enter para continuar...")

    def crear_evento(self, usuario):
        """Crea un nuevo evento."""
        limpiar_consola()
        id_evento = len(self.eventos) + 1
        fecha_evento = input("Ingrese la fecha del evento (YYYY-MM-DD): ")
        mensaje_evento = input("Ingrese la descripción del evento: ")

        # Ver si el usuario quiere asociar una nota
        asociar_nota = input("¿Desea asociar una nota existente? (s/n): ").lower()
        nota_asociada = None
        if asociar_nota == "s" and usuario.notas:
            print("Selecciona una de las notas disponibles:")
            for idx, nota in enumerate(usuario.notas, start=1):
                print(f"{idx}. {nota.titulo}")
            nota_idx = int(input("Ingrese el número de la nota: ")) - 1
            nota_asociada = usuario.notas[nota_idx]

        nuevo_evento = Evento(id_evento, fecha_evento, mensaje_evento, nota_asociada, notificacion=False)
        self.eventos.append(nuevo_evento)
        print("Evento creado con éxito.")
        input("Presione Enter para continuar...")

    def editar_evento(self):
        """Edita un evento existente."""
        limpiar_consola()
        self.mostrar_eventos()
        id_evento = int(input("Ingrese el ID del evento que desea editar: "))
        for evento in self.eventos:
            if evento.id_evento == id_evento:
                nuevo_mensaje = input("Ingrese la nueva descripción (dejar en blanco para no cambiar): ")
                nueva_fecha = input("Ingrese la nueva fecha (YYYY-MM-DD, dejar en blanco para no cambiar): ")

                if nuevo_mensaje:
                    evento.mensaje_evento = nuevo_mensaje
                if nueva_fecha:
                    evento.fecha_evento = nueva_fecha

                print(f"Evento con ID {id_evento} actualizado.")
                input("Presione Enter para continuar...")
                return
        print(f"No se encontró un evento con ID {id_evento}.")
        input("Presione Enter para continuar...")

    def eliminar_evento(self):
        """Elimina un evento."""
        limpiar_consola()
        self.mostrar_eventos()
        id_evento = int(input("Ingrese el ID del evento que desea eliminar: "))
        self.eventos = [evento for evento in self.eventos if evento.id_evento != id_evento]
        print(f"Evento con ID {id_evento} eliminado.")
        input("Presione Enter para continuar...")

    def mostrar_eventos(self):
        """Muestra todos los eventos."""
        limpiar_consola()
        if not self.eventos:
            print("No hay eventos.")
        else:
            for evento in self.eventos:
                print(f"ID: {evento.id_evento} - {evento.mensaje_evento} - Fecha: {evento.fecha_evento}")
                if evento.nota_asociada:
                    print(f"  Nota asociada: {evento.nota_asociada.titulo}")
        input("Presione Enter para continuar...")
