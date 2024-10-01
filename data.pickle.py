#dictionary
import tkinter as tk
from tkinter import colorchooser
root = tk.Tk()
color = colorchooser.askcolor(title="Pick a color")
print("Selected color:", color[1])

root.mainloop()
import pickle
list1=[1,2,3,4,5]
filename="data.pickle"

with open(filename,"wb") as fileHandle:
    pickle.dump(list1,fileHandle)

    print("")

mylist = [10,20,30,40,50]

















