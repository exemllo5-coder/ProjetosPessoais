import mysql.connector

class Base_DAO:
    def __init__(self, db_config):
        self.conexao = mysql.connector.connect(**db_config)
        self.cursor = self.conexao.cursor()

    def executar(self, sql, valores=None):
        if valores:
            self.cursor.execute(sql, valores)
        else:
            self.cursor.execute(sql)
        self.conexao.commit()

    def buscar_um(self, sql, valores=None):
        if valores:
            self.cursor.execute(sql, valores)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchone()

    def buscar_todos(self, sql, valores=None):
        if valores:
            self.cursor.execute(sql, valores)
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchall()
