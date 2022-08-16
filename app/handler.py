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
    entry_instance.delete(0, tk.END)

def callback_clearexp(entry_instance: tk.Entry):
    '''Clear Expression Button Callback'''
    entry_instance.delete(0, tk.END)

def callback_operator(operator_text: str, entry_instance: tk.Entry):
    '''Operator Button Callback'''
    callback_calc(entry_instance)

    entry_instance.insert(tk.END, ' ' + operator_text + ' ')

def callback_point(entry_instance: tk.Entry):
    '''Point Button Callback'''
    if '.' not in entry_instance.get():
        entry_instance.insert(tk.END, '.')

def callback_calc(entry_instance: tk.Entry):
    '''Calculate Button Callback'''
    operator_dict = {'＋': '+', '－': '-', '×': '*', '÷': '/'}
    calc_exp = entry_instance.get()
    result = ''

    try:
        for char in operator_dict:
            calc_exp = calc_exp.replace(char, operator_dict[char])

        result = eval(calc_exp)
    finally:
        entry_instance.delete(0, tk.END)
        entry_instance.insert(0, str(result))

def callback_transform(transform_text: str, entry_instance: tk.Entry):
    '''％, 1/χ, χ², √χ, ＋/－ Button Callback'''
    transform_dict = {'％': '/100', '1/χ': '**-1', 'χ²': '**2', '√χ': '**(1/2)', '＋/－': '*-1'}
    entry_instance.insert(tk.END, transform_dict[transform_text])

    callback_calc(entry_instance)

# Keyboard Event Handlers
def handler_return(event: tk.Event, entry_instance: tk.Entry):
    '''Return Key Handler'''
    callback_calc(entry_instance)

def handler_back(event: tk.Event, entry_instance: tk.Entry):
    '''BackSpace Key Handler'''
    callback_clear(entry_instance)
