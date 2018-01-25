from tkinter import *


class MyTextBox:
    root = Tk()

    def __init__(self):
        self.root.title("Enter your Name")
        Label(self.root, text="Enter your name: ").pack(side=LEFT)

        self.name = ""
        self.text = StringVar()
        self.e = Entry(self.root, textvariable=self.text)
        self.e.bind('<Return>', self.getName)
        self.e.pack()

        quitButton = Button(text="Quit", command=self.getName)
        quitButton.pack()

    def show(self):
        self.root.mainloop()

    def client_exit(self):
        self.root.quit()

    def getName(self, event=None):
        self.name = self.e.get()
        self.client_exit()
