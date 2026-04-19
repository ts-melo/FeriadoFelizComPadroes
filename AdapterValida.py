class ValidadorAntigo:
    def check_old_format(self, doc):
        return len(doc) == 11
    

class AdaptadorDocumento:
    def __init__(self, legado):
        self.legado = legado
    
    def validar(self, doc):
        return self.legado.check_old_format(doc)