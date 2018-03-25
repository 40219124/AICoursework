from tkinter import *
import tkinter as tk
from Solver import Solver


class Renderer:

    def __init__(self):
        self.window = Tk()
        self.window.title("Hey!")
        self.window.geometry("300x300")

        frame = Frame(self.window)
        frame.pack()

        bottomframe = Frame(self.window)
        bottomframe.pack(side=BOTTOM)

        redbutton = Button(bottomframe, text="Red", fg="red")
        redbutton.pack(side=RIGHT)

        bluebutton = Button(bottomframe, text="Blue", fg="blue")
        bluebutton.pack(side=LEFT)

        greenbutton = Button(bottomframe, text="Green", fg="green")
        greenbutton.pack(side=TOP)

        blackbutton = Button(bottomframe, text="Black", fg="black", command=Solver.generate_path)
        blackbutton.pack(side=BOTTOM)

        self.window.mainloop()
