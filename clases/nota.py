from datetime import datetime
import os
from clases.historial import HistorialNota
from clases.etiqueta import Etiqueta


class Nota:
    """Clase principal para la gestión de notas."""
    notas = {}  # Diccionario de todas las notas (ID -> Nota)

    def __init__(self, id_nota, titulo, contenido, usuario):
        self.id_nota = id_nota
        self.titulo = titulo
        self.contenido = contenido
        self.usuario = usuario
        self.fecha_creacion = datetime.now()
        self.fecha_modificacion = None  # Inicialmente no hay modificaciones
        self.etiquetas = []  # Lista de etiquetas asociadas a la nota
        self.historial = HistorialNota(self)  # Instancia de historial de cambios

    @classmethod
    def limpiar_consola(cls):
        """Limpia la consola."""
        os.system("cls" if os.name == "nt" else "clear")

    @classmethod
    def generar_id_unico(cls):
        """Genera un ID único para una nueva nota usando el diccionario."""
        return max(cls.notas.keys(), default=0) + 1

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
            print("5. Agregar etiqueta a nota")
            print("6. Eliminar etiqueta de nota")
            print("7. Revertir cambios en una nota")
            print("8. Ver historial de modificaciones")
            print("9. Volver al menú principal")

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
                if cls.verificar_existencia_notas(usuario):
                    cls.editar_nota(usuario)
            elif opcion == "4":
                if cls.verificar_existencia_notas(usuario):
                    cls.eliminar_nota(usuario)
            elif opcion == "5":
                if cls.verificar_existencia_notas(usuario):
                    cls.agregar_etiqueta_a_nota(usuario)
            elif opcion == "6":
                if cls.verificar_existencia_notas(usuario):
                    cls.eliminar_etiqueta_de_nota(usuario)
            elif opcion == "7":
                if cls.verificar_existencia_notas(usuario):
                    cls.revertir_cambio_nota(usuario)
            elif opcion == "8":
                if cls.verificar_existencia_notas(usuario):
                    cls.ver_historial_nota(usuario)
            elif opcion == "9":
                print("Volviendo al menú principal...")
                cls.limpiar_consola()
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                input("Presione Enter para continuar...")
                cls.limpiar_consola()

    @classmethod
    def verificar_existencia_notas(cls, usuario):
        """Verifica si el usuario tiene notas y muestra un mensaje si no tiene."""
        if not cls.imprimir_notas(usuario):
            print("No tiene notas creadas.")
            input("Presione Enter para continuar...")
            cls.limpiar_consola()
            return False
        return True

    @classmethod
    def crear_nota(cls, usuario):
        """Crea una nueva nota para el usuario."""
        titulo = input("Ingrese el título de la nota: ")
        contenido = input("Ingrese el contenido de la nota: ")

        # Asignar un nuevo ID único
        id_nota = cls.generar_id_unico()

        nueva_nota = cls(id_nota, titulo, contenido, usuario)
        cls.notas[id_nota] = nueva_nota  # Guardar en el diccionario
        cls.limpiar_consola()
        print("Nota creada con éxito.")
        input("Presione Enter para continuar...")
        cls.limpiar_consola()

    @classmethod
    def imprimir_notas(cls, usuario):
        """Imprime las notas del usuario con detalles de ID, título, fecha de creación y modificación."""
        notas_usuario = [nota for nota in cls.notas.values() if nota.usuario == usuario]
        if not notas_usuario:
            return False

        cls.limpiar_consola()
        print("\n===== Sus Notas =====")
        for nota in notas_usuario:
            fecha_creacion = nota.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")
            if nota.fecha_modificacion:
                fecha_modificacion = nota.fecha_modificacion.strftime("%Y-%m-%d %H:%M:%S")
                print(f"ID: {nota.id_nota:04}, Título: {nota.titulo}, Creada: {fecha_creacion}, Modificada: {fecha_modificacion}")
            else:
                print(f"ID: {nota.id_nota:04}, Título: {nota.titulo}, Creada: {fecha_creacion}")
        return True

    @classmethod
    def ver_contenido_nota(cls, usuario):
        """Permite ver el contenido de una nota específica."""
        id_nota = cls.obtener_indice_valido(usuario)
        if id_nota is not None:
            nota = cls.obtener_nota_por_indice(usuario, id_nota)
            cls.limpiar_consola()
            print(f"\nTítulo: {nota.titulo}")
            print(f"Contenido: {nota.contenido}")
            print(f"Creada: {nota.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}")
            if nota.fecha_modificacion:
                print(f"Última modificación: {nota.fecha_modificacion.strftime('%Y-%m-%d %H:%M:%S')}")
            input("Presione Enter para continuar...")
            cls.limpiar_consola()

    @classmethod
    def editar_nota(cls, usuario):
        """Delegar la edición de una nota a la clase HistorialNota."""
        id_nota = cls.obtener_indice_valido(usuario)
        if id_nota is not None:
            nota = cls.obtener_nota_por_indice(usuario, id_nota)
            nota.historial.editar()

    @classmethod
    def eliminar_nota(cls, usuario):
        """Elimina una nota existente."""
        id_nota = cls.obtener_indice_valido(usuario)
        if id_nota is not None:
            nota = cls.obtener_nota_por_indice(usuario, id_nota)
            confirmacion = input("¿Está seguro que desea eliminar esta nota? (s/n): ").lower()
            if confirmacion == "s":
                del cls.notas[nota.id_nota]
                cls.limpiar_consola()
                print("Nota eliminada con éxito.")
            else:
                print("Eliminación de nota cancelada.")
            input("Presione Enter para continuar...")
            cls.limpiar_consola()

    @classmethod
    def agregar_etiqueta_a_nota(cls, usuario):
        """Agrega una etiqueta a una nota existente."""
        id_nota = cls.obtener_indice_valido(usuario)
        if id_nota is not None:
            nota = cls.obtener_nota_por_indice(usuario, id_nota)
            nombre_etiqueta = input("Ingrese el nombre de la etiqueta: ")

            etiqueta = Etiqueta.obtener_o_crear_etiqueta(nombre_etiqueta)
            nota.agregar_etiqueta(etiqueta)
            cls.limpiar_consola()
            print(f"Etiqueta '{nombre_etiqueta}' agregada a la nota.")
            input("Presione Enter para continuar...")
            cls.limpiar_consola()

    @classmethod
    def eliminar_etiqueta_de_nota(cls, usuario):
        """Elimina una etiqueta de una nota existente."""
        id_nota = cls.obtener_indice_valido(usuario)
        if id_nota is not None:
            nota = cls.obtener_nota_por_indice(usuario, id_nota)
            nombre_etiqueta = input("Ingrese el nombre de la etiqueta a eliminar: ")

            etiqueta = Etiqueta.buscar_etiqueta(nombre_etiqueta)
            if etiqueta:
                nota.eliminar_etiqueta(etiqueta)
                cls.limpiar_consola()
                print(f"Etiqueta '{nombre_etiqueta}' eliminada de la nota.")
            else:
                print("Etiqueta no encontrada en la nota.")
            input("Presione Enter para continuar...")
            cls.limpiar_consola()

    @classmethod
    def revertir_cambio_nota(cls, usuario):
        """Delegar la reversión de un cambio a la clase HistorialNota."""
        id_nota = cls.obtener_indice_valido(usuario)
        if id_nota is not None:
            nota = cls.obtener_nota_por_indice(usuario, id_nota)
            nota.historial.revertir_cambio()

    @classmethod
    def ver_historial_nota(cls, usuario):
        """Delegar la visualización del historial a la clase HistorialNota."""
        id_nota = cls.obtener_indice_valido(usuario)
        if id_nota is not None:
            nota = cls.obtener_nota_por_indice(usuario, id_nota)
            nota.historial.mostrar_historial()

    @classmethod
    def obtener_indice_valido(cls, usuario):
        """Obtiene un índice válido de nota para operar, validando la entrada."""
        while True:
            try:
                id_nota = int(input("Ingrese el ID de la nota: "))
                nota = cls.obtener_nota_por_indice(usuario, id_nota)
                if nota:
                    return id_nota
            except ValueError:
                print("Entrada no válida. Debe ingresar un número entero.")
                continue
            print("ID no válido o no pertenece a sus notas.")
            return None

    @classmethod
    def obtener_nota_por_indice(cls, usuario, id_nota):
        """Obtiene una nota específica por el ID."""
        nota = cls.notas.get(id_nota)
        if nota and nota.usuario == usuario:
            return nota
        print("Nota no encontrada.")
        return None

    def editar_titulo(self, nuevo_titulo):
        """Edita el título de la nota."""
        self.titulo = nuevo_titulo
        self.fecha_modificacion = datetime.now()

    def editar_contenido(self, nuevo_contenido):
        """Edita el contenido de la nota."""
        self.contenido = nuevo_contenido
        self.fecha_modificacion = datetime.now()

    def agregar_etiqueta(self, etiqueta):
        """Agrega una etiqueta a la nota si no está presente."""
        if etiqueta not in self.etiquetas:
            self.etiquetas.append(etiqueta)

    def eliminar_etiqueta(self, etiqueta):
        """Elimina una etiqueta de la nota si está presente."""
        if etiqueta in self.etiquetas:
            self.etiquetas.remove(etiqueta)
