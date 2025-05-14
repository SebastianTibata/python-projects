import customtkinter 
import tkinter
import keyboard

#Dimensiones
screen_width=400
screen_height=700


#Colores
colors={
    "black":"#000000",
    "white":"#FFFFFF",
    "numbers": "#E0F7FA",
    "functions":"#BBDEFB",
    "del/ac":"#FFCDD2",
    "hoovernumbers":"#B2EBF2",
    "hooverfunctions":"#90CAF9",
    "hooverdel/ac":"#EF9A9A",
    "box":"#E8F5E9"    
}

#Funciones

def click(number):
    global expresion
    inputText.set(inputText.get()+(str(number)))

def delete():
    global expresion
    expresion=""
    inputText.set(inputText.get()[0:-1])
def ac():
    inputText.set("")
    
def equal():
    result=""
    try:
        result=eval(inputText.get())
        inputText.set(result)
    except:
        result="Error"
        inputText.set(result)
        
#Ventana

root=customtkinter.CTk()
root.title("Calculator")
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False,False)

expresion=""
inputText=tkinter.StringVar()

mainframe=customtkinter.CTkFrame(width=360,height=150,master=root,fg_color=colors["box"])
mainframe.grid(row=0,column=0,columnspan=4,padx=20,pady=(40,10))


inputField=customtkinter.CTkEntry(mainframe,width=300,height=40,textvariable=inputText,font=('Helvetica',40),fg_color=colors["box"],text_color="#686868",border_color=colors["box"])
inputField.grid(row=0,column=0,padx=30,pady=55)


ACbutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["del/ac"],hover_color=colors["hooverdel/ac"],text="AC",font=('Helvetica',25),text_color=colors["black"],command=lambda: ac())
ACbutton.grid(row=1,column=0,padx=(10,5),pady=5)
percentagebutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["del/ac"],hover_color=colors["hooverdel/ac"],text="%",font=('Helvetica',25),text_color=colors["black"],command=lambda: click('%'))
percentagebutton.grid(row=1,column=1,padx=5,pady=5)
delbutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["del/ac"],hover_color=colors["hooverdel/ac"],text="del",font=('Helvetica',25),text_color=colors["black"],command=lambda: delete())
delbutton.grid(row=1,column=2,padx=5,pady=5)
divbutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["functions"],hover_color=colors["hooverfunctions"],text="/",font=('Helvetica',35),text_color=colors["black"],command=lambda: click('/'))
divbutton.grid(row=1,column=3,padx=(5,10),pady=5)

sevenbutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["numbers"],hover_color=colors["hoovernumbers"],text="7",font=('Helvetica',25),text_color=colors["black"], command=lambda: click('7'))
sevenbutton.grid(row=2,column=0,padx=(10,5),pady=5)
eightbutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["numbers"],hover_color=colors["hoovernumbers"],text="8",font=('Helvetica',25),text_color=colors["black"],command=lambda: click('8'))
eightbutton.grid(row=2,column=1,padx=5,pady=5)
ninebutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["numbers"],hover_color=colors["hoovernumbers"],text="9",font=('Helvetica',25),text_color=colors["black"],command=lambda: click('9'))
ninebutton.grid(row=2,column=2,padx=5,pady=5)
multiplicationbutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["functions"],hover_color=colors["hooverfunctions"],text="X",font=('Helvetica',25),text_color=colors["black"],command=lambda: click('*'))
multiplicationbutton.grid(row=2,column=3,padx=(5,10),pady=5)

fourbutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["numbers"],hover_color=colors["hoovernumbers"],text="4",font=('Helvetica',25),text_color=colors["black"],command=lambda: click('4'))
fourbutton.grid(row=3,column=0,padx=(10,5),pady=5)
fivebutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["numbers"],hover_color=colors["hoovernumbers"],text="5",font=('Helvetica',25),text_color=colors["black"],command=lambda: click('5'))
fivebutton.grid(row=3,column=1,padx=5,pady=5)
sixbutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["numbers"],hover_color=colors["hoovernumbers"],text="6",font=('Helvetica',25),text_color=colors["black"],command=lambda: click('6'))
sixbutton.grid(row=3,column=2,padx=5,pady=5)
substractionbutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["functions"],hover_color=colors["hooverfunctions"],text="-",font=('Helvetica',35),text_color=colors["black"],command=lambda: click('-'))
substractionbutton.grid(row=3,column=3,padx=(5,10),pady=5)

onebutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["numbers"],hover_color=colors["hoovernumbers"],text="1",font=('Helvetica',25),text_color=colors["black"],command=lambda: click('1'))
onebutton.grid(row=4,column=0,padx=(10,5),pady=5)
twobutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["numbers"],hover_color=colors["hoovernumbers"],text="2",font=('Helvetica',25),text_color=colors["black"],command=lambda: click('2'))
twobutton.grid(row=4,column=1,padx=5,pady=5)
threebutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["numbers"],hover_color=colors["hoovernumbers"],text="3",font=('Helvetica',25),text_color=colors["black"],command=lambda: click('3'))
threebutton.grid(row=4,column=2,padx=5,pady=5)
additionbutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["functions"],hover_color=colors["hooverfunctions"],text="+",font=('Helvetica',35),text_color=colors["black"],command=lambda: click('+'))
additionbutton.grid(row=4,column=3,padx=(5,10),pady=5)

dotbutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["numbers"],hover_color=colors["hoovernumbers"],text=".",font=('Helvetica',35),text_color=colors["black"],command=lambda: click('.'))
dotbutton.grid(row=5,column=0,padx=(10,5),pady=5)
zerobutton=customtkinter.CTkButton(master=root,width=75,height=75,fg_color=colors["numbers"],hover_color=colors["hoovernumbers"],text="0",font=('Helvetica',25),text_color=colors["black"],command=lambda: click('0'))
zerobutton.grid(row=5,column=1,padx=5,pady=5)
equalbutton=customtkinter.CTkButton(master=root,width=170,height=75,fg_color=colors["functions"],hover_color=colors["hooverfunctions"],text="=",font=('Helvetica',35),text_color=colors["black"],command=lambda: equal())
equalbutton.grid(row=5,column=2,columnspan=2,padx=(5,10),pady=5)

keyboard.add_hotkey('enter',equal)

root.mainloop()