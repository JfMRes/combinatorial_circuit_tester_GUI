from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
from PIL import Image,ImageTk
import serial
import time, sys
from docs.init import * 


current_number=-1
mode=0
time_delay=1000

def empezar(num_inputs,num_outputs,in_port):

    home=ThemedTk(background=True)
    home.config(theme=def_theme)


    im_play = PhotoImage(file=("Y:/Universidad/TFG/CodigoTFG/Project/docs/icons/play.png"))
    im_play = im_play.subsample(4)

    im_pause = PhotoImage(file=('Y:/Universidad/TFG/CodigoTFG/Project/docs/icons/pause.png'))
    im_pause=im_pause.subsample(4)

    im_stop = PhotoImage(file=(sys.path[0]+'/docs/icons/stop.png'))
    im_stop=im_stop.subsample(4)

    im_next = PhotoImage(file=(sys.path[0]+'/docs/icons/down.png'))
    im_next=im_next.subsample(4)

    im_prev = PhotoImage(file=(sys.path[0]+'/docs/icons/up.png'))
    im_prev=im_prev.subsample(4)

    im_ff = PhotoImage(file=(sys.path[0]+'/docs/icons/fast.png'))
    im_ff=im_ff.subsample(4)

    inuse=ttk.Style()
    inuse.theme_use(def_theme)
    inuse.configure('inuse.TButton',background="red")


    home.title(t_head_debug)
    home.geometry("400x500")

    main_frame=Frame(home)
    main_frame.pack(fill=BOTH,expand=1)

    my_canvas=Canvas(main_frame,highlightthickness=0)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

    scrollbar = ttk.Scrollbar(my_canvas, orient= VERTICAL, command=my_canvas.yview)
    scrollbar.pack(side=RIGHT,fill=Y)

    my_canvas.configure(yscrollcommand=scrollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame=Frame(my_canvas)

    my_canvas.create_window((60,0),window=second_frame, anchor="nw")


    list_button_select=[]
    list_check=[]
    list_check_var=[]

    b0=[];b1=[];b2=[];b3=[];b4=[];b5=[];b6=[];b7=[]
    bit_in=[b0,b1,b2,b3,b4,b5,b6,b7]

    out0=[];out1=[];out2=[];out3=[];out4=[];out5=[];out6=[];out7=[]
    bit_out=[out0,out1,out2,out3,out4,out5,out6,out7]
    
    inputs=int(num_inputs)
    outputs=int(num_outputs)
    portset=in_port
    ser=serial.Serial(
        baudrate=115200,
        timeout=def_timeout,
        port=portset
    )
    ser.read()

    def generate_lists(inputs,outputs):
        for i in range (2**inputs):
            bin_in=str(bin(i))         
            bin_in=bin_in[2:]               
            bin_in='0'*(8-len(bin_in))+bin_in     
            for x in range(8):
                bit_in[x].append(int(bin_in[7-x]))
        for i in range(0,2**inputs):
            for x in range(0,8):
                bit_out[x].append(StringVar())
                bit_out[x][i].set("x")


    def press(entrada):
        global current_number
        list_button_select[current_number].config(style='TButton')
        current_number=entrada
        list_button_select[current_number].config(style='inuse.TButton')
        process(entrada)


    def play():
        global mode
        mode=1
        run()
    
    def run():
        global mode
        global current_number
        while True:
            if mode==0:
                return
            if current_number==(2**inputs)-1:
                return
            if current_number!=-1:
                list_button_select[current_number].config(style='TButton')
            current_number+=1
            process(current_number)
            list_button_select[current_number].config(style='inuse.TButton')
            home.update()
            global time_delay
            if mode==1:
                if time_entry.get()!="":
                    time_delay=int(time_entry.get())
                time.sleep(time_delay/1000)
            if list_check_var[current_number].get()==True:
                return



    

    def pause():
        global mode
        mode=0

    def fast():
        global mode
        mode=2
        run()

    def next():
        global current_number
        if current_number==(2**inputs)-1:
            return
        if current_number!=-1:
            list_button_select[current_number].config(style='TButton')
        current_number+=1
        process(current_number)
        list_button_select[current_number].config(style='inuse.TButton')

    def prev():
        global current_number
        if current_number<=0:
            return
        list_button_select[current_number].config(style='TButton')    
        current_number-=1
        list_button_select[current_number].config(style='inuse.TButton')
        process(current_number)

    def read(numero):
        ser.write((str(numero)+';').encode("utf-8"))
        valor=str(ord(ser.read()))


    def process(indice):
        ser.write((str(indice)+';').encode("utf-8"))
        ndecimal=ord(ser.read())
        read=str(bin(ndecimal))    
        read=read[2:]              
        read='0'*(8-len(read))+read
        for x in range(8):
            bit_out[x][indice].set(read[7-x])


    generate_lists(inputs,outputs)

    for i in range(0,2**inputs):
        list_button_select.append(ttk.Button(second_frame, text=str(i),command=lambda x=int(i): press(x),width=3))
        list_check_var.append(BooleanVar(second_frame))
        list_check.append(Checkbutton(second_frame,variable=  list_check_var[i]))
        
        list_button_select[i].grid(column=0,row=i)
        list_check[i].grid(column=1,row=i)
        for x in range(0,inputs):
            dato=bit_in[inputs-x-1][i]
            Label(second_frame, text=str(dato)).grid(column=x+2,row=i)
    Label(second_frame,width=4).grid(column=3+inputs)
    for filas in range(0,2**inputs):
        for columnas in range(0,outputs):
            Label(second_frame,textvariable=bit_out[columnas][filas]).grid(column=inputs+2+1+outputs-columnas,row=filas)

    b_play=Button(my_canvas,image=im_play,text="play", command=play)
    b_play.place(relx=0,rely=0)

    b_pause=Button(my_canvas,text="pause",image=im_pause,command=pause)
    b_pause.place(relx=0,rely=0.16)

    b_next=Button(my_canvas,text="next",image=im_next,command=next)
    b_next.place(relx=0,rely=0.32)

    b_prev=Button(my_canvas,text="prev",image=im_prev,command=prev)
    b_prev.place(relx=0,rely=0.48)

    b_ff=Button(my_canvas,text="",image=im_ff,command=fast)
    b_ff.place(relx=0,rely=0.64)
    if ' ' in t_label_time_step:
        time_title=t_label_time_step[0:t_label_time_step.index(" ")]+"\n"+t_label_time_step[t_label_time_step.index(" ")+1:]
    else:
        time_title=t_label_time_step
    Label(text=time_title).place(relx=0,rely=0.8)
    time_entry=Entry(my_canvas,width=8)
    time_entry.place(relx=0,rely=0.9)

    windowWidth = home.winfo_reqwidth()
    windowHeight = home.winfo_reqheight()
    positionRight = int(home.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(home.winfo_screenheight()/2 - windowHeight/2)
    home.geometry("+{}+{}".format(positionRight, positionDown))

    home.mainloop()

#empezar(4,4,"COM3")