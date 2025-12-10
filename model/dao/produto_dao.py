from model.produto import Produto

class Produto_DAO:
    def __init__(self):
        self._produtos = []   # usa underline
        self.next_id = 1

    def save(self, produto):
        if produto._id is None:
            produto._id = self.next_id
            self.next_id += 1

        self._produtos.append(produto)
        return produto

    def update(self, produto_atualizado):
        for i, p in enumerate(self._produtos):
            if p._id == produto_atualizado._id:
                self._produtos[i] = produto_atualizado
                return produto_atualizado
        return None

    def delete(self, id_produto):
        for p in self._produtos:
            if p._id == id_produto:
                self._produtos.remove(p)
                return True
        return False

    def find_all(self):
        return self._produtos

    def find_by_id(self, id_produto):
        for p in self._produtos:
            if p._id == id_produto:
                return p
        return None


def update(self, novo_produto:Produto):
        produto = self.get_by_id(novo_produto._id)
        if produto:
            produto._nome = novo_produto._nome
            produto._valor = novo_produto._valor
            produto._estoque = novo_produto._estoque
            return True
        return False

