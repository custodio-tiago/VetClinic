import tkinter as tk
from tkinter import messagebox, ttk
from utils import save_data, load_data, create_table_window


class ConsultationManagement:
    @staticmethod
    def register_consultation():
        def save_and_close():
            date = entry_date.get()
            vet = combo_vet.get()
            animal = combo_animal.get()
            description = entry_description.get()
            if not date or not vet or not animal:
                messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios.")
                return
            save_data("data/consultas.txt", f"{date},{vet},{animal},{description}")
            messagebox.showinfo("Cadastro", "Consulta cadastrada com sucesso!")
            popup.destroy()

        def cancel():
            popup.destroy()

        # Carregar veterinários e animais para as opções
        veterinarians = [line.split(",")[0] for line in load_data("data/veterinarios.txt")]
        animals = [line.split(",")[0] for line in load_data("data/animais.txt")]

        popup = tk.Toplevel()
        popup.title("Abrir Consulta")
        popup.geometry("400x400")

        tk.Label(popup, text="Data da Consulta (dd/mm/yyyy):").pack(pady=5)
        entry_date = tk.Entry(popup)
        entry_date.pack()

        tk.Label(popup, text="Veterinário:").pack(pady=5)
        combo_vet = ttk.Combobox(popup, values=veterinarians, state="readonly")
        combo_vet.pack()

        tk.Label(popup, text="Animal:").pack(pady=5)
        combo_animal = ttk.Combobox(popup, values=animals, state="readonly")
        combo_animal.pack()

        tk.Label(popup, text="Descrição da Consulta:").pack(pady=5)
        entry_description = tk.Entry(popup)
        entry_description.pack()

        # Posicionamento centralizado dos botões
        btn_frame = tk.Frame(popup)
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="OK", command=save_and_close).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Cancelar", command=cancel).pack(side="right", padx=10)

    @staticmethod
    def view_consultations():
        data = load_data("data/consultas.txt")
        create_table_window("Consultas Marcadas", data, "data/consultas.txt", ["Data", "Veterinário", "Animal", "Descrição"])
