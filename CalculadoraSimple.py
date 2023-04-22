from tkinter import *
from math import *
 
#Para ver en la pantalla
def btnClick(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)
 
#Para calcular y ver los resultados
def resultado():
    global operador
    try:
        operacion=str(eval(operador))
        input_text.set(operacion)
    except:
        input_text.set("ERROR")
    operador = ""
 
#Para limpiar la pantalla
def clear():
    global operador
    operador=("")
    input_text.set("0")
 
#Creo espacio de trabajo
ventana=Tk()
ventana.title("Calculadora")
ventana.geometry("392x550")
ventana.configure(background="light pink")
color_boton=("white")

#Creo variables
ancho_btn= 10
alto_btn= 3
input_text=StringVar()
operador=""

#Creo pantalla de visualización
Salida=Entry(ventana,font=('arial',20,'bold'),width=22,
textvariable=input_text,bd=20,insertwidth=4,bg="White",justify="right")
Salida.place(x=10,y=60)
 
#Creo botones
btn7=Button(ventana,text="7",width=ancho_btn, height=alto_btn,command=lambda:btnClick(7)).place(x=17,y=180)
btn8=Button(ventana,text="8",width=ancho_btn, height=alto_btn,command=lambda:btnClick(8)).place(x=107,y=180)
btn9=Button(ventana,text="9",width=ancho_btn, height=alto_btn,command=lambda:btnClick(9)).place(x=197,y=180)
btnC=Button(ventana,text="C",width=ancho_btn, height=alto_btn,command=clear).place(x=287,y=180)
btn4=Button(ventana,text="4",width=ancho_btn, height=alto_btn,command=lambda:btnClick(4)).place(x=17,y=240)
btn5=Button(ventana,text="5",width=ancho_btn, height=alto_btn,command=lambda:btnClick(5)).place(x=107,y=240)
btn6=Button(ventana,text="6",width=ancho_btn, height=alto_btn,command=lambda:btnClick(6)).place(x=197,y=240)
btnMas=Button(ventana,text="+",width=ancho_btn, height=alto_btn,command=lambda:btnClick("+")).place(x=287,y=240)
btn1=Button(ventana,text="1",width=ancho_btn, height=alto_btn,command=lambda:btnClick(1)).place(x=17,y=300)
btn2=Button(ventana,text="2",width=ancho_btn, height=alto_btn,command=lambda:btnClick(2)).place(x=107,y=300)
btn3=Button(ventana,text="3",width=ancho_btn, height=alto_btn,command=lambda:btnClick(3)).place(x=197,y=300)
btnMenos=Button(ventana,text="-",width=ancho_btn, height=alto_btn,command=lambda:btnClick("-")).place(x=287,y=300)
btn0=Button(ventana,text="0",width=ancho_btn, height=alto_btn,command=lambda:btnClick(0)).place(x=17,y=360)
btnComa=Button(ventana,text=",",width=ancho_btn, height=alto_btn,command=lambda:btnClick(",")).place(x=107,y=360)
btnDivision=Button(ventana,text="/",width=ancho_btn, height=alto_btn,command=lambda:btnClick("/")).place(x=197,y=360)
btnMultiplicacion=Button(ventana,text="x",bg=color_boton,width=ancho_btn,height=alto_btn,command=lambda:btnClick("*")).place(x=287,y=360)
btnIgual=Button(ventana,text="=",width=40, height=alto_btn,command=resultado).place(x=50,y=420)

#llamada a funciones 
clear()
 
ventana.mainloop()