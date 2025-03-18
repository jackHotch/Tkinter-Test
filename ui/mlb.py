import tkinter as tk
from tkinter import ttk

class MLB(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MLB Page")
        label.grid(row=0, column=0)