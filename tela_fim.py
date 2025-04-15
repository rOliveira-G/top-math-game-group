import tkinter as tk
from utilitarios import resetaTela

class TelaFim:
    def __init__(self, root, pontuacao):
        self.root = root
        self.pontuacao = pontuacao
        
    def frameTelaFim(self):
        resetaTela(self.root)
        
        titulo = tk.Frame(self.root)
        titulo.pack(side="top", pady=10)
        
        titulo = tk.Label(
            titulo,
            text="The Math Game",
            font=("Arial", 32, "bold"),
            fg="blue"
        )
        titulo.pack(side="top",pady=10)
        
        tk.Label(self.root, text="Jogo Finalizado!", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.root, text=f"Pontuação final: {self.pontuacao}", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.root, text="Novo Jogo", font=("Arial", 24), bg="green", fg="white", command=self.abrirTelaJogo).pack(pady=20)
        tk.Button(self.root, text="Instruções", font=("Arial", 24), bg="green", fg="white", command=self.abrirInstrucoes).pack(pady=20)

        tk.Label(
            self.root,
            text="Desenvolvido por: Adrian Roberti, Pedro Henrique e Yan Heindrick (Senai Betim 2025)",
            font=("Arial", 8)
        ).pack(side="bottom", pady=10)

    def abrirTelaJogo(self):
        from tela_jogo import TelaJogo
        tela_jogo = TelaJogo(self.root)
        tela_jogo.frameTelaJogo()
        
    def abrirInstrucoes(self):
        from tela_instrucoes import TelaInstrucoes
        tela_inf = TelaInstrucoes(self.root)
        tela_inf.frameTelaInstrucoes()