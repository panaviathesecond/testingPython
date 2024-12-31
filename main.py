import tkinter as tk
from tkinter import messagebox

def on_really_click():
    messagebox.showinfo("Message", "No")

root = tk.Tk()
root.withdraw()  # Hide the main window

messagebox.showinfo("Message", "You got ratted, skid.", buttons=["Oh no!", "Really?"])

# Bind the "Really?" button to the on_really_click function
messagebox.askyesno("Message", "Really?", command=on_really_click)

root.mainloop()
