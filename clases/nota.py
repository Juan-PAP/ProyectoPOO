from datetime import datetime
import os


class Nota:
    notas = []  # Lista de todas las notas

    def __init__(self, id_nota, titulo, contenido, usuario):
        self.id_nota = id_nota
        self.titulo = titulo
        self.contenido = contenido
        self.usuario = usuario
        self.fecha_creacion = datetime.now()
        self.fecha_modificacion = None  # Inicialmente no hay modificaciones

    @classmethod
    def limpiar_consola(cls):
        """Limpia la consola en Windows."""
        os.system("cls")

    @classmethod
    def generar_id_unico(cls):
        """Genera un ID único para una nueva nota."""
        id_nota = 1
        while any(nota.id_nota == id_nota for nota in cls.notas):
            id_nota += 1
        return id_nota

    @classmethod
    def gestionar_notas(cls, usuario):
        """Gestiona las notas del usuario."""
        while True:
            cls.limpiar_consola()
            print("\n===== Gestión de Notas =====")
            print("1. Ver todas las notas")
            print("2. Crear nueva nota")
            print("3. Editar nota existente")
            print("4. Eliminar nota existente")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                cls.limpiar_consola()
                if not cls.imprimir_notas(usuario):
                    print("No tiene notas creadas.")
                else:
                    cls.ver_contenido_nota(usuario)
            elif opcion == "2":
                cls.limpiar_consola()
                cls.crear_nota(usuario)
            elif opcion == "3":
                cls.limpiar_consola()
                if cls.imprimir_notas(usuario):
                    cls.editar_nota(usuario)
            elif opcion == "4":
                cls.limpiar_consola()
                if cls.imprimir_notas(usuario):
                    cls.eliminar_nota(usuario)
            elif opcion == "5":
                print("Volviendo al menú principal...")
                cls.limpiar_consola()
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                input("Presione Enter para continuar...")
                cls.limpiar_consola()

    @classmethod
    def crear_nota(cls, usuario):
        """Crea una nueva nota para el usuario."""
        titulo = input("Ingrese el título de la nota: ")
        contenido = input("Ingrese el contenido de la nota: ")

        # Asignar un nuevo ID único
        id_nota = cls.generar_id_unico()

        nueva_nota = cls(id_nota, titulo, contenido, usuario)
        cls.notas.append(nueva_nota)
        cls.limpiar_consola()
        print("Nota creada con éxito.")

    @classmethod
    def imprimir_notas(cls, usuario):
        """Imprime las notas del usuario con detalles de ID, título, fecha de creación y modificación."""
        notas_usuario = [nota for nota in cls.notas if nota.usuario == usuario]
        if not notas_usuario:
            return False

        cls.limpiar_consola()
        print("\n===== Sus Notas =====")
        for nota in notas_usuario:
            fecha_creacion = nota.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")
            if nota.fecha_modificacion:
                fecha_modificacion = nota.fecha_modificacion.strftime("%Y-%m-%d %H:%M:%S")
                print(
                    f"ID: {nota.id_nota:04}, Título: {nota.titulo}, Creada: {fecha_creacion}, Modificada: {fecha_modificacion}")
            else:
                print(f"ID: {nota.id_nota:04}, Título: {nota.titulo}, Creada: {fecha_creacion}")
        return True

    @classmethod
    def ver_contenido_nota(cls, usuario):
        """Permite ver el contenido de una nota específica."""
        while True:
            indice = cls.obtener_indice_valido(usuario)
            if indice is not None:
                nota = cls.obtener_nota_por_indice(usuario, indice)
                cls.limpiar_consola()
                print(f"\nTítulo: {nota.titulo}")
                print(f"Contenido: {nota.contenido}")
                print(f"Creada: {nota.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}")
                if nota.fecha_modificacion:
                    print(f"Última modificación: {nota.fecha_modificacion.strftime('%Y-%m-%d %H:%M:%S')}")
                input("Presione Enter para continuar...")
                cls.limpiar_consola()
                break

    @classmethod
    def editar_nota(cls, usuario):
        """Permite editar una nota existente."""
        while True:
            indice = cls.obtener_indice_valido(usuario)
            if indice is not None:
                nota = cls.obtener_nota_por_indice(usuario, indice)

                cambiar_titulo = input("¿Desea cambiar el título? (s/n): ").lower()
                cambiar_contenido = input("¿Desea cambiar el contenido? (s/n): ").lower()

                editado = False

                if cambiar_titulo == 's':
                    nuevo_titulo = input("Ingrese el nuevo título: ")
                    nota.editar_titulo(nuevo_titulo)
                    editado = True

                if cambiar_contenido == 's':
                    nuevo_contenido = input("Ingrese el nuevo contenido: ")
                    nota.editar_contenido(nuevo_contenido)
                    editado = True

                if editado:
                    cls.limpiar_consola()
                    print("Nota editada con éxito.")
                else:
                    print("La nota no ha sido editada.")
                input("Presione Enter para continuar...")
                cls.limpiar_consola()
                break

    @classmethod
    def eliminar_nota(cls, usuario):
        """Elimina una nota existente."""
        while True:
            indice = cls.obtener_indice_valido(usuario)
            if indice is not None:
                nota = cls.obtener_nota_por_indice(usuario, indice)
                confirmacion = input("¿Está seguro que desea eliminar esta nota? (s/n): ").lower()
                if confirmacion == "s":
                    cls.notas.remove(nota)
                    cls.limpiar_consola()
                    print("Nota eliminada con éxito.")
                    input("Presione Enter para continuar...")
                    cls.limpiar_consola()
                else:
                    print("Eliminación de nota cancelada.")
                break

    @classmethod
    def obtener_indice_valido(cls, usuario):
        """Solicita un índice válido y verifica si existe la nota."""
        notas_usuario = [nota for nota in cls.notas if nota.usuario == usuario]
        if not notas_usuario:
            print("No tiene notas para gestionar.")
            return None

        while True:
            try:
                indice = int(input("Seleccione el ID de la nota: "))
                if any(nota.id_nota == indice for nota in notas_usuario):
                    return indice
                else:
                    print("ID no válido. Intente de nuevo.")
            except ValueError:
                print("Entrada no válida. Ingrese un número.")

    @classmethod
    def obtener_nota_por_indice(cls, usuario, id_nota):
        """Obtiene una nota específica por el ID."""
        for nota in cls.notas:
            if nota.usuario == usuario and nota.id_nota == id_nota:
                return nota

    def editar_titulo(self, nuevo_titulo):
        """Edita el título de la nota y actualiza la fecha de modificación."""
        self.titulo = nuevo_titulo
        self.fecha_modificacion = datetime.now()

    def editar_contenido(self, nuevo_contenido):
        """Edita el contenido de la nota y actualiza la fecha de modificación."""
        self.contenido = nuevo_contenido
        self.fecha_modificacion = datetime.now()
