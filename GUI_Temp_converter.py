import tkinter
from tkinter import *

window = Tk()


window.title("Simple Project")


label = Label(text="Temp converter", font="Arial,20")



label.pack(padx=20,pady=10)

entry = Entry()
entry.pack(padx=20,pady=10)



    
    
def celsius_to_fahrenheit():
    celsius = float(entry.get())
    fahrenheit = (celsius * 9/5) + 32
    label.config(text=f"the temperature in F is {fahrenheit}")
    return fahrenheit

    
    
button = Button(text="click me!",command=celsius_to_fahrenheit)


button.pack(padx=20,pady=10)


window.mainloop()

