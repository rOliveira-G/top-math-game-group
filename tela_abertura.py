import tkinter as tk
from tela_instrucoes import TelaInstrucoes 
from utilitarios import resetaTela

class TelaInicial:
    def __init__(self, root):
        self.root = root
        resetaTela(self.root)
        self.root.title("The Math Game")

    def frameTelaInicial(self):    
        titulo = tk.Label(
            self.root,
            text="The Math Game",
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
            command=self.abrirInstrucoes
        )
        botao_play.pack(pady=20)
        
        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: Adrian Roberti, Pedro Henrique e Yan Heindrick (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

        self.root.mainloop()
    
    def abrirInstrucoes(self):
        tela_inst = TelaInstrucoes(self.root)
        tela_inst.frameTelaInstrucoes()
