import tkinter as tk
from tkinter import ttk

class College(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="College Page")
        label.grid(row=0, column=0)