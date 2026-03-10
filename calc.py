from tkinter import *

root = Tk()
root.title("Color Calculator")
root.geometry("300x380")
root.configure(bg="#1e1e2f")   # window background color

# Entry field
entry = Entry(root, width=16, font=('Arial', 24), bd=0, bg="#f5f5f5", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Functions
def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(num))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button style
btn_color = "#4CAF50"
op_color = "#ff9500"
text_color = "white"

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2)
]

for (text,row,col) in buttons:
    color = op_color if text in ['/', '*', '-', '+'] else btn_color
    Button(root, text=text, width=6, height=2,
           font=('Arial',14), bg=color, fg=text_color,
           activebackground="#666",
           command=lambda t=text: click(t)
           ).grid(row=row, column=col, padx=5, pady=5)

# Equal button
Button(root, text='=', width=14, height=2, font=('Arial',14),
       bg="#2196F3", fg="white",
       command=calculate).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Clear button
Button(root, text='C', width=14, height=2, font=('Arial',14),
       bg="#f44336", fg="white",
       command=clear).grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()