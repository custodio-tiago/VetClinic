import tkinter as tk
from tkinter import PhotoImage
from splash_screen import SplashScreen
from animal_management import AnimalManagement
from veterinarian_management import VeterinarianManagement
from consultation_management import ConsultationManagement
from utils import load_image


def center_window(window, width, height):
    """Centraliza uma janela na tela."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def open_window(window_class):
    window_class()


class VetClinicApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TLC VET")
        self.root.geometry("670x400")
        self.root.iconbitmap("images/cat.ico")  # Define o ícone da janela

        # Centralizar a janela principal
        center_window(self.root, 670, 400)

        # Criação dos botões
        buttons_data = [
            ("Cadastrar Animal", "button1.png", lambda: AnimalManagement.register_animal()),
            ("Abrir Consulta", "button2.png", lambda: ConsultationManagement.register_consultation()),
            ("Cadastrar Veterinário", "button3.png", lambda: VeterinarianManagement.register_veterinarian()),
            ("Olhar Consultas", "button4.png", lambda: ConsultationManagement.view_consultations()),
            ("Olhar Animais", "button5.png", lambda: AnimalManagement.view_animals()),
            ("Olhar Veterinários", "button6.png", lambda: VeterinarianManagement.view_veterinarians()),
        ]

        for i, (text, img, action) in enumerate(buttons_data):
            image = load_image(f"images/{img}", (190, 140))
            btn = tk.Button(
                self.root,
                text=text,
                image=image,
                compound="top",
                command=lambda action=action: open_window(action)
            )
            btn.image = image  # Mantém referência para a imagem
            btn.grid(row=i // 3, column=i % 3, padx=10, pady=10)

        self.root.mainloop()


if __name__ == "__main__":
    SplashScreen()
    VetClinicApp()
