import tkinter as tk
from tkinter import ttk

def calculate_gugudan():
    try:
        num = int(entry.get())
        result = ""
        for i in range(1, 10):
            result += f"{num} x {i} = {num * i}\n"
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="올바른 숫자를 입력하세요")

root = tk.Tk()
root.title("구구단 프로그램")
root.geometry("300x400")

entry_label = ttk.Label(root, text="숫자를 입력하세요:")
entry_label.pack(pady=10)

entry = ttk.Entry(root, width=20)
entry.pack(pady=5)

calculate_button = ttk.Button(root, text="계산", command=calculate_gugudan)
calculate_button.pack(pady=10)

result_label = ttk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()
