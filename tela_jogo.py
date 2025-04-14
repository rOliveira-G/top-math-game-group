import tkinter as tk
from utilitarios import resetaTela
from logica_jogo import DadosFuncionais
from tkinter import messagebox
import tela_instrucoes

class TelaJogo:
    def __init__(self, root):
        self.root = root
        self.pontuacao = 0
        self.partida = 1
        self.s, self.m = 00, 00
        self.tempo_id = None

    def frameTelaJogo(self):
        if self.tempo_id:
            self.root.after_cancel(self.tempo_id)
            self.tempo_id = None
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
            tk.Label(cabecalho, text="Pontuação:").grid(row=1, column=0, padx=10)
            tk.Label(cabecalho, text=str(self.pontuacao)).grid(row=1, column=1, padx=10)
            
            # Exibindo tempo 
            self.label_tempo = tk.Label(cabecalho, text=f"Tempo: {self.m:02d}:{self.s:02d}")
            self.label_tempo.grid(row=1, column=2, pady=10)
            
            # Exibição da partida
            tk.Label(cabecalho, text="Partida:").grid(row=2, column=1, padx=10)
            tk.Label(cabecalho, text=str(self.partida)).grid(row=2, column=2, padx=10)
            
            # Botão de parar o jogo
            botao_parar = tk.Button(cabecalho, text="Instruções", font=("Arial", 10), command=self.abrirInstrucoes)
            botao_parar.grid(row=3, column=0, padx=0)
            
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
            
            self.aumentarTempo()
            
        else:
            self.finalizarJogo()

    def verificarResposta(self, operacaoEsc, operacaoCorreta):
        if operacaoEsc == operacaoCorreta:
            if self.m<1 and self.s<1:
                self.pontuacao += 6
            elif self.m<1 and self.s<5:
                self.pontuacao += 5
            elif self.m<1 and self.s<10:
                self.pontuacao += 3
            elif self.m<1 and self.s<30:
                self.pontuacao += 1
            else:
                self.m += 0.666
            if self.m>=2:
                messagebox.showinfo("Aviso:","Você é lento")
            
        self.partida += 1
        self.s = 0
        self.m = 0
        self.frameTelaJogo()
        
    def aumentarTempo(self):
        self.s += 1
        if self.s == 60:
            self.m += 1
            self.s = 0
        if self.m == 99:
            self.root.destroy
            
        if hasattr(self, 'label_tempo'):
            self.label_tempo.config(text=f"Tempo: {self.m:02d}:{self.s:02d}")

        # Repetir a função a cada 1000ms (1 segundo)
        self.tempo_id = self.root.after(1000, self.aumentarTempo)
        

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
