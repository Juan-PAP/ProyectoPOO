class Agenda:
    def __init__(self, id_agenda):
        self.id_agenda = id_agenda
        self.notas = []

    # Métodos
    def imprimir_nota(self):
        # Lógica para imprimir las notas
        for nota in self.notas:
            print(f"Nota: {nota.titulo_nota}, Contenido: {nota.contenido_nota}")

    def filtrar_notas(self, filtro):
        # Lógica para filtrar notas según un criterio
        notas_filtradas = [nota for nota in self.notas if filtro in nota.titulo_nota]
        return notas_filtradas
