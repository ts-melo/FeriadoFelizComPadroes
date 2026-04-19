class ConfiguracaoSistema:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfiguracaoSistema, cls).__new__(cls)
            cls._instance.api_key = "TOKEN"
            cls._instance.ambiente = "PRODUCAO"
        return cls._instance