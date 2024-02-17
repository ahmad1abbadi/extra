import os, tk

def execute_command():
    command = "echo 'Button Clicked!'"
    os.system("termux-open -a com.termux.app.TermuxActivity -e {}".format(command))

# Create a window
root = tk.Tk()
root.title("Interactive Termux")

# Create a button
button = tk.Button(root, text="Click Me", command=execute_command)
button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
###"Execute Command", command=e
