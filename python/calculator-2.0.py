from tkinter import *

def button_press(num):
    """Handle button press and update the equation text."""
    current = equation_text.get()
    equation_text.set(current + str(num))

def equals():
    """Evaluate the equation and display the result."""
    try:
        result = eval(equation_text.get())
        equation_text.set(result)
    except Exception:
        equation_text.set("Error")

def clear():
    """Clear the equation text."""
    equation_text.set("")

# Create the main window
window = Tk()
window.title("Calculator Program")
window.geometry("500x600")

# Equation text variable
equation_text = StringVar()

# Label to display the equation
label = Label(window, textvariable=equation_text, font=("consolas", 20), bg="white", width=24, height=2)
label.pack()

# Frame to hold the buttons
frame = Frame(window)
frame.pack()

# Button layout
buttons = [
    ['1', '2', '3', '/'],
    ['4', '5', '6', '*'],
    ['7', '8', '9', '-'],
    ['C', '0', '=', '+']
]

# Generate buttons dynamically
for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        if button_text.isdigit() or button_text == '.':
            btn_command = lambda x=button_text: button_press(x)
        elif button_text == 'C':
            btn_command = clear
        elif button_text == '=':
            btn_command = equals
        else:
            btn_command = lambda x=button_text: button_press(x)

        Button(
            frame,
            text=button_text,
            height=4,
            width=9,
            font=("consolas", 20),
            command=btn_command
        ).grid(row=i, column=j)

# Run the application
window.mainloop()