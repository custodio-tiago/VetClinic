import tkinter as tk
from tkinter import simpledialog, messagebox
from utils import save_data, load_data, create_table_window


class ConsultationManagement:
    @staticmethod
    def register_consultation():
        date = simpledialog.askstring("Abrir Consulta", "Data da Consulta (dd/mm/yyyy):")
        veterinarians = load_data("data/veterinarios.txt")
        animals = load_data("data/animais.txt")
        vet = simpledialog.askstring("Abrir Consulta", f"Escolha o Veterinário:\n\n{', '.join(veterinarians)}")
        animal = simpledialog.askstring("Abrir Consulta", f"Escolha o Animal:\n\n{', '.join(animals)}")
        description = simpledialog.askstring("Abrir Consulta", "Descrição da Consulta:")
        save_data("data/consultas.txt", f"{date},{vet},{animal},{description}")
        messagebox.showinfo("Cadastro", "Consulta cadastrada com sucesso!")

    @staticmethod
    def view_consultations():
        data = load_data("data/consultas.txt")
        create_table_window("Consultas Marcadas", data, "data/consultas.txt")
