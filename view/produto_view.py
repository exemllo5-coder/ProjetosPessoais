from model.produto import Produto
import sys


class Produto_View:
    def __init__(self):
        self.controller = None

    def show_menu(self):
        print("=== Menu de Produtos ===")
        print("1. Adicionar Produto")
        print("2. Atualizar Produto")
        print("3. Deletar Produto")
        print("4. Listar Produtos")
        print("5. Buscar Produto por ID")
        print("6. Sair")

    def get_user_choice(self):
        return input("Escolha uma opção: ")

    def run(self):
        while True:
            try:
                self.show_menu()
                choice = self.get_user_choice()
                if choice == "6":
                    print("Saindo do sistema...")
                    sys.exit()
                if self.controller:
                    self.controller.choice_processor(choice)
            except KeyboardInterrupt:
                print("\nSaindo do sistema...")
                break
            except Exception as e:
                self.show_error(str(e))

    def show_error(self, message):
        print(f"[ERRO]: {message}")

    def show_message(self, message):
        print(f"[INFO]: {message}")

    def get_nome(self, default_nome=""):
        return input(f"Nome [{default_nome}]: ") or default_nome

    def get_valor(self, default_valor=0.0):
        while True:
            valor_input = input(f"Valor [{default_valor:.2f}]: ") or str(default_valor)
            try:
                return float(valor_input.replace(",", "."))
            except ValueError:
                print("[ERRO] Valor deve ser um número!")

    def get_estoque(self, default_estoque=0):
        while True:
            estoque_input = input(f"Estoque [{default_estoque}]: ") or str(default_estoque)
            if estoque_input.isdigit():
                return int(estoque_input)
            print("[ERRO] Estoque deve ser um número inteiro!")

    def get_id(self):
        return int(input("ID do Produto: "))

    def get_dados_produto(self, produto=None):
        if produto is None:
            nome = self.get_nome()
            valor = self.get_valor()
            estoque = self.get_estoque()
        else:
            nome = self.get_nome(produto.nome)
            valor = self.get_valor(produto.valor)
            estoque = self.get_estoque(produto.estoque)

        return {
            "nome": nome,
            "valor": valor,
            "estoque": estoque
        }

    def show_produtos(self, produtos):
        if not produtos:
            print("Nenhum produto cadastrado.")
            return

        print("-" * 80)
        print(f"{'LISTA DE PRODUTOS':^80}")
        print("-" * 80)
        print(f"{'ID':<5} {'NOME':<20} {'VALOR':<12} {'ESTOQUE':<10} {'VALOR EM ESTOQUE':<20}")

        for produto in produtos:
            print(
                f"{produto.id:<5} "
                f"{produto.nome:<20} "
                f"R$ {produto.valor:<10.2f} "
                f"{produto.estoque:<10} "
                f"R$ {produto.valor_em_estoque:<20.2f}"
            )

    def show_produto_details(self, produto):
        if produto is None:
            print("Produto não encontrado.")
            return

        print("-" * 40)
        print(f"{'DETALHES DO PRODUTO':^40}")
        print("-" * 40)
        print(f"ID: {produto.id}")
        print(f"Nome: {produto.nome}")
        print(f"Valor: R$ {produto.valor:.2f}")
        print(f"Estoque: {produto.estoque}")
        print(f"Valor em Estoque: R$ {produto.valor_em_estoque:.2f}")
