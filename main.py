import tkinter as tk
from tkinter import Frame, Label, Menu, Button, PhotoImage
import os

class sketchPad():
    def __init__(self,width = 500, height = 500):
        self.cursorcolor = "#ffffff"
        self.bgcolor = "#000000"
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry('500x520+200+200')
        self.canvas = tk.Canvas(self.root, height=self.width, width=self.height, bg=self.bgcolor)
        self.frame = Frame(self.root, width = 500, height = 20, bg = "white", relief = 'raised', bd=2)
        self.frame.pack(expand=1, fill = 'x')
        self.close = Button(self.frame, text = 'X', command = self.root.destroy)
        self.close.pack(side = tk.RIGHT)
        self.title = Label(self.frame, text="SketchPad")
        self.title.pack(side = tk.LEFT)
        self.menu = Menu(self.root)
        self.file = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = "File", menu = self.file)
        # Ok so what needs to be done... - implement menu bar, file and help, implement move window, implement save button
        # Make into an executable
        self.root.config(menu=self.menu)
        self.img = None
        self.canvas.pack(side = tk.BOTTOM)
        self.create()
        self.root.mainloop()

    def create(self):
        self.img = PhotoImage(width=self.width, height=self.height)
        self.canvas.create_image((self.width // 2, self.height // 2), image=self.img, state="normal")
        self.canvas.bind("<Button-1>", self.clicked_callback)
        self.canvas.bind("<B1-Motion>", self.clicked_callback)
        self.canvas.bind("<Button-2>", self.change_cursorcolor)
        self.canvas.bind("<Button-3>", self.clear_callback)
        self.canvas.focus_set()
        self.canvas.bind("<Key>", self.invert_colorscheme)

    def clicked_callback(self, event):
        self.img.put(self.cursorcolor,(event.x,event.y))
        self.root.update()

    def clear_callback(self, event):
        self.canvas.delete("all")
        self.create()
        self.root.update()

    def change_cursorcolor(self,event):
        self.cursorcolor = ("#ffffff" if self.cursorcolor == "#000000" else "#000000")

    def invert_colorscheme(self, event):
        (self.bgcolor, self.cursorcolor) = ("#ffffff","#000000") if self.bgcolor=="#000000" else ("#000000", "#ffffff")
        self.canvas.delete("all")
        self.canvas.configure(bg = self.bgcolor)
        self.create()
        self.root.update()



if __name__ == "__main__":
    sketchPad = sketchPad()



