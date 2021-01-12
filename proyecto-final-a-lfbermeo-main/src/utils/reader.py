class ReaderData(object):
    """
    Clase que implemtan metodos para la lectura, procesamiento y obtencion de la informacion dentro de un csv
    """

    def __init__(self, dataPath: str) -> None:
        super().__init__()

        self._dataPath = dataPath
