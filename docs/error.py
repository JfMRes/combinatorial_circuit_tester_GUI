from tkinter import *
from ttkthemes import ThemedTk
from tkinter.ttk import *
from docs.init import *

theme=""
def appear(text_in):
    window=ThemedTk(background=True)
    window.config(theme=def_theme)
    window.title("Error!")
    window.geometry('350x200')
    def destroy():
        window.destroy()
    button=Button(window,text="OK", command=destroy)
    button.grid(column=0,row=1,anchor=CENTER)
    textpin= Label(window,text=text_in,font=("Arial Bold", 15))
    textpin.grid(column=0,row=0)
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
    window.geometry("+{}+{}".format(positionRight, positionDown))

    window.mainloop()
