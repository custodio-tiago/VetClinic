import tkinter as tk
from tkinter import messagebox
from utils import save_data, load_data, create_table_window


class AnimalManagement:
    @staticmethod
    def register_animal():
        def save_and_close():
            name = entry_name.get()
            animal_type = entry_type.get()
            age = entry_age.get()
            observations = entry_observations.get()
            if not name or not animal_type or not age:
                messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios.")
                return
            save_data("data/animais.txt", f"{name},{animal_type},{age},{observations}")
            messagebox.showinfo("Cadastro", "Animal cadastrado com sucesso!")
            popup.destroy()

        def cancel():
            popup.destroy()

        popup = tk.Toplevel()
        popup.title("Cadastrar Animal")
        popup.geometry("400x400")

        tk.Label(popup, text="Nome do Animal:").pack(pady=5)
        entry_name = tk.Entry(popup)
        entry_name.pack()

        tk.Label(popup, text="Tipo (Cachorro, Gato, etc):").pack(pady=5)
        entry_type = tk.Entry(popup)
        entry_type.pack()

        tk.Label(popup, text="Idade:").pack(pady=5)
        entry_age = tk.Entry(popup)
        entry_age.pack()

        tk.Label(popup, text="Observações:").pack(pady=5)
        entry_observations = tk.Entry(popup)
        entry_observations.pack()

        # Posicionamento centralizado dos botões
        btn_frame = tk.Frame(popup)
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="OK", command=save_and_close).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Cancelar", command=cancel).pack(side="right", padx=10)

    @staticmethod
    def view_animals():
        data = load_data("data/animais.txt")
        create_table_window("Animais Cadastrados", data, "data/animais.txt", ["Nome", "Tipo", "Idade", "Observações"])
