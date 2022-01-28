#ReeMindaGUI class

import tkinter as tk
from tkinter import filedialog, Text
import os

class ReeMindaGUI(tk.Frame):
    def __init__(self, master):
        dataFrames = []
        
        self.canvas = tk.Canvas(master, height=700, width=700, bg="#263D42")
        self.canvas.pack()

        self.frame = tk.Frame(master, bg = "white")
        self.frame.place(relwidth=.8, relheight=.8, relx=.1, rely=.1)

        #Buttons
        self.importFile = tk.Button(master, text="Import File", padx = 10, pady = 5, fg="white", bg="#263D42", command=self.addDF)
        self.importFile.pack()

        #Packing
        #canvas.pack()

    def addDF(self):
        filename = filedialog.askopenfilename(initialdir="/",title="Select File", 
        filetypes=(("excelsheet",".xlsx"), ("all files", "*.*")))
        self.dataFrames.append(filename)
        