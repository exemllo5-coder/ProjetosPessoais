from model.dao.produto_dao_mysql import Produto_DAO
from view.produto_gui import Produto_View
from control.produto_controller import Produto_Controller   
from dotenv import load_dotenv
import os


DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

def main():
    produto_dao = Produto_DAO(DB_CONFIG)
    produto_view = Produto_View()
    produto_controller = Produto_Controller(produto_dao, produto_view)
    produto_view.run()

if __name__ == "__main__":
    main()
