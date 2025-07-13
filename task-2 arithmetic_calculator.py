from tkinter import * 
window = Tk()
window.title("Arithmetic Calculater")
window.geometry("800x200")

def calculate():
    try :
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    except ValueError:
        result_label.config(text = "Please enter the valid number.")
        return
    
    operation = operation_var.get()
    if operation == '+':
        result = num1 + num2 
    elif operation == '-':
        result = num1 - num2 
    elif operation == '*':
        result = num1 * num2 
    elif operation == '/':
        if num2 == 0:
            result_label.config(text = "Cannot divide by zero.")
            return
        result = num1/num2 
    else:
        result_label.config(text = "Please select an opertion")
        return
    result_label.config(text = f"Result : {result}")

label1 = Label(window , text= "Number1:" )
label1.grid(row = 0 , column = 0 , padx = 10 , pady = 5)

entry1 = Entry(window)
entry1.grid(row = 0 , column = 1 , padx = 10 , pady = 5)

label2 = Label(window , text = "Number2:")
label2.grid(row = 1 , column = 0 , padx = 10 , pady = 5)

entry2 = Entry(window)
entry2.grid(row = 1 , column = 1 , padx = 10 , pady = 5)

operation_var = StringVar()
operation_var.set('+')

label3 = Label(window , text = "Operation")
label3.grid(row = 2 , column = 0 , padx =10 , pady = 5)

operation_frame = Frame(window)
operation_frame.grid(row = 2 , column = 1 , padx = 10 , pady = 5)

radio_add = Radiobutton(operation_frame , text = "+" , variable = operation_var , value = "+" , bg = "lightblue")
radio_add.pack(side = LEFT)

radio_sub = Radiobutton (operation_frame , text = "-" , variable = operation_var , value = "-" , bg = "lightgreen")
radio_sub.pack(side = LEFT)

radio_mul = Radiobutton(operation_frame , text = "*" , variable = operation_var , value = "*" , bg = "lightyellow")
radio_mul.pack(side=LEFT)

radio_divide = Radiobutton(operation_frame , text = "/", variable = operation_var , value = "/" , bg = "lightpink")
radio_divide.pack(side = LEFT)


submit_button = Button(window , text = "Calculate" , command = calculate)
submit_button.grid(row = 3 , column = 0 , columnspan = 2 , pady = 10 )

result_label = Label(window, text = "Result: ")
result_label.grid(row = 4 , column = 0 , columnspan = 2 , pady = 5 )

window.mainloop()