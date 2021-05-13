import tkinter as tk     ## Python 3.x

from functools import partial

class TestStop():
    def __init__(self, master):
        self.master=master
        self.this_num=tk.IntVar()
        tk.Label(master, textvariable=self.this_num,
                 bg="blue").grid(sticky="nsew")
        tk.Button(self.master, text="Quit",
                  bg="orange", command=self.master.quit).grid(row=1)
        self.ctr=0
        self.test_stop()

    def button_continue(self, top):
        """ button click event
        """
        print("button continue")
        top.destroy()
        self.test_stop()

    def test_stop(self):
        self.ctr += 1
        self.this_num.set(self.ctr)

        ## limit it for testing
        if self.ctr < 10:
            if self.ctr==5:  ## event=some condition is met 
                top=tk.Toplevel(self.master)
                tk.Button(top, text="Continue", bg="lightblue",
                      command=partial(self.button_continue, top)).grid(row=1)
            else:  ## event=condition is not met
                ## wait one second so you can see the numbers going up
                self.master.after(1000, self.test_stop)
        else:
            self.master.quit()  ## event=all data exhausted

master=tk.Tk()
TestStop(master)
master.mainloop()
