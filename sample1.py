#python -m tkinter
import tkinter as tk
from tkinter import messagebox

# Perform the calculation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
            return
        
        label_result.config(text=f"Result: {result}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Clear inputs
def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")
    operation_var.set('+')

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Input fields
tk.Label(root, text="Number 1:").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root, text="Number 2:").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Operation selection
tk.Label(root, text="Select Operation:").pack(pady=5)
operation_var = tk.StringVar(value='+')
operations_frame = tk.Frame(root)
operations_frame.pack(pady=5)

for op in ['+', '-', '*', '/']:
    tk.Radiobutton(operations_frame, text=op, variable=operation_var, value=op).pack(side=tk.LEFT, padx=5)

# Calculate button
btn_calculate = tk.Button(root, text="Calculate", command=calculate, bg="green", fg="white")
btn_calculate.pack(pady=10)

# Clear button
btn_clear = tk.Button(root, text="Clear", command=clear, bg="red", fg="white")
btn_clear.pack(pady=5)

# Result display
label_result = tk.Label(root, text="Result: ", font=("Arial", 14))
label_result.pack(pady=10)

# Start the GUI loop

root.mainloop()
