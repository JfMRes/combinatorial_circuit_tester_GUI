from tkinter import *
from ttkthemes import ThemedTk
from tkinter.ttk import *
from init import *

theme=""
def appear(text_in):
    window=ThemedTk(background=True)
    window.config(theme=def_theme)
    window.title("Error!")
    window.geometry('450x200')
    def destroy():
        window.destroy()
    button=Button(window,text="OK", command=destroy)
    button.place(relx=0.45,rely=0.7)
    textpin= Label(window,text=text_in,font=("Arial Bold", 15))
    textpin.place(relx=0.2,rely=0.1)
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
    window.geometry("+{}+{}".format(positionRight, positionDown))

    window.iconbitmap(sys.path[0]+'/docs/icons/warning.ico')

    window.mainloop()

