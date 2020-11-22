class DireccionDesconocidaExcepcion(Exception):
    """
    Clase de Excepcion de direccion de memoria inexistente
    """

    def __init__(self, dir):
        """
        Clase de Excepcion de direccion de memoria inexistente

        Parameters:
            dir(str): Nombre de la direccion de memoria
        """
        self.error = "No se reconoce la direccion de memoria: '%s'" % dir

    def __str__(self):
        """
        Metodo toString
        """
        return self.error
