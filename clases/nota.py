import os
from datetime import datetime

class Nota:
    notas = []  # Lista de todas las notas
    id_counter = 1  # Contador de ID para nuevas notas
    ids_disponibles = []  # Lista de IDs libres que se pueden reutilizar

    def __init__(self, titulo, contenido, usuario):
        self.id_nota = self.generar_id()  # Genera un ID único
        self.titulo = titulo
        self.contenido = contenido
        self.usuario = usuario
        self.fecha_creacion = datetime.now()
        self.fecha_modificacion = None  # Inicialmente no hay modificaciones

    @classmethod
    def generar_id(cls):
        """Genera un ID único para la nota, reutilizando IDs libres si es posible."""
        if cls.ids_disponibles:
            return cls.ids_disponibles.pop()  # Usa un ID libre disponible
        else:
            id_nota = f"{cls.id_counter:04}"
            cls.id_counter += 1
            return id_nota

    @classmethod
    def limpiar_consola(cls):
        """Limpia la consola en Windows."""
        os.system("cls")

    @classmethod
    def gestionar_notas(cls, usuario):
        """Gestiona las notas del usuario."""
        while True:
            cls.limpiar_consola()  # Limpiar consola antes de mostrar el menú de gestión de notas
            print("\n===== Gestión de Notas =====")
            print("1. Ver todas las notas")
            print("2. Crear nueva nota")
            print("3. Editar nota existente")
            print("4. Eliminar nota existente")
            print("5. Volver al menú principal")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                cls.limpiar_consola()  # Limpia la consola antes de imprimir las notas
                if not cls.imprimir_notas(usuario):
                    print("No tiene notas creadas.")
                else:
                    cls.ver_contenido_nota(usuario)  # Ver el contenido específico de una nota
            elif opcion == "2":
                cls.limpiar_consola()  # Limpia la consola antes de crear una nueva nota
                cls.crear_nota(usuario)
            elif opcion == "3":
                cls.limpiar_consola()  # Limpia la consola antes de editar una nota
                if cls.imprimir_notas(usuario):  # Solo mostrar si hay notas
                    cls.editar_nota(usuario)
            elif opcion == "4":
                cls.limpiar_consola()  # Limpia la consola antes de eliminar una nota
                if cls.imprimir_notas(usuario):  # Solo mostrar si hay notas
                    cls.eliminar_nota(usuario)
            elif opcion == "5":
                print("Volviendo al menú principal...")
                cls.limpiar_consola()  # Limpia la consola antes de volver al menú principal
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                input("Presione Enter para continuar...")
                cls.limpiar_consola()  # Limpia la consola después de mostrar el mensaje de error

    @classmethod
    def crear_nota(cls, usuario):
        """Crea una nueva nota para el usuario."""
        titulo = input("Ingrese el título de la nota: ")
        contenido = input("Ingrese el contenido de la nota: ")
        nueva_nota = cls(titulo, contenido, usuario)
        cls.notas.append(nueva_nota)
        cls.limpiar_consola()  # Limpia la consola después de crear la nota
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
                print(f"ID: {nota.id_nota}, Título: {nota.titulo}, Creada: {fecha_creacion}, Modificada: {fecha_modificacion}")
            else:
                print(f"ID: {nota.id_nota}, Título: {nota.titulo}, Creada: {fecha_creacion}")
        return True

    @classmethod
    def ver_contenido_nota(cls, usuario):
        """Permite ver el contenido de una nota específica."""
        while True:
            id_nota = cls.obtener_id_valido(usuario)
            if id_nota is not None:
                nota = cls.obtener_nota_por_id(usuario, id_nota)
                cls.limpiar_consola()
                print(f"\nTítulo: {nota.titulo}")
                print(f"Contenido: {nota.contenido}")
                print(f"Creada: {nota.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}")
                if nota.fecha_modificacion:
                    print(f"Última modificación: {nota.fecha_modificacion.strftime('%Y-%m-%d %H:%M:%S')}")
                input("Presione Enter para continuar...")
                cls.limpiar_consola()  # Limpia la consola después de mostrar el contenido de la nota
                break

    @classmethod
    def editar_nota(cls, usuario):
        """Permite editar una nota existente."""
        while True:
            id_nota = cls.obtener_id_valido(usuario)
            if id_nota is not None:
                nota = cls.obtener_nota_por_id(usuario, id_nota)

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
                cls.limpiar_consola()  # Limpia la consola después de editar la nota
                break

    @classmethod
    def eliminar_nota(cls, usuario):
        """Elimina una nota existente."""
        while True:
            id_nota = cls.obtener_id_valido(usuario)
            if id_nota is not None:
                nota = cls.obtener_nota_por_id(usuario, id_nota)
                confirmacion = input("¿Está seguro que desea eliminar esta nota? (s/n): ").lower()
                if confirmacion == "s":
                    cls.notas.remove(nota)
                    cls.ids_disponibles.append(id_nota)  # Marca el ID como disponible
                    cls.limpiar_consola()
                    print("Nota eliminada con éxito.")
                    input("Presione Enter para continuar...")
                    cls.limpiar_consola()  # Limpia la consola después de eliminar la nota
                else:
                    print("Eliminación de nota cancelada.")
                break

    @classmethod
    def obtener_id_valido(cls, usuario):
        """Solicita un ID válido y verifica si existe la nota."""
        while True:
            id_nota = input("Seleccione el ID de la nota (o '0' para cancelar): ")
            if id_nota == '0':
                cls.limpiar_consola()
                print("Operación cancelada.")
                return None
            if len(id_nota) <= 4 and id_nota.isdigit():
                nota = cls.obtener_nota_por_id(usuario, id_nota)
                if nota:
                    return id_nota
                else:
                    print("ID no válido. Intente de nuevo.")
            else:
                print("ID no válido. Intente de nuevo.")

    @classmethod
    def obtener_nota_por_id(cls, usuario, id_nota):
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
