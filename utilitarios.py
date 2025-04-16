import tkinter as tk

def resetaTela(root):
    for widget in root.winfo_children():
        widget.destroy()
        
def abrirInstrucoes(root):
    from tela_instrucoes import TelaInstrucoes
    tela_inf = TelaInstrucoes(root)
    tela_inf.frameTelaInstrucoes()
    
def abrirJogo(root):
    from tela_jogo import TelaJogo
    tela_jogo = TelaJogo(root)
    tela_jogo.frameTelaJogo()
    
def abrirFim(root,pontuacao):
    from tela_fim import TelaFim
    telaFim = TelaFim(root,pontuacao)
    telaFim.frameTelaFim()
    
def mostraTitulo(root):
    titulo = tk.Frame(root)
    titulo.pack(side="top", pady=10)
    
    titulo = tk.Label(
        titulo,
        text="The Math Game",
        font=("Arial", 32, "bold"),
        fg="blue"
    )
    titulo.pack(side="top",pady=10)
    
def mostraRodape(root):
    rodape = tk.Frame(root)
    rodape.pack(side="bottom", pady=10)
    
    rodape = tk.Label(
        rodape,
        text="Desenvolvido por: Adrian Roberti, Pedro Henrique e Yan Heindrick (Senai Betim 2025)",
        font=("Arial", 8)
    )
    rodape.pack(side="bottom", pady=10)