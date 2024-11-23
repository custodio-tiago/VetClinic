import tkinter as tk
from tkinter import PhotoImage
from splash_screen import SplashScreen
from animal_management import AnimalManagement
from veterinarian_management import VeterinarianManagement
from consultation_management import ConsultationManagement
from utils import load_image


def open_window(window_class):
    window_class()


class VetClinicApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistemaa de Clínica Veterinária")
        self.root.geometry("400x300")
        
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
            image = load_image(f"images/{img}", (50, 50))
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
