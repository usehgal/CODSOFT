import tkinter as tk
import math

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "clear":
        entry.delete(0, tk.END)
    elif text == "<-":
        entry.delete(len(entry.get()) - 1, tk.END)
    elif text == "√":
        try:
            result = math.sqrt(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "!":
        try:
            result = math.factorial(int(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font="Arial 20", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["<-", "√", "!", "clear"]
]

for i in range(5):
    for j in range(4):
        button = tk.Button(root, text=button_texts[i][j], font="Arial 20", padx=20, pady=20)
        button.grid(row=i+1, column=j, padx=5, pady=5)
        button.bind("<Button-1>", on_click)

root.mainloop()
