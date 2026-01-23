class Produto:
    _contador_id = 1

    def __init__(self, nome: str, valor: float, estoque: int):
        self._id = Produto._contador_id
        Produto._contador_id += 1

        self._nome = nome
        self._valor = valor
        self._estoque = estoque

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor

    @property
    def estoque(self):
        return self._estoque

    @property
    def valor_em_estoque(self):
        return self._valor * self._estoque
