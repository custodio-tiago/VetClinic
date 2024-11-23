import tkinter as tk
from tkinter import PhotoImage
import random
from utils import load_image


def center_window(window, width, height):
    """Centraliza uma janela na tela."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


class SplashScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bem-vindo")
        self.root.geometry("400x200")
        self.root.overrideredirect(1)  # Remove a barra de título

        # Centralizar a splash screen
        center_window(self.root, 400, 200)

        # Adicionando imagem e texto
        img = load_image("images/Splash.png", (100, 100))
        lbl_img = tk.Label(self.root, image=img)
        lbl_img.image = img
        lbl_img.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

        tips = [
            "Cachorros precisam de água limpa diariamente!",
            "Gatos gostam de arranhadores para se divertir.",
            "Um check-up regular no veterinário é essencial.",
            "Brinque com seu animal para estimular sua saúde mental.",
            "Alimentação balanceada é essencial para a saúde!",
        ]

        tip = random.choice(tips)
        lbl_tip = tk.Label(self.root, text=f"Dica do dia:\n\n{tip}", wraplength=250, justify="left")
        lbl_tip.grid(row=0, column=1, sticky="w")

        btn_ok = tk.Button(self.root, text="OK", command=self.root.destroy)
        btn_ok.grid(row=1, column=1, sticky="e", padx=10, pady=10)

        self.root.mainloop()
