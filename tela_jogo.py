import tkinter as tk
from utilitarios import resetaTela
from logica_jogo import DadosFuncionais
import tela_instrucoes

class TelaJogo:
    def __init__(self, root):
        self.root = root
        self.pontuacao = 0
        self.partida = 1

    def frameTelaJogo(self):
        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: Adrian Roberti, Pedro Henrique e Yan Heindrick (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)
        
        if self.partida <= 20:
            num1, num2 = DadosFuncionais.gerarNumeros()
            operador = DadosFuncionais.selecionarOperador()
            resultado = DadosFuncionais.calcularResultado(num1, num2, operador)
            
            resetaTela(self.root)
            self.root.title("The Math Game - Jogo")
            
            cabecalho = tk.Frame(self.root)
            cabecalho.pack(pady=10)
            
            # Exibição da pontuação
            tk.Label(cabecalho, text="Pontuação:").grid(row=2, column=0, padx=10)
            tk.Label(cabecalho, text=str(self.pontuacao)).grid(row=2, column=1, padx=10)
            
            # Exibição da partida
            tk.Label(cabecalho, text="Partida:").grid(row=3, column=0, padx=10)
            tk.Label(cabecalho, text=str(self.partida)).grid(row=3, column=1, padx=10)
            
            # Botão de parar o jogo
            botao_parar = tk.Button(cabecalho, text="Instruções", font=("Arial", 10), command=self.abrirInstrucoes)
            botao_parar.grid(row=1, column=0, padx=0)
            
            # Exibição dos números e operação
            numeros_frame = tk.Frame(self.root)
            numeros_frame.pack(pady=40)
            tk.Label(numeros_frame, text=str(num1), font=("Arial", 32)).pack(side="left", padx=20)
            tk.Label(numeros_frame, text="?", font=("Arial", 32)).pack(side="left", padx=20)
            tk.Label(numeros_frame, text=str(num2), font=("Arial", 32)).pack(side="left", padx=20)
            tk.Label(numeros_frame, text="=", font=("Arial", 32)).pack(side="left", padx=10)
            tk.Label(numeros_frame, text=str(resultado), font=("Arial", 32)).pack(side="left", padx=10)
            
            # Exibição dos botões de operação
            operacoes_frame = tk.Frame(self.root)
            operacoes_frame.pack(pady=30)
            
            for operacao in ["+", "-", "*", "/"]:
                tk.Button(operacoes_frame, text=operacao, font=("Arial", 16), width=5, height=5, 
                          command=lambda op=operacao: self.verificarResposta(op, operador)).pack(side="left", padx=10)
            
            rodape = tk.Label(
            self.root,
            text="Desenvolvido por: Adrian Roberti, Pedro Henrique e Yan Heindrick (Senai Betim 2025)",
            font=("Arial", 8)
            )
            rodape.pack(side="bottom", pady=10)
            
        else:
            self.finalizarJogo()

    def verificarResposta(self, operacaoEsc, operacaoCorreta):
        if operacaoEsc == operacaoCorreta:
            self.pontuacao += 1
        self.partida += 1
        self.frameTelaJogo()

    def abrirInstrucoes(self):
        tela_inf = tela_instrucoes.TelaInstrucoes(self.root)
        tela_inf.frameTelaInstrucoes()

    def finalizarJogo(self):
        resetaTela(self.root)
        
        tk.Label(self.root, text="Jogo Finalizado!", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.root, text=f"Pontuação final: {self.pontuacao}", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.root, text="Novo Jogo", command=self.reiniciarJogo).pack(pady=10)
        tk.Button(self.root, text="Instruções", command=self.abrirInstrucoes).pack(pady=10)

        tk.Label(
            self.root,
            text="Desenvolvido por: Adrian Roberti, Pedro Henrique e Yan Heindrick (Senai Betim 2025)",
            font=("Arial", 8)
        ).pack(side="bottom", pady=10)

    def reiniciarJogo(self):
        self.pontuacao = 0
        self.partida = 1
        self.frameTelaJogo()
