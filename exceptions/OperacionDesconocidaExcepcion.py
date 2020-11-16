class OperacionDesconocidaExcepcion(Exception):
    """
    Clase de Excepcion de operacion desconocida
    """

    def __init__(self, operacion):
        """
        docstring
        """
        self.error = "No se reconoce la operacion: '%s'" % operacion

    def __str__(self):
        """
        docstring
        """
        return self.error
