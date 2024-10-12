import tkinter as tk
from time import strftime
root=tk.Tk()
root.title("Digital clock")

def time():
    string=strftime("%I:%M:%S %p \n%D")
    Label.config(text=string)
    Label.after(1000,time)

Label=tk.Label(root,font=("ds-digital",50,"bold"),background="yellow",foreground="black")
Label.pack(anchor="center") 


time()

root.mainloop()
