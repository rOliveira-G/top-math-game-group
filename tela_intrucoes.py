import tkinter as tk
from utilitarios import resetaTela

class TelaInstrucoes:
    def __init__(self, root):
        self.root = root
        resetaTela(self.root)
        self.root.title("The Math Game")
        
    def frameTelaInstrucoes():
        tk.Label()