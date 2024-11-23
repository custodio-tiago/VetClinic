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
        self.root.overrideredirect(1)  # Remove a barra de título

        # Dimensões ajustadas para caber os elementos
        splash_width = 500
        splash_height = 200
        center_window(self.root, splash_width, splash_height)

        # Adicionando imagem
        img = load_image("images/Splash.png", (120, 120))  # Aumentado o tamanho da imagem
        lbl_img = tk.Label(self.root, image=img)
        lbl_img.image = img
        lbl_img.grid(row=0, column=1, rowspan=2, padx=20, pady=10, sticky="e")  # Alinhado à direita

        # Adicionando a dica do dia
        tips = [
        "Cachorros precisam de água limpa diariamente!",
        "Gatos gostam de arranhadores para se divertir.",
        "Um check-up regular no veterinário é essencial.",
        "Brinque com seu animal para estimular sua saúde mental.",
        "Alimentação balanceada é essencial para a saúde!",
        "Leve seu pet para passeios regulares para manter a saúde física.",
        "Vacinas ajudam a prevenir doenças graves em animais.",
        "A carinha de um pet feliz é o melhor presente!",
        "Animais também precisam de descanso, não os sobrecarregue.",
        "Sempre mantenha os brinquedos do seu pet limpos e higienizados.",
        "Gatos adoram esconderijos, prepare um cantinho aconchegante.",
        "Gaste tempo com seu pet, ele é um membro da família!",
        "Animais podem sentir suas emoções, compartilhe o amor com eles.",
        "Compre ração de qualidade para garantir uma boa alimentação.",
        "Não se esqueça de escovar os dentes do seu cachorro!",
        "Cães são ótimos para animar os dias mais tristes.",
        "Gatos adoram um bom lugar para dormir, cuide do cantinho deles.",
        "Leve seu pet para consultas regulares com o veterinário.",
        "Animais sentem quando estamos tristes, e nos confortam.",
        "Pets adoram uma boa massagem, tente dar um carinho especial.",
        "Tenha sempre uma cama confortável para o seu animal de estimação.",
        "Cachorros podem aprender truques e se divertir muito fazendo isso!",
        "Alguns gatos amam água, outros não. Teste com calma!",
        "Cães adoram uma boa corrida, mas sempre respeite o limite deles.",
        "Não esqueça de cortar as unhas do seu pet regularmente.",
        "A amizade entre um animal e seu dono é um dos maiores presentes da vida.",
        "Você sabia que os cachorros podem até detectar doenças como o câncer?",
        "Quem resgata um animal, resgata um pedaço de sua própria alma.",
        "Bichos também têm personalidade, e cada um é especial do seu jeito.",
        "Seu pet vai sempre te amar, mesmo quando você estiver com mau humor.",
        "Leve o seu animal para passeios, mas lembre-se de levar sacolinhas para recolher o cocô!",
        "A maior alegria do mundo é ver seu pet correndo feliz pela casa.",
        "Cães entendem palavras, mas adoram o som da sua voz ao chamá-los!"
        ]


        tip = random.choice(tips)
        lbl_tip = tk.Label(
            self.root, 
            text=f"Dica do dia:\n\n{tip}", 
            wraplength=300, 
            justify="center", 
            font=("Arial", 12)
        )
        lbl_tip.grid(row=0, column=0, sticky="w", padx=20)

        # Botão OK abaixo de tudo
        btn_ok = tk.Button(self.root, text="OK", font=("Arial", 10), command=self.root.destroy)
        btn_ok.grid(row=2, column=0, columnspan=2, pady=20)  # Centralizado abaixo da dica e da imagem

        self.root.mainloop()
