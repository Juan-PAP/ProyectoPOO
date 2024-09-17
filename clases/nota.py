class Nota:
    def __init__(self, id_nota, titulo_nota, contenido_nota, fecha_creacion, ultima_modificacion):
        self.id_nota = id_nota
        self.titulo_nota = titulo_nota
        self.contenido_nota = contenido_nota
        self.fecha_creacion = fecha_creacion
        self.ultima_modificacion = ultima_modificacion

    # Métodos
    def crear_nota(self):
        # Lógica para crear una nueva nota
        print(f"Nota '{self.titulo_nota}' creada.")

    def editar_nota(self, nuevo_contenido):
        # Lógica para editar el contenido de una nota
        self.contenido_nota = nuevo_contenido
        print(f"Nota '{self.titulo_nota}' editada.")

    def eliminar_nota(self):
        # Lógica para eliminar la nota
        print(f"Nota '{self.titulo_nota}' eliminada.")
