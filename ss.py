import tkinter as tk

def get_input():
    print(entry.get())

root = tk.Tk()
root.title("Entry Example")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Input", command=get_input)
button.pack()

root.mainloop()
