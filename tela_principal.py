import tkinter as tk
from tkinter import messagebox

#instale pygame se n tiver
def framePrincipal():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("The Math Game")
    root.resizable(False, False)

    root.continua_jogo = tk.BooleanVar(value=False)
    root.running = True

    def funcao_fechar():
        if messagebox.askyesno("Confirmação", "Você realmente deseja sair do jogo?"):
            root.running = False
            root.continua_jogo.set(True)
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", funcao_fechar)

    return root

if __name__ == "__main__":
    root = framePrincipal()
    from tela_abertura import TelaAbertura
    tela_inicial = TelaAbertura(root)
    tela_inicial.frameTelaAbertura()

    try:
        root.mainloop()
    except Exception as e:
        print(f"Erro durante a execução: {e}")