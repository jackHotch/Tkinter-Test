import tkinter as tk
from tkinter import ttk
from fetch_data import fetch_next_race

info = fetch_next_race()

root = tk.Tk()
root.title("F1")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

countryLabel = ttk.Label(frame, text=f'Next Race: {info['country']}')
countryLabel.grid(row=0, column=0)

locationLabel = ttk.Label(frame, text=info['location'])
locationLabel.grid(row=1, column=0)

fp1Label = ttk.Label(frame, text='FP1')
fp1Label.grid(row=2, column=0)

fp1Info = ttk.Label(frame, text=f'{info['fp1Date']}: {info['fp1Time']}')
fp1Info.grid(row=3, column=0)

fp2Label = ttk.Label(frame, text='FP2')
fp2Label.grid(row=2, column=1)

fp2Info = ttk.Label(frame, text=f'{info['fp2Date']}: {info['fp2Time']}')
fp2Info.grid(row=3, column=1)

fp3Label = ttk.Label(frame, text='FP3')
fp3Label.grid(row=2, column=2)

fp3Info = ttk.Label(frame, text=f'{info['fp3Date']}: {info['fp3Time']}')
fp3Info.grid(row=3, column=2)

qualyLabel = ttk.Label(frame, text='Qualy')
qualyLabel.grid(row=2, column=3)

qualyInfo = ttk.Label(frame, text=f'{info['qualifyingDate']}: {info['qualifyingTime']}')
qualyInfo.grid(row=3, column=3)

raceLabel = ttk.Label(frame, text='Race')
raceLabel.grid(row=2, column=4)

raceInfo = ttk.Label(frame, text=f'{info['raceDate']}: {info['raceTime']}')
raceInfo.grid(row=3, column=4)

root.mainloop()