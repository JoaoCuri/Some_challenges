from tkinter import *

window=Tk()

window.title("Mile to Km converter")
window.minsize(width=300,height=50)


input=Entry(width=14)
input.place(x=115,y=30)
#miles=input.get()

Label(window,text="Miles").place(x=170,y=30)

def button_click(): 
    miles=input.get()
    km=int(miles)*(1.60934)
    Label(window,text=km).place(x=115,y=55)
    Label(window,text="Km").place(x=170,y=55)
       
def sair():
    window.destroy()
    

button=Button(text='Calculate',command=button_click)
button.place(x=115,y=80)


button=Button(text='sair',command=sair)
button.place(x=190,y=130)

window.mainloop()