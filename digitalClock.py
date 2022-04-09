# from cProfile import label
# from curses import window
from time import strftime
from tkinter import Label, Tk

# Window Config for the clock

windows=Tk()
windows.title("")
windows.geometry("200x80")
windows.config(bg="black")
windows.resizable(False, False)

# Displaying boxes using label

clock_label = Label(windows, bg="black", fg="white", font=("Titan", 30, "bold"), relief="flat") 
clock_label.place(x=20, y=20)

def updateing_label():
    current_time=strftime('%H: %M: %S')
    clock_label.configure(text= current_time)
    clock_label.after(80, updateing_label)

updateing_label()
windows.mainloop()
