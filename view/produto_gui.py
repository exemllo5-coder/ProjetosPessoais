import tkinter as tk
from tkinter import messagebox, ttk

class Produto_View:
    def __init__(self):
        self.controller = None
        self.root = tk.Tk()
        self.root.title("Gerenciamento de Produtos")
        self.root.geometry = ("1200x600")

        self.var_id = tk.StringVar()
        self.var_nome = tk.StringVar()
        self.var_valor = tk.StringVar()
        self.var_estoque = tk.StringVar()

        self._setup_ui()

    def _setup_ui(self):
        tk.Label(self.root, text="CONTROLE PRODUTOS", font=("Arial", 14, "bold"), pady=10).pack()

        frame_form = tk.Frame(self.root, text="Formulário de Produto", padx=10, pady=10)
        frame_form.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_form, text="ID:").grid(row=0, column=0, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_id, state="readonly", width=10, 
                 bg="#f0f0f0").grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        tk.Label(frame_form, text="Nome:").grid(row=0, column=2, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_nome, width=35).grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Valor:").grid(row=1, column=0, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_valor, width=15).grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(frame_form, text="Estoque:").grid(row=1, column=2, sticky="e")
        tk.Entry(frame_form, textvariable=self.var_estoque, width=15).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        frame_botoes = tk.Frame(self.root, pady=10)
        frame_botoes.pack()

        tk.Button(frame_botoes, text="SALVAR NOVO", command=self._acao_adicionar, bg="#4CAF50", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="ATUALIZAR", command=self._acao_atualizar, bg="#2196F3", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="DELETAR", command=self._acao_deletar, bg="#f44336", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="LIMPAR", command=self._acao_limpar, bg="#9E9E9E", width=15).pack(side=tk.LEFT, padx=5)

root.mainloop()







