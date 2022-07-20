'''Event Handler'''
import tkinter as tk
import tkinter.messagebox as msgbox

def callback_number(number_text, entry_instance: tk.Entry):
    '''Number Button Callback'''
    print(number_text, entry_instance)
    entry_instance.insert(tk.END, number_text)

def callback_back(entry_instance: tk.Entry):
    '''Backspace Button Callback'''
    result = entry_instance.get()
    entry_instance.delete(0, tk.END)
    entry_instance.insert(0, result[0:-1])
