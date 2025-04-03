import tkinter as tk
from tela_instrucoes import TelaInstrucoes

class TelaInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("The Math Game")

    def frameTelaInicial(self):

    
    #titulo que vai aparecer grande na tela (tk.Label)
    #botão de play (tk.Button)
    #o button deve ter um command para chamar a tela de instruções

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: João Silva e Maria Souza (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

        self.root.mainloop()
