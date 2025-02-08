import tkinter as tk

def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        result.set("Invalid input")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        result.set("Invalid input")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        result.set("Invalid input")

def divide():
    try:
        if float(entry2.get()) == 0:
            result.set("Error! Division by zero.")
        else:
            result.set(float(entry1.get()) / float(entry2.get()))
    except ValueError:
        result.set("Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=2, padx=5, pady=5)

result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, textvariable=result).grid(row=1, column=2, padx=5, pady=5)

tk.Button(root, text="+", command=add).grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="-", command=subtract).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="*", command=multiply).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="/", command=divide).grid(row=2, column=2, padx=5, pady=5)

root.mainloop()