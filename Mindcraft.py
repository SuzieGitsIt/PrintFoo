# https://stackoverflow.com/questions/65325062/change-colour-of-tkinter-button-created-in-a-loop


import tkinter as tk
import random

def button_click(btn):
    color = random.choice(['white', 'pink', 'white'])
    btn.config(bg=color)
    print(btn)

GUI = tk.Tk()

frame = tk.Frame(GUI)
frame.pack()

for x in range(10):
    for y in range(10):
        btn = tk.Button(frame)    
        btn.config(text=f'{x}{y}',height=1, width=1, command=lambda button=btn: button_click(button))
        btn.grid(column=x, row=y, sticky='nsew')

GUI.mainloop()