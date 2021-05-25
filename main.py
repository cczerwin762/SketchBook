
import tkinter as tk
from tkinter import PhotoImage
class sketchPad():

    def __init__(self,width = 500, height = 500):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=width, width=height, bg="#000000")
        self.canvas.pack()
        self.img = None
        self.create()
        self.root.mainloop()

    def create(self):
        self.img = PhotoImage(width=self.width, height=self.height)
        self.canvas.create_image((self.width // 2, self.height // 2), image=self.img, state="normal")
        self.canvas.bind("<Button-1>", self.clicked_callback)
        self.canvas.bind("<B1-Motion>", self.clicked_callback)
        self.canvas.bind("<Button-3>", self.clear_callback)

    def clicked_callback(self, event):
        self.img.put("#ffffff",(event.x,event.y))
        self.root.update()

    def clear_callback(self, event):
        self.canvas.delete("all")
        self.create()
        self.root.update()

if __name__ == "__main__":
    sketchPad = sketchPad()



