import tkinter as tk
from tkinter import ttk

def show_message(msg):
    root = tk.Tk()
    root.attributes("-alpha", 0.5)
    root.config(width=100, height=100)
    root.overrideredirect(True)

    label=tk.Label(root,text=msg)
    label.pack(anchor='center', expand=1)
    root.after(500, lambda: root.destroy()) 
    root.mainloop()