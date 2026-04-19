class SeguroFraudeDecorator:
    def __init__(self, pagamento_decorado):
        self.pagamento = pagamento_decorado

    def processar(self, valor):
        valor_com_seguro = valor * 1.1  # Adiciona 10% de seguro
        print(f"Valor com seguro: {valor_com_seguro}")
        self.pagamento.processar(valor_com_seguro)