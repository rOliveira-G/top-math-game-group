import tkinter as tk
from utilitarios import resetaTela
from utilitarios import mostraTitulo
from utilitarios import mostraRodape
from utilitarios import abrirInstrucoes
from utilitarios import abrirJogo

class TelaFim:
    def __init__(self, root, pontuacao):
        self.root = root
        resetaTela(self.root)
        self.root.title("The Math Game - Fim")
        self.pontuacao = pontuacao
        
    def frameTelaFim(self):

        mostraTitulo(self.root)
        mostraRodape(self.root)
        
        tk.Label(self.root, text="Jogo Finalizado!", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.root, text=f"Pontuação final: {self.pontuacao}", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.root, text="Novo Jogo", font=("Arial", 24), bg="green", fg="white", command=lambda: abrirJogo(self.root)).pack(pady=20)
        tk.Button(self.root, text="Instruções", font=("Arial", 24), bg="green", fg="white", command=lambda: abrirInstrucoes(self.root)).pack(pady=20)