import tkinter as tk
from tkinter import ttk

def show_message(msg):
    root = tk.Tk()
    root.overrideredirect(True)
    root.wait_visibility(root)
    root.attributes('-alpha', 0.7)

    label=tk.Label(root, text=msg, font=('', 36, 'normal'))
    label.pack(anchor='center')
    root.after(400, lambda: root.destroy()) 
    root.mainloop()
