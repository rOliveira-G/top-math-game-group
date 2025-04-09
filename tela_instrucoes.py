import tkinter as tk
from tela_jogo import TelaJogo
from utilitarios import resetaTela

class TelaInstrucoes:
    def __init__(self, root):
        self.root = root
        resetaTela(self.root)
        self.root.title("The Math Game - Instruções")
        
    def frameTelaInstrucoes(self):
        titulo = tk.Label(
            self.root,
            text="Instruções",
            font=("Arial", 32, "bold"),
            fg="blue"
        )
        titulo.pack(pady=60)
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
        
    
    def abrirJogo(self):
        tela_jogo = TelaJogo(self.root)
        tela_jogo.frameTelaJogo(self.root,0,0)