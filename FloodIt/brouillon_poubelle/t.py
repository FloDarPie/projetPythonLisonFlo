import tkinter as tk

def exit(event):
    root.destroy()

root = tk.Tk()

root.bind("<Escape>", exit)
root.mainloop()
