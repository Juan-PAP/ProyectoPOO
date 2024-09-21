from datetime import datetime

class HistorialNota:
    """Clase para gestionar el historial de modificaciones de una nota."""

    def __init__(self, nota):
        self.nota = nota
        self.historial = []  # Lista de cambios

    def registrar_cambio(self, campo, valor_anterior, valor_nuevo):
        """Registra un cambio en la nota."""
        timestamp = datetime.now()
        self.historial.append({
            "campo": campo,
            "valor_anterior": valor_anterior,
            "valor_nuevo": valor_nuevo,
            "fecha_modificacion": timestamp
        })

    def editar(self):
        """Permite editar la nota y registra los cambios en el historial."""
        cambiar_titulo = input("¿Desea cambiar el título? (s/n): ").lower()
        cambiar_contenido = input("¿Desea cambiar el contenido? (s/n): ").lower()

        if cambiar_titulo == 's':
            nuevo_titulo = input("Ingrese el nuevo título: ")
            self.registrar_cambio("titulo", self.nota.titulo, nuevo_titulo)
            self.nota.editar_titulo(nuevo_titulo)

        if cambiar_contenido == 's':
            nuevo_contenido = input("Ingrese el nuevo contenido: ")
            self.registrar_cambio("contenido", self.nota.contenido, nuevo_contenido)
            self.nota.editar_contenido(nuevo_contenido)

        print("Nota editada con éxito.")

    def revertir_cambio(self):
        """Revertir un cambio según el historial."""
        self.mostrar_historial()  # Mostrar el historial antes de revertir
        try:
            indice = int(input("Ingrese el número de la modificación que desea revertir: ")) - 1
            if 0 <= indice < len(self.historial):
                cambio = self.historial[indice]
                if hasattr(self.nota, cambio["campo"]):
                    setattr(self.nota, cambio["campo"], cambio["valor_anterior"])
                    self.nota.fecha_modificacion = datetime.now()
                    print("El cambio ha sido revertido exitosamente.")
                else:
                    print(f"Error: El campo '{cambio['campo']}' no existe en la nota.")
            else:
                print("Índice no válido.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

    def mostrar_historial(self):
        """Muestra el historial de cambios realizados."""
        if not self.historial:
            print("No hay modificaciones en esta nota.")
        for i, cambio in enumerate(self.historial):
            print(f"{i + 1}. {cambio['campo']} - {cambio['valor_anterior']} -> {cambio['valor_nuevo']} "
                  f"(Modificado el {cambio['fecha_modificacion']})")
