import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Simple App")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

entry = ttk.Entry(frame)
entry.grid(row=0, column=0)

entry_btn = ttk.Button(frame, text='Hello World')
entry_btn.grid(row=0, column=1)

root.mainloop()