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
        texto = tk.Label(
            self.root,
            text="O jogo ira mostrar uma tela com uma equação matematica com o operador faltando,\nvocê tem que acertar qual o operador faltante para ganhar pontos",
            font=("Arial", 14),
            fg="black")
        texto.pack(pady=20)
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
    
    def abrirJogo(self):
        tela_jogo = TelaJogo(self.root)
        tela_jogo.frameTelaJogo()