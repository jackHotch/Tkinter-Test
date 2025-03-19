import tkinter as tk
from tkinter import ttk
from ui.home import HomePage
from ui.f1 import F1
from ui.nfl import NFL
from ui.nba import NBA
from ui.nhl import NHL
from ui.mlb import MLB
from ui.college import College

class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.wm_title("My Sports")
        self.geometry("600x400")  # Set full window size

        self.container = ttk.Frame(self)
        self.container.grid(row=1, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.navbar = tk.Frame(self, bg="#333")
        self.navbar.grid(row=0, column=0, sticky="ew")

        self.create_navbar()

        self.frames = {}
        for F in (HomePage, F1, NFL, NBA, NHL, MLB, College):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def create_navbar(self):
        buttons = [
            ("Home", HomePage),
            ("F1", F1),
            ("NFL", NFL),
            ("NBA", NBA),
            ("NHL", NHL),
            ("MLB", MLB),
            ("College", College)
        ]
        for i, (label, page) in enumerate(buttons):
            button = ttk.Button(self.navbar, text=label, command=lambda p=page: self.show_frame(p))
            button.grid(row=0, column=i)

        # Allow navbar to expand horizontally
        self.navbar.grid_columnconfigure(len(buttons) - 1, weight=1)

# Start the app
if __name__ == "__main__":
    root = windows()
    # root.state('zoomed')  # Maximize window
    root.mainloop()
