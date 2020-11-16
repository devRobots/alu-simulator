class DireccionDesconocidaExcepcion(Exception):
    """
    Clase de Excepcion de direccion de memoria inexistente
    """

    def __init__(self, dir):
        """
        docstring
        """
        self.error = "No se reconoce la direccion de memoria: '%s'" % dir

    def __str__(self):
        """
        docstring
        """
        return self.error
