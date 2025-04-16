import tkinter as tk
from utilitarios import resetaTela
from utilitarios import mostraTitulo
from utilitarios import mostraRodape
from utilitarios import abrirInstrucoes
from utilitarios import abrirJogo

class TelaAbertura:
    def __init__(self, root):
        self.root = root
        resetaTela(self.root)
        self.root.title("The Math Game - Abertura")

    def frameTelaAbertura(self):
        mostraTitulo(self.root)
        mostraRodape(self.root)
        
        botao_instrucoes = tk.Button( self.root, text="Instruções",
            font=("Arial", 16), bg="green", fg="white",
            padx=20, pady=10,
            command=lambda: abrirInstrucoes(self.root)
        )
        botao_instrucoes.pack(pady=20)
        
        botao_jogar = tk.Button( self.root, text="Jogar",
            font=("Arial", 16), bg="green", fg="white",
            padx=20, pady=10,
            command=lambda: abrirJogo(self.root)
        )
        botao_jogar.pack(pady=20)