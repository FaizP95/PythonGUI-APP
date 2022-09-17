#LIBRARIES AND MODULES THAT NEED TO BE IMPORTED
from cProfile import label
from fileinput import filename
import tkinter as tk 
from tkinter import Canvas, Frame, filedialog, Text
import os
from unittest import TextTestResult

root = tk.Tk()
apps = []

#LOADS FILE DIRECTORY AND ALLOWS US TO SELECT PROGRAM
def addApp():
#ENSURES THAT DUPLICATES DO NOT APPEAR
    for widget in Frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables","*.exe"),("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(Frame, text=app, bg= "gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

TextTestResult

#THIS ALLOWS YOU TO CHANGE THE SIZE OF THE GUI
canvas = tk.Canvas(root, height=500, width=500, bg= "black")
canvas.pack() #ATTACHES THE CANVAS TO THE ROOT

#ENABLES YOU TO CONTROL THE CENTERING/SIZE OF THE SECOND SQUARE
Frame = tk.Frame (root, bg= "white")
Frame.place (relwidth=0.8, relheight=0.8, relx= 0.1, rely= 0.1)

#OPEN FILE BUTTON
openFile = tk.Button(root, text = "Open File", padx= 10,
                    pady=5, fg= "white", bg= "black", command=addApp)
openFile.pack()

#RUN APPLICATION BUTTON
runApps = tk.Button(root, text = "Run Apps", padx= 10,
                    pady=5, fg= "white", bg= "black", command= runApps)
runApps.pack()



root.mainloop()

#SAVES THE TEXT FILE THAT YOU OPEN
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')