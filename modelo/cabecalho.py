class Cabecalho:

    def __init__(self):
        self.identificador = None
        self.titulo = None
        self.data = None

    def preencher_objeto_cabecalho(self, linhas_separadas):
        self.titulo = linhas_separadas[1]
        self.data = linhas_separadas[2]
