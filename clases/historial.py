from datetime import datetime


class HistorialNota:
    """Clase para gestionar el historial de modificaciones de una nota."""

    def __init__(self, nota):
        self.nota = nota
        self.historial = []

    def registrar_cambio(self, campo, valor_anterior, valor_nuevo):
        """Registra un cambio en la nota."""
        timestamp = datetime.now()
        self.historial.append({
            "campo": campo,
            "valor_anterior": valor_anterior,
            "valor_nuevo": valor_nuevo,
            "fecha_modificacion": timestamp
        })

    def revertir_cambio(self, indice):
        """Revertir un cambio en la nota según el historial."""
        if 0 <= indice < len(self.historial):
            cambio = self.historial[indice]

            # Verificar que el diccionario tiene las claves necesarias
            if all(k in cambio for k in ("campo", "valor_anterior", "valor_nuevo")):
                # Verificar que el campo existe en la nota antes de revertir
                if hasattr(self.nota, cambio["campo"]):
                    setattr(self.nota, cambio["campo"], cambio["valor_anterior"])
                    self.nota.fecha_modificacion = datetime.now()
                    return True
                else:
                    print(f"Error: El campo '{cambio['campo']}' no existe en la nota.")
                    return False
            else:
                print("Error: El historial de cambios no tiene la estructura esperada.")
                return False
        return False

    def mostrar_historial(self):
        """Muestra el historial de cambios realizados."""
        if not self.historial:
            print("No hay modificaciones en esta nota.")
        for i, cambio in enumerate(self.historial):
            print(f"{i + 1}. {cambio['campo']} - {cambio['valor_anterior']} -> {cambio['valor_nuevo']} "
                  f"(Modificado el {cambio['fecha_modificacion']})")
