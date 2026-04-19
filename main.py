from CheckoutFacade import SistemaCheckout

def rodar_sistema():
    print("iniciando sistema de checkout...")
    checkout = SistemaCheckout()
    ##tudo certo
    res1 = checkout.realizar_pagamento("pix", 100.0, "12345678900", True)
    print("-"*30)
    ##n logado
    res2 = checkout.realizar_pagamento("cartao", 200.0, "12345678900", False)

if __name__ == "__main__":
    rodar_sistema()
