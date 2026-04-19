
from AdapterValida import AdaptadorDocumento, ValidadorAntigo
from Configuracao import ConfiguracaoSistema
from PagamentoFactory import PagamentoFactory
from EstrategiaDesconto import DescontoPix, SemDesconto
from extras import SeguroFraudeDecorator
from Seguranca import ProxyPagamento
from Eventos import MonitorVendas

class SistemaCheckout:

    def realizar_pagamento(self, tipo, valor, documento, user):

        config = ConfiguracaoSistema()

        validador = AdaptadorDocumento(ValidadorAntigo())
        if not validador.validar(documento):
            print("Documento inválido.")
            return
        
        metodo = PagamentoFactory.criar_pagamento(tipo)
        if tipo == "pix":
            estrategia = DescontoPix()
            valor = estrategia.aplicar(valor)
        else:
            estrategia = SemDesconto()
            valor = estrategia.aplicar(valor)
        
        pagamento_seguro = SeguroFraudeDecorator(metodo)
        final = ProxyPagamento(pagamento_seguro, user)

        final.processar(valor)

        monitor = MonitorVendas()
        monitor.notificar(f"Venda realizada: {tipo} - R${valor:.2f}")
        monitor.notificar(f"Venda realizada: {tipo} - R${valor:.2f}")
    
