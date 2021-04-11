import setuptools
from tkinter import ttk,END,LEFT,BOTH
from tkinter.ttk import *
from tkinter import filedialog, PhotoImage
from ttkthemes import ThemedTk
import os, sys, serial, csv, time, debugMode
import serial.tools.list_ports
from docs import  error, timingDiagram
from docs.init import *


list_ports=[]


ser=serial.Serial(
    baudrate=def_baudrate,
    timeout=def_timeout
)

def send(i):
    ser.write((str(i)+';').encode(def_encode))


def start():
    errorflag= False
    txterror=""
    ser.read()
    if(file_path.get()==""):
        txterror+=t_error_path+"\n"
        errorflag= True
    if(input_bitin.get()==""):
        txterror+=t_error_noinput+"\n"
        errorflag= True
    if( input_bitout.get()==""):
        errorflag= True
        txterror+=t_error_output+"\n"

    if(ser.isOpen()):
        send(0)
        time.sleep(0.2)
        if(len(str(ord(ser.read())))==0):
            errorflag= True
            txterror+=t_error_noconexion
    else:
        errorflag= True
        txterror+=t_error_noconexion
    
    if errorflag:
        error.appear(txterror)



    name=str(file_path.get())
    if name[-4:]!=".csv":
        name=name+".csv"

    with open(name,'w',newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        aux=str(0)+','+ str(0)+','+"Ignore this"
        writer.writerow(aux)
        maxval=2**int(input_bitin.get())
        ser.read()
        for i in range (0,maxval):
            send(i)
            valor=str(ord(ser.read()))
            writer.writerow([str(i)+','+ str(valor)])
            progressbar['value']=i/(maxval-1)*100
            home.update_idletasks()

    send(0)
    ser.read()

def makeDiagram():
    name_file= str(file_path.get())
    print(name_file)
    num_out=input_bitout.get()
    timingDiagram.showDiagram(name_file,num_out)

def connect():
    try:
        if combo_ports.get()=="":
            error.appear(t_error_noconexion)
            return
        ser.port=combo_ports.get()
        ser.open()
    except:
        error.appear(t_error_no_succes_connection)

def debug():
    num_entradas=int(input_bitin.get())
    num_salidas=int(input_bitout.get())
    ser.close()
    puerto=combo_ports.get()
    home.destroy()
    debugMode.empezar(num_entradas,num_entradas,puerto)
def openfile():
    print("openfile")
    file_path.delete(0,END)
    text = filedialog.askopenfilename()
    file_path.insert(0,text)
    print(text)
    
def newfile():
    file_path.delete(0,END)
    text = str(filedialog.asksaveasfilename())+".csv"
    file_path.insert(0,text)



home =ThemedTk(background=True,toplevel=True)
home.title(t_head_main)

home.config(theme=def_theme)

labelin= Label(home,text=t_label_input_pins,font=font,width=25).grid(column=0,row=0)
labelout= Label(home,text=t_label_output_pins,font=font,width=25).grid(column=0,row=1)


labelfile= Label(home,text=t_label_file_path,font=font,width=25).grid(column=0,row=2)
file_path=Entry(home,width=20)
file_path.grid(column=1,row=2)

boton_start= ttk.Button(home, text=t_button_start,command=start)
boton_start.grid(column=0,row=3,columnspan=4)

input_bitin = Combobox(home,state="readonly",width=25)
input_bitin['values']=[1,2,3,4,5,6,7,8]
input_bitin.grid(column=1,row=0,columnspan=4)
input_bitout = Combobox(home,state="readonly",width=25)
input_bitout['values']=[1,2,3,4,5,6,7,8]
input_bitout.grid(column=1,row=1,columnspan=4)

progressbar=Progressbar(home, length=400, mode='determinate')
progressbar.grid(column=0,row=5,columnspan=4)

diagram_button=ttk.Button(home,text=t_button_diagram,command=makeDiagram)
diagram_button.grid(column=0,row=4,columnspan=4)


ports = serial.tools.list_ports.comports()
list_ports.clear()
for port in ports:
    list_ports.append(port.name)
combo_ports=ttk.Combobox(home,state="readonly")
combo_ports['values']=list_ports
combo_ports.grid(column=0,row=6,columnspan=4)

debug_button=ttk.Button(home,text=t_button_debug, command=debug)
debug_button.grid(column=0,row=8,columnspan=4)

connect_button=ttk.Button(home,text=t_button_connect,command=connect)
connect_button.grid(column=0,row=7,columnspan=4)

home.iconbitmap(sys.path[0]+'/docs/icons/logo.ico')

im_open_file = PhotoImage(file=(sys.path[0]+'/docs/icons/openfile.png'))
im_open_file = im_open_file.subsample(33)
open_file_button=Button(home,image=im_open_file,command=openfile)
open_file_button.grid(column=3,row=2)

im_new_file = PhotoImage(file=(sys.path[0]+'/docs/icons/newfile.png'))
im_new_file = im_new_file.subsample(33)
new_file_button=Button(home,image=im_new_file,command=newfile)
new_file_button.grid(column=4,row=2)

windowWidth = home.winfo_reqwidth()
windowHeight = home.winfo_reqheight()
positionRight = int(home.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(home.winfo_screenheight()/2 - windowHeight/2)
home.geometry("+{}+{}".format(positionRight, positionDown))

Label(text=" ").grid(column=0,row=9)


home.mainloop()
#ser.close()
