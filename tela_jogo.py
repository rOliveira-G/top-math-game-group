import tkinter as tk
from utilitarios import resetaTela
from utilitarios import mostraTitulo
from utilitarios import mostraRodape
from utilitarios import abrirInstrucoes
from utilitarios import abrirFim
from logica_jogo import DadosFuncionais
import time



class TelaJogo:
    def __init__(self, root):
        self.root = root
        resetaTela(self.root)
        self.root.title("The Math Game - Jogo")
        self.pontuacao = 0
        self.partida = 1
        self.s, self.m = -1, 00
        self.tempo_id = None

    def frameTelaJogo(self):
        if self.tempo_id:
            self.root.after_cancel(self.tempo_id)
            self.tempo_id = None
        
        num1, num2 = DadosFuncionais.gerarNumeros()
        operador = DadosFuncionais.selecionarOperador()
        resultado = DadosFuncionais.calcularResultado(num1, num2, operador)
        
        resetaTela(self.root)
        
        mostraTitulo(self.root)
        mostraRodape(self.root)
        
        cabecalho = tk.Frame(self.root)
        cabecalho.pack(pady=10)
        
        # Exibição da pontuação
        tk.Label(cabecalho, text=f"Pontuação: {self.pontuacao}",font=("Arial", 10, "bold")).grid(row=0,column=0,padx=10)
        
        # Exibindo tempo 
        self.label_tempo = tk.Label(cabecalho, text=f"Tempo: {self.m:02d}:{self.s:02d}",font=("Arial", 10, "bold"))
        self.label_tempo.grid(row=0,column=1,pady=10)
        
        # Exibição da partida
        tk.Label(cabecalho, text=f"Partida: {self.partida}",font=("Arial", 10, "bold")).grid(row=0,column=2,padx=10)
        
        # Mostrar pontuação aumentando
        self.label_pontuacaoAumenta = tk.Label(cabecalho, text=f" ",font=("Arial", 20, "bold"), fg="green", width=5)
        self.label_pontuacaoAumenta.grid(row=1,column=0,padx=30)
        
        # Botão de voltar para as instrucoes
        botao_instrucoes = tk.Button(cabecalho, text="Instruções", font=("Arial", 15), bg="green", fg="white", command=self.abrirInstrucoes)
        botao_instrucoes.grid(row=1,column=1,padx=20)
        
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
        operacoes_frame.pack(padx=60)
        
        for operacao in ["+", "-", "*", "/"]:
            tk.Button(operacoes_frame, text=operacao, font=("Arial", 16), bg="green", fg="white", width=5, height=5, 
                        command=lambda op=operacao: self.verificarResposta(op, operador)).pack(side="left", padx=10, pady=10)
        
        self.aumentarTempo()
        
    def pontuacaoAnimada(self,texto):
        if hasattr(self, "label_pontuacaoAumenta") and self.label_pontuacaoAumenta.winfo_exists():
            self.root.after(0, lambda: self.label_pontuacaoAumenta.config(text=texto, fg="green"))
            self.root.after(500, lambda: self.label_pontuacaoAumenta.config(text=" ", fg="green"))

    def verificarResposta(self, operacaoEsc, operacaoCorreta):
        if self.tempo_id:
            self.root.after_cancel(self.tempo_id)
            self.tempo_id = None
        if operacaoEsc == operacaoCorreta:
            if self.m<1 and self.s<1:
                self.pontuacao += 6
                self.pontuacaoAnimada("+6 Pts")
            elif self.m<1 and self.s<3:
                self.pontuacao += 5
                self.pontuacaoAnimada("+5 Pts")
            elif self.m<1 and self.s<5:
                self.pontuacao += 3
                self.pontuacaoAnimada("+3 Pts")
            elif self.m<1 and self.s<10:
                self.pontuacao += 1
                self.pontuacaoAnimada("+1 Pts")
            else:
                self.pontuacaoAnimada("+0 Pts")
        else:
            self.pontuacao -= 1
            self.pontuacaoAnimada("-1 Pts")
            
        self.partida += 1
        self.s = -1
        self.m = 0
        if self.partida >= 21:
            self.abrirFim()
        else:
            self.frameTelaJogo()
        
    def aumentarTempo(self):
        self.s += 1
        if self.s == 60:
            self.m += 1
            self.s = 0
        if self.m == 99:
            self.root.destroy
            
        if hasattr(self, 'label_tempo') and self.label_tempo.winfo_exists():
            self.label_tempo.config(text=f"Tempo: {self.m:02d}:{self.s:02d}")


        # Repetir a função a cada 1000ms (1 segundo)
        self.tempo_id = self.root.after(1000, self.aumentarTempo)
        
    def abrirFim(self):
        #Função para parar o temporizador quando sair
        time.sleep(500)
        if self.tempo_id:
            self.root.after_cancel(self.tempo_id)
            self.tempo_id = None
        abrirFim(self.root,self.pontuacao)

    def abrirInstrucoes(self):
        #Função para parar o temporizador quando sair
        if self.tempo_id:
            self.root.after_cancel(self.tempo_id)
            self.tempo_id = None
        abrirInstrucoes(self.root)