import tkinter as tk
from tkinter import ttk


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.wm_title("My Sports")
        self.geometry("600x400")

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
        home_button = ttk.Button(self.navbar, text='Home', command=lambda: self.show_frame(HomePage))
        home_button.grid(row=0, column=0)

        f1_button = ttk.Button(self.navbar, text='F1', command=lambda: self.show_frame(F1))
        f1_button.grid(row=0, column=1)

        nfl_button = ttk.Button(self.navbar, text='NFL', command=lambda: self.show_frame(NFL))
        nfl_button.grid(row=0, column=2)

        nba_button = ttk.Button(self.navbar, text='NBA', command=lambda: self.show_frame(NBA))
        nba_button.grid(row=0, column=3)

        nhl_button = ttk.Button(self.navbar, text='NHL', command=lambda: self.show_frame(NHL))
        nhl_button.grid(row=0, column=4)

        mlb_button = ttk.Button(self.navbar, text='MLB', command=lambda: self.show_frame(MLB))
        mlb_button.grid(row=0, column=5)

        college_button = ttk.Button(self.navbar, text='College', command=lambda: self.show_frame(College))
        college_button.grid(row=0, column=6)


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Home Page")
        label.grid(row=0, column=0)


class F1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="F1 Page")
        label.grid(row=0, column=0)

        
class NFL(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="NFL Page")
        label.grid(row=0, column=0)


class NBA(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="NBA Page")
        label.grid(row=0, column=0)


class NHL(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NHL Page")
        label.grid(row=0, column=0)


class MLB(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MLB Page")
        label.grid(row=0, column=0)


class College(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="College Page")
        label.grid(row=0, column=0)


if __name__ == "__main__":
    root = windows()
    root.mainloop()