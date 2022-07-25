'''Event Handler'''
import tkinter as tk
import tkinter.messagebox as msgbox

# Button Callbacks
def callback_number(number_text, entry_instance: tk.Entry):
    '''Number Button Callback'''
    entry_instance.insert(tk.END, number_text)

def callback_back(entry_instance: tk.Entry):
    '''Backspace Button Callback'''
    result = entry_instance.get()
    entry_instance.delete(0, tk.END)
    entry_instance.insert(0, result[0:-1])

def callback_clear(entry_instance: tk.Entry):
    '''Clear Button Callback'''

def callback_clearexp(entry_instance: tk.Entry):
    '''Clear Expression Button Callback'''
    entry_instance.delete(0, tk.END)

def callback_operator(operator_text: tk.Button, entry_instance: tk.Entry):
    '''Operator Button Callback'''

def callback_point(entry_instance: tk.Entry):
    if '.' not in entry_instance.get():
        entry_instance.insert(tk.END, '.')

def callback_calc(entry_instance: tk.Entry):
    try:
        msgbox.showinfo("Result", str(eval(entry_instance.get())))
    except:
        pass

# Keyboard Event Handlers
def handler_return(event: tk.Event, entry_instance: tk.Entry):
    callback_calc(entry_instance)