import tkinter as tk
from tkinter import PhotoImage

class sketchPad():
    def __init__(self,width = 500, height = 500):
        self.cursorcolor = "#ffffff"
        self.bgcolor = "#000000"
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=self.width, width=self.height, bg=self.bgcolor)
        self.img = None
        self.canvas.pack()
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



