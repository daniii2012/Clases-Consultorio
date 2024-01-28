import uuid  # Para generar IDs únicos


class UsuarioPaciente:
    def __init__(self, nombre, datos_personales, historial_clinico):
        self.id = str(uuid.uuid4())  # Genera un ID único para el usuario
        self.nombre = nombre
        self.datos_personales = datos_personales
        self.historial_clinico = historial_clinico

    def registrar_cuenta(self):
        # Lógica para registrar la cuenta del usuario
        print(f"Cuenta registrada para {self.nombre} con ID: {self.id}")

    def gestionar_citas(self):
        # Lógica para gestionar citas del usuario
        print(f"Gestionando citas para {self.nombre}")


class SistemaGestionUsuarios:
    def __init__(self, base_de_datos, opciones_citas):
        self.base_de_datos = base_de_datos
        self.opciones_citas = opciones_citas

    def guardar_informacion(self, usuario):
        # Lógica para guardar información en la base de datos
        print(f"Guardando información del usuario {usuario.nombre} en {self.base_de_datos}")

    def controlar_acceso(self, usuario):
        # Lógica para controlar el acceso del usuario
        print(f"Controlando acceso para {usuario.nombre}")


class HistorialClinico:
    def __init__(self, antecedentes_clinicos, tratamiento, imagenes):
        self.antecedentes_clinicos = antecedentes_clinicos
        self.tratamiento = tratamiento
        self.imagenes = imagenes

    def llenar_antecedentes(self):
        # Lógica para llenar antecedentes clínicos
        print("Llenando antecedentes clínicos")

    def describir_tratamiento(self):
        # Lógica para describir el tratamiento
        print("Describiendo tratamiento")

    def incluir_imagenes(self):
        # Lógica para incluir imágenes en el historial clínico
        print("Incluyendo imágenes en el historial clínico")


class SistemaHistorialClinico:
    def __init__(self, base_de_datos, opciones_imagenes):
        self.base_de_datos = base_de_datos
        self.opciones_imagenes = opciones_imagenes

    def guardar_informacion(self, historial_clinico):
        # Lógica para guardar información en la base de datos
        print(f"Guardando información del historial clínico en {self.base_de_datos}")

    def notificar_doctor(self, paciente, mensaje):
        # Lógica para notificar al doctor sobre el historial clínico
        print(f"Notificando al doctor sobre el historial clínico de {paciente.nombre}: {mensaje}")


class PagoEnEfectivo:
    def __init__(self, total, recepcionista, tiempo):
        self.total = total
        self.recepcionista = recepcionista
        self.tiempo = tiempo

    def realizar_pago(self):
        # Lógica para realizar el pago en efectivo
        print(f"Realizando pago en efectivo de ${self.total}")

    def notificar_paciente(self):
        # Lógica para notificar al paciente sobre el pago
        print("Notificando al paciente sobre el pago")


class PagoConAseguradora:
    def __init__(self, total, aseguradora, recepcionista, tiempo):
        self.total = total
        self.aseguradora = aseguradora
        self.recepcionista = recepcionista
        self.tiempo = tiempo

    def realizar_pago(self):
        # Lógica para realizar el pago con aseguradora
        print(f"Realizando pago con aseguradora {self.aseguradora} de ${self.total}")

    def verificar_aseguradora(self):
        # Lógica para verificar la aseguradora
        print(f"Verificando aseguradora: {self.aseguradora}")

    def notificar_aseguradora(self):
        # Lógica para notificar a la aseguradora sobre el pago
        print(f"Notificando a {self.aseguradora} sobre el pago")


class SistemaPago:
    def procesar_pago(self, pago):
        # Lógica para procesar el pago
        pago.realizar_pago()
        # Lógica adicional si es necesario

    def notificar_error_pago(self, mensaje):
        # Lógica para notificar un error en el pago
        print(f"Error en el pago: {mensaje}")

    def registrar_pago_en_base_de_datos(self, pago):
        # Lógica para registrar el pago en la base de datos
        print(f"Registrando pago en la base de datos")


class SistemaPrincipal:
    def __init__(self):
        # Creamos instancias de cada subsistema
        self.subsistema_gestion_usuarios = SistemaGestionUsuarios("BaseDeDatosGestionUsuarios", "OpcionesCitas")
        self.subsistema_historial_clinico = SistemaHistorialClinico("BaseDeDatosHistorialClinico", "OpcionesImagenes")
        self.subsistema_pago = SistemaPago()

    def iniciar_sistema(self):
        # Lógica para iniciar el sistema y cargar subsistemas
        print("Sistema iniciado")

    def procesar_solicitud_registro(self, usuario):
        usuario.registrar_cuenta()
        self.subsistema_gestion_usuarios.guardar_informacion(usuario)
        self.subsistema_gestion_usuarios.controlar_acceso(usuario)

    def procesar_solicitud_gestion_citas(self, usuario):
        # Lógica para coordinar la gestión de citas
        usuario.gestionar_citas()

    def procesar_solicitud_historial_clinico(self, usuario):
        # Lógica para coordinar la gestión del historial clínico
        historial_clinico = HistorialClinico("Antecedentes", "Tratamiento", "Imagen1, Imagen2")
        historial_clinico.llenar_antecedentes()
        historial_clinico.describir_tratamiento()
        historial_clinico.incluir_imagenes()

        self.subsistema_historial_clinico.guardar_informacion(historial_clinico)
        self.subsistema_historial_clinico.notificar_doctor(usuario, "Nuevo historial clínico disponible")

    def procesar_solicitud_pago(self, pago):
        self.subsistema_pago.procesar_pago(pago)
        # Lógica adicional si es necesario


# Ejemplo de uso
sistema_principal = SistemaPrincipal()
usuario = UsuarioPaciente("Juan", "Datos personales", "Historial clínico")
pago_efectivo = PagoEnEfectivo(100, "Recepcionista1", "10:00 AM")

sistema_principal.iniciar_sistema()
sistema_principal.procesar_solicitud_registro(usuario)
sistema_principal.procesar_solicitud_pago(pago_efectivo)

