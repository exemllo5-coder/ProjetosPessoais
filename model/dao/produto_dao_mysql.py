from model.produto import Produto
from .base_dao import Base_DAO


class Produto_DAO(Base_DAO):
    def __init__(self, db_config):
        super().__init__(db_config)

    def save(self, produto: Produto):
        sql = """
        INSERT INTO produto (nome, valor, estoque)
        VALUES (%s, %s, %s)
        """
        self.executar(sql, (produto.nome, produto.valor, produto.estoque))
        produto._id = self.cursor.lastrowid
        return produto

    def get_all(self):
        rows = self.buscar_todos("SELECT * FROM produto")
        produtos = []

        for row in rows:
            p = Produto(row[1], float(row[2]), row[3])
            p._id = row[0]
            produtos.append(p)

        return produtos

    def get_by_id(self, produto_id):
        row = self.buscar_um(
            "SELECT * FROM produto WHERE id=%s",
            (produto_id,)
        )

        if row:
            p = Produto(row[1], float(row[2]), row[3])
            p._id = row[0]
            return p
        return None

    def update(self, produto: Produto):
        sql = """
        UPDATE produto
        SET nome=%s, valor=%s, estoque=%s
        WHERE id=%s
        """
        self.executar(sql, (produto.nome, produto.valor, produto.estoque, produto._id))
        return self.cursor.rowcount > 0

    def delete(self, produto_id):
        self.executar("DELETE FROM produto WHERE id=%s", (produto_id,))
        return self.cursor.rowcount > 0
