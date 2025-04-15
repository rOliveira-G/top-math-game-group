import tkinter as tk
from utilitarios import resetaTela

class TelaInicial:
    def __init__(self, root):
        self.root = root
        resetaTela(self.root)
        self.root.title("The Math Game - Abertura")

    def frameTelaInicial(self):
        titulo = tk.Label(
            self.root,
            text="The Math Game",
            font=("Arial", 32, "bold"),
            fg="blue"
        )
        titulo.pack(pady=60)
        
        botao_intructions = tk.Button(
            self.root,
            text="Instructions",
            font=("Arial", 16),
            bg="green",
            fg="white",
            padx=20,
            pady=10,
            command=self.abrirInstrucoes
        )
        botao_intructions.pack(pady=20)
        
        botao_play = tk.Button(
            self.root,
            text="Play",
            font=("Arial", 16),
            bg="green",
            fg="white",
            padx=20,
            pady=10,
            command=self.abrirJogo
        )
        botao_play.pack(pady=20)
        
        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: Adrian Roberti, Pedro Henrique e Yan Heindrick (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)
    
    def abrirInstrucoes(self):
        from tela_instrucoes import TelaInstrucoes
        tela_inf = TelaInstrucoes(self.root)
        tela_inf.frameTelaInstrucoes()
        
    def abrirJogo(self):
        from tela_jogo import TelaJogo
        tela_jogo = TelaJogo(self.root)
        tela_jogo.frameTelaJogo()
