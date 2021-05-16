from tkinter import *


def alert_popup(title, message, path):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10, height=3)
    b.pack()
    mainloop()
    
    
alert_popup("Title goes here..", "Hello World!", "A path or second message can go here..")
alert_popup("Success!", "Processing completed. Your report was saved here:", "C:/path/to/my_reports/report1.xlsx")
