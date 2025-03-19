import tkinter as tk
from tkinter import ttk
from data.fetch_f1_data import fetch_next_race

class F1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky="nsew")  # Expand frame horizontally
        next_race = fetch_next_race()

        for i in range(5):
            self.columnconfigure(i, weight=1)
        for i in range(6):
            self.rowconfigure(i, weight=1)

        label = tk.Label(self, text=f"{next_race['season']} F1 Season")
        label.grid(row=0, column=0, columnspan=5, sticky="ew")

        countryLabel = ttk.Label(self, text=f"Next Race: {next_race['country']} - {next_race['location']}")
        countryLabel.grid(row=1, column=0, columnspan=5, sticky="ew")

        fp1Label = ttk.Label(self, text='FP1')
        fp1Label.grid(row=3, column=0, sticky="ew")

        fp1Info = ttk.Label(self, text=f"{next_race['fp1_date']}: {next_race['fp1_time']}")
        fp1Info.grid(row=4, column=0, sticky="ew")

        if 'sprint_date' in next_race:
            sprint_qualy_label = ttk.Label(self, text='Sprint Qualifying')
            sprint_qualy_label.grid(row=3, column=1, sticky="ew")

            sprint_qualy_info = ttk.Label(self, text=f"{next_race['sprint_qualy_date']}: {next_race['sprint_qualy_time']}")
            sprint_qualy_info.grid(row=4, column=1, sticky="ew")

            sprint_label = ttk.Label(self, text='Sprint')
            sprint_label.grid(row=3, column=2, sticky="ew")

            sprint_info = ttk.Label(self, text=f"{next_race['sprint_date']}: {next_race['sprint_time']}")
            sprint_info.grid(row=4, column=2, sticky="ew")
        else:
            fp2Label = ttk.Label(self, text='FP2')
            fp2Label.grid(row=3, column=1, sticky="ew")

            fp2Info = ttk.Label(self, text=f"{next_race['fp2_date']}: {next_race['fp2_time']}")
            fp2Info.grid(row=4, column=1, sticky="ew")

            fp3Label = ttk.Label(self, text='FP3')
            fp3Label.grid(row=3, column=2, sticky="ew")

            fp3Info = ttk.Label(self, text=f"{next_race['fp3_date']}: {next_race['fp3_time']}")
            fp3Info.grid(row=4, column=2, sticky="ew")

        qualyLabel = ttk.Label(self, text='Qualy')
        qualyLabel.grid(row=3, column=3, sticky="ew")

        qualyInfo = ttk.Label(self, text=f"{next_race['qualy_date']}: {next_race['qualy_time']}")
        qualyInfo.grid(row=4, column=3, sticky="ew")

        raceLabel = ttk.Label(self, text='Race')
        raceLabel.grid(row=3, column=4, sticky="ew")

        raceInfo = ttk.Label(self, text=f"{next_race['race_date']}: {next_race['race_time']}")
        raceInfo.grid(row=4, column=4, sticky="ew")
