# import tkinter as tk
# from tkinter import ttk
# from fetch_f1_data import fetch_next_race

# info = fetch_next_race()

# root = tk.Tk()
# root.title("F1")

# frame = ttk.Frame(root, padding=10)
# frame.grid(row=0, column=0)

# countryLabel = ttk.Label(frame, text=f'Next Race: {info['country']}')
# countryLabel.grid(row=0, column=0)

# locationLabel = ttk.Label(frame, text=info['location'])
# locationLabel.grid(row=1, column=0)

# fp1Label = ttk.Label(frame, text='FP1')
# fp1Label.grid(row=2, column=0)

# fp1Info = ttk.Label(frame, text=f'{info['fp1Date']}: {info['fp1Time']}')
# fp1Info.grid(row=3, column=0)

# fp2Label = ttk.Label(frame, text='FP2')
# fp2Label.grid(row=2, column=1)

# fp2Info = ttk.Label(frame, text=f'{info['fp2Date']}: {info['fp2Time']}')
# fp2Info.grid(row=3, column=1)

# fp3Label = ttk.Label(frame, text='FP3')
# fp3Label.grid(row=2, column=2)

# fp3Info = ttk.Label(frame, text=f'{info['fp3Date']}: {info['fp3Time']}')
# fp3Info.grid(row=3, column=2)

# qualyLabel = ttk.Label(frame, text='Qualy')
# qualyLabel.grid(row=2, column=3)

# qualyInfo = ttk.Label(frame, text=f'{info['qualifyingDate']}: {info['qualifyingTime']}')
# qualyInfo.grid(row=3, column=3)

# raceLabel = ttk.Label(frame, text='Race')
# raceLabel.grid(row=2, column=4)

# raceInfo = ttk.Label(frame, text=f'{info['raceDate']}: {info['raceTime']}')
# raceInfo.grid(row=3, column=4)

# root.mainloop()

import tkinter as tk
from tkinter import ttk


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")

        # creating a frame and assigning it to container
        container = ttk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (HomePage, F1, NFL, NBA, NHL, MLB, College):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

class Navbar(tk.Tk):
    def __init__(self, controller):
        frame = ttk.Frame(self)
        frame.grid(row=0)

        home_button = ttk.Button(frame, text='Home', command=lambda: controller.show_frame(HomePage))
        home_button.grid(row=0, column=0)

        f1_button = ttk.Button(frame, text='F1', command=lambda: controller.show_frame(F1))
        f1_button.grid(row=0, column=0)

        nfl_button = ttk.Button(frame, text='NFL', command=lambda: controller.show_frame(NFL))
        nfl_button.grid(row=0, column=0)

        nba_button = ttk.Button(frame, text='NBA', command=lambda: controller.show_frame(NBA))
        nba_button.grid(row=0, column=0)

        nhl_button = ttk.Button(frame, text='NHL', command=lambda: controller.show_frame(NHL))
        nhl_button.grid(row=0, column=0)

        mlb_button = ttk.Button(frame, text='MLB', command=lambda: controller.show_frame(MLB))
        mlb_button.grid(row=0, column=0)

        college_button = ttk.Button(frame, text='College', command=lambda: controller.show_frame(College))
        college_button.grid(row=0, column=0)

class HomePage(tk.frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home Page")
        label.grid(row=0, column=0)


class F1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="F1 Page")
        label.pack(padx=10, pady=10)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SidePage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class NFL(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NFL Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(CompletionScreen),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class NBA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NBA Page")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class NHL(tk.frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NHL Page")
        label.grid(row=0, column=0)


class MLB(tk.frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MLB Page")
        label.grid(row=0, column=0)


class College(tk.frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="College Page")
        label.grid(row=0, column=0)

if __name__ == "__main__":
    root = windows()
    root.mainloop()