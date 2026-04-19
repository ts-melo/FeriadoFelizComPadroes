class MonitorVendas:
    def __init__(self):
        self._observadores = []

    def adicionar(self, observador):
        self._observadores.append(observador)

    def notificar(self, mensagem):
        for observador in self._observadores:
            observador.atualizar(mensagem)

class DepartamentoLogistica:
    def atualizar(self, mensagem):
        print(f"[LOGISTICA] preparando envio: {mensagem}")
        