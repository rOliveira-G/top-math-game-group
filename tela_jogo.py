import tkinter as tk
from utilitarios import resetaTela
from logica_jogo import DadosFuncionais

class TelaJogo:
    def __init__(self, root):
        self.root = root


        
    def frameTelaJogo(self, root, partida, pontuacao):
        num1, num2 = DadosFuncionais.gerarNumeros()
        operador = DadosFuncionais.selecionarOperador()
        resultado = DadosFuncionais.calcularResultado(num1, num2, operador)

        resetaTela(self.root)
        self.root.title("The Math Game")
        cabecalho = tk.Frame(self.root)
        cabecalho.pack(pady=10)
        tk.Label(cabecalho, text="Pontuação:").grid(row=0, column=0, padx=10)
        tk.Label(cabecalho, text="0").grid(row=0, column=1, padx=10)
        botao_parar = tk.Button(cabecalho, text="Parar", font=("Arial", 10), command=lambda: self.pararJogo(root))
        botao_parar.grid(row=0, column=6, padx=10)
        numeros_frame = tk.Frame(self.root)
        numeros_frame.pack(pady=40)
        tk.Label(numeros_frame, text=str(num1), font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text="?", font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text=str(num2), font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(numeros_frame, text="=", font=("Arial", 32)).pack(side="left", padx=10)
        tk.Label(numeros_frame, text=str(resultado), font=("Arial", 32)).pack(side="left", padx=10)
        
        operacoes_frame = tk.Frame(self.root)
        operacoes_frame.pack(pady=30)
        
        for operacao in ["+", "-", "*", "/"]:
            tk.Button(operacoes_frame, text=operacao, font=("Arial", 16), width=5, height=5).pack(side="left", padx=10)