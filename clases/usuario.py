import re

class Usuario:
    usuarios = []  # Lista de usuarios registrados

    def __init__(self, id_usuario, nombre_usuario, correo_electronico, contrasena):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.notas = []  # Lista para almacenar las notas del usuario
        self.administrador_grupo = False

    @staticmethod
    def es_id_usuario_unico(id_usuario):
        """Verifica que el ID de usuario sea único."""
        return all(usuario.id_usuario != id_usuario for usuario in Usuario.usuarios)

    @staticmethod
    def es_nombre_usuario_unico(nombre_usuario):
        """Verifica que el nombre de usuario sea único."""
        return all(usuario.nombre_usuario != nombre_usuario for usuario in Usuario.usuarios)

    @staticmethod
    def es_correo_valido(correo_electronico):
        """Validación básica del formato del correo electrónico."""
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, correo_electronico) is not None

    @staticmethod
    def es_correo_unico(correo_electronico):
        """Verifica que el correo electrónico sea único."""
        return all(usuario.correo_electronico != correo_electronico for usuario in Usuario.usuarios)

    @staticmethod
    def es_contrasena_valida(contrasena):
        """Verifica que la contraseña tenga entre 4 y 12 caracteres."""
        return 4 <= len(contrasena) <= 12

    @staticmethod
    def ingresar_contrasena():
        """Usa input temporalmente para capturar la contraseña sin ocultarla."""
        contrasena = input("Ingrese contraseña (4-12 caracteres): ")
        return contrasena

    @staticmethod
    def solicitar_id_valido():
        """Solicita un ID de usuario válido, que solo contiene números."""
        while True:
            id_usuario = input("Ingrese ID de usuario (7-10 caracteres, solo números): ")
            if not re.match(r'^\d{7,10}$', id_usuario):
                print("Formato de ID no válido. Debe tener entre 7 y 10 caracteres y solo incluir números.")
            else:
                return id_usuario

    @staticmethod
    def solicitar_correo_valido():
        """Solicita un correo válido."""
        while True:
            correo_electronico = input("Ingrese correo electrónico: ")
            if not Usuario.es_correo_valido(correo_electronico):
                print("Formato de correo electrónico no válido. Intente de nuevo.")
            else:
                return correo_electronico

    @staticmethod
    def solicitar_nombre_usuario_valido():
        """Solicita un nombre de usuario válido."""
        while True:
            nombre_usuario = input("Ingrese nombre de usuario (8-16 caracteres): ")
            if len(nombre_usuario) < 8 or len(nombre_usuario) > 16:
                print("El nombre de usuario debe tener entre 8 y 16 caracteres.")
            else:
                return nombre_usuario

    @classmethod
    def registrar_usuario(cls):
        print("Ingrese los detalles del nuevo usuario")

        # Validación del ID de usuario
        id_usuario = cls.solicitar_id_valido()

        # Verificar si el ID de usuario es único
        if not cls.es_id_usuario_unico(id_usuario):
            print("El ID de usuario ya está en uso. Intente con otro ID.")
            return

        # Validación del nombre de usuario
        nombre_usuario = cls.solicitar_nombre_usuario_valido()

        # Verificar si el nombre de usuario es único
        if not cls.es_nombre_usuario_unico(nombre_usuario):
            print("El nombre de usuario ya está en uso. Intente con otro nombre.")
            return

        # Validación del correo electrónico
        correo_electronico = cls.solicitar_correo_valido()

        # Verificar si el correo electrónico es único
        if not cls.es_correo_unico(correo_electronico):
            print("El correo electrónico ya está en uso. Intente con otro correo.")
            return

        # Validación de la contraseña
        contrasena = cls.ingresar_contrasena()
        while not cls.es_contrasena_valida(contrasena):
            print("La contraseña debe tener entre 4 y 12 caracteres.")
            contrasena = cls.ingresar_contrasena()

        # Registrar nuevo usuario
        nuevo_usuario = cls(id_usuario, nombre_usuario, correo_electronico, contrasena)
        cls.usuarios.append(nuevo_usuario)

        print(f"Usuario '{nombre_usuario}' registrado con éxito.")
        print(f"Contraseña: {contrasena}")
        print("Puede iniciar sesión con sus nuevas credenciales.")

    @classmethod
    def iniciar_sesion(cls):
        print("Ingrese sus credenciales para iniciar sesión")

        # Solicitar nombre de usuario y verificar si está registrado
        usuario_encontrado = None
        while True:
            nombre_usuario = input("Nombre de usuario: ")
            usuario_encontrado = next((usuario for usuario in cls.usuarios if usuario.nombre_usuario == nombre_usuario),
                                      None)

            if usuario_encontrado is None:
                print("Nombre de usuario no registrado. Intente de nuevo.")
            else:
                break

        # Solicitar contraseña y verificar
        intentos_restantes = 3
        while intentos_restantes > 0:
            contrasena = cls.ingresar_contrasena()
            if usuario_encontrado.contrasena == contrasena:
                print(f"Inicio de sesión exitoso para {nombre_usuario}.")
                return usuario_encontrado  # Devuelve el usuario autenticado
            else:
                intentos_restantes -= 1
                print(f"Contraseña incorrecta. Le quedan {intentos_restantes} intentos.")

        print("Ha excedido el número de intentos.")
        return None  # Devuelve None si la autenticación falla

    @classmethod
    def recuperar_contrasena(cls):
        print("=== Recuperación de Contraseña ===")
        id_usuario = cls.solicitar_id_valido()

        # Verificar si existe un usuario con ese ID
        usuario_encontrado = next((usuario for usuario in cls.usuarios if usuario.id_usuario == id_usuario), None)

        if usuario_encontrado is None:
            print("ID de usuario no encontrado. Verifique los datos.")
            return

        # Validación del correo electrónico asociado
        correo_electronico = cls.solicitar_correo_valido()

        if usuario_encontrado.correo_electronico != correo_electronico:
            print("Correo electrónico no coincide con el registrado.")
            return

        # Permitir cambiar la contraseña
        print("ID y correo verificados. Puede cambiar su contraseña.")
        nueva_contrasena = cls.ingresar_contrasena()
        while not cls.es_contrasena_valida(nueva_contrasena):
            print("La contraseña debe tener entre 4 y 12 caracteres.")
            nueva_contrasena = cls.ingresar_contrasena()

        usuario_encontrado.contrasena = nueva_contrasena
        print("Contraseña actualizada con éxito.")
