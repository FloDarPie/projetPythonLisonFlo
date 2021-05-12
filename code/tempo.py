from tkinter import *

def hide_me(event):
    event.widget.pack_forget()

root = Tk()
btn=Button(root, text="Click")
btn.bind('<Button-1>', hide_me)
btn.pack()
btn2=Button(root, text="Click too")
btn2.bind('<Button-1>', hide_me)
btn2.pack()
root.mainloop()
