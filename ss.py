import tkinter as tk
import os

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
root.mainloop()import tkinter as tk
import subprocess

def execute_command():
    command = "ls -l"  # Replace this with the command you want to execute
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    result_text.insert(tk.END, output.decode("utf-8"))

# Create a Tkinter window
root = tk.Tk()
root.title("Customized Terminal")

# Create a button to execute the command
execute_button = tk.Button(root, text="Execute Command", command=execute_command)
execute_button.pack()

# Create a text area to display the output
result_text = tk.Text(root, height=10, width=50)
result_text.pack()

# Run the Tkinter event loop
root.mainloop()
