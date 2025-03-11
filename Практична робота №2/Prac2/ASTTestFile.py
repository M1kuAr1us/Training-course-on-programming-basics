import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import numpy as np

def stvorennya_matruci():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            try:
                value = float(entries[i][j].get())
            except ValueError:
                messagebox.showerror("Помилка")
                return
            row.append(value)
        matrix.append(row)
    return np.array(matrix)

def mnozhennya_matruci():
    try:
        scalar = float(scalarEntry.get())
        matrix = stvorennya_matruci()
        result = matrix * scalar
        rezyltat(result)
    except Exception as e:
        messagebox.showerror("Помилка", str(e))

def znahodzhennya_ranga():
    try:
        matrix = stvorennya_matruci()
        rank = np.linalg.matrix_rank(matrix)
        messagebox.showinfo("Ранг матриці", f"Ранг: {rank}")
    except Exception as e:
        messagebox.showerror("Помилка", str(e))

def znahodzhennya_determinant():
    try:
        matrix = stvorennya_matruci()
        determinant = np.linalg.det(matrix)
        messagebox.showinfo("Возначник матриці", f"Визначник: {determinant:.2f}")
    except Exception as e:
        messagebox.showerror("Помилка", str(e))

def znahodzhennya_obernenoi_matruci():
    try:
        matrix = stvorennya_matruci()
        inverse = np.linalg.inv(matrix)
        rezyltat(inverse)
    except np.linalg.LinAlgError:
        messagebox.showerror("Помилка", "Не має оберненого значення")
    except Exception as e:
        messagebox.showerror("Помилка", str(e))

def rezyltat(result):
    resultWindow = tk.Toplevel(root)
    resultWindow.title("Результат")
    for i, row in enumerate(result):
        for j, value in enumerate(row):
            tk.Label(resultWindow, text=f"{value:.2f}", width=10, borderwidth=2, relief="solid").grid(row=i, column=j)

root = tk.Tk()
root.title("Матриця")
root.configure(bg="#f0f0f0")
root.geometry("550x300")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TEntry", padding=5)

entries = []
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, columnspan=3)

for i in range(3):
    row_entries = []
    for j in range(3):
        entry = ttk.Entry(frame, width=5, font=("Arial", 12), justify="center")
        entry.grid(row=i, column=j, padx=5, pady=5)
        row_entries.append(entry)
    entries.append(row_entries)

scalarLabel = ttk.Label(root, text="Помножити на:")
scalarLabel.grid(row=4, column=0, pady=5, sticky="e")
scalarEntry = ttk.Entry(root, width=5, font=("Arial", 12), justify="center")
scalarEntry.grid(row=4, column=1, padx=5)

button_frame = ttk.Frame(root, padding="10")
button_frame.grid(row=5, column=0, columnspan=3)

ttk.Button(button_frame, text="Помножити", command=mnozhennya_matruci).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(button_frame, text="Знайти ранг", command=znahodzhennya_ranga).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(button_frame, text="Знайти визначник", command=znahodzhennya_determinant).grid(row=0, column=2, padx=5, pady=5)
ttk.Button(root, text="Знайти обернену матрицю", command=znahodzhennya_obernenoi_matruci).grid(row=5, column=3, pady=5)

root.mainloop()
