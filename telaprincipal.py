import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def mainScreen():
    # Create the main window
    root = tk.Tk()
    root.title("The Math Game")
    root.geometry("800x600")
    
    root.resizable(False, False)
    root.continua_jogo = tk.BooleanVar(value=False)
    root.running = True
    
    def closeScreen():
        if messagebox.askyesno("You really want to exit?"):
            root.running = False
            root.continua_jogo.set(True)
            root.destroy()
            
    root.protocol("WM_DELETE_WINDOW", closeScreen)
    return root
            
    root.mainloop()
    
window = mainScreen()

try:
    window.mainloop()
except Exception as e:
    print(f"Erro durante a execução: {e}")
