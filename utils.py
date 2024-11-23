import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def load_image(path, size):
    img = Image.open(path).resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)


def save_data(file_path, entry):
    with open(file_path, "a") as file:
        file.write(entry + "\n")


def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def create_table_window(title, data, file_path):
    def delete_entry(index):
        data.pop(index)
        with open(file_path, "w") as file:
            for line in data:
                file.write(line + "\n")
        table.destroy()
        create_table_window(title, data, file_path)

    table = tk.Toplevel()
    table.title(title)

    for i, entry in enumerate(data):
        lbl = tk.Label(table, text=entry)
        lbl.grid(row=i, column=0, sticky="w")
        btn_delete = tk.Button(table, text="Excluir", command=lambda idx=i: delete_entry(idx))
        btn_delete.grid(row=i, column=1)
