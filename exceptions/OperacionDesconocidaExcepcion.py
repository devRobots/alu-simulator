class OperacionDesconocidaExcepcion(Exception):
    """
    Clase de Excepcion de operacion desconocida
    """

    def __init__(self, operacion):
        """
        Clase de Excepcion de operacion desconocida

        Parameters:
            operacion(str): Nombre de la operacion
        """
        self.error = "No se reconoce la operacion: '%s'" % operacion

    def __str__(self):
        """
        Metodo toString
        """
        return self.error
