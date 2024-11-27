import tkinter as tk
from tkinter import messagebox
import math

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            screen.set("")
    elif text == "C":
        screen.set("")
    elif text == "√":
        try:
            value = float(screen.get())
            screen.set(math.sqrt(value))
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")
            screen.set("")
    elif text == "sin":
        try:
            value = math.radians(float(screen.get()))
            screen.set(math.sin(value))
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")
            screen.set("")
    elif text == "cos":
        try:
            value = math.radians(float(screen.get()))
            screen.set(math.cos(value))
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")
            screen.set("")
    elif text == "tan":
        try:
            value = math.radians(float(screen.get()))
            screen.set(math.tan(value))
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")
            screen.set("")
    elif text == "log":
        try:
            value = float(screen.get())
            if value > 0:
                screen.set(math.log(value))
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Logarithm requires a positive number")
            screen.set("")
    else:
        screen.set(screen.get() + text)

# Initialize Tkinter
root = tk.Tk()
root.title("Scientific Calculator")

# Create the input field
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 18", borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=10, padx=5, pady=5)

# Button layout
buttons = [
    "7", "8", "9", "+", "C",
    "4", "5", "6", "-", "√",
    "1", "2", "3", "*", "sin",
    "0", ".", "=", "/", "cos",
    "(", ")", "^", "log", "tan"
]

# Create and place buttons
row, col = 1, 0
for btn_text in buttons:
    btn = tk.Button(root, text=btn_text, font="Arial 14", borderwidth=1, relief="raised", width=5, height=2)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 4:
        col = 0
        row += 1

# Run the application
root.mainloop()
