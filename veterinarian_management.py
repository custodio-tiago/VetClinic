import tkinter as tk
from tkinter import simpledialog, messagebox
from utils import save_data, load_data, create_table_window


class VeterinarianManagement:
    @staticmethod
    def register_veterinarian():
        name = simpledialog.askstring("Cadastrar Veterinário", "Nome do Veterinário:")
        if not name:
            return
        specialty = simpledialog.askstring("Cadastrar Veterinário", "Especialidade:")
        save_data("data/veterinarios.txt", f"{name},{specialty}")
        messagebox.showinfo("Cadastro", "Veterinário cadastrado com sucesso!")

    @staticmethod
    def view_veterinarians():
        data = load_data("data/veterinarios.txt")
        create_table_window("Veterinários Cadastrados", data, "data/veterinarios.txt")
