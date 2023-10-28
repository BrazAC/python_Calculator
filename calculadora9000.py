from tkinter import *
#Window Configs
root = Tk()
root.title('Super calculadora 9000')
root.geometry('450x400')
root.iconbitmap('midia\pYicon.ico')


position, valor1, valor2 = 0, 0, 0
#Functions
def btnClickNumbers (simbol):
    global position
    entryBox.insert(position, simbol)
    value = entryBox.get()
    position = position + 1

    print(value)
    print(len(value))
    print(type(value))


action = ''
def btnClickOperators (operator):
    global action, position, valor1, valor2
    #Get valor1
    if operator == '+':
        action = '+'
        valor1 = int(entryBox.get())
        entryBox.delete(0, len(str(valor1)))
        position=0
    elif operator == 'x':
        action = 'x'
        valor1 = int(entryBox.get())
        entryBox.delete(0, len(str(valor1)))
        position=0
    elif operator == '-':
        action = '-'
        valor1 = int(entryBox.get())
        entryBox.delete(0, len(str(valor1)))
        position=0
    elif operator == '/':
        action = '/'
        valor1 = int(entryBox.get())
        entryBox.delete(0, len(str(valor1)))
        position=0
    elif operator == '<':
        valueDel = entryBox.get()
        entryBox.delete(0, len(valueDel))
    #Get valor2 and operate
    elif operator == '=':
        valor2 = int(entryBox.get())
        entryBox.delete(0, len(str(valor2)))
        if action == '+':
            entryBox.insert(position, valor1+valor2)
            position=0
        elif action == 'x':
            entryBox.insert(position, valor1*valor2)
            position=0
        elif action == '-':
            entryBox.insert(position, valor1-valor2)
            position=0
        elif action == '/':
            float(valor1)
            float(valor2)
            entryBox.insert(position, valor1/valor2)
            position=0
        valor1, valor2 = 0, 0


#Entry box
entryBox = Entry(root, width=35, borderwidth=1, font=('Atial', 15))
entryBox.grid(row=0, column=0, padx=30, pady=20, columnspan=4)

#NumberButtons
btn1 = Button(root, text='1', padx=40, pady=20, command=lambda:btnClickNumbers(1)).grid(row=1,column=0)
btn2 = Button(root, text='2', padx=40, pady=20, command=lambda:btnClickNumbers(2)).grid(row=1,column=1) 
btn3 = Button(root, text='3', padx=40, pady=20, command=lambda:btnClickNumbers(3)).grid(row=1,column=2) 
btn4 = Button(root, text='4', padx=40, pady=20, command=lambda:btnClickNumbers(4)).grid(row=2,column=0) 
btn5 = Button(root, text='5', padx=40, pady=20, command=lambda:btnClickNumbers(5)).grid(row=2,column=1) 
btn6 = Button(root, text='6', padx=40, pady=20, command=lambda:btnClickNumbers(6)).grid(row=2,column=2) 
btn7 = Button(root, text='7', padx=40, pady=20, command=lambda:btnClickNumbers(7)).grid(row=3,column=0) 
btn8 = Button(root, text='8', padx=40, pady=20, command=lambda:btnClickNumbers(8)).grid(row=3,column=1)
btn9 = Button(root, text='9', padx=40, pady=20, command=lambda:btnClickNumbers(9)).grid(row=3,column=2)
btn0 = Button(root, text='0', padx=40, pady=20, command=lambda:btnClickNumbers(0)).grid(row=4,column=1)  

#OperationButtons
btnPlus = Button(root, text='+', padx=38, pady=20, command=lambda:btnClickOperators('+')).grid(row=1, column=3)
btnMinus = Button(root, text='-', padx=39, pady=20, command=lambda:btnClickOperators('-')).grid(row=2, column=3)
btnX = Button(root, text='x', padx=38, pady=20, command=lambda:btnClickOperators('x')).grid(row=3, column=3)
btnDiv = Button(root, text='/', padx=39, pady=20, command=lambda:btnClickOperators('/')).grid(row=4, column=3)
btnEqual = Button(root, text='=', padx=152, pady=20, command=lambda:btnClickOperators('=')).grid(row=5, column=0, columnspan=3)
btnDel = Button(root, text='Clear', padx=28, pady=20, command=lambda:btnClickOperators('<')).grid(row=5, column=3)

root.mainloop()