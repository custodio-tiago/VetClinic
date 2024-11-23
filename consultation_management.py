import tkinter as tk
from tkinter import messagebox
from utils import save_data, load_data, create_table_window


class ConsultationManagement:
    @staticmethod
    def register_consultation():
        def save_and_close():
            date = entry_date.get()
            vet = entry_vet.get()
            animal = entry_animal.get()
            description = entry_description.get()
            if not date or not vet or not animal:
                messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios.")
                return
            save_data("data/consultas.txt", f"{date},{vet},{animal},{description}")
            messagebox.showinfo("Cadastro", "Consulta cadastrada com sucesso!")
            popup.destroy()

        def cancel():
            popup.destroy()

        popup = tk.Toplevel()
        popup.title("Abrir Consulta")
        popup.geometry("400x400")

        tk.Label(popup, text="Data da Consulta (dd/mm/yyyy):").pack(pady=5)
        entry_date = tk.Entry(popup)
        entry_date.pack()

        tk.Label(popup, text="Veterinário:").pack(pady=5)
        entry_vet = tk.Entry(popup)
        entry_vet.pack()

        tk.Label(popup, text="Animal:").pack(pady=5)
        entry_animal = tk.Entry(popup)
        entry_animal.pack()

        tk.Label(popup, text="Descrição da Consulta:").pack(pady=5)
        entry_description = tk.Entry(popup)
        entry_description.pack()

        tk.Button(popup, text="OK", command=save_and_close).pack(side="left", padx=20, pady=10)
        tk.Button(popup, text="Cancelar", command=cancel).pack(side="right", padx=20, pady=10)

    @staticmethod
    def view_consultations():
        data = load_data("data/consultas.txt")
        create_table_window("Consultas Marcadas", data, "data/consultas.txt", ["Data", "Veterinário", "Animal", "Descrição"])
