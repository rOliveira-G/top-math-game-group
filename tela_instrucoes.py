import tkinter as tk
from utilitarios import resetaTela
from utilitarios import mostraTitulo
from utilitarios import mostraRodape
from utilitarios import abrirJogo

class TelaInstrucoes:
    def __init__(self, root):
        self.root = root
        resetaTela(self.root)
        self.root.title("The Math Game - Instruções")
        
    def frameTelaInstrucoes(self):
        
        mostraTitulo(self.root)
        mostraRodape(self.root)
        
        texto = tk.Label(
            self.root,
            text="Bem vindo ao The Math Game, neste jogo você tera que acertar qual a operação matemática"
               "\nesta sendo realizada. Você podera escolher entre +, -, * e / que são as operações basi-"
               "\ncas soma, subtração, multiplicação e divisão respectivamente. Quanto mais rapido você"
               "\nresolver mais pontos ira ganhar, o jogo acaba na rodada 20. Boa sorte.",
            font=("Arial", 14),
            fg="black")
        texto.pack(pady=20)
        
        botao_jogar = tk.Button(
            self.root,
            text="Jogar",
            font=("Arial", 16),
            bg="green",
            fg="white",
            padx=20,
            pady=10,
            command=lambda: abrirJogo(self.root)
        )
        botao_jogar.pack(pady=20)