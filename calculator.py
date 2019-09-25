from tkinter import Tk, Label, Button, IntVar, Entry, END, W, E


class Calculator:
    def __init__(self, master):
        self.total = 0
        self.entered_number = 0

        self.title_label = Label(master, text="Calculator")

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, "%P"))

        self.addition_button = Button(
            master, text="Add", command=lambda: self.update("add")
        )
        self.subtract_button = Button(
            master, text="Minus", command=lambda: self.update("minus")
        )
        self.equalto_button = Button(
            master, text="Equals", command=lambda: self.update("equalto")
        )
        self.reset_button = Button(
            master, text="Reset", command=lambda: self.update("reset")
        )
        self.close_button = Button(master, text="Close", command=master.quit, bg="red")

        # LAYOUT
        self.label.grid(row=1, column=1, sticky=W)
        self.total_label.grid(row=1, column=0, columnspan=2, sticky=E)

        self.entry.grid(row=2, column=0, columnspan=2, sticky=W + E)

        self.addition_button.grid(row=3, column=0)
        self.subtract_button.grid(row=3, column=1)
        self.equalto_button.grid(row=3, column=2)
        self.reset_button.grid(row=4, column=0, sticky=W + E)
        self.close_button.grid(row=4, column=1)

    def validate(self, new_text):
        if not new_text:
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "minus":
            self.total -= self.entered_number
        # elif method == "equalto":
            # self.total += self.entered_number
        else:
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)


root = Tk()
my_gui = Calculator(root)
root.mainloop()
