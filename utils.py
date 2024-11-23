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


def create_table_window(title, data, file_path, headers):
    def delete_entry(index):
        data.pop(index)
        with open(file_path, "w") as file:
            for line in data:
                file.write(line + "\n")
        table.destroy()
        create_table_window(title, data, file_path, headers)

    table = tk.Toplevel()
    table.title(title)
    table.geometry("450x400")

    tk.Label(table, text=title, font=("Arial", 14)).pack(pady=10)

    frame = tk.Frame(table)
    frame.pack()

    # Add headers
    for col, header in enumerate(headers):
        tk.Label(frame, text=header, font=("Arial", 10, "bold")).grid(row=0, column=col, padx=10, pady=5)

    # Add data rows
    for i, entry in enumerate(data):
        cols = entry.split(",")
        for col, value in enumerate(cols):
            tk.Label(frame, text=value).grid(row=i + 1, column=col, padx=10, pady=5)
        btn_delete = tk.Button(frame, text="Excluir", command=lambda idx=i: delete_entry(idx))
        btn_delete.grid(row=i + 1, column=len(cols), padx=10, pady=5)
