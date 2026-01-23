import mysql.connector
from dotenv import load_dotenv
import os
from model.produto import Produto

load_dotenv()


class Produto_DAO:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.conn.cursor()

    def save(self, produto: Produto):
        sql = """
        INSERT INTO produto (nome, valor, estoque)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(sql, (produto.nome, produto.valor, produto.estoque))
        self.conn.commit()

        produto._id = self.cursor.lastrowid
        return produto

    def get_all(self):
        self.cursor.execute("SELECT * FROM produto")
        rows = self.cursor.fetchall()

        produtos = []
        for row in rows:
            p = Produto(row[1], float(row[2]), row[3])
            p._id = row[0]
            produtos.append(p)
        return produtos

    def get_by_id(self, produto_id):
        self.cursor.execute("SELECT * FROM produto WHERE id = %s", (produto_id,))
        row = self.cursor.fetchone()

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
        self.cursor.execute(
            sql,
            (produto.nome, produto.valor, produto.estoque, produto.id)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete(self, produto_id):
        self.cursor.execute("DELETE FROM produto WHERE id=%s", (produto_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0
