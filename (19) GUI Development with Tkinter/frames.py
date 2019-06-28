import tkinter as tk

from tkinter import ttk

root = tk.Tk()

main = ttk.Frame(root)
main.pack(side='left', fill='both', expand=True)

tk.Label(main, text='Label 1', bg='green').pack(side='top', fill='both', expand=True)
tk.Label(main, text='Label 2', bg='red').pack(side='top', fill='both', expand=True)

tk.Label(root, text='Label left', bg='yellow').pack(side='left', fill='both', expand=True)

root.mainloop()