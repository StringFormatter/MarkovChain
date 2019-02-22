import os
import sys
from tkinter import *
from tkinter import ttk

class MainApp():

    def __init__(self, master):
        
        self.mWidth = 1200
        self.mHeight = 800
        self.nodeList = []

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
        self.nodeList.append(self.canvas.create_oval(0, 0, 50, 50, outline="#0030e0", activeoutline="#00e0e0", fill="#0030e0", activefill="#00e0e0"))

    def removeNode(self):
        self.canvas.delete(self.nodeList.pop())


if __name__ == "__main__" :
    root = Tk()

    app = MainApp(root)

    root.mainloop()
