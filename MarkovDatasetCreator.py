import os
import sys
from tkinter import *
from tkinter import ttk

class MainApp():

    def __init__(self, master):
        
        self.mWidth = 1200
        self.mHeight = 800
        self.nodeList = []
        self.textList = []
        self.nodenum = 0

        frame = Frame(master, width=self.mWidth, height=self.mHeight)
        frame.pack(fill="both", expand=YES)

        self.createWidgets(frame)


        '''self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=TOP)'''


    def createWidgets(self, frame):
        
        self.notebook = ttk.Notebook(frame)
        
        self.gframe = Frame(self.notebook)
        self.gtframe = Frame(self.gframe)
        self.gbframe = Frame(self.gframe)
        
        self.gtframe.pack(fill="both", expand=YES)
        self.gbframe.pack(expand=NO)

        self.canvas = Canvas(self.gtframe, bg = "#1e1e1e")

        self.canvas.pack(fill="both", expand=YES)
        
        self.abttn = Button(self.gbframe, text="Add Node", command=self.addNode)
        self.rbttn = Button(self.gbframe, text="Remove Node", command=self.removeNode)
        
        self.abttn.grid(column=0, row=1)
        self.rbttn.grid(column=1, row=1)

        self.fframe = Frame(self.notebook)
        self.label = Label(self.fframe, text="WIP please ignore, JUST LEAVE", bg = "#3e3e3e")
        
        self.label.grid(column=0, row=0)
        
        self.notebook.add(self.gframe, text="Graph")
        self.notebook.add(self.fframe, text="File Text")
        
        self.notebook.pack(fill="both", expand=YES)

    def addNode(self):
        self.nodeList.append(self.canvas.create_oval(0, 0, 50, 50, outline="#0030e0", activeoutline="#00e0e0", fill="#0030e0", activefill="#00e0e0", tags=str(self.nodenum)))
        self.textList.append(self.canvas.create_text(25, 25, tags=str(self.nodenum), text="Test"))
        self.canvas.tag_bind(ALL, '<B1-Motion>', func = self.clickmove)
        self.nodenum += 1

    def removeNode(self):
        if self.nodeList == []: return 0
        self.canvas.delete(self.nodeList.pop())
        self.canvas.delete(self.textList.pop())

    def clickmove(self, event):
        mouse_x = self.canvas.winfo_pointerx()-self.canvas.winfo_rootx()
        mouse_y = self.canvas.winfo_pointery()-self.canvas.winfo_rooty()
        coords = self.canvas.coords(CURRENT)
        avgcoord_x = (coords[0]+coords[2])/2
        avgcoord_y = (coords[1]+coords[3])/2

        self.canvas.move(CURRENT, mouse_x-avgcoord_x, mouse_y-avgcoord_y)
        self.canvas.move(self.canvas.find_above(CURRENT), mouse_x-avgcoord_x, mouse_y-avgcoord_y)

        #print((mouse_x,mouse_y))
        #print(coords)

if __name__ == "__main__" :
    root = Tk()

    app = MainApp(root)

    root.mainloop()
