class Etiqueta:
    """Clase para gestionar etiquetas."""
    etiquetas_existentes = {}  # Diccionario para almacenar etiquetas únicas

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def obtener_o_crear_etiqueta(cls, nombre):
        """Obtiene una etiqueta si ya existe, o la crea si no."""
        if nombre not in cls.etiquetas_existentes:
            cls.etiquetas_existentes[nombre] = cls(nombre)
        return cls.etiquetas_existentes[nombre]

    @classmethod
    def buscar_etiqueta(cls, nombre):
        """Busca una etiqueta por nombre."""
        return cls.etiquetas_existentes.get(nombre, None)

    @classmethod
    def eliminar_etiqueta(cls, nombre):
        """Elimina una etiqueta del diccionario de etiquetas si existe."""
        if nombre in cls.etiquetas_existentes:
            del cls.etiquetas_existentes[nombre]
