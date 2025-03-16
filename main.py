import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Simple App")

# frame = tk.Frame(root)

entry_btn = ttk.Button(root, text='Hello World')
entry_btn.grid()

root.mainloop()