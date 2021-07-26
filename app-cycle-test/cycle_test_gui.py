import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Create a new window with the title "Simple Text Editor"
window = tk.Tk()
window.title("Cycle test")

# Set row and column configuration
window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(1, minsize=100, weight=1)

# Creating all of the widget components in this application
cycle_number = tk.Label(master=window, text="Input cycle start number and target number, then press start")
fr_entry = tk.Frame(window)
fr_btn = tk.Frame(window)
btn_start = tk.Button(fr_btn, text="Start")
btn_end = tk.Button(fr_btn, text="Stop")
start_number = tk.Entry(master=fr_entry, width=10)
target_number = tk.Entry(master=fr_entry, width=10)

# Arranging the widgets
start_number.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
target_number.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_start.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_end.grid(row=0, column=1, sticky="ew", padx=5)
fr_entry.grid(row=0, column=0, sticky="ns")
fr_btn.grid(row=1, column=1, sticky="ns")
cycle_number.grid(row=0,column=1,sticky="nsew")
# Run windows
window.mainloop()