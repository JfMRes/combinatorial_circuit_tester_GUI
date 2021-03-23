from csv import *
import matplotlib.pyplot as plt
import math
from PIL import Image
def showDiagram(path_in,salidas):

    path=str(path_in)

    with open(path,'r') as archivo:
        lectura = reader(archivo)

        read_array=list(lectura)
        numline=len(read_array)

        b0=[]; b1=[]; b2=[]; b3=[]; b4=[]; b5=[]; b6=[]; b7=[]; leyenda=[]
        out0=[]; out1=[]; out2=[]; out3=[]; out4=[]; out5=[]; out6=[]; out7=[]; leyenda2=[]

        max_in=0; max_out=0

        for i in range(0,numline):
            #decimal -> 0b11 -> 11 -> rellena a 0 digitos 00000011 -> cuarda cada digito en la read_array de su bit

            num_in=read_array[i][0]                        
            if int(num_in)>max_in:
                max_in=int(num_in)
            bin_in=str(bin(int(num_in)))         
            bin_in=bin_in[2:]               
            bin_in='0'*(8-len(bin_in))+bin_in      
            b0.append(int(bin_in[7]))
            b1.append(int(bin_in[6]))
            b2.append(int(bin_in[5]))
            b3.append(int(bin_in[4]))
            b4.append(int(bin_in[3]))
            b5.append(int(bin_in[2]))
            b6.append(int(bin_in[1]))
            b7.append(int(bin_in[0]))
            leyenda.append(i)
            
            num_out=read_array[i][1]                     
            if int(num_out)>max_out:
                pass
            bin_out=str(bin(int(num_out)))          
            bin_out=bin_out[2:]                     
            bin_out='0'*(8-len(bin_out))+bin_out    
            out0.append(int(bin_out[7]))
            out1.append(int(bin_out[6]))
            out2.append(int(bin_out[5]))
            out3.append(int(bin_out[4]))
            out4.append(int(bin_out[3]))
            out5.append(int(bin_out[2]))
            out6.append(int(bin_out[1]))
            out7.append(int(bin_out[0]))
        
        list_in=[b0,b1,b2,b3,b4,b5,b6,b7]
        list_out=[out0,out1,out2,out3,out4,out5,out6,out7]

        bits_in=int(math.log(max_in,2))+1
        bits_out=int(salidas)

        total=bits_in+bits_out

        figura_test, axes=plt.subplots(total,1,sharex=True)
        for i in range (0,bits_in):
            axes[i].plot(leyenda,list_in[i],drawstyle='steps-pre',color='blue')
            axes[i].grid(True)
            axes[i].set_ylabel("in"+str(i))
            plt.yticks([1,0])

        for i in range (bits_in,total):
            axes[i].plot(list_out[i-bits_in],drawstyle='steps-pre',color='red')
            axes[i].grid(True)
            axes[i].set_ylabel("out"+str(i-bits_in))
        figura_test.suptitle("Time diagram  "+path.split("/")[-1].split(".")[0])
       
        
        table_list=[]      

        for i in range(1,max_in+2):
            table_list.append([])
            table_list[i-1].append(str(i-1))
            for a in range(0,bits_in):
                table_list[i-1].append(list_in[bits_in-a-1][i])
            table_list[i-1].append("->")
            for x in range(0,bits_out):
                table_list[i-1].append(list_out[bits_out-x-1][i])
            table_list[i-1].append(read_array[i][1])
        
        column_label=[]
        column_label.append("Input value:")
        for i in range(bits_in-1,-1,-1):
            column_label.append("in"+str(i))
        column_label.append("->")
        
        for i in range(bits_out-1,-1,-1):
            column_label.append("in"+str(i))
        column_label.append("Output value:")

        

        fig2, ax2 =plt.subplots()
        ax2.axis('tight')
        ax2.axis('off')
        fig2.suptitle("True table  "+path.split("/")[-1].split(".")[0],ha='center')
        
        ax2.table(cellText=table_list,colLabels=column_label,loc='upper left').scale(2, 2)
        plt.savefig('test.jpeg',bbox_inches='tight',dpi=300)
        plt.close(fig2)
        img=Image.open('test.jpeg')

        fig2.set_visible(False)
        img.show()
        plt.show()
        
        


#showDiagram('prueba.csv',3)
