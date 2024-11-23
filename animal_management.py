import tkinter as tk
from tkinter import simpledialog, messagebox
from utils import save_data, load_data, create_table_window


class AnimalManagement:
    @staticmethod
    def register_animal():
        name = simpledialog.askstring("Cadastrar Animal", "Nome do Animal:")
        if not name:
            return
        animal_type = simpledialog.askstring("Cadastrar Animal", "Tipo (Cachorro, Gato, etc):")
        age = simpledialog.askinteger("Cadastrar Animal", "Idade:")
        observations = simpledialog.askstring("Cadastrar Animal", "Observações:")
        save_data("data/animais.txt", f"{name},{animal_type},{age},{observations}")
        messagebox.showinfo("Cadastro", "Animal cadastrado com sucesso!")

    @staticmethod
    def view_animals():
        data = load_data("data/animais.txt")
        create_table_window("Animais Cadastrados", data, "data/animais.txt")
