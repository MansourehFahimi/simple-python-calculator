import tkinter as tk
import math

def click(event):
    text = event.widget["text"]
    current = str(entry.get())

    if text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "√":
        try:
            number = float(current)
            if number < 0:
                entry.delete(0, tk.END)
                entry.insert(tk.END, "Invalid")
            else:
                result = math.sqrt(number)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("GUI Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font="Arial 18", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=10, padx=10)

buttons = [
    ['C', '±', '%', '√'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row_values in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for val in row_values:
        btn = tk.Button(frame, text=val, font="Arial 14", height=2, width=5)
        btn.pack(side=tk.LEFT, expand=True, fill="both")
        btn.bind("<Button-1>", click)
root.mainloop()