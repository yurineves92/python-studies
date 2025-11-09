import tkinter as tk
from app import TodoApp

def main():
    """Função principal"""
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()