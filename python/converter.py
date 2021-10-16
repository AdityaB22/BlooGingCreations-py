
from tkinter import *


win = Tk()
win.title("converter")

input1 = StringVar()

w = Label(win,text="This Is Weight Convertor! Entry Value Here(In kg) & Press Convert")
w.grid(row = 0 , column = 0)


def conversion():
    try:
        text1.insert(END, str(float(input1.get())*1000) + " grams")
        text2.insert(END, str(float(input1.get())*2.20462) + " pounds")
        text3.insert(END, str(float(input1.get())*35.274) + " ounches")
    except:
        pass

Input_box = Entry(win , textvariable = input1)
Input_box.grid(row = 1 , column = 0)

button1 = Button(win,text = "Convert", command = conversion )
button1.grid(row = 2 , column = 0)

text1 = Text(win,height = 1 , width = 40)
text1.grid(row = 3,column = 0)

text2 = Text(win,height = 1 , width = 40)
text2.grid(row = 4,column = 0)

text3 = Text(win,height = 1 , width = 40)
text3.grid(row = 5,column = 0)

w2 = Label(win,text="@developed BY aditya")
w2.grid(row = 6 , column = 1)

win.mainloop()