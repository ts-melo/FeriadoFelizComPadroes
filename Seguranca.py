class ProxyPagamento:
    def __init__(self, pagamento, usuario):
        self.pagamento = pagamento
        self.autenticado = usuario

    def processar(self, valor):
        if self.autenticado:
            self.pagamento_real.processar(valor)
        else:
            print("Acesso negado. Usuário não autenticado.")