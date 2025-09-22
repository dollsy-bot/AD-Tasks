import tkinter as tk

# Function to handle button clicks
def click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "undefined")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

# Input field
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row, col = 1, 0
for button in buttons:
    action = lambda x=button: click(x)
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 14), command=action)\
        .grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text="C", width=22, height=2, font=("Arial", 14), command=lambda: click("C"))\
    .grid(row=row, column=0, columnspan=4, padx=5, pady=5)

# Run the app
root.mainloop()
