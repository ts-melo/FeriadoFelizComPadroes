class PagamentoPix:
    def processar(self, valor):
        print(f"Processando pagamento via PIX no valor de R${valor:.2f}")

class PagamentoCartao:
    def processar(self, valor):
        print(f"Processando pagamento via Cartão de Crédito no valor de R${valor:.2f}")

class PagamentoDinheiro:
    def processar(self, valor):
        print(f"Processando pagamento em Dinheiro no valor de R${valor:.2f}")

class PagamentoFactory:
    @staticmethod
    def criar_pagamento(tipo):
        if tipo == "PIX":
            return PagamentoPix()
        elif tipo == "CARTAO":
            return PagamentoCartao()
        elif tipo == "DINHEIRO":
            return PagamentoDinheiro()
        else:
            raise ValueError("Tipo de pagamento desconhecido")