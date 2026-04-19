from abc import ABC, abstractmethod

class EstrategiaDesconto(ABC):
    @abstractmethod
    def aplicar(self, valor):
        pass

class DescontoPix(EstrategiaDesconto):
    def aplicar(self, valor):
        return valor * 0.90  # Aplica um desconto de 10%
    
class SemDesconto(EstrategiaDesconto):
    def aplicar(self, valor):
        return valor  # Sem desconto, retorna o valor original
    