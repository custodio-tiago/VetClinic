import tkinter as tk
from tkinter import messagebox
from utils import save_data, load_data, create_table_window


class VeterinarianManagement:
    @staticmethod
    def register_veterinarian():
        def save_and_close():
            name = entry_name.get()
            specialty = entry_specialty.get()
            if not name or not specialty:
                messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios.")
                return
            save_data("data/veterinarios.txt", f"{name},{specialty}")
            messagebox.showinfo("Cadastro", "Veterinário cadastrado com sucesso!")
            popup.destroy()

        def cancel():
            popup.destroy()

        popup = tk.Toplevel()
        popup.title("Cadastrar Veterinário")
        popup.geometry("400x200")

        tk.Label(popup, text="Nome do Veterinário:").pack(pady=5)
        entry_name = tk.Entry(popup)
        entry_name.pack()

        tk.Label(popup, text="Especialidade:").pack(pady=5)
        entry_specialty = tk.Entry(popup)
        entry_specialty.pack()

        # Posicionamento centralizado dos botões
        btn_frame = tk.Frame(popup)
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="OK", command=save_and_close).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Cancelar", command=cancel).pack(side="right", padx=10)

    @staticmethod
    def view_veterinarians():
        data = load_data("data/veterinarios.txt")
        create_table_window("Veterinários Cadastrados", data, "data/veterinarios.txt", ["Nome", "Especialidade"])
