class Etiqueta:
    """Clase para gestionar etiquetas."""
    etiquetas_existentes = {}  # Diccionario para almacenar etiquetas únicas (ID -> Etiqueta)
    ultimo_id = 0  # Contador para generar IDs únicos

    def __init__(self, id_etiqueta, nombre):
        self.id_etiqueta = id_etiqueta
        self.nombre = nombre
        self.notas_asociadas = []  # Lista de notas asociadas a esta etiqueta

    @classmethod
    def generar_id_unico(cls):
        """Genera un ID único para una nueva etiqueta."""
        cls.ultimo_id += 1
        return cls.ultimo_id

    @classmethod
    def obtener_o_crear_etiqueta(cls, nombre):
        """Obtiene una etiqueta si ya existe, o la crea si no."""
        # Buscar por nombre primero, ignorando mayúsculas/minúsculas
        for etiqueta in cls.etiquetas_existentes.values():
            if etiqueta.nombre.lower() == nombre.lower():
                return etiqueta

        # Si no existe, crear una nueva etiqueta
        nuevo_id = cls.generar_id_unico()
        nueva_etiqueta = cls(nuevo_id, nombre)
        cls.etiquetas_existentes[nuevo_id] = nueva_etiqueta
        return nueva_etiqueta

    @classmethod
    def mostrar_etiquetas_usuario(cls):
        """Muestra las etiquetas existentes y sus IDs."""
        if not cls.etiquetas_existentes:
            print("No hay etiquetas creadas.")
            return

        print("\n===== Etiquetas existentes =====")
        for id_etiqueta, etiqueta in cls.etiquetas_existentes.items():
            print(f"ID: {id_etiqueta}, Nombre: {etiqueta.nombre}")

    @classmethod
    def buscar_etiqueta_por_id(cls, id_etiqueta):
        """Busca una etiqueta por su ID."""
        return cls.etiquetas_existentes.get(id_etiqueta, None)

    @classmethod
    def eliminar_etiqueta(cls, id_etiqueta):
        """Elimina una etiqueta por su ID si existe."""
        if id_etiqueta in cls.etiquetas_existentes:
            etiqueta = cls.etiquetas_existentes[id_etiqueta]
            # Remover la etiqueta de todas las notas asociadas
            for nota in etiqueta.notas_asociadas:
                nota.eliminar_etiqueta(etiqueta)
            del cls.etiquetas_existentes[id_etiqueta]
            print(f"Etiqueta '{etiqueta.nombre}' eliminada con éxito.")
        else:
            print("Etiqueta no encontrada.")

    def asignar_a_nota(self, nota):
        """Asigna esta etiqueta a una nota."""
        if nota.etiqueta == self:
            print(f"La nota '{nota.titulo}' ya tiene la etiqueta '{self.nombre}' asignada.")
        elif nota.etiqueta is not None:
            # Preguntar si desea reemplazar la etiqueta existente
            print(f"La nota '{nota.titulo}' ya tiene la etiqueta '{nota.etiqueta.nombre}' asignada.")
            opcion = input("¿Desea cambiarla por la nueva etiqueta? (s/n): ").lower()
            if opcion == 's':
                nota.etiqueta.eliminar_de_nota(nota)  # Eliminar la etiqueta anterior
                self._asignar_directamente(nota)
        else:
            self._asignar_directamente(nota)

    def _asignar_directamente(self, nota):
        """Asigna esta etiqueta a una nota directamente, sin confirmación."""
        nota.etiqueta = self
        self.notas_asociadas.append(nota)
        print(f"Etiqueta '{self.nombre}' asignada a la nota '{nota.titulo}'.")

    def eliminar_de_nota(self, nota):
        """Elimina esta etiqueta de una nota."""
        if nota.etiqueta == self:
            nota.etiqueta = None
            self.notas_asociadas.remove(nota)
            print(f"Etiqueta '{self.nombre}' eliminada de la nota '{nota.titulo}'.")
        else:
            print(f"La nota '{nota.titulo}' no tiene asignada la etiqueta '{self.nombre}'.")

    @classmethod
    def buscar_notas_por_etiqueta(cls, id_etiqueta):
        """Muestra todas las notas relacionadas con una etiqueta específica."""
        etiqueta = cls.buscar_etiqueta_por_id(id_etiqueta)
        if etiqueta:
            if etiqueta.notas_asociadas:
                print(f"\nNotas asociadas a la etiqueta '{etiqueta.nombre}':")
                for nota in etiqueta.notas_asociadas:
                    print(f"ID Nota: {nota.id_nota}, Título: {nota.titulo}")
            else:
                print(f"No hay notas asociadas a la etiqueta '{etiqueta.nombre}'.")
        else:
            print("Etiqueta no encontrada.")
