# clases/evento.py

class Evento:
    def __init__(self, id_evento, fecha_evento, mensaje_evento, nota_asociada=None, notificacion=False):
        self.id_evento = id_evento
        self.fecha_evento = fecha_evento
        self.mensaje_evento = mensaje_evento
        self.nota_asociada = nota_asociada  # Puede ser una instancia de Nota
        self.notificacion = notificacion

    def mostrar_evento(self):
        nota_info = f"Nota asociada: {self.nota_asociada.titulo}" if self.nota_asociada else "No hay nota asociada."
        return f"Evento: {self.mensaje_evento} en {self.fecha_evento}. {nota_info}"
