import re

class Usuario:
    usuarios = []  # Lista para almacenar usuarios registrados

    def __init__(self, id_usuario, nombre_usuario, correo_electronico, contrasena):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
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
    def es_contrasena_valida(contrasena):
        """Verifica que la contraseña tenga entre 4 y 12 caracteres."""
        return 4 <= len(contrasena) <= 12

    @staticmethod
    def ingresar_contrasena():
        """Usa input temporalmente para capturar la contraseña sin ocultarla."""
        contrasena = input("Ingrese contraseña (4-12 caracteres): ")
        return contrasena

    @classmethod
    def registrar_usuario(cls):
        print("Ingrese los detalles del nuevo usuario")

        # Validación del ID de usuario
        id_usuario = input("Ingrese ID de usuario (7-10 caracteres): ")
        while len(id_usuario) < 7 or len(id_usuario) > 10:
            print("El ID de usuario debe tener entre 7 y 10 caracteres.")
            id_usuario = input("Ingrese ID de usuario (7-10 caracteres): ")

        # Verificar si el ID de usuario es único
        if not cls.es_id_usuario_unico(id_usuario):
            print("El ID de usuario ya está en uso. Intente con otro ID.")
            return

        # Validación del nombre de usuario
        nombre_usuario = input("Ingrese nombre de usuario (8-16 caracteres): ")
        while len(nombre_usuario) < 8 or len(nombre_usuario) > 16:
            print("El nombre de usuario debe tener entre 8 y 16 caracteres.")
            nombre_usuario = input("Ingrese nombre de usuario (8-16 caracteres): ")

        # Verificar si el nombre de usuario es único
        if not cls.es_nombre_usuario_unico(nombre_usuario):
            print("El nombre de usuario ya está en uso. Intente con otro nombre.")
            return

        # Validación del correo electrónico
        correo_electronico = input("Ingrese correo electrónico: ")
        while not cls.es_correo_valido(correo_electronico):
            print("El formato del correo electrónico no es válido. Intente de nuevo.")
            correo_electronico = input("Ingrese correo electrónico: ")

        # Validación de la contraseña
        contrasena = cls.ingresar_contrasena()
        while not cls.es_contrasena_valida(contrasena):
            print("La contraseña debe tener entre 4 y 12 caracteres.")
            contrasena = cls.ingresar_contrasena()

        # Registrar nuevo usuario
        nuevo_usuario = cls(id_usuario, nombre_usuario, correo_electronico, contrasena)
        cls.usuarios.append(nuevo_usuario)

        # Mostrar la contraseña oculta con asteriscos
        print(f"Usuario '{nombre_usuario}' registrado con éxito.")
        print(f"Contraseña: {'*' * len(contrasena)}")
        print("Puede iniciar sesión con sus nuevas credenciales.")

    @classmethod
    def iniciar_sesion(cls):
        print("Ingrese sus credenciales para iniciar sesión")

        nombre_usuario = input("Nombre de usuario: ")
        contrasena = cls.ingresar_contrasena()

        for usuario in cls.usuarios:
            if usuario.nombre_usuario == nombre_usuario and usuario.contrasena == contrasena:
                print(f"Inicio de sesión exitoso para {nombre_usuario}.")
                return usuario  # Devuelve el usuario autenticado

        print("Nombre de usuario o contraseña incorrectos.")
        return None  # Devuelve None si la autenticación falla
