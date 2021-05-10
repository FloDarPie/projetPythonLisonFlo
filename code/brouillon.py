import tkinter as tk
from tkinter import Tk, ttk, Frame, FALSE, Text, Button, \
    Scrollbar, Entry, END, INSERT



class MyTestApp(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.title('MY Test App')
        self.grid(column=0, row=0, sticky='nsew', padx=12, pady=5)

        self.data_textbox = Text(self, borderwidth=2, relief='sunken')
        self.data_textbox.config(height=30, width=80)
        self.data_textbox.grid(row=1, column=0, sticky="new")
        self.exit_btn = ttk.Button(self, text='Exit', command=self.on_exit)
        self.exit_btn.grid(row=2, column=0, sticky='W', pady=15)

        ## Not sure if im doing the below part correct
        ## Instantiate my popup class
        self.popup = Popup(parent)
        ## Assign self.popup.textbox_text to self.data_textbox
        self.popup.textbox_text = self.data_textbox
        # Add imported popup menu and bind to textbox widget
        self.data_textbox.bind("<Button-3>", self.popup.text_popup)

    # Exit the program. Linked to the Exit Button
    def on_exit(self):
        self.root.destroy()


def main():
    root = Tk()
    MyTestApp(root)
    root.mainloop()




class Popup(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        ### Not sure if this below part is correct
        ### Must it rather be set from the init parameter?
        self.textbox_text = ''

        self.text_widget = tk.Menu(self, tearoff=0, relief='sunken')
        self.text_widget.add_command(label="Copy", command=self.text_copy)
        self.text_widget.add_separator()
        self.text_widget.add_command(label="Paste", command=self.text_paste)
        self.text_widget.add_separator()
        self.text_widget.add_command(label="Clear", command=self.text_clear)


    def text_popup(self, event):
        self.text_widget.post(event.x_root, event.y_root)

    def text_copy(self, event=None):
        self.clipboard_clear()
        text = self.textbox_text.get("sel.first", "sel.last")
        self.clipboard_append(text)

    def text_paste(self):
        self.textbox_text.insert(INSERT, self.clipboard_get())

    def text_clear(self):
        self.textbox_text.delete(1.0, END)
        
if __name__ == '__main__':
    main()
