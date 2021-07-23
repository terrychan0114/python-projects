import tkinter as tk
import random

def roll_die():
    roll_value["text"] = str(random.randint(1,6))

window = tk.Tk()

window.rowconfigure([0,1], minsize=150, weight=1)
window.columnconfigure(0, minsize=150, weight=1)

roll = tk.Button(master=window, text="Roll",command=roll_die)
roll.grid(row=0, column=0, sticky="nsew")

roll_value = tk.Label(master=window, text="Start")
roll_value.grid(row=1, column=0)

window.mainloop()