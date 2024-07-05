from tkinter import *
from tkinter import ttk, messagebox
from random import randint
    

def change_color():
    color = (
        "blue", "yellow", "green", "red", "orange",
        "violet", "black", "skyblue", "yellow green", 
        "salmon", "grey", "dark green", "aquamarine", 
        "brown", "cyan", "navy", "coral", "maroon",         "gold", "brown", "purple", "pink", "dodger blue",
        "turquoise", "indigo"
    )
    
    index = randint(0, len(color)-1)
    
    lbl1.config(bg=color[index])
    
def move(firstmove=False):
    
    x = lbl1.winfo_x()
    y = lbl1.winfo_y()
    
    speed = 5
    
    operation_dict = {
    "minus" : "plus",
    "plus" : "minus"
    }
    
    
    if not firstmove:
        if x + lbl1.winfo_width() >= f.winfo_width() or x <= 0:
            change_color()
            x_direction.set(operation_dict[x_direction.get()])
        
        if y + lbl1.winfo_height() >= f.winfo_height() or y <= 0:
            change_color()
            y_direction.set(operation_dict[y_direction.get()])
            
    x += (speed * -1) if x_direction.get() == "minus" else speed
    y += (speed * -1) if y_direction.get() == "minus" else speed
    
    lbl1.place(x=x, y=y)
    root.after(1, move)
    
    
root = Tk()

root.geometry("720x1448")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

f = Frame(root, width=width, height=height)
f.pack()

x_direction = StringVar()
y_direction = StringVar()

x_direction.set("plus")
y_direction.set("plus")

lbl1 = Label(f, bg="blue", width=10, height=5)
lbl1.place(x=0, y=0)

firstmove = True
#lbl1.config()
move(firstmove)

root.mainloop()